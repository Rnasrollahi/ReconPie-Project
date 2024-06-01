# # import requests

# # # # domain="wikipedia.org"
# # # # f=open('wordlist.txt','r')
# # # # file=f.read()
# # # # subdomain=file.splitlines()

# # # # for sub in subdomain:
# # # #     url1=f"http://{sub}.{domain}"
# # # #     url2=f"https://{sub}.{domain}"
# # # #     try:
# # # #         requests.get(url1)
# # # #         print(f">>>{url1}")
# # # #         requests.get(url2)
# # # #         print(f">{url2}")
# # # #     except requests.ConnectionError:
# # # #         print("no find")
# # # #         pass


# # import re
# # import urllib
# # # import requests
# # from bs4 import BeautifulSoup
# # # # import bs4
# # # # url="https://w3schools.com"
# # # # # request=requests.get(url)
# # # # # soup=BeautifulSoup(request.text,"html.parser")
# # # # # print(soup.select('title')[0].text)
    
# # # # request=requests.get(url)
# # # # content=request.content
# # # # soup=BeautifulSoup(content,"html.parser")
# # # # s=soup.select('title')[0].text
# # # # d=request.status_code
# # # # print(s,d)
# # # # url = "https://www.example.com/page1"

# # # # domain = re.search(r"https?://(www\.)?(.*?)\/", url).group(2)

# # # # print(domain)



# # # # ...............
# # # # url = "https://www.example.com/page1"

# # # # domain = re.sub(r"https?://(?:www\.)?([^/]+).*", r"\1", url)

# # # # print(domain)


# # # # import socket

# # # # # Replace "example.com" with the domain name you want to map to an IP address
# # # # domain = "mrbug.ir"

# # # # # Use the gethostbyname() function from the socket library to get the IP address for the specified domain
# # # # ip_address = socket.gethostbyname(domain)

# # # # print(f"The IP address of {domain} is {ip_address}")


# # # import socket
# # # # open_port=""
# # # # ip = "maps.google.com"  # Replace with the IP address you want to scan

# # # # # List of commonly used ports to scan
# # # # common_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]

# # # # for port in common_ports:  
# # # #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # #     sock.settimeout(1)  # Set timeout to 1 second
# # # #     result = sock.connect_ex((ip, port))
# # # #     if result == 0:
# # # #       open_port+=" {} ".format(port)+" , "
      
    
# # # #     sock.close()
# # # # print(open_port)

# # # # def port_scan(url):
# # # #     print("p")
# # # #     open_port=""
# # # #     ports = [21,53, 80,123, 143,443, 445, 993]
# # # #     domain = re.sub(r"https?://(?:www\.)?([^/]+).*", r"\1",url) 
# # # #     for port in ports:  
# # # #         try:
# # # #             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # #             sock.settimeout(1) 
# # # #             sok = sock.connect_ex((domain, port))
# # # #             if sok == 0:
# # # #                 open_port+=" {} ".format(port)+" , "
             
# # # #             sock.close()
# # # #         except socket.error:
# # # #             pass
# # # #     return open_port
# # # # print(port_scan("https://www.google.com/imghp?hl=en&tab=wi"))
# # # # # /////
# # # # import socket

# # # # target = 'mrbug.ir'

# # # # for port in range(1, 65535):  # Scan all ports from 1 to 65535
# # # #     try:
# # # #         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # #         s.settimeout(1)
# # # #         result = s.connect_ex((target, port))
# # # #         if result == 0:
# # # #             print(f"Port {port} is open")
# # # #             s.close()
# # # #         else :
# # # #             print("no")
# # # #             pass
# # # #     except socket.error:
# # # #         pass
# # # # //////
# # # import requests
# # # from bs4 import BeautifulSoup
# # # import requests
# # # from bs4 import BeautifulSoup
# # # import re

# # # # import whois
# # # # w = whois.whois('digikala.com')
# # # # print(w)
# # # # .
# # # # .
# # # # .
# # # # .
# # # # import argparse
# # # # parser=argparse.ArgumentParser()
# # # # parser.add_argument('-u','--url',help='ENTER URL')

