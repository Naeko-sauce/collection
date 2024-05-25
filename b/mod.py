class prson:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        if isinstance(other, prson):
            return "{0}----{1}".format(self.name, other.name)
        else:
            return "no"

    def __mul__(self, other):
        if isinstance(other, int):
            return self.name  * other
        else:
            return "no"

p1 = prson("12")
p2 = prson("423")
x = p1 * p2
print(x)