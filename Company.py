class Company:
    @staticmethod  # methods for checking valid input
    def valid_str(str_name):
        name_l = slice(str_name, step=" ")
        valid_val = True
        for i in range(name_l):
            if len(name_l[i]) < 2 and not name_l[i][0].isupper:
                valid_val = False
            else:
                pass
        return valid_val

    def __init__(self, name, stock_num, stock_price, comp_type):
        if Company.valid_str(name):
            self.name = name
        else:
            raise ValueError + "Company name is not valid, mus be long then one character, have first letter in" \
                  + " upper case and only one character of space between each word"

        if isinstance(stock_price, float):
            self.stock_price = stock_price
        else:
            raise ValueError + "stock price must be an integer or a float"

        if isinstance(stock_num, int):
            self.stock_num = stock_num
        else:
            raise ValueError + "stock number must be an integer"

        if Company.valid_str(comp_type):
            self.comp_type = comp_type
        else:
            raise ValueError + "Company type is not valid, mus be long then one character, have first letter in" \
                  + " upper case and only one character of space between each word"
