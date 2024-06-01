import requests
from bs4 import BeautifulSoup
import dns.resolver
import re
import socket
import whois
import argparse
import argparse
import os
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import chardet
parser=argparse.ArgumentParser()
parser.add_argument('-u','--url',help='ENTER URL')
url=parser.parse_args()
href=[]
href2=[]
number_url=0
def remove():

    try:
        text_file = open("list.txt", "r")
   
    finally:
        text_file.close()
       

        with open("list.txt", "w") as file:
            file.truncate(0)


remove()

soup = BeautifulSoup("<html></html>", "html.parser")
head = soup.new_tag("head")
title = soup.new_tag("title")
title.string = "ReconePie"
head.append(title)
soup.html.append(head)
icon=soup.new_tag("link" , rel="icon",href="./Python.svg.png")
head.append(icon)
css=soup.new_tag("link",rel="stylesheet",href="./style.css")
head.append(css)
title_page=soup.new_tag("a",href=url.url,target="blank",id="link")
title_page.string="main link"



body = soup.new_tag("body")
soup.html.append(body)
h1 = soup.new_tag("h1")
h1.string = "Reconpie project-created by rez"
body.append(h1)
body.append(title_page)
header=soup.new_tag("span",id="span")
header.string="what do we do in this project?"
body.append(header)
captin=soup.new_tag("p",id="caption")
captin.string="In this project, we first get all the links of the desired site. Then, by using them, we get all the domains of the links, status codes, and titles. Then we get the IP of each link and the open ports in turn. We will find them. After that, we will find all the emails and phone numbers using the Regges language, and we will get all the specifications and information of the site builders using the Huiz library, and in the last step, all the files loaded on We download the siteWe hope you enjoy this project"
body.append(captin)



def get_image(url):
    print("image")
    request=requests.get(url)                
    content=request.content
    soup=BeautifulSoup(content,"html.parser")
    for j in soup.find_all('img'):
        try:
                r=requests.get(j.get('src'))
                print(j.get('src'))
                desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
                files_folder = os.path.join(desktop_path, 'image')
                os.makedirs(files_folder, exist_ok=True)
                file_name = os.path.basename(urlparse(j.get('src')).path)        
                file_path = os.path.join(files_folder, file_name)
                with open(file_path, 'wb') as file:
                        file.write(r.content)
        except:
                pass

def get_screenshot(url):
    print("screen")
    driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    driver.get(url)
    driver.save_screenshot("screenshot.png")
    driver.quit()

def get_links(url,href,):
    print("get")
    get_screenshot(url.url)
    get_image(url.url)
    href.append(url.url)
    request=requests.get(url.url)
    content=request.content
    soup=BeautifulSoup(content,"html.parser")

    for i in soup.find_all('a'):
        try:
            print(i.get('href'))
            request=requests.get(i.get('href'))
            if request.status_code==200:
                href.append(i.get('href'))
        except:
             print("no")
             pass
get_links(url,href)

def request(url):
        print("r")
        soup=""
        try:
                request=requests.get(url)                
                content=request.content
                soup=BeautifulSoup(content,"html.parser")
                if soup is not None :
                    return soup
        except :
                pass

def title(soup):
      print("t")
      title=""
      try:
        title=soup.select('title')[0].text
        if title is not None :
            return title
      except :
           pass

def status_code(url):
       print("sc")
       stat=""
       try:
            request=requests.get(url)                
            stat=request.status_code  
            if stat is not None :
                return stat
       except:
            pass

def subsomain(x):
      print("s")
      subdomein=""
      fsub=open("wordlist.txt","r")
      filesub=fsub.read()
      subdomains=filesub.splitlines()
      for sub  in subdomains:
            domain = re.sub(r"https?://(?:www\.)?([^/]+).*", r"\1", x)                 
            url2=f"https://{sub}.{domain}"  
                                                   
            try:
                requests.get(url2)
                subdomein+=sub+" , "                        
            except :                      
                pass
      return subdomein

def ip_address(url):
    print("i")
    ip_address=""
    domainip = re.sub(r"https?://(?:www\.)?([^/]+).*", r"\1",url)    
    try: 
        ip_address = socket.gethostbyname(domainip) 
        if ip_address is not None:
            return str(ip_address)
    except :
         pass
    
def port_scan(url):
    print("p")
    open_port=""
    ports = [21,53, 80,123, 143,443, 445, 993]
    domain = ip_address(url)
    for port in ports:  
        try:
            if domain is not None and port is not None:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1) 
                sok = sock.connect_ex((domain, port))
                if sok == 0:
                    open_port+=" {} ".format(port)+" , "
                
                sock.close()
        except socket.error:
            pass
    return open_port

def whoiss (ip):
     try:
        w = whois.whois(ip)
        return w
     except :
          pass

def regex_phonenumber(url):
     try:
        request=requests.get(url)                
        p=re.findall(r'09\d{9}',request.text)
        phone=f" {p} ,"
        return phone
     except :
           pass

def regex_emeil(url):
     try : 
        request=requests.get(url)                
        e=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',request.text)
        emeil=f" {e} ,"
        return emeil
     except:
          pass

def call_fanction(href,url,number_url):
    print("call")
    number_url=0
    for j in href:
        number_url+=int(1)
    for i in range(75,number_url-1):
            url=href[i]
            print(url)
            w=[".......................................",'\n','////////',url,'\n',"  subdomain : ", subsomain(url),'\n',"  title: ",str(title(request(url))),'\n',"  status_code : ",str(status_code(url)),'\n'," ip : ",str(ip_address(url)),'\n'," open port : ", port_scan(url),'\n'," emeil : ",regex_emeil(url),'\n'," phone number : ",regex_phonenumber(url),'\n'," whois : ",whoiss(ip_address(url)),'\n']
            print(w)
            for item in w:
                if item is None:
                    item = ""
                else:
                    # item = item
                    f = open("list.txt", "a", encoding='utf-8')
                    f.writelines(item)
                    f.close()
            try:
                for j in request(url).find_all('a'):
                    print(j.get('href'))
                    try:
                         respons=requests.get(j.get('href'))
                         if respons.status_code==200:
                                wj=['>>>>',j.get('href'),'\n',"  title:  ",title(request(j.get('href'))),'\n',"  status_code : ",str(status_code(j.get('href'))),'\n',"  subdomain : ",subsomain(j.get('href')),'\n'," ip : ",ip_address(j.get('href')),'\n'," open port : ", port_scan(j.get('href')),'\n'," emeil : ",regex_emeil(j.get('href')),'\n'," phone number : ",regex_phonenumber(j.get('href')),'\n'," whois : ",whoiss(ip_address(j.get('href'))),'\n']
                                print(wj)
                                for item in wj:
                                        if item is None:
                                            item = ""
                                        else:
                                            # item = item
                                            fj = open("list.txt", "a", encoding='utf-8')
                                            fj.writelines(item)
                                            fj.close()
                                
                                href.append(j.get('href'))

                    except:
                         pass
            except:
                pass

call_fanction(href,url,number_url)

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

i=soup.new_tag("img",id="ifg",src="./hack.jpg")
body.append(i)
git=soup.new_tag("a",target="blank",href="https://github.com/Rnasrollahi",id="git")
git.string="See my github"
body.append(git)

js=soup.new_tag("script",src="./js.js")
body.append(js)

file_name = "index.html"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(str(soup.prettify()))

