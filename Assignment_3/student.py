def read_student_data(filename):
    students = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            studentID, lastname, firstname, major, gpa = line.split(",")

            students[studentID] = [lastname, firstname, major, gpa]
    return students

def main():
    filename = input("What is the name of the file with the student data?:\n")
    students_dict = read_student_data(filename)

    while True:
        print("Choose an option:\n" \
        "1) Search by Last Name:\n" \
        "2) Search by Major:\n" \
        "3) Quit")
        option = int(input())

        if option == 1:
            searchedLastName = input("What Last Name are you looking for:\n")
            found = False
            for studentID, data in students_dict.items():
                lastname = data[0]
                if lastname.lower() == searchedLastName.lower():
                    print(f"{studentID}: {data[0]}, {data[1]}, Major: {data[2]}, GPA: {data[3]}\n")
                    found = True
            if not found:
                print("Could not find anyone with that Last Name.\n")

        elif option == 2:
            searchedMajor = input("What major are you lokking for?\n")
            found = False
            for studentID, data in students_dict.items():
                major = data[2]
                if major.lower() == searchedMajor.lower():
                    print(f"{studentID}: {data[0]}, {data[1]}, Major: {data[2]}, GPA: {data[3]}\n")
                    found = True
            if not found:
                print("Could not find anyone with that Major.\n")
        
        elif option == 3:
            print("Goodbye")
            break
        
        else:
            print("Please enter 1, 2, or 3.\n")
    
main()


