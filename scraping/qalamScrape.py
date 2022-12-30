from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from chromedriver.chromedriver import *
import requests
from bs4 import BeautifulSoup
import re

def qalamScrape(username, password):
    session=requests.Session()
    # Create a new Chrome browser
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.headless = True          #set the headless option
    driver = webdriver.Chrome(chromedriverpath, options=chrome_options)

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
    #Scrape the dashboard for the day's classes
    with open('txtData/timetable.txt', 'w') as f:
        dashhtml = driver.page_source
        dashsoup = BeautifulSoup(dashhtml, 'html.parser')
        classes = dashsoup.find_all(class_="user_heading_content")
        timetableraw=[]
        for timet in classes:
            timetableraw.append(timet.get_text())
        string = '\n'.join(timetableraw)
        # timetable=timetableraw.split("Today Classes:")
        # result = "Today Classes".join(timetable[2:])
        timetable = string.split('Today Classes:')
        result='\n'.join(timetable[1:])
            #Iterate over the elements of the list
        f.write(result)
        # for timet in timetable:
        # f.write(timet +"\n")
    f.close()
    

    
   #RESULTS DATA:
    anchors=dashsoup.find_all('a',href=re.compile(r'results/id/'))
    all_links=[]
    for link in anchors:
        if(link.get('href') != '#'):
            linkT="https://qalam.nust.edu.pk"+str(link.get('href'))
            all_links.append(linkT)
    # Open a new file in write mode
    with open('txtData/results.txt', 'w') as f:
        for link in all_links:

         # Send an HTTP request to the URL of the current link
            response2 = session.get(link,cookies=auth_keys)
            # Parse the response using Beautiful Soup
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
                    f.write(header.get_text()+"\n")
                for cell in cells:
                    cell_data.append(cell.get_text()) 
                    f.write(cell.get_text()+"\n")
            data.append(header_data)
            data.append(cell_data)
        
    # Iterate over the elements of the list
        for row in data:
            for element in row:
                f.write(element + "\t")
            f.write("\n")
    
        # Iterate over the elements of the list
            # for row in data:
            #     for element in row:
            #         f.write(element + "\t")
            #     f.write("\n")

        # print(soup.get_text())
    f.close()    
    #ATTENDANCE DATA:
    html2=session.get("https://qalam.nust.edu.pk/student/attendance",cookies=auth_keys)
    attendancesoup=BeautifulSoup(html2.text, 'html.parser')
    attanchors=attendancesoup.find_all('a',href=re.compile(r'attendancedetail/id/'))
    attd_links=[]
    for link in attanchors:
        if(link.get('href') != '#'):
            linkT="https://qalam.nust.edu.pk"+str(link.get('href'))
            attd_links.append(linkT)
    with open('txtData/attd_data.txt', 'w') as f:
        for link in attd_links:
            attendance = session.get(link,cookies=auth_keys)
            attendancesoup=BeautifulSoup(attendance.text,'html.parser')
            elements=attendancesoup.find_all(class_="md-color-blue-grey-900")
            attd_data=[]
            for element in elements:
                attd_data.append(element.get_text())
            #Iterate over the elements of the list
            for element in attd_data:
                f.write(element +"\n")
    f.close()         
    #  Close the session
    session.close()
    # Close the browser
    driver.close()