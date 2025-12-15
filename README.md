# Bài tập DFS – Thành phần liên thông (Python – mức cơ bản)

## 1) File trong thư mục

Trong `CTDLVGT/Graph/`:
- `graph_dfs_homework.py`: danh sách kề + hàm `dfs()` riêng + hàm giải 4 bài
- `main.py`: đọc input và in kết quả theo từng bài

## 2) Quy ước input (đơn giản)

Áp dụng cho cả vô hướng và có hướng.

- Dòng 1: `n m`
- Dòng 2: `t`
  - `0`: đồ thị vô hướng
  - `1`: đồ thị có hướng
- `m` dòng tiếp: `u v`

Ghi chú cho đồ thị có hướng: để dùng DFS cơ bản, chương trình tính **liên thông yếu**
(tức là **bỏ hướng** các cạnh rồi chạy DFS như vô hướng).

### Ví dụ vô hướng
```
6 3
0
1 2
2 3
5 6
```

### Ví dụ có hướng
```
6 5
1
1 2
2 3
4 5
5 4
6 6
```

## 3) Ý nghĩa các bài

- **Bài 1**: Đếm số thành phần liên thông.
- **Bài 2**: Thành phần liên thông có số đỉnh nhiều nhất.
- **Bài 3**: Đếm số thành phần có tổng nhãn đỉnh chẵn.
- **Bài 4**: Chọn thành phần có tổng nhãn chẵn lớn nhất, rồi đếm số đỉnh lẻ trong thành phần đó.

## 4) Cách chạy (Windows PowerShell)

Mở PowerShell tại `CTDLVGT/Graph/`:

```powershell
python .\main.py
```

Nếu bạn bấm **Run** trong VS Code mà không nhập được dữ liệu (bị lỗi `EOFError`), hãy tạo file `input.txt` rồi chạy theo cách redirect bên dưới.

Hoặc chạy bằng file input:

```powershell
Get-Content .\input.txt | python .\main.py
```

Nếu bạn muốn dùng cú pháp `< input.txt` (giống CMD), chạy:

```powershell
cmd /c "python .\main.py < input.txt"
```
