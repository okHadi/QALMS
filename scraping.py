from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import re

def login_and_scrape(username, password):
    session=requests.Session()
    # Create a new Chrome browser
    driver = webdriver.Chrome("chromedriver")

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

    # Check the current URL to see if the login was successful
    current_url = driver.current_url
    if current_url != "https://qalam.nust.edu.pk/student/dashboard":
        raise Exception("Login failed")
    

    # Scrape the dashboard page
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    # Do something with the scraped data
    # title=soup.title.string
    # print(title)

    
    anchors=soup.find_all('a',href=re.compile(r'results/id/'))
    all_links=[]
    for link in anchors:
        if(link.get('href') != '#'):
            
            linkT="https://qalam.nust.edu.pk"+str(link.get('href'))
            all_links.append(linkT)
    for link in all_links:
        driver = webdriver.Chrome("chromedriver")
        driver.get("https://qalam.nust.edu.pk/")
        username_field = driver.find_element(By.ID, 'login')
        username_field.send_keys(username)

        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(password)

        # Click the login button
        driver.find_element(By.CLASS_NAME,"btn-nust").click()

        # Wait for the dashboard page to load
        driver.implicitly_wait(10)

        # Send an HTTP request to the URL of the current link
        response = session.get(link)
        print(response.text)
        # Parse the response using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        driver.close()

        # print(soup.get_text())
        
    # Close the session
    session.close()
    # Close the browser

username='mkaleem.bscs22seecs'
password='4IE8bhkp1234!@#$'
login_and_scrape(username, password)


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
 
