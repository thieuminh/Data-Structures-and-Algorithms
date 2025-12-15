import sys

from graph_dfs_homework import get_components, solve_homework


def _readline_or_exit(message_when_no_input):
    try:
        return input()
    except EOFError:
        print(message_when_no_input)
        sys.exit(1)


def main():
    # Input đơn giản:
    # Dòng 1: n m
    # Dòng 2: t (0: vô hướng, 1: có hướng)
    # m dòng tiếp: u v

    interactive = sys.stdin.isatty()

    if interactive:
        print("Nhap theo format:")
        print("Dong 1: n m")
        print("Dong 2: t (0: vo huong, 1: co huong)")
        print("m dong tiep: u v")
        print()

    line1 = _readline_or_exit(
        "Khong co du lieu dau vao. Hay nhap input trong Terminal hoac dung: python .\\main.py < input.txt"
    )
    n, m = map(int, line1.split())

    line2 = _readline_or_exit(
        "Thieu dong t (0/1). Hay nhap du input hoac dung: python .\\main.py < input.txt"
    )
    t = int(line2.strip())
    directed = (t == 1)

    edges = []
    for _ in range(m):
        line = _readline_or_exit(
            "Thieu canh u v. Hay kiem tra m dong canh trong input.txt"
        )
        u, v = map(int, line.split())
        edges.append((u, v))

    components = get_components(n, edges, directed=directed)
    ans = solve_homework(components)

    if directed:
        print("ĐỒ THỊ CÓ HƯỚNG (liên thông yếu - bỏ hướng để DFS)")
    else:
        print("ĐỒ THỊ VÔ HƯỚNG")
    print(f"n={n}, m={m}")
    print()

    print("BÀI 1: Đếm số thành phần liên thông")
    print(ans["bai_1"])
    print()

    print("BÀI 2: Thành phần liên thông có số đỉnh nhiều nhất")
    print("Kích thước lớn nhất:", ans["bai_2_max_size"])
    print("Các thành phần (danh sách đỉnh):")
    for comp in ans["bai_2_components"]:
        print(" ", sorted(comp))
    print()

    print("BÀI 3: Có bao nhiêu TP liên thông có tổng nhãn đỉnh chẵn")
    print(ans["bai_3"])
    print()

    print("BÀI 4: Đếm số đỉnh lẻ trong TP có tổng chẵn lớn nhất")
    if ans["bai_4_sum_max"] is None:
        print("Không có thành phần nào có tổng nhãn chẵn.")
        print(0)
    else:
        print("Tổng chẵn lớn nhất:", ans["bai_4_sum_max"])
        print("Số đỉnh lẻ trong TP đó:", ans["bai_4_odd_count"])
        print("TP đó (danh sách đỉnh):", sorted(ans["bai_4_component"]))


if __name__ == "__main__":
    main()
