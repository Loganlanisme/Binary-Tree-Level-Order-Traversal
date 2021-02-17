class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []

        stack = [root]

        while stack:
            level_values = []
            for i in range(len(stack)):
                top = stack.pop(0)
                level_values.append(top.val)

                if top.left:
                    stack.append(top.left)
                if top.right:
                    stack.append(top.right)

            result.append(level_values)
        return result