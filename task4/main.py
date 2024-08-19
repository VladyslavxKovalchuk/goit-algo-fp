import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    @staticmethod
    def get_height(node):
        if node is None:
            return 0
        return 1 + max(Node.get_height(node.left), Node.get_height(node.right))


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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def heapify_node(node, maximize=True):
    if node is None:
        return
    root_node = node
    if node.left:
        if (maximize and node.left.val > root_node.val) or (
            not maximize and node.left.val < root_node.val
        ):
            root_node = node.left
    if node.right:
        if (maximize and node.right.val > root_node.val) or (
            not maximize and node.right.val < root_node.val
        ):
            root_node = node.right
    if root_node != node:
        node.val, root_node.val = root_node.val, node.val
        heapify_node(root_node)


def get_nodes_at_depth(node, depth):
    nodes = []

    def traverse(n, d):
        if n is None:
            return
        if d > depth:
            return
        if d == depth:
            nodes.append(n)
        else:
            traverse(n.left, d + 1)
            traverse(n.right, d + 1)

    traverse(node, 0)
    return nodes


def heapify_tree(root, maximize=True):
    height = Node.get_height(root)
    for level in range(height - 1, -1, -1):
        nodes_at_level = get_nodes_at_depth(root, level)
        for n in nodes_at_level:
            heapify_node(n, maximize)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

heapify_tree(root)
draw_tree(root)