# # # # args=parser.parse_args()
# # # # print(args)
# # # # try:
# # # #     request=requests.get(args.url)   
# # # #     print(request.status_code)             
# # # # except:
    
# # # #     print(request.status_code)             
# # # #     pass
# # # url="https://u3er.xyz"
# # # ip_address=""
# # # domainip = re.sub(r"https?://(?:www\.)?([^/]+).*", r"\1",url)    
# # # try: 
# # #         ip_address = socket.gethostbyname(domainip) 
# # #         if ip_address is not None:
# # #             print(str(ip_address))
# # # except :
# # #          pass
# # # # # s=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',request.text)
# # # # print(s)
# # # # # .
# # # # .
# # # # .
# # # # .
# # # import requests
# # # from bs4 import BeautifulSoup
# # # import re

# # # # url = "https://tahrirclick.com"  # آدرس سایت مورد نظر
# # # # response = requests.get(url)
# # # # soup = BeautifulSoup(response.text, 'html.parser')

# # # # # emails = set()  # استفاده از مجموعه برای جلوگیری از تکرار ایمیل‌ها

# # # # # for email in re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text):
# # # # #     emails.add(email)

# # # # # for link in soup.find_all('a'):
# # # # #     subpage = link.get('href')
# # # # #     if subpage and subpage.startswith('http'):
# # # # #         subresponse = requests.get(subpage)
# # # # #         for email in re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', subresponse.text):
# # # # #             emails.add(email)

# # # # # print(emails)





# # # import requests
# # # import os
# # # # Function to enumerate files on the target domain
# # # def enumerate_files(target_domain):
# # #     files_list = []
# # #     url = f"http://{target_domain}/"
    
# # #     response = requests.get(url)
# # #     response=BeautifulSoup(response,'html.parser')
# # #     if response.status_code == 200:
# # #         for file in response.text.split('href="')[1:]:
# # #             file_name = file.split('"')[0]
# # #             if '.' in file_name:
# # #                 files_list.append(file_name)
    
# # #     return files_list

# # # # Function to download files from the target domain
# # # def download_files(target_domain, files_list):
# # #     url = f"http://{target_domain}/"
    
# # #     for file_name in files_list:
# # #         file_url = f"{url}{file_name}"
# # #         response = requests.get(file_url)
        
# # #         if response.status_code == 200:
# # #             with open(file_name, 'wb') as file:
# # #                 file.write(response.content)
# # #                 print(f"{file_name} downloaded successfully")
# # #         else:
# # #             print(f"Failed to download {file_name}")

# # # # Main function to use the above functions
# # # def main():
# # #     target_domain = "https://jobinja.ir"
# # #     files_list = enumerate_files(target_domain)
    
# # #     if files_list:
# # #         download_files(target_domain, files_list)
# # #     else:
# # #         print("No files found on the target domain")

# # # if __name__ == "__main__":
# # #     main()


# # # import wget

# # # print('Beginning file download with wget module')

# # # url = 'http://jobinja.ir'
# # # wget.download(url, r'C:\Users\star pc\Desktop\cat4.jpg')

# # # import requests

# # # s=requests.get('https://downloadscdn6.freepik.com/23/2151311/2151310893.jpg?filename=smart-feeder-pets-still-life.jpg&token=exp=1715678276~hmac=64252abb55c1c3a0e9f0968fd6a9617b&_gl=1*issch9*_ga*MTE3NDU3MDQ3OS4xNzE1Njc3MzMw*_ga_QWX66025LC*MTcxNTY3NzMyOS4xLjEuMTcxNTY3NzM3OC4xMS4wLjA.')
# # # with open('E:\lllustrator   تمرینیییی','wb') as f:
# # #     f.write()


# # # import requests

# # # def download_image(url, save_as):
# # #     response = requests.get(url)
# # #     with open(save_as, 'wb') as file:
# # #         file.write(response.content)

