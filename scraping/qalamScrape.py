from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import re

def qalamScrape(username, password):
    session=requests.Session()
    # Create a new Chrome browser
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.headless = True          #set the headless option
    driver = webdriver.Chrome("chromedriver", options=chrome_options)

    # Navigate to the login page
    driver.get("https://qalam.nust.edu.pk/")

    # Find the username and password input fields and enter your credentials
    username_field = driver.find_element(By.ID, 'login')
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)

    # Click the login button
    driver.find_element(By.CLASS_NAME,"btn-nust").click()

    # Wait for the dashboard page to load
    driver.implicitly_wait(10)
    auth_keys = {c["name"]: c["value"] for c in driver.get_cookies()}
    response = requests.get("https://qalam.nust.edu.pk/student/dashboard", cookies=auth_keys)

    # Check the current URL to see if the login was successful
    current_url = driver.current_url
    if current_url != "https://qalam.nust.edu.pk/student/dashboard":
        raise Exception("Login failed")
    
    
    # Scrape the dashboard page
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    
    #RESULTS DATA:
    anchors=soup.find_all('a',href=re.compile(r'results/id/'))
    all_links=[]
    open('txtData/results.txt', 'a').close()  #resets the results file to 0
    for link in anchors:
        if(link.get('href') != '#'):
            linkT="https://qalam.nust.edu.pk"+str(link.get('href'))
            all_links.append(linkT)
    for link in all_links:

        # Send an HTTP request to the URL of the current link
        response2 = session.get(link,cookies=auth_keys)
        # Parse the response using Beautiful Soup
        # print(response2.text)
        soup = BeautifulSoup(response2.text, 'html.parser')
        #Find the table
        table = soup.find('table')
        data=[] #Array to store all the data
        #Find all the rows in the table
        if table!='None':
            rows = table.find_all('tr')
        header_data=[]
        cell_data=[]
        #Print the contents of each cell of every row
        for row in rows:
            headers=row.find_all('th')
            cells=row.find_all('td')
            #header_data = [header.get_text() for header in headers]
            #cell_data = [cell.get_text() for cell in cells]        
            for header in headers:
                header_data.append(header.get_text())
            for cell in cells:
                cell_data.append(cell.get_text()) 
        data.append(header_data)
        data.append(cell_data)
        # Open a new file in write mode

    with open('txtData/results.txt', 'a') as f:
    # Iterate over the elements of the list
        for row in data:
            for element in row:
                f.write(element + "\t")
            f.write("\n")

        # print(soup.get_text())
        
    #ATTENDANCE DATA:
    html2=session.get("https://qalam.nust.edu.pk/student/attendance",cookies=auth_keys)
    attendancesoup=BeautifulSoup(html2.text, 'html.parser')
    attanchors=attendancesoup.find_all('a',href=re.compile(r'attendancedetail/id/'))
    attd_links=[]
    open('txtData/attd_data.txt', 'w').close() #resets the attendance file to 0
    for link in attanchors:
        if(link.get('href') != '#'):
            linkT="https://qalam.nust.edu.pk"+str(link.get('href'))
            attd_links.append(linkT)
    for link in attd_links:
        attendance = session.get(link,cookies=auth_keys)
        attendancesoup=BeautifulSoup(attendance.text,'html.parser')
        elements=attendancesoup.find_all(class_="md-color-blue-grey-900")
        attd_data=[]

        for element in elements:
            attd_data.append(element.get_text())
        
        with open('txtData/attd_data.txt', 'a') as f:
        #Iterate over the elements of the list
            for element in attd_data:
                f.write(element +"\n")
             
    #  Close the session
    session.close()
    # Close the browser
    driver.close()



# import requests
# from bs4 import BeautifulSoup
# import re
# # Set the login URL
# login_url = "https://qalam.nust.edu.pk/student/login"

# # Set the payload for the login form
# payload = {
#     "login": "USERNAME",
#     "password": "PASSWORD"
# }

# # Send an HTTP POST request to the login URL with the payload
# response = requests.post(login_url, data=payload)
# #print(response.text)
# # Extract the authentication keys from the response
# auth_keys = response.cookies

# # Use the authentication keys to authenticate future requests
# response = requests.get("https://qalam.nust.edu.pk/student/dashboard", cookies=auth_keys)

# # Print the response
# # print(response.text)

# # Extract the links from the response
# soup = BeautifulSoup(response.text, 'html.parser')
# anchors = soup.find_all('a', href=re.compile(r'results/id/'))
# all_links = []
# for link in anchors:
#     if link.get('href') != '#':
#         linkT = "https://qalam.nust.edu.pk" + str(link.get('href'))
#         print(linkT)
#         all_links.append(linkT)
# print(all_links)
# # Iterate through the links and make requests to them
# for link in all_links:
#     # Send an HTTP request to the URL of the current link using the session object
#     response2 = requests.get(link, cookies=auth_keys)
#     print(response.text)








# def login_and_scrape(username, password):
#     session=requests.Session()
#     # Create a new Chrome browser
#     driver = webdriver.Chrome("chromedriver")

#     # Navigate to the login page
#     driver.get("https://qalam.nust.edu.pk/")

#     # Find the username and password input fields and enter your credentials
#     username_field = driver.find_element(By.ID, 'login')
#     username_field.send_keys(username)

