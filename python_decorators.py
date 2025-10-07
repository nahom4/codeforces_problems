class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value


    

obj = MyClass(5)
print(obj.value)
obj.value = 12
print(obj.value)
del obj.value
print(obj.value)

