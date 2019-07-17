# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        def isReflection(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and node2 and node1.val == node2.val:
                return isReflection(node1.left, node2.right) and isReflection(node1.right, node2.left)
            else:
                return False

        if not root: return True
        else: return isReflection(root.left, root.right)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


if __name__ == '__main__':
    tree1 = '[1,2,2,3,4,4,3]'
    root1 = stringToTreeNode(tree1);
    print( Solution().isSymmetric(root1) )

    tree2 = '[1,2,3,4,5]'
    root2 = stringToTreeNode(tree2);
    print( Solution().isSymmetric(root2) )


# Testing git 
# Mai test git 
