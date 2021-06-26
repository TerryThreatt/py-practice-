# ask for age

age = input("How old are you: ")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but you need a wristband!")
    elif age >= 21:
        print("You are good to enter and can drink!")
    else:
        print("You can't come in!")
else:
    print("Please enter an age!")
# 18 - 21 wristband
# 21+ drink, normal entry
# too young, sorry