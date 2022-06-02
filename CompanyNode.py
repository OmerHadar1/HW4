from Company import Company
import copy


class CompanyNode(Company):

    _comparison_type = Company._comparison_type

    def __init__(self, name, stocks_num, stock_price, comp_type):
        Company.__init__(self, name, stocks_num, stock_price, comp_type)
        self.__children = []
        self.__parent = None

    def get_parent(self):
        """
        This function print th company node parent
        :return: CompanyNode
        """
        return copy.deepcopy(self.__parent)

    def get_children(self):
        """
        This function print the company node list of children
        :return: list
        """
        return copy.deepcopy(self.__children)

    def is_leaf(self):
        """
        This function tells us if the node is a leaf in the company tree or not
        :return: bool
        """
        if not self.__children:
            return True
        else:
            return False

    def add_child(self, child):
        """
        This function add sub company to the company node children list
        :param child: CompanyNode
        :return: bool
        """
        if isinstance(child, CompanyNode):
            if child <= self:
                for boy in child.__children:
                    if boy in self.__children:
                        pass
                    else:
                        self.__children.append(child)
                child.__parent = self
                return True
            else:
                return False
        else:
            return False

    def total_net_worth(self):
        """
        This function calculate the total sum of net worth of all the children company's of the company node
        :return: int or float
        """
        count = Company.net_worth(self)
        for child in self.__children:
            count += Company.net_worth(child)
        return count

    def test_node_order_validity(self):
        """
        The method checks whether the current node (“self”) satisfies the "Company Node rule" with respect to his
        ancestors and descendants. The method returns the Boolean value True if the conditions are met and False
        otherwise.
        :return: bool
        """
        valid_children = False not in [self >= child for child in self.__children]
        if self.__parent is None:
            return True
        elif valid_children and CompanyNode.test_node_order_validity(self.__parent):
            return True
        else:
            return False

    def __len__(self):
        """
        The method bring the length of thr company node list of children
        :return: int
        """
        return len(self.__children)

    def __repr__(self):
        """
        This method overrides the parent method. The method returns a string that contains the description of the
        company and its descendants.
        :return: str
        """
        res = "[" + Company.__repr__(self)
        for child in self.__children:
            res += Company.__repr__(child) + ","
        return res + "]"

    def is_ancestor(self, other):
        """
        The method checks whether the current node (“self”) is an ancestor to “other”
        :param other: CompanyNode
        :return: bool
        """
        if other in self.__children:
            return True
        else:
            return False

    def __add__(self, other):
        if other.is_ancestor(self):
            raise ValueError("other is not valid")
        else:
            name = Company.__add__(self, other).name
            comp_type = Company.__add__(self, other).comp_type
            stocks_num = Company.__add__(self, other).stocks_num
            stock_price = Company.__add__(self, other).stock_price
            new_company_node = CompanyNode(name, stocks_num, stock_price, comp_type)
            new_company_node.__children = self.__children + other.__children
            new_company_node.__parent = copy.deepcopy(self.__parent)
            return new_company_node

    def set_stock_price(self, stock_price):
        self_try = copy.deepcopy(self)
        Company.set_stock_price(self_try, stock_price)
        if self_try.test_node_order_validity() and Company.set_stock_price(self_try, stock_price):
            return Company.set_stock_price(self, stock_price)
        else:
            return False

    def set_stocks_num(self, stocks_num):
        self_try = copy.deepcopy(self)
        Company.set_stocks_num(self_try, stocks_num)
        if self_try.test_node_order_validity() and Company.set_stocks_num(self_try, stocks_num):
            Company.set_stocks_num(self, stocks_num)
        else:
            return False

    def update_net_worth(self, net_worth):
        self_try = copy.deepcopy(self)
        Company.update_net_worth(self_try, net_worth)
        if self_try.test_node_order_validity() and Company.update_net_worth(self_try, net_worth):
            return Company.update_net_worth(self, net_worth)
        else:
            return False

    def add_stocks(self, number):
        self_try = copy.deepcopy(self)
        Company.add_stocks(self_try, number)
        if self_try.test_node_order_validity() and Company.add_stocks(self_try, number):
            return Company.add_stocks(self, number)
        else:
            return False

    @classmethod
    def change_comparison_type(cls, comparison_type):
        if comparison_type == "total sum":
            cls._comparison_type = "total sum"
        else:
            Company.change_comparison_type(cls, comparison_type)

    def __lt__(self, other):
        if isinstance(other, CompanyNode):
            if CompanyNode._comparison_type == "total sum":
                return self.total_net_worth() == other.total_net_wort()
            else:
                return Company.__lt__(self, other)
        elif type(other) == Company:
            return Company.__lt__(self, other)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, CompanyNode):
            if CompanyNode._comparison_type == "total sum":
                return self.total_net_worth() < other.total_net_wort()
            else:
                return Company.__gt__(self, other)
        elif type(other) == Company:
            return Company.__gt__(self, other)
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, CompanyNode):
            if CompanyNode._comparison_type == "total sum":
                return self.total_net_worth() == other.total_net_wort()
            else:
                return Company.__eq__(self, other)
        elif type(other) == Company:
            return Company.__eq__(self, other)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, CompanyNode):
            if CompanyNode._comparison_type == "total sum":
                return self.total_net_worth() != other.total_net_wort()
            else:
                return Company.__ne__(self, other)
        elif type(other) == Company:
            return Company.__ne__(self, other)
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, CompanyNode):
            if CompanyNode._comparison_type == "total sum":
                return self.total_net_worth() >= other.total_net_wort()
            else:
                return Company.__ge__(self, other)
        elif type(other) == Company:
            return Company.__ge__(self, other)
        else:
            return False

    def __le__(self, other):
        if isinstance(other, CompanyNode):
            if CompanyNode._comparison_type == "total sum":
                return self.total_net_worth() <= other.total_net_wort()
            else:
                return Company.__le__(self, other)
        elif type(other) == Company:
            return Company.__le__(self, other)
        else:
            return False



