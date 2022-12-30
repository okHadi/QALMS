def teacherinfo():
    result = {}

    # Open the file and read the data
    with open("txtData/courseteacherinfo.txt", "r") as f:
        data = f.readlines()

    # Initialize variables to store the course name, instructor name, and instructor email
    course_name = ""
    instructor_name = ""
    instructor_email = ""

    # Loop through the data and parse each line
    for line in data:
        # Check if the line is the course name
        if "2k22" in line:
            course_name = line.strip()
        # Check if the line is the instructor name
        elif " " in line:
            instructor_name = line.strip()
        # The line is the instructor email
        else:
            instructor_email = line.strip()
            # Check if the course is already in the result dictionary
            if course_name in result:
                # If the course is already in the dictionary, append the instructor to the list of instructors
                result[course_name]["instructor_names"].append(instructor_name)
                result[course_name]["instructor_emails"].append(instructor_email)
            else:
                result[course_name] = {
                "instructor_names": [instructor_name],
                "instructor_emails": [instructor_email]
            }
    return result