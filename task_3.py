from tree import AVLNode, create_tree

# Для того щоб знайти суму всіх значень в дереві, потрібно пройтись по всіх гілках дерева
def find_sum(node: AVLNode | None) -> int:
    if node is None:
        return 0
    return node.key + find_sum(node.left) + find_sum(node.right)

def main() -> None:
    keys = [9, 5, 10, 14, 0, 6, 11, 18, -1, 1, -4, 2]
    
    root = create_tree(keys)

    print("Сума значень:", find_sum(root))
    print("Перевірка:", sum(keys))
    
if __name__ == "__main__":
    main()