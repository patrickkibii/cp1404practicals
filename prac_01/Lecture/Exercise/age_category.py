# user_age = int(input("Age: "))
# if user_age >= 66:
#     age_category = "old"
# elif user_age >= 18:
#     age_category = "adult"
# elif user_age >= 5:
#     age_category = "Child"
# else:
#     age_category = "baby"
# print(f"You are a/an {age_category}")
# total = 0
# average = 0
# people = int(input("Number of people: "))
# for person in range(people):
#     age = int(input("Age: "))
#     total = age + total
# average = total/people
# print(f"Total {total} Average {average}")


total = 0
average = 0
age = int(input("Age: "))
while age >= 0:
    age = int(input("Age: "))
    total = age + total
    average = total/age
print(average,total)



