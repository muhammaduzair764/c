print("ONLINE UNIVERSITY ADMISSION SYSTEM")

# Personal Information
print("\n--- Personal Information ---")

app_id = input("Application ID: ")
name = input("Name: ")
father_name = input("Father Name: ")
gender = input("Gender: ")
phone = input("Phone: ")
email = input("Email: ")

with open("personal.txt", "a") as file:
    file.write("Application ID: " + app_id + "\n")
    file.write("Name: " + name + "\n")
    file.write("Father Name: " + father_name + "\n")
    file.write("Gender: " + gender + "\n")
    file.write("Phone: " + phone + "\n")
    file.write("Email: " + email + "\n")
    file.write("------------------------\n")


# Guardian Information
print("\n--- Guardian Information ---")

guardian_name = input("Guardian Name: ")
relation = input("Relation: ")
guardian_phone = input("Guardian Phone: ")

with open("guardian.txt", "a") as file:
    file.write("Application ID: " + app_id + "\n")
    file.write("Guardian Name: " + guardian_name + "\n")
    file.write("Relation: " + relation + "\n")
    file.write("Guardian Phone: " + guardian_phone + "\n")
    file.write("------------------------\n")


# Address Information
print("\n--- Address Information ---")

address = input("Address: ")
city = input("City: ")
province = input("Province: ")

with open("address.txt", "a") as file:
    file.write("Application ID: " + app_id + "\n")
    file.write("Address: " + address + "\n")
    file.write("City: " + city + "\n")
    file.write("Province: " + province + "\n")
    file.write("------------------------\n")


# Education Information
print("\n--- Education Information ---")

matric_marks = input("Matric Marks: ")
matric_total = input("Matric Total Marks: ")
inter_marks = input("Intermediate Marks: ")
inter_total = input("Intermediate Total Marks: ")
board = input("Board: ")

with open("education.txt", "a") as file:
    file.write("Application ID: " + app_id + "\n")
    file.write("Matric Marks: " + matric_marks + "/" + matric_total + "\n")
    file.write("Intermediate Marks: " + inter_marks + "/" + inter_total + "\n")
    file.write("Board: " + board + "\n")
    file.write("------------------------\n")


# Program Information
print("\n--- Program Preferences ---")

program1 = input("1st Program: ")
program2 = input("2nd Program: ")
program3 = input("3rd Program: ")

with open("program.txt", "a") as file:
    file.write("Application ID: " + app_id + "\n")
    file.write("1st Program: " + program1 + "\n")
    file.write("2nd Program: " + program2 + "\n")
    file.write("3rd Program: " + program3 + "\n")
    file.write("------------------------\n")


# Documents Information
print("\n--- Documents Information ---")

photo = input("Photo Available: ")
cnic = input("CNIC Available: ")
matric_certificate = input("Matric Certificate Available: ")
inter_certificate = input("Intermediate Certificate Available: ")

with open("documents.txt", "a") as file:
    file.write("Application ID: " + app_id + "\n")
    file.write("Photo: " + photo + "\n")
    file.write("CNIC: " + cnic + "\n")
    file.write("Matric Certificate: " + matric_certificate + "\n")
    file.write("Intermediate Certificate: " + inter_certificate + "\n")
    file.write("------------------------\n")


# Additional Information
print("\n--- Additional Information ---")

nationality = input("Nationality: ")
domicile = input("Domicile: ")

with open("application.txt", "a") as file:
    file.write("Application ID: " + app_id + "\n")
    file.write("Nationality: " + nationality + "\n")
    file.write("Domicile: " + domicile + "\n")
    file.write("------------------------\n")


print("\nApplication Saved Successfully!")
print("Data has been saved in separate TXT files.")