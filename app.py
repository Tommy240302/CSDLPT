import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime, timedelta

stream_R = [
    {"id": 1, "value": "r1", "event_time": datetime(2023, 1, 1, 10, 0, 0)},
    {"id": 2, "value": "r2", "event_time": datetime(2023, 1, 1, 10, 0, 5)},
    {"id": 3, "value": "r3", "event_time": datetime(2023, 1, 1, 10, 0, 10)},
]

stream_S = [
    {"id": 1, "value": "s1", "event_time": datetime(2023, 1, 1, 10, 0, 3)},
    {"id": 2, "value": "s2", "event_time": datetime(2023, 1, 1, 10, 0, 6)},
    {"id": 3, "value": "s3", "event_time": datetime(2023, 1, 1, 10, 0, 13)},
]

window_size = timedelta(seconds=5)

def sliding_window_join(arrival_ordered_R, arrival_ordered_S, use_event_time=False):
    result = []
    buffer_R = []
    buffer_S = []
    watermark = None

    for r in arrival_ordered_R + arrival_ordered_S:
        is_R = r in arrival_ordered_R
        if use_event_time:
            if watermark is None or r["event_time"] > watermark:
                watermark = r["event_time"] - timedelta(seconds=1)
            buffer_R = [x for x in buffer_R if x["event_time"] >= watermark - window_size]
            buffer_S = [x for x in buffer_S if x["event_time"] >= watermark - window_size]

        if is_R:
            for s in buffer_S:
                if abs((r["event_time"] - s["event_time"]).total_seconds()) <= window_size.total_seconds():
                    result.append((r["value"], s["value"]))
            buffer_R.append(r)
        else:
            for rr in buffer_R:
                if abs((r["event_time"] - rr["event_time"]).total_seconds()) <= window_size.total_seconds():
                    result.append((rr["value"], r["value"]))
            buffer_S.append(r)
    return result

def run_join():
    mode = mode_var.get()
    use_event_time = (mode == "Deterministic")

    arrival_ordered_R = stream_R
    arrival_ordered_S = stream_S
    if not use_event_time:
        arrival_order = [stream_R[0], stream_S[2], stream_S[0], stream_R[1], stream_S[1], stream_R[2]]
        arrival_ordered_R = [x for x in arrival_order if x in stream_R]
        arrival_ordered_S = [x for x in arrival_order if x in stream_S]

    result = sliding_window_join(arrival_ordered_R, arrival_ordered_S, use_event_time=use_event_time)

    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "== Stream R ==\n")
    for r in stream_R:
        output_text.insert(tk.END, f"{r['value']} @ {r['event_time'].time()}\n")

    output_text.insert(tk.END, "\n== Stream S ==\n")
    for s in stream_S:
        output_text.insert(tk.END, f"{s['value']} @ {s['event_time'].time()}\n")

    output_text.insert(tk.END, f"\n== Join Result ({mode}) ==\n")
    for pair in result:
        output_text.insert(tk.END, f"{pair[0]} - {pair[1]}\n")

    if use_event_time:
        output_text.insert(tk.END, "\n(Ghi chú: Join theo thời gian sự kiện, có áp dụng watermark)\n")
    else:
        output_text.insert(tk.END, "\n(Ghi chú: Join theo thứ tự đến, không có watermark)\n")

root = tk.Tk()
root.title("Mô phỏng Sliding Window Join")

tk.Label(root, text="Chọn chế độ xử lý:").pack()

mode_var = tk.StringVar()
mode_combo = ttk.Combobox(root, textvariable=mode_var, state="readonly")
mode_combo['values'] = ("Non-deterministic", "Deterministic")
mode_combo.current(0)
mode_combo.pack()

tk.Button(root, text="Thực hiện Join", command=run_join).pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=60, height=20)
output_text.pack()

root.mainloop()
