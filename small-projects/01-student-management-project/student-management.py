import json
import os

# Change the directory for the project
os.chdir("F:\\python\\small-projects\\01-student-management-project")

STUDENT_FILE = 'students.json'


# Function to load students from the JSON file
def load_students(): 
    with open(STUDENT_FILE, 'r') as file:
        try:
            return json.load(file)
        except FileNotFoundError:
           return [] 

# Function to list all students
def list_students():
    students = load_students()
    
    if not students:
        print("No students found.")
        return
    
    print(f"List of {len(students)} students:\n")
    
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']} ({student['roll_number']}) - {student['course']} - {student['marks']} Marks")

# save student function
def save_student(students):
    with open(STUDENT_FILE,'w')as file:
        json.dump(students,file,indent=4)

# take user choice
def user_choice(text):
    choice=int(input(text))
    if not isinstance(choice, int):
        print("Invalid choice. Please enter a number.")
    return choice

def passed_students():
    students=load_students()

    print("\n *** Passed students ***")
    for index,student in enumerate(students,start=1):
        if(student["marks"]>40):
            print(f"{index}. {student['name']} ({student['roll_number']}) - {student['course']} - {student['marks']} Marks")

def students_by_course():
    students=load_students()

    course_name=input("\nEnter course name by which you want to filter:").strip().lower()
    print(f"\n*** Students having course name {course_name} ***")
    count=0
    for student in students:
        if(student["course"].strip().lower()==course_name):
            count=count+1
            print(f"{count}. {student['name']} ({student['roll_number']}) - {student['course']} - {student['marks']} Marks")

    print(f"Total students:{count}")    

    if(count==0):
            print(f"No students found with {course_name} course name")  

def get_remaining_students(student,choice):
    if(student["roll_number"] != choice):
        return student


# delete student function
def delete_student():
    students=load_students()
    choice=user_choice("\nEnter the roll_no of the student:")

    new_students = filter(lambda student: get_remaining_students(student, choice), students)
    students=list(new_students)
    save_student(students)
    print("Student deleted successfully!")


# search student by roll no
def search_by_roll_no():
    students=load_students()
    choice=user_choice("\nEnter the roll_no:")

    students=list(filter(lambda student:student["roll_number"] == choice , students))
    if not students:
        print("*** Sorry the student your looking for is not found ***")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']} ({student['roll_number']}) - {student['course']} - {student['marks']} Marks")


def search_by_student_name():
    students = load_students()
    name = input("Enter user name:").strip().lower()
    matching_students = []
    
    for student in students:
        if name in student['name'].lower():
            matching_students.append(student)
    if not matching_students:
        print("*** Sorry, the student you're looking for is not found ***")
    else:
        for index, student in enumerate(matching_students, start=1):
            print(f"{index}. {student['name']} ({student['roll_number']}) - {student['course']} - {student['marks']} Marks")


# search the student 
def search_student():
    while True:
        print("\n *** Search students ***")
        print("1. Search by roll_no")
        print("2. Search by name")
        print("3. Exit")

        choice=user_choice("\nEnter your choice:")

        if choice==1:
            search_by_roll_no()
        elif choice==2:
            search_by_student_name()
        elif choice==3:
            print("Exiting form students filter...")
            break
        else:
            print("Invalid choice. Please enter a number.")

    
    

# add new student function
def add_student():
    students=load_students()
     
    print("Enter students details:\n")
    roll_number=int(input("Enter Roll_No:"))
  
    for student in students:
        if(student["roll_number"]==roll_number):
            print("Error: Roll Number already exists")
            return

    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    course=input("Enter Course:")
    marks=float(input("Enter Marks:"))

    if not isinstance(age,int):
        print("Invalid Age")
    elif not isinstance(marks,float):
        print("Invalid Marks") 
    elif not isinstance(roll_number,int):
        print("Invalid Roll_No")   
    
    student={"roll_number":roll_number,"name":name,"marks":marks,"age":age,"course":course}
    students.append(student)
    save_student(students)
    print("Student added successfully!")

# filter the  student function
def filter_students():
    while True:
        print("\n *** Filter students ***")
        print("1. Filter passed students")
        print("2. Filter students by course")
        print("3. Exit")

        choice=user_choice("Enter your choice:")

        if choice==1:
            passed_students()
        elif choice==2:
            students_by_course()
        elif choice==3:
            print("Exiting form students filter...")
            break
        else:
            print("Invalid choice. Please enter a number.")
            

def menu():
   while True:
    print("\n *** Welcome to student management system ***")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Filter Students")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice=user_choice("Enter your choice:")

    if choice == 1:
        add_student()
    elif choice == 2:
        list_students()
    elif choice == 3:
        filter_students()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        search_student()
    elif choice== 6:
        print("Exiting from app...")
        break
    else:
        print("Invalid choice. Please enter a number.")
            

menu()