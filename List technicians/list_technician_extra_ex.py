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