# # # save_as = 'image.jpg'
# # # image_url = 'https://downloadscdn6.freepik.com/23/2151311/2151310893.jpg?filename=smart-feeder-pets-still-life.jpg&token=exp=1715678835~hmac=5b49b6a9552df9c9a5afd718140d1a61&_gl=1*1en2gub*_ga*MTE3NDU3MDQ3OS4xNzE1Njc3MzMw*_ga_QWX66025LC*MTcxNTY3NzMyOS4xLjEuMTcxNTY3NzkzNy4yLjAuMA..'

# # # download_image(image_url, save_as)







# # # from urllib.parse import urljoin, urlparse
# # # import os
# # # import shutil

# # # s=[]
# # # url="https://mrbug.ir"
# # # request=requests.get(url)                
# # # content=request.content
# # # soup=BeautifulSoup(content,"html.parser")
# # # for j in soup.find_all('img'):
# # #    try:
# # #         r=requests.get(j.get('src'))
# # #         print(j.get('src'))
# # #         desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
# # #         files_folder = os.path.join(desktop_path, 'image')
# # #         os.makedirs(files_folder, exist_ok=True)
# # #         file_name = os.path.basename(urlparse(j.get('src')).path)        
# # #         file_path = os.path.join(files_folder, file_name)
# # #         with open(file_path, 'wb') as file:
# # #                 file.write(r.content)
# # #    except:
# # #         pass













# # # import os
# # # import requests
# # # from bs4 import BeautifulSoup

# # # # آدرس صفحه وب مورد نظر
# # # url = "https://mrbug.ir"

# # # # ارسال درخواست GET به صفحه وب
# # # response = requests.get(url)

# # # # چک کردن وضعیت درخواست
# # # if response.status_code == 200:
# # #     # تجزیه و تحلیل محتوای HTML صفحه وب
# # #     soup = BeautifulSoup(response.text, 'html.parser')
    
# # #     # ایجاد یک پوشه برای ذخیره فایل‌ها در دسکتاپ
# # #     desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
# # #     files_folder = os.path.join(desktop_path, 'downloaded_files')
# # #     os.makedirs(files_folder, exist_ok=True)
    
# # #     # یافتن و دانلود تصاویر و فایل‌ها
# # #     for tag in soup.find_all(['img', 'a']):
# # #         file_url = tag.get('src') or tag.get('href')
# # #         if file_url and file_url.startswith('http'):
# # #             # دریافت نام فایل از آدرس
# # #             file_name = os.path.basename(urlparse(file_url).path)
            
# # #             # چک کردن پسوند فایل
# # #             file_extension = os.path.splitext(file_name)[1].lower()
# # #             if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ico']:
# # #                 # دریافت محتوا
# # #                 file_content = requests.get(file_url).content
                
# # #                 # ذخیره فایل در پوشه مقصد
# # #                 file_path = os.path.join(files_folder, file_name)
# # #                 with open(file_path, 'wb') as file:
# # #                     file.write(file_content)
                
# # #                 print(f"File '{file_name}' downloaded successfully.")
# # #             else:
# # #                 print(f"Ignored file '{file_name}' (unsupported format).")
    
# # #     print("All files downloaded successfully!")
# # # else:
# # #     print('Failed to retrieve page:', response.status_code)



# # # import requests

# # # url = "https://api.wappalyzer.com/lookup/v1/"
# # # headers = {"X-Api-Key": "YOUR_API_KEY"}

# # # website = "https://google.com"
# # # data = {"url": website}

# # # response = requests.post(url, headers=headers, json=data)

# # # if response.status_code == 200:
# # #     apps = response.json()
# # #     for app in apps:
# # #         print(app)
# # # else:
# # #     print("Failed to retrieve data. Status code: ", response.status_code)



# # # import requests

# # # url = "https://api.wappalyzer.com/lookup/v1/"
# # # headers = {"X-Api-Key": "YOUR_API_KEY"}

# # # website = "https://github.com"
# # # data = {"url": website}

# # # response = requests.post(url, headers=headers, json=data)