#     password_field = driver.find_element(By.ID, 'password')
#     password_field.send_keys(password)

#     # Click the login button
#     driver.find_element(By.CLASS_NAME,"btn-nust").click()

#     # Wait for the dashboard page to load
#     driver.implicitly_wait(10)

#     # Check the current URL to see if the login was successful
#     current_url = driver.current_url
#     if current_url != "https://qalam.nust.edu.pk/student/dashboard":
#         raise Exception("Login failed")

#     # Scrape the dashboard page
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')

#     # Do something with the scraped data
#     # title=soup.title.string
#     # print(title)

    
#     anchors=soup.find_all('a',href=re.compile(r'results/id/'))
#     all_links=set()
#     for link in anchors:
#         if(link.get('href') != '#'):
#             linkT="https://qalam.nust.edu.pk"+str(link.get('href'))
#             all_links.add(linkT)
#     for link in all_links:
#         # Send an HTTP request to the URL of the current link
#         response = sessions.get(link)

#         # Parse the response using Beautiful Soup
#         soup = BeautifulSoup(response.text, 'html.parser')
#         print(soup.get_text())
        
#     session.close()
#     # Close the browser
#     driver.close()

# #Get all the anchor tags from the page
# anchors=soup.find_all('a')
# #Get all the links from the page:
# #all_links=set()
# #for link in anchors:
#     #if(link.get('href') != '#'):
#         #linkT="https://qalam.nust.edu.pk"+link.get('href')
#         #all_links.add(linkT)



# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# def logging(username, password):
#     driver = webdriver.Chrome("chromedriver")
#     # head to github login page
#     driver.get("https://qalam.nust.edu.pk/")
#     # find username/email field and send the username itself to the input field
#     print(username)
#     driver.find_element(By.ID, 'login').send_keys(username)
#     # find password input field and insert password as well
#     print(password)
#     driver.find_element(By.ID, 'password').send_keys(password)
#     # click login button
#     driver.find_element(By.CLASS_NAME,"btn-nust").click()

#     # wait the ready state to be complete
#     WebDriverWait(driver=driver, timeout=10).until(
#         lambda x: x.execute_script("return document.readyState === 'complete'")
#     )
#     error_message = "Incorrect username or password."
#     currentURL = driver.current_url
#     if currentURL == "https://qalam.nust.edu.pk/student/dashboard":
#         print("Login successful")
#         return "Login Successful"
#     else:
#         print("Login failed")
#         return "Login failed"
#     driver.close()
# username='USERNAME'
# password='PASSWORD'
# logging(username,password)
    
    
# import requests
# from bs4 import BeautifulSoup
# url="https://qalam.nust.edu.pk/student/dashboard"
# #Get the HTML as string
# req=requests.get(url)
# html=req.content

# #Parse the HTML
# soup=BeautifulSoup(html,'html.parser')

# #HTML Tree Traversal
# #Tag
# #NavigableString
# #BeautifulSoup
# #Comment
# title = soup.title #Title of the HTML page

# #Get all the paragraphs from the page
# paras=soup.find_all('p')

# #Get all the anchor tags from the page
# anchors=soup.find_all('a')
# #Get all the links from the page:
# #all_links=set()
# #for link in anchors:
#     #if(link.get('href') != '#'):
#         #linkT="https://qalam.nust.edu.pk"+link.get('href')
#         #all_links.add(linkT)

# #print(soup.find('p')) gives the first paragraph, the first element
# #print(soup.find('p')['class']) gives the class of any element in the HTML

# #Find all the elements with class lead:
# # print(soup.find_all("p",class_="lead"))


# #Get the text from the tags/soup
# # print(soup.find('p').get_text())
# #All the text of the page: print(soup.get_text())

# #Can take comments from HTML as well.
# #markup="<p><! This is a comment></p>"
# #soup2=BeautifulSoup(markup)
# #print(soup2) would print in the form of HTML. print(soup2.p.string) prints only the text as string.
# #Type is still being stored as a comment

# #Getting the content of a div from the id:
# #divcontent=soup.find(id='id') This returns the whole content of that div
# #To print the children, we can do: divcontent.children. divcontent.contents returns the contents as a list
# #We can iterate through divcontent.contents to print/work with all the contents inside.
# #Both would give the same output when printed.
# #.contents - a tag's children are available as a list, basically occupies memory
# #.children - a tag's children are available as a generator. This is not actively occupying space, but can be retrieved via a loop.

# #for item in divcontent.strings:
#     #print(item) returns all the strings present in the div.
# #If we replace strings with stripped_strings, simply removes the spaces and puts them all together.

# #divcontent.parent gives us the parent of the div.
# #.parents gives us a generator object. If we iterate through, it goes through all the parents up to the start of the doc.
# #divcontent.next_sibling or #divcontent.previous_sibling gives the next/previous siblings.
# #Can double these up to get prev sibling's prev sibling etc. divcontent.previous_sibling.previous_sibling

# #CSS selectors:
# #element=soup.select('#login') # is the CSS selector. This stores the element under the 'login' id in variable element.
# # elem=soup.select('.login') returns the class of this name as a list.
 
#CSS selectors:
#element=soup.select('#login') # is the CSS selector. This stores the element under the 'login' id in variable element.
# elem=soup.select('.login') returns the class of this name as a list.
 
