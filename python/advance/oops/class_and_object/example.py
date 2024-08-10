class Hostel_Entry:
    class Person_Info:
        def __init__(self, age, gender, status):
            self.age = age
            self.gender = gender
            self.status = status

        def validate_age(self):
            if (self.age) > 25:
                return False
            return True
        
        def validate_gender(self):
            if self.gender.lower() == "male":
                return False
            return True
        
        def validate_status(self):
            if self.status.lower() == "married":
                return False
            return True
        
        def display_info(self):
            if self.validate_age() and self.validate_gender() and self.validate_status():
                print("You got entry.")
            else:
                print("Sorry ! you are not allowed.")

    class Entry:
        def __init__(self, gender, status):
            self.gender = gender
            self.status = status

        def entry_permit(self):
            if self.gender.lower() == "female" and self.status.lower() == "single":
                print("You can enter in the hostel.")
            else:
                print("Sorry, You are not allowed here.")

student = Hostel_Entry()

student1 = Hostel_Entry.Person_Info(23, "male", "married")
student1.display_info()

entry_person_1 =  Hostel_Entry.Entry("male", "married")
entry_person_1.entry_permit()

while(1):
    gender = input("Enter your gender : ")
    status = input("Enter your status : ")
    entry_person = Hostel_Entry.Entry(gender, status)
    entry_person.entry_permit()
    break
