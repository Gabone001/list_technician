# service_book.py
# gabriel mihail
# service auto, create a menu with update, delete, add, display all, create service alert and exit


# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# Load data from services.txt
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

owners = []
kms = []

try:
    with open("services.txt", "r") as file:
        for line in file:
            name, km = line.strip().split(",")
            owners.append(name)
            kms.append(int(km))
except FileNotFoundError:
    print("services.txt not found. Starting with empty lists.")



# >>>>>>>>>>>>>>
# Main Menu Loop
# >>>>>>>>>>>>>>

while True:
     print("\nVehicle Service Management System")
     print("1. Update a service record")
     print("2. Delete a service record")
     print("3. Add a service record")
     print("4. Display all records")
     print("5. Create service alert")
     print("6. Save & Exit")

     choice = input("Choose an option: ")

# >>>>>>>>>>>>>>>
# Update a record
# >>>>>>>>>>>>>>>

     if choice == "1":
         name = input("Enter owner name to update: ")
         if name in owners:
             index = owners.index(name)
             new_km = int(input("Enter new kilometres: "))
             kms[index] = new_km
             print("Record updated.")
         else:
             print("Owner not found.")

# >>>>>>>>>>>>>>>
# Delete a record
# >>>>>>>>>>>>>>>

     elif choice == "2":
         name = input("Enter owner name to delete: ")
         if name in owners:
             index = owners.index(name)
             deleted_name = owners.pop(index)
             deleted_km = kms.pop(index)

             with open("deleted.txt", "a") as file:
                 file.write(f"{deleted_name},{deleted_km}\n")

             print("Record deleted and stored in deleted.txt.")
         else:
             print("Owner not found.")

# >>>>>>>>>>>>
# Add a record
# >>>>>>>>>>>>

     elif choice == "3":
         name = input("Enter new owner name: ")
         km = int(input("Enter kilometres since last service: "))
         owners.append(name)
         kms.append(km)
         print("Record added.")

# >>>>>>>>>>>>>>>>>>>
# Display all records
# >>>>>>>>>>>>>>>>>>>

     elif choice == "4":
         print("\nOwner Name                 Kilometres     Service Status")
         print("------------------------------------------------------------")

         for name, km in zip(owners, kms):
            if km < 5000:
                 status = "No Service Needed"
            elif km <= 10000:
                 status = "Service Due Soon"
            else:
                 status = "Service Overdue"

            print(f"{name:<25} {km:<13} {status}")

# >>>>>>>>>>>>
# Create alert
# >>>>>>>>>>>>

     elif choice == "5":
         if len(kms) == 0:
             print("No records available.")
         else:
             max_km = max(kms)
             index = kms.index(max_km)
             print(f"ALERT: {owners[index]} needs servicing immediately!")

# >>>>>>>>>>>
# Save & Exit
# >>>>>>>>>>>>

     elif choice == "6":
         with open("services.txt", "w") as file:
             for name, km in zip(owners, kms):
                 file.write(f"{name},{km}\n")

         print("Data saved. Goodbye.")
         break

     else:
         print("Invalid choice. Try again.")
