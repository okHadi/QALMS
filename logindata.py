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