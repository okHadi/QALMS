from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import re

def lmsScrape(luser, lpass):
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.headless = True          #set the headless option
    driver = webdriver.Chrome("chromedriver", options=chrome_options)
    LMSsession=requests.Session()
    # head to LMS login page
    driver.get("https://lms.nust.edu.pk/portal/login/index.php")
    # find username/email field and send the username itself to the input field
    #print(username)
    driver.find_element(By.ID, 'username').send_keys(luser)
    # find password input field and insert password as well
    #print(password)
    driver.find_element(By.ID, 'password').send_keys(lpass)
    # click login button
    driver.find_element(By.ID,"loginbtn").click()
    # try:

    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    auth_keysLMS = {c["name"]: c["value"] for c in driver.get_cookies()}
    currentURL = driver.current_url
    
    if currentURL == "https://lms.nust.edu.pk/portal/my/":
        print("Login successful")
    else:
        print("Login failed")
    lmshtml=LMSsession.get("https://lms.nust.edu.pk/portal/?redirect=0",cookies=auth_keysLMS)
    lmssoup=BeautifulSoup(lmshtml.text,'html.parser')
    anchors=lmssoup.find_all('a',href=re.compile(r'portal/course/view'))
    course_links=[]
    for link in anchors:
        # if(link.get('href') != '#'):
        course_links.append(link.get('href'))
    # print(course_links)
    with open('courseteacherinfo.txt', 'w') as f:
        for link in course_links:
            lms = LMSsession.get(link,cookies=auth_keysLMS)
            coursesoup=BeautifulSoup(lms.text,'html.parser')
            coursetitle=coursesoup.find_all(class_="page-header-headings")
            coursetitlelist=[]
            for title in coursetitle:
                coursetitlelist.append(title)
                f.write(title.get_text() + "\n")
                searchprof=coursesoup.find_all('div',class_='col-md-12 align-self-center')
                for prof in searchprof:
                    teacherprof=prof.find_all('a',href=re.compile(r'portal/user/profile'))
                    teacherprofs=[]
                    for prof in teacherprof:
                        teacherprofs.append(prof.get_text())
                        f.write(prof.get_text()+"\n")
                        emailsearch=LMSsession.get(prof.get('href'),cookies=auth_keysLMS)
                        emailsoup=BeautifulSoup(emailsearch.text,'html.parser')
                        emails=emailsoup.find_all('a',href=re.compile(r'mailto:%'))
                        emaillist=[]
                        for email in emails:
                            emaillist.append(email)
                            f.write(email.get_text() + "\n")
    f.close()

    LMSsession.close()
    driver.close()