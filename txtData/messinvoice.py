def messinvoice():
    # Open the text file in read mode
    with open('txtData/messinvoice.txt', 'r') as f:
        # Read the lines of the file into a list
        lines = f.readlines()
        
        # Remove all the empty lines from the list
        lines = [line for line in lines if line.strip() != ""]

    # Open the text file in write mode
    with open('txtData/messinvoice.txt', 'w') as f:
        # Write the modified lines to the file
        f.writelines(lines)


    # Open the text file in read mode
    with open('txtData/messinvoice.txt', 'r') as f:
        # Read the lines of the file into a list
        lines = f.readlines()
        
        # Extract the student name line and find the indices of "of" and "for" in it
        student_name_line = lines[1].strip()
        of_index = student_name_line.index("of")
        for_index = student_name_line.index("for")
        
        # Extract the student name as the text between "of" and "for"
        student_name = student_name_line[of_index+3:for_index-1]
        
        # Extract the invoice date, due date, amount, and status from the list of lines
        invoice_date = lines[2].strip()
        due_date = lines[3].strip()
        amount = lines[8].strip()
        status = lines[9].strip()
        
        # Create a dictionary with the extracted data
        data = {
            'student_name': student_name,
            'invoice_date': invoice_date,
            'due_date': due_date,
            'amount': amount,
            'status': status
        }
    
    # Print the dictionary
    return data