import copy
class Company:

    @staticmethod
    def valid_str(str_name):
        """
        checks valid name
        :param: str
        :return: bool
        """
        name_l = str_name.split()
        valid_val = True
        for i in range(len(name_l)):
            if len(name_l[i]) < 2 or not(name_l[i][0].isupper()) or not(name_l[i].isalpha()):
                valid_val = False
            else:
                pass
        return valid_val

    _comparison_type = "net value"

    def __init__(self, name, stocks_num, stock_price, comp_type):
        if Company.valid_str(name):
            self.name = name
        else:
            raise ValueError + "Company name is not valid, mus be long then one character, have first letter in" \
                  + " upper case and only one character of space between each word"

        if isinstance(stock_price, float) or isinstance(stock_price, int):
            self.stock_price = stock_price
        else:
            raise ValueError + "stock price must be an integer or a float"

        if isinstance(stocks_num, int):
            self.stocks_num = stocks_num
        else:
            raise ValueError + "stock number must be an integer"

        if Company.valid_str(comp_type):
            self.comp_type = comp_type
        else:
            raise ValueError + "Company type is not valid, mus be long then one character, have first letter in" \
                  + " upper case and only one character of space between each word"

    def net_worth(self):
        """
        This function return the market cap, calculate the company's market cap
        :return: float or int
        """
        return self.stocks_num * self.stock_price

    def set_name(self, name):
        """
        This function change the company's name
        :param name: str
        :return: bool
        """
        if Company.valid_str(name):
            self.name = name
            return True
        else:
            return False

    def set_stocks_num(self, stocks_num):
        """
        this function change the stocks_num and the stock_price following the new stocks_num
        :param stocks_num: int
        :return: bool
        """
        if isinstance(stocks_num, int):
            self.stock_price = self.net_worth() / stocks_num
            self.stocks_num = stocks_num
            return True
        else:
            return False

    def set_stock_price(self, stock_price):
        """
        this function change the stocks_num and the stocks_price following the new stocks_price
        :param stock_price: float or int
        :return: bool
        """
        if type(stock_price) is int or type(stock_price) is float:
            if self.net_worth() > stock_price:
                self.stocks_num = int(self.net_worth() // stock_price)
                self.stock_price = stock_price
                return True
            else:
                return False
        else:
            return False

    def set_comp_type(self, comp_type):
        """
        This function change the company type
        :param comp_type: str
        :return: bool
        """
        if Company.valid_str(comp_type):
            self.comp_type = comp_type
            return True
        else:
            return False

    def update_net_worth(self, net_worth):
        """
        This function updates the company's market cap and change the stock price following by the new net worth
        :param net_worth: int or float
        :return: bool
        """
        if (type(net_worth) is int or type(net_worth) is float) and (net_worth > 0):
            self.stock_price = net_worth / self.stocks_num
            return True
        else:
            return False

    def add_stocks(self, number):
        """
        This function adds increase the number of stocks the company holds with the number the function gets
        :param number: int
        :return: bool
        """
        if self.stocks_num + number > 0:
            self.stocks_num = self.stocks_num + number
            return True

    @classmethod
    def change_comparison_type(cls, comparison_type):
        if cls._comparison_type is comparison_type:
            return True
        if comparison_type == "stock num":
            cls._comparison_type = comparison_type
            return True
        elif comparison_type == "stock price":
            cls._comparison_type = comparison_type
            return True
        elif comparison_type == "net value":
            cls._comparison_type = comparison_type
            return True
        else:
            return False

    def __str__(self):
        return "(" + self.name + ", " + str(self.stocks_num) + " stocks, Price: " + str(self.stock_price) + ", " \
                + self.comp_type + ", Net Worth: " + str(self.net_worth()) + ")"

    def __repr__(self):
        return "(" + self.name + ", " + str(self.stocks_num) + " stocks, Price: " + str(self.stock_price) + ", " \
               + self.comp_type + ", Net Worth: " + str(self.net_worth()) + ")"

    def __lt__(self, other):
        if isinstance(other, Company):
            if Company._comparison_type == "net value":
                return self.net_worth() < Company.net_worth(other)
            elif Company._comparison_type == "stock num":
                return self.stocks_num < other.stocks_num
            elif Company._comparison_type == "stock price":
                return self.stock_price < other.stock_price
            else:
                raise ValueError("_comparison_type")
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Company):
            if Company._comparison_type == "net value":
                return self.net_worth() > Company.net_worth(other)
            elif Company._comparison_type == "stock num":
                return self.stocks_num > other.stocks_num
            elif Company._comparison_type == "stock price":
                return self.stock_price > other.stock_price
            else:
                raise ValueError("_comparison_type")
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Company):
            if Company._comparison_type == "net value":
                return self.net_worth() == Company.net_worth(other)
            elif Company._comparison_type == "stock num":
                return self.stocks_num == other.stocks_num
            elif Company._comparison_type == "stock price":
                return self.stock_price == other.stock_price
            else:
                raise ValueError("_comparison_type")
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Company):
            if Company._comparison_type == "net value":
                return self.net_worth() >= Company.net_worth(other)
            elif Company._comparison_type == "stock num":
                return self.stocks_num >= other.stocks_num
            elif Company._comparison_type == "stock price":
                return self.stock_price >= other.stock_price
            else:
                raise ValueError("_comparison_type")
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Company):
            if Company._comparison_type == "net value":
                return self.net_worth() <= Company.net_worth(other)
            elif Company._comparison_type == "stock num":
                return self.stocks_num <= other.stocks_num
            elif Company._comparison_type == "stock price":
                return self.stock_price <= other.stock_price
            else:
                raise ValueError("_comparison_type")
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Company):
            if Company._comparison_type == "net value":
                return self.net_worth() != Company.net_worth(other)
            elif Company._comparison_type == "stock num":
                return self.stocks_num != other.stocks_num
            elif Company._comparison_type == "stock price":
                return self.stock_price != other.stock_price
            else:
                raise ValueError("_comparison_type")
        else:
            return False

    def __add__(self, other):
        name = copy.deepcopy(self.name)
        comp_type = copy.deepcopy(self.comp_type)
        stocks_num = self.stocks_num + other.stocks_num
        market_cap = self.net_worth() + other.net_worth()
        stock_price = market_cap / stocks_num
        return Company(name, stocks_num, stock_price, comp_type)


