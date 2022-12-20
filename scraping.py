from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
def logging(username, password):
    driver = webdriver.Chrome("chromedriver")
    # head to github login page
    driver.get("https://qalam.nust.edu.pk/")
    # find username/email field and send the username itself to the input field
    print(username)
    driver.find_element(By.ID, 'login').send_keys(username)
    # find password input field and insert password as well
    print(password)
    driver.find_element(By.ID, 'password').send_keys(password)
    # click login button
    driver.find_element(By.CLASS_NAME,"btn-nust").click()

    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Incorrect username or password."
    currentURL = driver.current_url
    if currentURL == "https://qalam.nust.edu.pk/student/dashboard":
        print("Login successful")
        return "Login Successful"
    else:
        print("Login failed")
        return "Login failed"
    driver.close()
username='mkaleem.bscs22seecs'
password='4IE8bhkp1234!@#$'
logging(username,password)
    
    
import requests
from bs4 import BeautifulSoup
url="https://qalam.nust.edu.pk/student/dashboard"
#Get the HTML as string
req=requests.get(url)
html=req.content

#Parse the HTML
soup=BeautifulSoup(html,'html.parser')

#HTML Tree Traversal
#Tag
#NavigableString
#BeautifulSoup
#Comment
title = soup.title #Title of the HTML page

#Get all the paragraphs from the page
paras=soup.find_all('p')

#Get all the anchor tags from the page
anchors=soup.find_all('a')
#Get all the links from the page:
#all_links=set()
#for link in anchors:
    #if(link.get('href') != '#'):
        #linkT="https://qalam.nust.edu.pk"+link.get('href')
        #all_links.add(linkT)

#print(soup.find('p')) gives the first paragraph, the first element
#print(soup.find('p')['class']) gives the class of any element in the HTML

#Find all the elements with class lead:
# print(soup.find_all("p",class_="lead"))


#Get the text from the tags/soup
# print(soup.find('p').get_text())
#All the text of the page: print(soup.get_text())

#Can take comments from HTML as well.
#markup="<p><! This is a comment></p>"
#soup2=BeautifulSoup(markup)
#print(soup2) would print in the form of HTML. print(soup2.p.string) prints only the text as string.
#Type is still being stored as a comment

#Getting the content of a div from the id:
#divcontent=soup.find(id='id') This returns the whole content of that div
#To print the children, we can do: divcontent.children. divcontent.contents returns the contents as a list
#We can iterate through divcontent.contents to print/work with all the contents inside.
#Both would give the same output when printed.
#.contents - a tag's children are available as a list, basically occupies memory
#.children - a tag's children are available as a generator. This is not actively occupying space, but can be retrieved via a loop.

#for item in divcontent.strings:
    #print(item) returns all the strings present in the div.
#If we replace strings with stripped_strings, simply removes the spaces and puts them all together.

#divcontent.parent gives us the parent of the div.
#.parents gives us a generator object. If we iterate through, it goes through all the parents up to the start of the doc.
#divcontent.next_sibling or #divcontent.previous_sibling gives the next/previous siblings.
#Can double these up to get prev sibling's prev sibling etc. divcontent.previous_sibling.previous_sibling

#CSS selectors:
#element=soup.select('#login') # is the CSS selector. This stores the element under the 'login' id in variable element.
# elem=soup.select('.login') returns the class of this name as a list.
 