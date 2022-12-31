from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from chromedriver.chromedriver import *
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
def qalamLogin(username, password):
    session=requests.Session()
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.headless = True          #set the headless option
    driver = webdriver.Chrome(chromedriverpath, options=chrome_options)

    # head to github login page
    driver.get("https://qalam.nust.edu.pk/")
    # find username/email field and send the username itself to the input field
    #print(username)
    driver.find_element(By.ID, 'login').send_keys(username)
    # find password input field and insert password as well
    #print(password)
    driver.find_element(By.ID, 'password').send_keys(password)
    # click login button
    driver.find_element(By.CLASS_NAME,"btn-nust").click()
    auth_keys = {c["name"]: c["value"] for c in driver.get_cookies()}
    response = requests.get("https://qalam.nust.edu.pk/student/dashboard", cookies=auth_keys)
    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    currentURL = driver.current_url
    if currentURL == "https://qalam.nust.edu.pk/student/dashboard":
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
        coursesearch=dashsoup.find_all('span',class_='md-list-heading md-color-grey-900')
        coursenames=[]
        for name in coursesearch:
            coursenames.append(name.text)
        anchors=dashsoup.find_all('a',href=re.compile(r'results/id/'))
        all_links=[]
        for link in anchors:
            if(link.get('href') != '#'):
                linkT="https://qalam.nust.edu.pk"+str(link.get('href'))
                all_links.append(linkT)
        # Open a new file in write mode
            #Get student's name and CMS ID
        with open('txtData/studentinfo.txt','w') as f:
            info = dashsoup.find_all('h2',class_='heading_b')
            for text in info:
                f.write(text.get_text()+'\n')
        f.close()
        #RESULTS DATA:
        coursesearch=dashsoup.find_all('span',class_='md-list-heading md-color-grey-900')
        coursenames=[]
        for name in coursesearch:
            coursenames.append(name.text)
        anchors=dashsoup.find_all('a',href=re.compile(r'results/id/'))
        all_links=[]
        for link in anchors:
            if(link.get('href') != '#'):
                linkT="https://qalam.nust.edu.pk"+str(link.get('href'))
                all_links.append(linkT)
        # Open a new file in write mode

        with open('txtData/messinvoice.txt', 'w') as f:
            messinv = session.get("https://qalam.nust.edu.pk/student/messinvoices",cookies=auth_keys)
            messsoup = BeautifulSoup(messinv.text, 'html.parser')
            messtable = messsoup.find('table')
            if messtable != 'None':
                messrows =  messtable.find_all('tr')
            messheaders = messtable.find_all('th')
            messcells = messrows[-1].find_all('td')
            for j,header in enumerate(messheaders):
                if j!=9:
                    f.write(header.get_text() + '\t')
            print('\n')
            for k,cell in enumerate(messcells):
                if k!=9:
                    f.write(cell.get_text() + '\t')
        f.close()


        with open('txtData/results.txt', 'w') as f:
            i=0
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
                    f.write(coursenames[i] + '\n')
                    df = pd.read_html(str(table))[0]
                    mask = df['Obtained Percentage'].notnull()
                    df = df[mask]
                    f.write(df.to_string())
                    f.write('\n')
                    
                i+=1

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
    else:
        return "Login failed"
        session.close()
        driver.close()