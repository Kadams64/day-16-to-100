def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1,2,3,4,5))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # get prevents failure for missing parameters
        self.model = kw.get("model") # such values will be populated with 'None'

my_car = Car(make="Nissan")
print(my_car.model)