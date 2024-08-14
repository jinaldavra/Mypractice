from abc import ABC, abstractmethod

class ANIMAL(ABC):
    @abstractmethod
    def sound():
        pass

class DOG(ANIMAL):
    def sound(self):
        return "Bark"
    
class CAT(ANIMAL):
    def sound(self):
        return "Meow"
    
obj_of_dog = DOG()

# print(dir(DOG))
print(obj_of_dog.sound())

obj_of_cat = CAT()

# print(dir(CAT))
# print(obj_of_cat.sound())