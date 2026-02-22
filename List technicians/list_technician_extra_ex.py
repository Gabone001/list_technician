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

# >>>>>>>>>>>>>>>>>>
# ADD new technician
# >>>>>>>>>>>>>>>>>>
name = input("Enter a new person: ").strip()
role = input("Enter a title: ").strip()
years = input("Enter the years of experience: ").strip()

if name in  names:
        print("That name is already in the database.")
else:
        names.append(name)
        roles.append(role)
        years_experience.append(years)
with open("staff.txt", "w") as file:
    for name, role, years in zip(names, roles, years_experience):
        file.write(f" {name}, {role}, {years} \n")
        print("New person: ", name,"-" "Role: ", role,"-" "Years Experience: ", years)
        print("Book added successfully.")
