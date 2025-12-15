"""
Đỉnh được đánh số từ 1..n.

Với đồ thị có hướng: để dùng đúng DFS cơ bản, ta xét "liên thông yếu"
(bỏ hướng các cạnh) rồi tìm thành phần liên thông như đồ thị vô hướng.
"""


def build_adj(n, edges, directed=False):
    """Tạo danh sách kề.
    directed=False  -> vô hướng
    directed=True   -> có hướng (nhưng khi làm liên thông yếu, ta vẫn thêm 2 chiều)
    """

    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def dfs(start, adj, visited):
    """DFS (dùng stack) trả về danh sách các đỉnh trong 1 thành phần."""

    stack = [start]
    visited[start] = True
    comp = []

    while stack:
        u = stack.pop()
        comp.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    return comp


def get_components(n, edges, directed=False):
    """Lấy các thành phần liên thông.

    - Vô hướng: DFS trực tiếp
    - Có hướng: liên thông yếu -> bỏ hướng cạnh (thêm cả 2 chiều) rồi DFS
    """

    if directed:
        adj = build_adj(n, edges, directed=False)  # bỏ hướng
    else:
        adj = build_adj(n, edges, directed=False)

    visited = [False] * (n + 1)
    components = []
    for v in range(1, n + 1):
        if not visited[v]:
            components.append(dfs(v, adj, visited))
    return components


def solve_homework(components):
    """Trả về kết quả 4 bài (dùng đúng DFS ở trên)."""

    # Bài 1: số thành phần liên thông
    bai_1 = len(components)

    # Bài 2: thành phần có số đỉnh nhiều nhất
    max_size = 0
    for comp in components:
        if len(comp) > max_size:
            max_size = len(comp)
    bai_2_components = [comp for comp in components if len(comp) == max_size]

    # Bài 3: đếm số TP có tổng nhãn đỉnh chẵn
    bai_3 = 0
    even_sum_components = []
    for comp in components:
        s = sum(comp)
        if s % 2 == 0:
            bai_3 += 1
            even_sum_components.append(comp)

    # Bài 4: trong các TP có tổng chẵn, lấy TP có tổng lớn nhất, đếm số đỉnh lẻ
    if not even_sum_components:
        bai_4_sum_max = None
        bai_4_odd_count = 0
        bai_4_comp = []
    else:
        bai_4_comp = even_sum_components[0]
        bai_4_sum_max = sum(bai_4_comp)
        for comp in even_sum_components[1:]:
            s = sum(comp)
            if s > bai_4_sum_max:
                bai_4_sum_max = s
                bai_4_comp = comp

        bai_4_odd_count = 0
        for x in bai_4_comp:
            if x % 2 != 0:
                bai_4_odd_count += 1

    return {
        "bai_1": bai_1,
        "bai_2_max_size": max_size,
        "bai_2_components": bai_2_components,
        "bai_3": bai_3,
        "bai_4_sum_max": bai_4_sum_max,
        "bai_4_odd_count": bai_4_odd_count,
        "bai_4_component": bai_4_comp,
    }


# 8 5
# 0
# 1 2
# 2 3
# 4 5
# 6 7
# 7 8


# 8 6
# 1
# 1 2
# 2 3
# 4 5
# 5 4
# 6 7
# 8 8
