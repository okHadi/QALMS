import csv


def resultsData():
    def delete_line_with_string(filename, string):
        with open(filename, 'r') as f:
            lines = f.readlines()

        # Iterate over each line in the file
        for line in lines:
            if string in line:
            # Remove the line from the list of lines
                lines.remove(line)

        # Write the modified lines back to the file
        with open(filename, 'w') as f:
            f.write(''.join(lines))

    # Test the function
    delete_line_with_string("txtData/results.txt", "Unnamed:")



    def convert_spaces_to_dashes(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        # Iterate over each line in the file
        for i, line in enumerate(lines):
            # Find the position of all spaces in the line
            space_indices = [pos for pos, char in enumerate(line) if char == ' ']

            # Replace all single spaces with dashes
            for index in space_indices:
                if index == 0:  # Skip leading spaces
                    continue
                if index == len(line) - 1:  # Skip trailing spaces
                    continue
                if line[index - 1] == ' ' or line[index + 1] == ' ':  # Skip multiple spaces
                    continue
                # Replace the single space with a dash
                line = line[:index] + '-' + line[index + 1:]

            # Update the modified line in the list of lines
            lines[i] = line

        # Write the modified lines back to the file
        with open(filename, 'w') as f:
            f.write(''.join(lines))

    # Test the function
    convert_spaces_to_dashes("txtData/results.txt")
    # Read the text from the file "grades.txt"
    with open("txtData/results.txt") as f:
        text = f.read()

    # Split the text into lines and store them in a list
    lines = text.split("\n")

    # Open a file for writing in CSV format
    with open("txtData/results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        # Iterate through the lines and write each one to the CSV file
        for line in lines:
            # Split the line into fields
            fields = line.split()
            
            # Replace the spaces in all the fields with dashes
            fields = [field.replace(" ", "-") for field in fields]
            
            # Write the fields to the CSV file
            writer.writerow(fields)
            
        # Close the file when you are done writing to it
        csvfile.close()


    # Open the CSV file
    with open('txtData/results.csv', 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)
        
        # Initialize an empty dictionary
        data = {}
        
        # Initialize a variable to store the current subject
        current_subject = None
        
        # Iterate over the rows of the CSV file
        for row in reader:
            # If the current row is empty, skip it
            if not row:
                continue
            
            # If the current row is the name of a subject, store it as the current subject
            if len(row) == 1:
                current_subject = row[0]
                data[current_subject] = {}
            else:
                # If the current row is an assessment, store it in the dictionary
                assessment = row[1]
                data[current_subject][assessment] = {
                    'Max_Mark': row[2],
                    'Obtained_Mark': row[3],
                    'Class_Average': row[4],
                    'Percentage': row[5]
                }
        return data