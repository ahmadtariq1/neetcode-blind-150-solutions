from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        res = []
        q = deque([root])
        level = 0
        
        while q:

            temp = []

            for i in range(len(q)):
                temp_node = q.popleft()
                temp.append(temp_node.val)

                if temp_node.left:
                    q.append(temp_node.left)
                
                if temp_node.right:
                    q.append(temp_node.right)

            level += 1
            res.append(temp)
            


        return res