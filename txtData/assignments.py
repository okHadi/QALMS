def assignmentData():

    # open the text file and read the data
    with open("txtData/assignmentdata.txt", "r") as file:
        data = file.read()

    # split the data into lines
    lines = data.split("\n")

    # initialize an empty dictionary to store the course information
    courses = {}
    course_name = ""
    assignments = []
    # initialize a counter variable to keep track of the number of assignments
    assignment_counter = 1

    # iterate through each line
    for line in lines:
        # check if the line contains the string "2k22" (indicating a course name)
        if "2k22" in line:
            # split the line into words
            words = line.split()
            # find the index of the "2k22" string
            index = words.index("2k22")
            # extract the course name from the words before the "2k22" string
            course_name = " ".join(words[:index])
            if course_name.endswith("BSCS"):
                # If it does, remove "BSCS" from the course name
                course_name = course_name[:-4].strip()
            # initialize an empty list to store the assignments for this course
            assignments = []
            # reset the counter for the new course
            assignment_counter = 1
            # add the course name and assignments list to the dictionary
            courses[course_name] = assignments
        # if the line does not contain "2k22", it might be an assignment
        else:
            # check if the line does not contain the word "submission"
            if "submission" not in line.lower():
                # rename the assignment to "Assignment i" where i is the counter value
                assignment_name = "Assignment {}".format(assignment_counter)
                # check if the current course is "CS110 Fundamentals of Computer Programming BSCS"
                if course_name == "CS110 Fundamentals of Computer Programming BSCS":
                    # if it is, check if the assignment name does not contain "submission"
                    if "submission" not in assignment_name.lower():
                        # if it does not, add the assignment to the assignments list
                        assignments.append(assignment_name)
                        # increment the counter
                        assignment_counter += 1
                # if the current course is not "CS110 Fundamentals of Computer Programming BSCS", add the assignment to the assignments list
                else:
                    assignments.append(assignment_name)
                    # increment the counter
                    assignment_counter += 1

    # print the resulting dictionary
    return courses