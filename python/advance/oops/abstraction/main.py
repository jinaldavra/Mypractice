from abc import ABC, abstractmethod

class RBI(ABC):
    # @abstractmethod
    def loan_interest(self):
        pass

class SBI(RBI):
    def loan_interest(self):
        return 8.5
    
class IDBI(RBI):
    def loan_interest(self):
        return 9.0
    
class HDFC(RBI):
    def loan_interest(self):
        return 5.0
    
obj_of_sbi = SBI()

# print(dir(obj_of_sbi))
# print(obj_of_sbi.loan_interest())

obj_of_idbi = IDBI()

# print(dir(obj_of_idbi))
# print(obj_of_idbi.loan_interest())

obj_of_hdfc = HDFC()

# print(dir(obj_of_hdfc))
print(obj_of_hdfc.loan_interest())