# # # if response.status_code == 200:
# # #     apps = response.json()
# # #     print(apps)
# # # else:
# # #     print("Failed to retrieve data. Status code: ", response.status_code)





# # # python -m pip install python-Wappalyzer


# # # def get_wappalyzer(url):
# # #     wappalyzer = Wappalyzer.latest()
# # #     webpage = WebPage.new_from_url('https://' + url)
# # #     data = wappalyzer.analyze_with_versions_and_categories(webpage)
# # #     return data
# # # f="mrbug.ir"
# # # get_wappalyzer(f)


# # # from Wappalyzer import Wappalyzer, WebPage

# # # def get_wappalyzer(url):
# # #     wappalyzer = Wappalyzer.latest()
# # #     webpage = WebPage.new_from_url('https://' + url)
# # #     data = wappalyzer.analyze_with_versions_and_categories(webpage)
# # #     return data

# # # f = "mrbug.ir"
# # # result = get_wappalyzer(f)
# # # print(result)

# # # # URL of the website you want to analyze
# # # website_url = "https://example.com"

# # # # Create a Wappalyzer instance
# # # wappalyzer = Wappalyzer()

# # # # Load the website using WebPage class
# # # webpage = WebPage.new_from_url(website_url)

# # # # Analyze the website and get the technologies used
# # # technologies = wappalyzer.analyze(webpage)

# # # # Print the detected technologies
# # # for technology in technologies:
# # #     print(technology)


# # # from pywappalyzer import wappalyzer, webpage

# # # # URL of the website you want to analyze
# # # website_url = "https://example.com"

# # # # Create a Wappalyzer instance
# # # wappalyzer = wappalyzer.Wappalyzer()

# # # # Load the website using WebPage class
# # # webpage = WebPage.new_from_url(website_url)

# # # # Analyze the website and get the technologies used
# # # technologies = wappalyzer.analyze(webpage)

# # # # Print the detected technologies
# # # for technology in technologies:
# # #     print(technology)

# # # from pywappalyzer import wappalyzer, WebPage

# # # # URL of the website you want to analyze
# # # website_url = "https://example.com"

# # # # Create a Wappalyzer instance
# # # wappalyzer = wappalyzer.Wappalyzer()

# # # # Load the website using WebPage class
# # # webpage = WebPage.new_from_url(website_url)

# # # # Analyze the website and get the technologies used
# # # technologies = wappalyzer.analyze(webpage)

# # # # Print the detected technologies
# # # for technology in technologies:
# # #     print(technology)





# # # from Wappalyzer import WebPage , Wappalyzer
# # # def step12():
# # #     wap = Wappalyzer.Wappalyzer
# # #     try : 
# # #         web = WebPage.new_from_url("https://digikala.com")
# # #         technoligies = wap.analyze(web)
# # #         for t in technoligies:
# # #             print("technoligies detected : {}".format(t))
# # #     except:
# # #         print("ERROR!!!")
# # # try:
# # #         step12()
# # # except KeyboardInterrupt:
# # #         print("bye")
# # #         exit()























# # # from Wappalyzer import Wappalyzer, WebPage

# # # def analyze_website(url):
# # #     try:
# # #         # ایجاد یک نمونه از کلاس Wappalyzer
# # #         wappalyzer = Wappalyzer

# # #         # ایجاد یک نمونه از کلاس WebPage برای آدرس وب‌سایت مورد نظر
# # #         webpage = WebPage.new_from_url(url)

# # #         # تحلیل تکنولوژی‌های مورد استفاده در وب‌سایت
# # #         technologies = wappalyzer.analyze(webpage)

# # #         # چاپ تکنولوژی‌های تشخیص داده شده
# # #         for tech in technologies:
# # #             print("Technology detected: {}".format(tech))
# # #     except Exception as e:
# # #         print("ERROR:", e)

# # # def main():
# # #     # آدرس وب‌سایت مورد نظر
# # #     website_url = "https://digikala.com"

