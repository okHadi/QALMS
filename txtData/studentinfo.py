def studentInfo():
    with open('txtData/studentinfo.txt', 'r') as f:
    # Read the lines of the file into a list
        lines = f.readlines()
        
        # Extract the name, roll number, and department from the list of lines
        name = lines[1].strip()
        roll_number = lines[2].strip()
        department = lines[3].strip()
        
        # Filter the department name to include only the text within the brackets
        department = department[department.index("(")+1:department.index(")")]
        
        # Create an object with key-value pairs for the extracted data
        data = {
            'name': name,
            'roll_number': roll_number,
            'department': department
        }
    
    # Print the object
    return data
