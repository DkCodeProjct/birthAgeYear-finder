user_input = input("find :Birth_Year/Current_Age: \n enter(BY/CA) ").lower()

if user_input == "by":
    user_age = int(input("current_age: "))
    result_0 = 2023 - user_age
    print(f"birth year was {result_0}")

elif user_input == "ca":
    userBirth_year = int(input("birth_year: "))
    result_1 = 2023 - userBirth_year
    print(f"your age is {result_1}")

else:
    print("invalid input")
    


