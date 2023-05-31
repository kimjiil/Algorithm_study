class Node:
    def __init__(self, node_info):
        self.idx = node_info[2]
        self.x = node_info[0]
        self.y = node_info[1]
        self.right = None
        self.left = None

    def set_child(self, node):
        if self.x < node.x:
            self.right = node
        else:
            self.left = node

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, node_info):

        node = Node(node_info)
        if self.root is None:
            self.root = node
        else:
            cur_node = self.root

            while True:
                if cur_node.x < node.x:
                    if cur_node.right:
                        cur_node = cur_node.right
                    else:
                        cur_node.right = node
                        return
                else:
                    if cur_node.left:
                        cur_node = cur_node.left
                    else:
                        cur_node.left = node
                        return

def solution(nodeinfo):
    nodeinfo = [[x, y, i + 1] for i, (x, y) in enumerate(nodeinfo)]
    answer = [[],[]]
    a = sorted(nodeinfo, key=lambda x: (x[1], -x[0]), reverse=True)
    tree = Tree()
    for node_info in a:
        tree.add_node(node_info)

    visit_q = [tree.root]

    while len(visit_q) > 0:
        node = visit_q.pop(-1)
        answer[0].append(node.idx)
        if node.right:
            visit_q.append(node.right)
        if node.left:
            visit_q.append(node.left)

    visit_q = [tree.root]
    while len(visit_q) > 0:
        node = visit_q[-1]

        has_right = False
        has_left = False
        if node.right and not node.right.idx in answer[1]:
            visit_q.append(node.right)
            has_right = True
        if node.left and not node.left.idx in answer[1]:
            visit_q.append(node.left)
            has_left = True

        if not has_left and not has_right:
            visited_node = visit_q.pop(-1)
            answer[1].append(visited_node.idx)

    return answer


nodeinfo = [[5,3, 1],[11,5, 2],[13,3, 3],[3,5, 4],[6,1, 5],[1,3, 6],[8,6, 7],[7,2, 8],[2,2, 9]]
answer = solution(nodeinfo)
result = [[7,4,6,9,1,8,5,2,3],
          [9,6,5,8,1,4,3,2,7]]

print(answer)
