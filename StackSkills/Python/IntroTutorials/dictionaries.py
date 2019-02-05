gradeDict = {'Kelly': 94, 'David': 65, 'Jack': 88, 'Samantha': 72}
print(gradeDict)

print(gradeDict['David'])
gradeDict['David'] = 56
print(gradeDict)

# Add a Student
gradeDict['Jessie'] = 95
print(gradeDict)

# Remove Student
del gradeDict['David']
print(gradeDict)

# Create a student with a list of Grades
gradeDict2 = {'Kelly': [94, 88],
              'Jack': [88, 79],
              'Samantha': [72, 69],
              'Jessie': [95, 89]
              }
print(gradeDict2)
print(gradeDict2['Jessie'])
