# list_technician_extra_ex.py
# gabriel mihail
# create a Python file using Git, code to read from the file into three lists

# >>>>>>>>>>>>>>>>>>>>>>>>>
# LOAD DATA INTO LISTS
# >>>>>>>>>>>>>>>>>>>>>>>>>

# names = []
# roles = []
# years_experience = []
#
# with open("staff.txt", "r") as file:
#     for line in file:
#         parts = line.strip().split(",")
#         names.append(parts[0].strip())
#         roles.append(parts[1].strip())
#         years_experience.append(int(parts[2].strip()))
# print("Names          | Roles           |Years Experience")
# print("--------------------------------------------------")
# for name, role, years in zip(names, roles, years_experience):
#   print(f"{name:<20} | {role:<28} | {years:>5}")
# print("\nTotal number: ", len(names))

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

# longest_name = max(names, key=len)
# length = len(longest_name)
#
# print("Longest Technician Name Result: ")
# print(f"Longest name: {longest_name}")
# print(f"Number of characters: {length}")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 7 - Filter by role.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# search_role = input("\nEnter a job role to search for: ").strip()
#
# # Find all technicians matching that role
# matched_names = []
#
# for name, role in zip(names, roles):
#     if role.lower() == search_role.lower():
#         matched_names.append((name))
#
# # Display results
# if matched_names:
#     print("\nTechnicians with the role:", search_role)
#     print("--------------------------------------------------")
#     for tech in matched_names:
#         print(tech)
# else:
#     print("\nNo technicians found with that role.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 8 - Classifies the technicians by years of experience.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# junior_count = 0
# mid_count = 0
# senior_count = 0
#
# for years in years_experience:
#     if years < 3:
#         junior_count += 1
#     elif 3 <= years <= 6:
#         mid_count += 1
#     else:  # years > 6
#         senior_count += 1
#
# print("\nTechnician Experience Categories")
# print("--------------------------------")
# print(f"Junior (<3 years): {junior_count}")
# print(f"Mid-level (3–6 years): {mid_count}")
# print(f"Senior (>6 years): {senior_count}")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 9 - report generation.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 1. Total technicians
# total_techs = len(names)
#
# # 2. Average years of experience
# average_experience = sum(years_experience) / total_techs
#
# # 3. Longest technician name
# longest_name = max(names, key=len)
# longest_name_length = len(longest_name)
#
# # 4. Categorization counts
# junior = 0
# mid = 0
# senior = 0
#
# for years in years_experience:
#     if years < 3:
#         junior += 1
#     elif 3 <= years <= 6:
#         mid += 1
#     else:
#         senior += 1
#
# # 5. Write report to file
# with open("report.txt", "w") as report:
#     report.write("IT TECHNICIAN SUMMARY REPORT\n")
#     report.write("-----------------------------------\n")
#     report.write(f"Total number of technicians: {total_techs}\n")
#     report.write(f"Average experience: {average_experience:.2f} years\n")
#     report.write(f"Technician with the longest name: {longest_name}\n")
#     report.write(f"Length of longest name: {longest_name_length} characters\n")
#     report.write("\nExperience categories:\n")
#     report.write(f"  Junior (<3 years): {junior}\n")
#     report.write(f"  Mid-level (3–6 years): {mid}\n")
#     report.write(f"  Senior (>6 years): {senior}\n")
#
# print("\nReport successfully generated in 'report.txt'.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 10 - saving edits.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>


# with open("staff.txt", "w") as file:
#     for name, role, years in zip(names, roles, years_experience):
#         file.write(f"{name}, {role}, {years}\n")
#
# print("\nAll changes have been successfully saved to staff.txt.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 11 - menu driven system.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


names = []
roles = []
years_experience = []
filename = "staff.txt"

# ================== LOAD FILE ==================
with open(filename, "r") as file:
    for line in file:
        n, r, y = line.strip().split(",")
        names.append(n.strip())
        roles.append(r.strip())
        years_experience.append(int(y.strip()))

# ================== MENU LOOP ==================
while True:
    print("\n===== IT TECHNICIAN MANAGEMENT SYSTEM =====")
    print("1. Add Technician")
    print("2. Edit Technician")
    print("3. Delete Technician")
    print("4. View All")
    print("5. Filter by Job Role")
    print("6. Generate Report")
    print("7. Exit")

    option = input("Choose an option: ")

    # ---------- ADD ----------
    if option == "1":
        name = input("Enter name: ").strip()
        role = input("Enter role: ").strip()
        years = int(input("Enter years of experience: "))

        names.append(name)
        roles.append(role)
        years_experience.append(years)

        print(f"\n{name} added successfully!")

    # ---------- EDIT ----------
    elif option == "2":
        name = input("Enter technician name to edit: ").strip()

        if name not in names:
            print("Technician not found.")
            continue

        index = names.index(name)

        print("\n1. Edit Role")
        print("2. Edit Years Experience")
        choice = input("Choose option: ")

        if choice == "1":
            new_role = input("Enter new role: ").strip()
            roles[index] = new_role
            print("Role updated.")
        elif choice == "2":
            new_years = int(input("Enter new years: "))
            years_experience[index] = new_years
            print("Experience updated.")
        else:
            print("Invalid option.")

    # ---------- DELETE ----------
    elif option == "3":
        name = input("Enter technician name to delete: ").strip()

        if name not in names:
            print("Technician not found.")
            continue

        index = names.index(name)

        del names[index]
        del roles[index]
        del years_experience[index]

        print(f"{name} deleted successfully!")

    # ---------- VIEW ALL ----------
    elif option == "4":
        print("\nNAME                 | ROLE                    | YEARS")
        print("------------------------------------------------------------")
        for n, r, y in zip(names, roles, years_experience):
            print(f"{n:<20} | {r:<20} | {y:>3}")
        print("\nTotal technicians:", len(names))

    # ---------- FILTER ----------
    elif option == "5":
        role = input("Enter job role to filter by: ").strip()
        print(f"\nTechnicians with role '{role}':")

        found = False
        for n, r in zip(names, roles):
            if r.lower() == role.lower():
                print(n)
                found = True

        if not found:
            print("No technicians found.")

    # ---------- REPORT ----------
    elif option == "6":
        total = len(names)
        avg_exp = sum(years_experience) / total
        longest = max(names, key=len)
        length_longest = len(longest)

        junior = sum(1 for y in years_experience if y < 3)
        mid = sum(1 for y in years_experience if 3 <= y <= 6)
        senior = sum(1 for y in years_experience if y > 6)

        with open("report.txt", "w") as rep:
            rep.write("IT Technicians Summary Report\n")
            rep.write("-----------------------------------\n")
            rep.write(f"Total technicians: {total}\n")
            rep.write(f"Average experience: {avg_exp:.2f} years\n")
            rep.write(f"Longest name: {longest} ({length_longest} chars)\n")
            rep.write("\nExperience categories:\n")
            rep.write(f"Junior (<3): {junior}\n")
            rep.write(f"Mid-level (3–6): {mid}\n")
            rep.write(f"Senior (>6): {senior}\n")

        print("\nReport generated as 'report.txt'!")

    # ---------- EXIT ----------
    elif option == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")