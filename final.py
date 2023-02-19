import mimetypes
import os
import re
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver
import ctypes
import json
import socket

global driver, user, key, direc

connected = False
while not connected:
    try:
        # Try to connect to Google's website to check for internet connection
        socket.create_connection(("www.google.com", 80))
        connected = True
        print("Internet connection is established.")
    except OSError:
        # If there's no internet connection, wait for 1 second and try again
        print("Waiting for internet connection...")
        time.sleep(1)
# direc = str(input("Enter your directory of choosing (eg G:\web): "))
# user = str(input("Input your username: "))
# key = getpass.getpass("Input your password: ")
if(connected):
    
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
    with open(json_path) as f:
        data = json.load(f)
        user = data['username']
        key = data['password']
        direc = data['direc']


    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-restrictions')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    # options.add_argument("--headless")
    # options.binary_location = "/usr/bin/chromium"

    # disable_restrictions option
    options.add_argument('--disable-download-restriction')
    driver = webdriver.Chrome(chrome_options=options)

    links = []

    driver.get('https://lms.nust.edu.pk/portal/login/index.php')
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(key)
    driver.find_element(
        By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
    driver.implicitly_wait(300)
    element_list = driver.find_elements(
        By.XPATH, "//a[contains(@class, 'aalink coursename')]")
    for j in element_list:
        links.append(j.get_attribute('href'))


    for i in range(len(links)):
        # Set the download directory
        text = driver.find_element(
            By.XPATH, "//a[contains(@class,'aalink coursename')]").text
        print("text with xpath is ", text)
        text_x = element_list[i].text
        text_test = "".join(ch for ch in text_x if ch.isalnum())
        text_test.replace("Coursename", "")

        normal_string = text_test.replace("Coursename", "")
        website_name = normal_string
        print("text without xpath is ", normal_string)
        download_dir = os.path.join(direc, website_name)
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {
            # Change default directory for downloads
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            # It will not show PDF directly in chrome
            "plugins.always_open_pdf_externally": True
        })
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--disable-autoplay-policy")
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-restrictions')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")

        driver_x = webdriver.Chrome(options=chrome_options)

        driver_x.get(links[i])
        driver_x.find_element(
            By.XPATH, "//input[@name='username']").send_keys(user)
        driver_x.find_element(
            By.XPATH, "//input[@name='password']").send_keys(key)
        driver_x.find_element(
            By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        driver.implicitly_wait(300)
        sleep(3)
        # all links excluding urls like to articles or others
        elements = driver_x.find_elements(
            By.XPATH, "//a[contains(@href, 'https://lms.nust.edu.pk/portal/mod/resource/view.php?')]")
        elements_url = driver_x.find_elements(
            By.XPATH, "//a[contains(@href, 'https://lms.nust.edu.pk/portal/mod/url/view.php?')]")
        elements_folder = driver_x.find_elements(
            By.XPATH, "//a[contains(@href, 'https://lms.nust.edu.pk/portal/mod/folder/view.php?')]")

        urls = []
        urls_real = []
        folders = []
        new_urls = []
        new_urls_real = []
        new_folders = []
        for k in elements:
            urls.append(k.get_attribute('href'))
        for k in elements_url:
            urls_real.append(k.get_attribute('href'))
        for k in elements_folder:
            folders.append(k.get_attribute('href'))

        with open(download_dir + "/url.txt", 'a+') as f:
            f.write("")
        with open(download_dir + "/url_real.txt", 'a+') as f:
            f.write("")
        with open(download_dir + "/folders.txt", 'a+') as f:
            f.write("")

        def store_list_to_urls(urls, path):
            with open(path + "/url.txt", "r+") as file:
                contents = file.read()
                for item in urls:
                    if ((item) in contents):
                        continue
                    else:
                        file.write(str(item) + "\n")
                        new_urls.append(item)

        def store_list_to_urls_real(urls_real, path):
            with open(path + "/url_real.txt", "r+") as file:
                contents = file.read()
                for item in urls_real:
                    if ((item) in contents):
                        continue
                    else:
                        file.write(str(item) + "\n")
                        new_urls_real.append(item)

        def store_list_to_folders(folders, path):
            with open(path + "/folders.txt", "r+") as file:
                contents = file.read()
                for item in folders:
                    if ((item) in contents):
                        continue
                    else:
                        file.write(str(item) + "\n")
                        new_folders.append(item)

        store_list_to_urls(urls, download_dir)
        store_list_to_urls_real(urls_real, download_dir)
        store_list_to_folders(folders, download_dir)

        print(new_urls)
        print(new_urls_real)
        print(new_folders)

        # urls_to_display = []
        for j in range(len(new_urls)):
            # initialize the driver
            driver_x.execute_script("window.open('');")
            driver_x.switch_to.window(driver_x.window_handles[j])
            driver_x.get(new_urls[j])
            sleep(3)
            pdf_links = driver_x.find_elements(
                By.XPATH, "//a[contains(@href, '.pdf')]")

            # for VID links

            # vid_links = driver_x.find_elements(
            #     By.XPATH, "//video//source[contains(@src,'.mp4')]")
            # real_vid_links = []
            # if len(vid_links) != 0:
            #     for link in vid_links:
            #         real_vid_links.append(link.get_attribute('src'))
            # print(real_vid_links)
            # for k in range(len(real_vid_links)):
            #     # driver_x.execute_script("window.open('');")
            #     # driver_x.switch_to.window(driver_x.window_handles[j+k])
            #     # driver_x.get(real_vid_links[k])
            #     # urllib.request.urlretrieve(real_vid_links[k], 'video.mp4')
            #     url = real_vid_links[k]
            #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
            #     with open(r'G:\web\vid.mp4'+str(k), 'wb') as f_out:
            #         r = requests.get(url, headers=headers, stream=True)
            #         print(r)
            #         for chunk in r.iter_content(chunk_size=1024):
            #             if chunk:
            #                 f_out.write(chunk)

            # Extract the href attribute of each anchor tag
            pdf_links = [link.get_attribute("href") for link in pdf_links]
            for u in range(len(pdf_links)):
                driver_x.execute_script("window.open('');")
                driver_x.switch_to.window(driver_x.window_handles[u+j])
                driver_x.get(pdf_links[u])
                sleep(3)

            print(pdf_links)

        # FOR URLS

        # if len(urls_real) != 0:
        #     for l in range(len(urls_real)):
        #         if l == 0:
        #             continue
        #         else:
        #             driver_x.execute_script("window.open('');")
        #             driver_x.switch_to.window(driver_x.window_handles[l])
        #             driver_x.get(urls_real[l])
        #             driver_x.implicitly_wait(10)

        #             get_url = driver_x.current_url
        #             print(l, get_url)
        #             urls_to_display.append(get_url)

        #             url = driver_x.find_elements(
        #                 By.XPATH, "//div[@class='urlworkaround']//a")
        #             print(l, url)
        #             if len(url) != 0:
        #                 print(url[0].get_attribute('href'))
        #                 urls_to_display.append(url[0].get_attribute('href'))

        # download_dir_new = os.path.join(download_dir, "urls.txt")
        # if len(urls_to_display) != 0:
        #     with open(download_dir_new, 'w') as f:
        #         for item in urls_to_display:
        #             f.write(item+"\n")

        # removing all lms links from url.text
        # Open the file for reading
        # with open(download_dir_new, "r") as f:
        #     # Read the contents of the file
        #     contents = f.read()

        # # Define the regular expression to match
        # pattern = re.compile(
        #     "https://lms\.nust\.edu\.pk/portal/mod/url/view\.php\?id=\d+")

        # # Replace all matches with an empty string
        # new_contents = re.sub(pattern, "", contents)

        # # Open the file for writing
        # with open(download_dir_new, "w") as f:
        #     # Write the new contents to the file
        #     f.write(new_contents)

        if len(new_folders) != 0:
            for l in range(len(new_folders)):
                driver_x.execute_script("window.open('');")
                driver_x.switch_to.window(driver_x.window_handles[l])
                driver_x.get(new_folders[l])
                sleep(3)
                driver_x.find_element(
                    By.XPATH, "//button[@class='btn btn-secondary'][@type='submit']").click()

        ctypes.windll.kernel32.SetFileAttributesW(download_dir + "/url.txt", 2)
        ctypes.windll.kernel32.SetFileAttributesW(
            download_dir + "/url_real.txt", 2)
        ctypes.windll.kernel32.SetFileAttributesW(
            download_dir + "/folders.txt", 2)
        driver_x.close()


    driver.close()
