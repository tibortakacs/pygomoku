import rulematcher.rules.rules as rules

class Matcher:
    def __init__(self, x_val = 1, o_val = 2, e_val = 0):
        self.__vals = {
            x_val : rules.cell_x,
            o_val : rules.cell_o,
            e_val : rules.cell_e
        }

    # Check whether the rule fits on the row or not. If it fits, it returns the index of the currently empty element
    # which has to be transformed to x, otherwise it returns -1.
    def match(self, rule, row):
        row = [self.__vals[v] for v in row]

        if len(rule) != len(row):
            return -1

        index = -1
        for i in range(len(row)):
            if row[i] == rules.cell_e and rule[i] == rules.cell_X:
                if index == -1:
                    index = i
                else:
                    return -1
            elif row[i] != rule[i]:
                return -1

        return index
