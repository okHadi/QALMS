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
            # Split the line into words
            words = line.split()
            # Find the index of the "2k22" string
            index = words.index("2k22")
            # Extract the course name from the words before the "2k22" string
            course_name = " ".join(words[:index])
            if course_name.endswith("BSCS"):
                # If it does, remove "BSCS" from the course name
                course_name = course_name[:-4].strip()
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
    del result[""]
    return result
