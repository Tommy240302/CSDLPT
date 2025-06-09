# CSDLPT
# Sliding Window Join Simulator

Đây là một ứng dụng mô phỏng **Sliding Window Join** giữa hai luồng dữ liệu (`stream_R` và `stream_S`) bằng giao diện đồ họa (`tkinter`). Ứng dụng hỗ trợ hai chế độ xử lý:

- **Non-deterministic:** Join theo thứ tự đến (arrival order).
- **Deterministic:** Join theo thời gian sự kiện (event time) với áp dụng **watermark**.

## Mô tả chức năng

- Cho phép chọn chế độ xử lý giữa Non-deterministic và Deterministic.
- Hiển thị dữ liệu từng stream và kết quả join.
- Mỗi join được thực hiện trong một **cửa sổ trượt (sliding window)** có kích thước 5 giây.
- Khi chọn chế độ Deterministic, hệ thống sẽ sử dụng **event time** để xử lý join, đồng thời sử dụng **watermark** để loại bỏ bản ghi trễ.

## Ví dụ dữ liệu

### Stream R

| ID | Value | Event Time        |
|----|-------|-------------------|
| 1  | r1    | 10:00:00          |
| 2  | r2    | 10:00:05          |
| 3  | r3    | 10:00:10          |

### Stream S

| ID | Value | Event Time        |
|----|-------|-------------------|
| 1  | s1    | 10:00:03          |
| 2  | s2    | 10:00:06          |
| 3  | s3    | 10:00:13          |

## Cách sử dụng

1. Chạy script Python có chứa mã GUI.
2. Trong cửa sổ giao diện:
   - Chọn chế độ xử lý.
   - Bấm nút **"Thực hiện Join"** để xem kết quả.

## Lưu ý

- **Non-deterministic:** Join dựa trên thứ tự đến của dữ liệu, không quan tâm đến thời gian sự kiện.
- **Deterministic:** Join sử dụng event time và áp dụng watermark (chậm 1 giây) để loại bỏ bản ghi quá trễ.

## Yêu cầu

- Python 3.x
- Thư viện chuẩn: `tkinter`, `datetime`

## Giao diện mẫu

![image](https://github.com/user-attachments/assets/a5ec19d6-4f74-4721-80e2-07bb2ffc9c53)

Kết quả Join khi không áp dụng watermark

![image](https://github.com/user-attachments/assets/7dbb2579-8b38-408e-b6a3-7e9c031ba16a)

Kết quả Join khi có áp dụng watermark

---

*Tác giả: [Lại Khắc Minh Quang]*  
*Ngày hoàn thành: [9/6/2025]*
