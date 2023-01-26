def checkAVL(root):
    if root is None:
        return True
    if not (checkAVL(root.left) and checkAVL(root.right)):
        return False
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return True


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