# # #     # تحلیل و چاپ تکنولوژی‌های مورد استفاده در وب‌سایت
# # #     analyze_website(website_url)

# # # if __name__ == "__main__":
# # #     main()









# # # .
# # # .
# # # .
# # # .
# # # from PIL import ImageGrab

# # # # Capture the entire screen
# # # screenshot = ImageGrab.grab()

# # # # Save the screenshot to a file
# # # screenshot.save("screenshot.png")

# # # # Close the screenshot
# # # screenshot.close()
# # # .
# # # .
# # # .
# # # .
# # # .
# # # .         



# # # import subprocess
# # # from pathlib import Path
# # # import os
# # # from selenium import webdriver
# # # import os
# # # import time
# # # from selenium import webdriver


# # # def go_witness(url, path, type = 'png'):
# # #     """insert just path object \n
# # #         type: png or pdf """
    
# # #     Path(path).mkdir(parents=True, exist_ok=True)
# # #     image_path = os.path.join(path, f'{url}.png')
# # #     # Create a new instance of the Firefox driver
# # #     try:
# # #         options = webdriver.ChromeOptions()
# # #         options.add_argument('headless')

# # #         driver = webdriver.Chrome(options=options)

# # #         # Go to the Google website
# # #         driver.get(f'https://{url}')

# # #         time.sleep(1)
# # #         # Take a screenshot of the webpage
# # #         driver.save_screenshot(image_path)

# # #         # Close the driver
# # #         driver.quit()
# # #         return image_path 
# # #     except:
# # #         return ""
# # # url="mrbug,ir"
# # # path="Desktop"
# # # go_witness(url, path, type = 'png')





















# # # اسکرین شات اصتی
# # # from selenium import webdriver
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # url = "https://mrbug.ir"  # URL مورد نظر خود را وارد کنید

# # # # راه‌اندازی مرورگر Chrome
# # # driver = webdriver.Chrome(options=webdriver.ChromeOptions())

# # # # باز کردن صفحه مورد نظر
# # # driver.get(url)

# # # # گرفتن اسکرین‌شات
# # # driver.save_screenshot("screenshot.png")

# # # # بستن مرورگر
# # # driver.quit()

# # # تا اینجا

























# # # from selenium import webdriver
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # url = "https://tavapc.ir"  # URL مورد نظر خود را وارد کنید

# # # # تنظیمات مرورگر
# # # chrome_options = webdriver.ChromeOptions()
# # # chrome_options.add_argument("--headless")  # اجرای در حالت Headless

# # # # راه‌اندازی مرورگر Chrome با تنظیمات
# # # driver = webdriver.Chrome(options=webdriver.ChromeOptions())

# # # # باز کردن صفحه مورد نظر
# # # driver.get(url)

# # # # گرفتن اسکرین‌شات
# # # driver.save_screenshot("screenshot.png")

# # # # بستن مرورگر
# # # driver.quit()


















# # # import os
# # # from selenium import webdriver
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # url = "https://digikala.com"  # URL مورد نظر خود را وارد کنید

# # # # تنظیمات مرورگر
# # # chrome_options = webdriver.ChromeOptions()
# # # chrome_options.add_argument("--headless")  # اجرای در حالت Headless

# # # # راه‌اندازی مرورگر Chrome با تنظیمات
# # # driver = webdriver.Chrome(options=webdriver.ChromeOptions())

# # # # باز کردن صفحه مورد نظر
# # # driver.get(url)

# # # # گرفتن اسکرین‌شات
# # # screenshot_path = "screenshot.png"
# # # driver.save_screenshot(screenshot_path)

# # # # ذخیره عکس در پوشه "screenshots"
# # # destination_folder = "screenshots"
# # # if not os.path.exists(destination_folder):
# # #     os.makedirs(destination_folder)
# # # os.rename(screenshot_path, os.path.join(destination_folder, screenshot_path))

# # # # بستن مرورگر
# # # driver.quit()

























# # # import requests
# # # from concurrent.futures import ThreadPoolExecutor
# # # from bs4 import BeautifulSoup

