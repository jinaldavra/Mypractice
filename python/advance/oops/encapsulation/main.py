# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_make(self):
#         return self.__make
    
#     def set_make(self, make):
#         self.__make = make

#     def get_model(self):
#         return self.__model

#     def set_model(self, model):
#         self.__model = model 

class ATM:
    def __init__(self,pin):
        self.__pin = pin

    def set_pin(self,pin):
        if len(pin) == 4 and pin.isdigit():
            self.__pin = pin
        else:
            raise ValueError("Pin must be a 4-digit number")
        
    def get_pin(self):
        return self.__pin
    
obj = ATM('1234')
obj.set_pin('1345')
print(obj._ATM__pin)
print(obj.get_pin())