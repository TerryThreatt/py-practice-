# 4 principles of OOP (Abstration - Inheritance - Encapsulation - Polymorphism)

# _name   - private variable
# __name  - name mangling
# __name__  - dunder method


class User:

    # class variable
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    # constructor - initialization
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        print(f"{self.first} has been created!")

    def __repr__(self):
        return f"{self.first}"

    # instance methods
    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"


# instantiate new User
user1 = User("Joe", "Smith", 40)
print(User.display_active_users())
User.from_string("Jon,Stones, 63")

# output
print(User.active_users)
