# list_technician_extra_ex.py
# gabriel mihail
# create a Python file using Git, code to read from the file into three lists

# >>>>>>>>>>>>>>>>>>>>>>>>>
# LOAD DATA INTO LISTS
# >>>>>>>>>>>>>>>>>>>>>>>>>

names = []
roles = []
years_experience = []

with open("staff.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        names.append(parts[0].strip())
        roles.append(parts[1].strip())
        years_experience.append(int(parts[2].strip()))
print("Names          | Roles           |Years Experience")
print("--------------------------------------------------")
for name, role, years in zip(names, roles, years_experience):
  print(f"{name:<20} | {role:<28} | {years:>5}")
print("\nTotal number: ", len(names))

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # Exercise 2- ADD new technician
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# name = input("Enter a new person: ").strip()
# role = input("Enter a title: ").strip()
# years = input("Enter the years of experience: ").strip()
#
# if name in  names:
#         print("That name is already in the database.")
# else:
#         names.append(name)
#         roles.append(role)
#         years_experience.append(years)
# with open("staff.txt", "w") as file:
#     for name, role, years in zip(names, roles, years_experience):
#         file.write(f" {name}, {role}, {years} \n")
#         print("New person: ", name,"-" "Role: ", role,"-" "Years Experience: ", years)
#         print("Book added successfully.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 3- Delete a technician
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# name = input("Enter a person that left: ").strip()
#
# if name not in  names:
#         print("That name is not in the database. ")
# else:
#     index = names.index(name)
#     del names[index]
#     del roles[index]
#     del years_experience[index]
#     with open("staff.txt", "w") as file:
#         for name, role, years in zip(names, roles, years_experience):
#             file.write(f" {name}, {role}, {years} \n")
#     print("Book deleted successfully. ")

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # Exercise 4- Update technician's details or years of experience
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# name = input("\nEnter technician's name: ").strip()
#
# if name not in names:
#     print("That name is not in the database.")
# else:
#     index = names.index(name)   # <--- IMPORTANT
#
#     print("\nWhat would you like to update?")
#     print("1. Job Role")
#     print("2. Years of Experience")
#     choice = input("Choose (1/2): ")
#
#     if choice == "1":
#         new_role = input("Enter new job role: ")
#         roles[index] = new_role
#
#     elif choice == "2":
#         new_years = int(input("Enter new years of experience: "))
#         years_experience[index] = new_years
#
#     else:
#         print("Invalid option!")
#
#     # Save all lists back to file
#     with open("staff.txt", "w") as file:
#         for n, r, y in zip(names, roles, years_experience):
#             file.write(f"{n},{r},{y}\n")
#
#     # Show updated record
#     print("\nUpdated Technician Record:")
#     print(f"Name: {names[index]}")
#     print(f"Role: {roles[index]}")
#     print(f"Experience: {years_experience[index]} years")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 5- Average, the highest and the lowest years of experience.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# average = sum(years_experience) / len(years_experience)
# print(f"Average years experience: {average}")
# print(max(years_experience))
# print(min(years_experience))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 6- Find the longest name.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

longest_name = max(names, key=len)
length = len(longest_name)

print("Longest Technician Name Result: ")
print(f"Longest name: {longest_name}")
print(f"Number of characters: {length}")
