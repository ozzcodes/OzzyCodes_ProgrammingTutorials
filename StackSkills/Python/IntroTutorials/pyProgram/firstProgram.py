from statistics import mean as m

# Create admin dictionary
admins = {'Python': 'Pass123!', 'User2': 'Pass2!'}

# Students and grades dictionary
studentDict = {'Jeff': [78, 88, 93],
               'Alex': [91, 91, 75],
               'Sam': [89, 75, 90]
               }


# Add grades for a specified student
def enterGrades():
    nameToEnter = input('Student name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(int(gradeToEnter))
    else:
        print('Student does not exist!')

    print(studentDict)


# Remove students from class
def removeStudent():
    nameToRemove = input('What student do you want to remove? ')
    if nameToRemove in studentDict:
        print('Removing student...')
        del studentDict[nameToRemove]

    print(studentDict)


# Obtain the student average grades
def studentAverage():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent, 'has a grade of: ', avgGrade)


# Display main feature/ functions
def main():
    print("""
    Welcome to Grade Central
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    # Take a users input
    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAverage()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again!')


# Main function loop with login access credentials from dictionary
login = input('Username: ')
pwd = input('Password: ')

if login in admins:
    if admins[login] == pwd:
        print('Welcome,', login)

        while True:
            main()
    else:
        print('Invalid password! You are locked out!')
else:
    print('Invalid username, calling the FBI to report this!')