# # # # تابع برای ارسال درخواست و دریافت داده‌ها از یک URL
# # # def fetch_data(url):
# # #     try:
# # #         response = requests.get(url)
# # #         response.raise_for_status()  # بررسی خطاهای HTTP
# # #         return response.text
# # #     except requests.RequestException as e:
# # #         print(f"Error fetching {url}: {e}")
# # #         return None

# # # # تابع برای تجزیه و تحلیل داده‌های HTML و استخراج اطلاعات مورد نظر
# # # def parse_data(html):
# # #     if html:
# # #         soup = BeautifulSoup(html, 'html.parser')
# # #         title = soup.find('title').get_text()
# # #         return title
# # #     return "No data"

# # # # لیست URLها
# # # urls = ['https://mrbug.ir', 'https://time.ir']

# # # # تابع اصلی برای مدیریت همزمانی و اجرای درخواست‌ها
# # # def main():
# # #     with ThreadPoolExecutor(max_workers=5) as executor:  # می‌توانید max_workers را بسته به نیاز خود تنظیم کنید
# # #         html_responses = list(executor.map(fetch_data, urls))
# # #         data = [parse_data(html) for html in html_responses]
# # #         for idx, datum in enumerate(data):
# # #             print(f"Data from site {idx + 1}: {datum}")

# # # if __name__ == "__main__":
# # #     main()









# # import requests
# # from bs4 import BeautifulSoup
# # import dns.resolver
# # import re
# # import socket
# # import whois
# # import argparse
# # import argparse
# # import os
# # from urllib.parse import urljoin, urlparse
# # from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager



# # import os
# # import requests
# from bs4 import BeautifulSoup
# # from urllib.parse import urlparse
# # import os
# # import requests
# # from bs4 import BeautifulSoup
# # from urllib.parse import urljoin, urlparse

# # # # ارسال درخواست به سایت
# # # response = requests.get("https://mongard.ir")
# # # content = response.content
# # # soup = BeautifulSoup(content, "html.parser")

# # # # ایجاد مسیر پوشه برای ذخیره تصاویر
# # # desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
# # # files_folder = os.path.join(desktop_path, 'images')
# # # os.makedirs(files_folder, exist_ok=True)

# # # # استخراج و ذخیره تصاویر
# # # for img_tag in soup.find_all('img'):
# # #     try:
# # #         img_url = img_tag.get('src')
        
# # #         # بررسی معتبر بودن URL تصویر
# # #         if img_url:
# # #             # ساخت URL کامل در صورت نیاز
# # #             img_url = urljoin(response.url, img_url)
            
# # #             # ارسال درخواست به URL تصویر
# # #             r = requests.get(img_url, stream=True)
            
# # #             if r.status_code == 200:
# # #                 # استخراج نام فایل و مسیر ذخیره
# # #                 file_name = os.path.basename(urlparse(img_url).path)
# # #                 file_path = os.path.join(files_folder, file_name)
                
# # #                 # اطمینان از یکتا بودن نام فایل
# # #                 base, extension = os.path.splitext(file_name)
# # #                 counter = 1
# # #                 while os.path.exists(file_path):
# # #                     file_name = f"{base}_{counter}{extension}"
# # #                     file_path = os.path.join(files_folder, file_name)
# # #                     counter += 1
                
# # #                 # ذخیره تصویر
# # #                 with open(file_path, 'wb') as file:
# # #                     for chunk in r.iter_content(1024):
# # #                         file.write(chunk)
# # #                 print(f'Saved: {file_path}')
# # #             else:
# # #                 print(f'Failed to retrieve image: {img_url} (Status code: {r.status_code})')
# # #         else:
# # #             print(f'Invalid image URL: {img_url}')
# # #     except Exception as e:
# # #         print(f'Error: {e} (URL: {img_url})')




