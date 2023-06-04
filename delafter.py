class A(type):
    def __new__(cls, name, bases, attrs):
        attrs['my_attr'] = 'Hello'

        return super().__new__(cls, name, bases, attrs)

class B(metaclass=A):
    pass

print(B().my_attr)
