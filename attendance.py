# Create an empty dictionary
my_dict = {'Course':[],'Number of Classes Conducted':[],'Number of Classes Attended':[],'Attendance Percentage':[]}
temp = 1
temp1 = 9
temp2 = 13
temp3 = 17
# Open the file in read mode
with open('attendance.txt', 'r') as file:
  # Read the entire file into a list of lines
  lines = file.readlines()
  # Access the specific line you want using the index of the list
  while(temp < len(lines)):
    a = lines[temp].rstrip()
    my_dict['Course'].append(a)
    temp+=20
  while(temp1 < len(lines)):
    a = lines[temp1].rstrip()
    my_dict['Number of Classes Conducted'].append(a)
    temp1+=20
  while(temp2 < len(lines)):
    a = lines[temp2].rstrip()
    my_dict['Number of Classes Attended'].append(a)
    temp2+=20
  while(temp3 < len(lines)):
    a = lines[temp3].rstrip()
    my_dict['Attendance Percentage'].append(a)
    temp3+=20
  # Print the dict
  print(my_dict)
  


# Open the file in read mode
#with open('attendance.txt', 'r') as file:
#  # Iterate over the lines of the file
#  for i, line in enumerate(file):
#    # Check if the current line is the one you want to read
#    if i == line_number - 1:
#      # Print the line and exit the loop
#     
#      break
