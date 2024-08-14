# Overloading method :

# class Math:
#     def add(self,a,b):
#         return a + b
                                          # This code showing overloading error  
#     def add(self,a,b,c):
#         return a + b + c
    
# obj_of_add = Math()
# print(obj_of_add.add(10,20,30))

class Math:
    def add(self, a = None, b = None, c = None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        
        elif a is not None and b is not None:
            return a + b
        
        else:
            raise ValueError("At least two number must be provided.")
        
obj_of_add = Math()
print(obj_of_add.add(10,20,30))
        
    