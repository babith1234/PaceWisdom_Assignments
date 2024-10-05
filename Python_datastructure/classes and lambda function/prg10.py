class MyClass:
    pass

instance = MyClass()
class_name = instance.__class__.__name__

print("The class name of the instance is:", class_name)
