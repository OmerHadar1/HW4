import copy

from Company import Company
from CompanyNode import CompanyNode


class CompanyTree:
    def __init__(self, root=None):
        if isinstance(root, CompanyNode) and root.__parent is None:
            self.__root = root
        else:
            raise ValueError("root is not valid")

    def set_root(self, root):
        if isinstance(root, CompanyNode) and root.__parent is None:
            self.__root = root
            return True
        else:
            return False

    def get_root(self):
        return self.__root

    @staticmethod
    def grown_child(father):
        for child in father.__children:
            child.__parent is None

    @staticmethod
    def no_children(self=list):
        for child in self:
            self.remove(child)

    @staticmethod
    def tree_list(lst):
        new_lst = []
        for child in lst:
            new_lst.append(child)
            new_lst.append(" * ")
        return new_lst

    def __str__(self):
        CompanyTree.grown_child(self.__root)
        new_children = copy.deepcopy(self.__root.__children)
        for child in new_children:
            CompanyTree(child)
        new_children_new = copy.deepcopy(new_children)
        CompanyTree.no_children(new_children_new)
        return self.__root.name + "\n" + repr(new_children_new)


    def __iter__(self):
        pass

    def __next__(self):
        pass

    def insert_node(self, node):
        if isinstance(node, CompanyNode) and node.__parent is None:
            pass

    def remove_node(self, name):
        pass
