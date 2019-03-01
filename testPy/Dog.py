class Dog():
    """docstring for Dog"""
    def __init__(self, name ,age):
        super(Dog, self).__init__()
        self.age = age
        self.name= name

    def sit(self):
        print(self.name.title() + " is now sitting.")
        