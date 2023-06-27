"""
Transcript Reader:
This program locates and reads a transcript file, then prints name, major, university credit hours, GPA, major credit hours, major GPA.

File Name: howry_project_8.py
Author: Ken Howry
Date: 22.11.11
Course: COMP 1351
Assignment: Project VIII
Collaborators: N/A
Internet Source: N/A
"""

#while loop that locates the student transcript
quit=False
while not quit:
    first_name = input("Enter the first name of the student: ")
    last_name = input("Enter the last name of the student: ")

    first_name = first_name.lower()
    last_name = last_name.lower()

    file = f"{first_name}_{last_name}.txt"
    print(file)
    try:
        transcript = []
        with open(f"data_files/{file}", "r") as a_file:
            for line in a_file:
                data = line.strip().split(",")
                transcript.append(data[:])
        print(f"Transcript file {file} sucessfully located.")

        quit = True
    except:
        print("File not located. Enter the name again.")
        
#variables 
credit_hours = 0
major_credit_hours = 0
points = 0
gpa_credit_hours = 0
major_points = 0
major_gpa_credit_hours = 0

#identifying major
major = input("What is the student's major? ")
major = major.upper()

#calculating university credit hours
for i in range(len(transcript)):
    if transcript[i][4] != "F":
        credit_hours += float(transcript[i][3])

#calculating GPA
for i in range(len(transcript)):
    if transcript[i][4] != "P" and transcript[i][4] != "T":
        gpa_credit_hours += float(transcript[i][3])
        if transcript[i][4] == "A+" or transcript[i][4] == "A":
            points += (4.0 * float(transcript[i][3]))
        elif transcript[i][4] == "A-":
            points += (3.7 * float(transcript[i][3]))
        elif transcript[i][4] == "B+":
            points += (3.3 * float(transcript[i][3]))
        elif transcript[i][4] == "B":
            points += (3.0 * float(transcript[i][3]))
        elif transcript[i][4] == "B-":
            points += (2.7 * float(transcript[i][3]))
        elif transcript[i][4] == "C+":
            points += (2.3 * float(transcript[i][3]))
        elif transcript[i][4] == "C":
            points += (2.0 * float(transcript[i][3]))
        elif transcript[i][4] == "C-":
            points += (1.7 * float(transcript[i][3]))
        elif transcript[i][4] == "D+":
            points += (1.3 * float(transcript[i][3]))
        elif transcript[i][4] == "D":
            points += (1.0 * float(transcript[i][3]))
        else:
            points += (0.0 * float(transcript[i][3]))

#calculating major credit hours
for i in range(len(transcript)):
    if transcript[i][0] == major and transcript[i][4] != "F":
        major_credit_hours += float(transcript[i][3])

#calculating major GPA
for i in range(len(transcript)):
    if transcript[i][0] == major and transcript[i][4] != "P" and transcript[i][4] != "T":
        major_gpa_credit_hours += float(transcript[i][3])
        if transcript[i][4] == "A+" or transcript[i][4] == "A":
            major_points += (4.0 * float(transcript[i][3]))
        elif transcript[i][4] == "A-":
            major_points += (3.7 * float(transcript[i][3]))
        elif transcript[i][4] == "B+":
            major_points += (3.3 * float(transcript[i][3]))
        elif transcript[i][4] == "B":
            major_points += (3.0 * float(transcript[i][3]))
        elif transcript[i][4] == "B-":
            major_points += (2.7 * float(transcript[i][3]))
        elif transcript[i][4] == "C+":
            major_points += (2.3 * float(transcript[i][3]))
        elif transcript[i][4] == "C":
            major_points += (2.0 * float(transcript[i][3]))
        elif transcript[i][4] == "C-":
            major_points += (1.7 * float(transcript[i][3]))
        elif transcript[i][4] == "D+":
            major_points += (1.3 * float(transcript[i][3]))
        elif transcript[i][4] == "D":
            major_points += (1.0 * float(transcript[i][3]))
        else:
            major_points += (0.0 * float(transcript[i][3]))

#printing information
first_name = first_name.capitalize()
last_name = last_name.capitalize()

#printing information
print(f"Name: {first_name} {last_name}")
print(f"Major: {major}")
print(f"University credit hours: {credit_hours} ")
print(f"GPA: {round(points/gpa_credit_hours, 2)} ")
print(f"Credits in major: {major_credit_hours}")

#fixing GPA computing issues
if major_credit_hours == 0 and major_points == 0:
    print(f"GPA in major: {round(major_points/major_gpa_credit_hours, 2)}")
elif major_credit_hours != 0 and major_points != 0:
    print(f"GPA in major: {round(major_points/major_gpa_credit_hours, 2)}")
elif major_credit_hours != 0 and major_points == 0:
    print("No major GPA yet.")