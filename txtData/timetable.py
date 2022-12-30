def extactTimeTable():
    temp1 = 4
    timetable_dict = {'Course' : [],'Time' :{ 'From' :[], 'To' : []}}
    # Open the file in read mode
    with open('txtData/timetable.txt', 'r') as f:
    # Read the lines of the file into a list
        lines = f.readlines()
            # Access the specific line you want using the index of the list
        while(temp1 < len(lines)):
            a = lines[temp1].strip()
            timetable_dict['Course'].append(a)
            temp1+=10
        # String to search for
    string = ":"

    # Open the file in read mode
    with open('txtData/timetable.txt', 'r') as f:
    # Iterate through the lines of the file
        for line in f:
            # Check if the string exists in the line
            if string in line:
            # Print the line and break the loop
                line = f.readline()
                line = f.readline()
                line = f.readline()
                timetable_dict['Time']['From'].append(line.strip())
                line = f.readline()
                line = f.readline()
                timetable_dict['Time']['To'].append(line.strip())
        
    # Close the file
    f.close()

    return timetable_dict