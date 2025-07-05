marks = int(input("Enter your marks: ") )
if marks >= 90:
    grade = "A"
elif marks >= 80 and marks <= 89: 
    grade = "B"
elif marks >= 70 and marks <= 79: 
    grade = "C"
elif marks >= 60 and marks <= 69:
    grade = "D"
else:
    grade = "F"

print(grade)





grades = {}
while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Print All Grades")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
    elif choice == '2':
        name = input("Enter name to update: ")
        grade = input("Enter new grade: ")
        grades[name] = grade
    elif choice == '3':
        for name in grades:
            print(name + ": " + grades[name])
    elif choice == '4':
        break
    else:
        print("Invalid choice")




file = open("text.txt", "w")
file.write("Hello tutedude!.\n")
file.write("this is my assignment 2 related to python.\n")
file.close()
print("Content written to 'text.txt' successfully.")



file = open("text.txt", "r")
text = file.read()
print("File text:\n")
print(text)
file.close()
