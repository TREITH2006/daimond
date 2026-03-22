class fruits:
    def colour(self):
        pass
class apple(fruits):
    def colour(self):
        print("red")
class orange(fruits):
    def colour(self):
        print("orange")
a=apple()
a.colour()
o=orange()
o.colour()