import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def get_color_sequence(nodes):
    cmap = plt.get_cmap("Blues")  # Use a colormap to generate colors
    norm = mcolors.Normalize(vmin=0, vmax=len(nodes) - 1)
    return [mcolors.rgb2hex(cmap(norm(i))) for i in range(len(nodes))]


def get_colors(nodes):
    n = len(nodes)
    colors = []
    for i in range(n):
        alpha = int(255 * (1 - i / (n - 1)))
        hex_color = f"#{alpha:02X}0000FF"
        colors.append(hex_color)
    return colors


def dfs_order(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited


def bfs_order(root):
    queue = [root]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited


def draw_tree(tree_root, move_order):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = get_colors(move_order)
    node_colors = {node.id: colors[i] for i, node in enumerate(move_order)}

    colors = [node_colors.get(node[0], "skyblue") for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("DFS")
dfs_order = dfs_order(root)
draw_tree(root, dfs_order)

print("BFS")
bfs_order = bfs_order(root)
draw_tree(root, bfs_order)
