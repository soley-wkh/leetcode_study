# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/5 20:21
    file   : binary_tree.py
    
"""


# 树节点的定义
class Node:
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.lchild = lchild  # 表示左子树
        self.rchild = rchild  # 表示又子树
        self.data = data  # 表示数据域


# 递归创建二叉树
class Tree:
    def __init__(self, root=None):
        self.root = root

    def create(self):
        self.root = self.b_create(self.root)

    # 递归创建二叉树
    def b_create(self, root, type="root"):
        if type == 'root':
            data = input("请输入根节点数据：")
        elif type == "left":
            data = input("请输入{}左子树数据：".format(root.data))
        else:
            data = input("请输入{}右子树数据：".format(root.data))
        if data is "#":
            root = None
        else:
            root = Node(data)
            root.lchild = self.b_create(root, "left")
            root.rchild = self.b_create(root, "right")
        return root

    def level_traversal(self):
        """

        :return:lst
        """
        lst = []
        # 队列
        queue = [self.root]
        while len(queue) > 0:
            # 出队
            node = queue.pop(0)
            if node:
                # 加入列表
                lst.append(node.data)
                # 若有左子树,左子树入队
                if node.lchild:
                    queue.append(node.lchild)
                # 若有右子树，右子树入队
                if node.rchild:
                    queue.append(node.rchild)
        return lst

    # 先序遍历
    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, root, list1=[]):
        if root:
            list1.append(root.data)
        if root.lchild:
            self._preorder_traversal(root.lchild, list1)
        if root.rchild:
            self._preorder_traversal(root.rchild, list1)
        return list1

    # 中序遍历
    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, root, list1=[]):
        if root.lchild:
            self._inorder_traversal(root.lchild, list1)
        if root:
            list1.append(root.data)
        if root.rchild:
            self._inorder_traversal(root.rchild, list1)
        return list1

    # 后序遍历
    def postorder_traversal(self):
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, root, list1=[]):
        if root.lchild:
            self._postorder_traversal(root.lchild, list1)
        if root.rchild:
            self._postorder_traversal(root.rchild, list1)
        if root:
            list1.append(root.data)
        return list1

    # 求深度
    def deep(self):
        return self._deep(self.root, 0, 0)

    def _deep(self, root, ld, rd):
        if not root:
            return 0
        ld = self._deep(root.lchild, ld, rd)
        rd = self._deep(root.rchild, ld, rd)
        return ld + 1 if ld > rd else rd + 1


tree = Tree()
tree.create()
print("根节点：", tree.root.data)  # 0
print("根节点左子树：", tree.root.lchild.data)  # 1
print("根节点左子树的右子树：", tree.root.lchild.rchild.data)  # 3
print("根节点右子树：", tree.root.rchild.data)  # 2
print("层次遍历：", tree.level_traversal())
print("先序遍历：", tree.preorder_traversal())
print("中序遍历：", tree.inorder_traversal())
print("后序遍历：", tree.postorder_traversal())
print("二叉树的深度：", tree.deep())
