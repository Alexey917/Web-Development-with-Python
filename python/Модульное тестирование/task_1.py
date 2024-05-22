class SumOfElem:
    def __init__(self):
        self.elements = [5, -9, 34, -12, 187, -101, 1563]

    def sum_of_elem(self):
        s = 0
        for i in self.elements:
            s += i
        return s


class AdapterMid:
    def __init__(self, obj):
        self.obj = obj

    def mid(self):
        middle = self.obj.sum_of_elem() / len(self.obj.elements)
        return middle


class AdapterMax:
    def __init__(self, obj):
        self.obj = obj

    def max_of_elem(self):
        res = max(self.obj.elements)
        return res


class AdapterMin:
    def __init__(self, obj):
        self.obj = obj

    def min_of_elem(self):
        res = min(self.obj.elements)
        return res


sum_of_elem = SumOfElem()
print(sum_of_elem.sum_of_elem())

mid = AdapterMid(sum_of_elem)
print(mid.mid())

maximum = AdapterMax(sum_of_elem)
print(maximum.max_of_elem())

minimum = AdapterMin(sum_of_elem)
print(minimum.min_of_elem())