# # # request=requests.get("https://mongard.ir")                
# # # content=request.content
# # # soup=BeautifulSoup(content,"html.parser")
# # # for j in soup.find_all('img'):
# # #         try:
# # #                 r=requests.get(j.get('src'))
# # #                 print(j.get('src'))
# # #                 desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
# # #                 files_folder = os.path.join(desktop_path, 'image')
# # #                 os.makedirs(files_folder, exist_ok=True)
# # #                 file_name = os.path.basename(urlparse(j.get('src')).path)        
# # #                 file_path = os.path.join(files_folder, file_name)
# # #                 with open(file_path, 'wb') as file:
# # #                         file.write(r.content)
# # #         except:
# # #                 pass




# import requests
# soup = BeautifulSoup("<html></html>", "html.parser")

# # اضافه کردن head
# head = soup.new_tag("head")
# title = soup.new_tag("title")
# title.string = "ReconePie"
# head.append(title)
# soup.html.append(head)
# icon=soup.new_tag("link" , rel="icon",href="./Python.svg.png")
# head.append(icon)
# css=soup.new_tag("link",rel="stylesheet",href="./style.css")
# head.append(css)



# # اضافه کردن body
# body = soup.new_tag("body")
# soup.html.append(body)

# h1 = soup.new_tag("h1")
# h1.string = "Reconpie project-created by rez"
# body.append(h1)


# def request(url):
#         print("r")
#         soup=""
#         try:
#                 request=requests.get(url)                
#                 content=request.content
#                 soup=BeautifulSoup(content,"html.parser")
#                 if soup is not None :
#                     return soup
#         except :
#                 pass
# def title(soup):
#       print("t")
#       title=""
#       try:
#         title=soup.select('title')[0].text
#         if title is not None :
#             return title
#       except :
#            pass
      
# w=title(request("https://mrbug.ir"))
# item=soup.new_tag("p")
# item.string=w
# body.append(item)  

# file_name = "reza.html"
# with open(file_name, "w",encoding="utf-8") as file:

from bs4 import BeautifulSoup
import chardet

soup = BeautifulSoup("<html></html>", "html.parser")

# اضافه کردن head
head = soup.new_tag("head")
title = soup.new_tag("title")
title.string = "ReconePie"
head.append(title)
soup.html.append(head)
icon=soup.new_tag("link" , rel="icon",href="./Python.svg.png")
head.append(icon)
css=soup.new_tag("link",rel="stylesheet",href="./style.css")
head.append(css)




# اضافه کردن body
body = soup.new_tag("body")
soup.html.append(body)
h1 = soup.new_tag("h1")
h1.string = "Reconpie project-created by rez"
body.append(h1)
# از اینجا تا خط 982 رو بعد از بادیه بزار مثل همین کد یعنی بزار بعد اچ وان
header=soup.new_tag("span",id="span")
header.string="what do we do in this project?"
body.append(header)
captin=soup.new_tag("p",id="caption")
captin.string="In this project, we first get all the links of the desired site. Then, by using them, we get all the domains of the links, status codes, and titles. Then we get the IP of each link and the open ports in turn. We will find them. After that, we will find all the emails and phone numbers using the Regges language, and we will get all the specifications and information of the site builders using the Huiz library, and in the last step, all the files loaded on We download the siteWe hope you enjoy this project"
body.append(captin)






def write_to_html():
     f=open("list.txt","rb")
     raw_data = f.read()
     result = chardet.detect(raw_data)
     encoding = result['encoding']
     f.close()
     file=open("list.txt","r",encoding=encoding)
     for i in file.readlines():
          line=i.strip()
          information=soup.new_tag("p")
          information.string=line
          body.append(information)

write_to_html()
# از اینجا تا خط 1007 رو بزار قبل از کد سیو و رایت اچ تی ام ال قبل فایل نیم مثل همینجا

i=soup.new_tag("img",id="ifg",src="./hack.jpg")
body.append(i)
git=soup.new_tag("a",target="blank",href="https://github.com/rnasrollahi",id="git")
git.string="See my github"
body.append(git)

js=soup.new_tag("script",src="./js.js")
body.append(js)

file_name = "index.html"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(str(soup.prettify()))











