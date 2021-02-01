#!/bin/python3

#A script by Lmmp04
#This script can be used to check if a website is up, along with latency by pinging and it can also test for changes on one of the listed websites.

import multiping
import socket
import random
import os

urls = ["google"], ["bing"], ["yahoo"], ["duckduckgo"], ["Yandex"]
ips = ["172.217.12.174"], ["204.79.197.200"], ["74.6.231.20"], ["52.149.246.39"], ["5.255.255.80"]

port = 80
googles_ip = socket.gethostbyname('google.com')
bings_ip = socket.gethostbyname('bing.com')
yahoos_ip = socket.gethostbyname('yahoo.com')
duckduckgos_ip = socket.gethostbyname('duckduckgo.com')
yandexs_ip = socket.gethostbyname('yandex.com')

#google = 172.217.12.174
#bing = 204.79.197.200
#yahoo = 74.6.231.20
#duckduckgo = 52.149.246.39
#yandex = 5.255.255.80

print ("[1]: Google.com")
print ("[2]: Bing.com")
print ("[3]: Yahoo.com")
print ("[4]: Yandex.com")

answer = input("Which of these websites would you like to monitor? Choose 1-5:  ").lower().strip()
if answer == "1":
	print ("-"*75)
	print ("Currently monitoring Google.com")
	print (ips[0])
	print ("")	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created...")
	s.connect((googles_ip, port))
	print ("")
	print ("Successfully connected to google.com, The website is up!")
	print ("")
	print ("Pinging Google.com to check for latency")
	os.system('ping -c 3 ' + googles_ip)
if answer == "2": 
	print ("-"*75)
	print ("Currently monitoring Bing.com")
	print (ips[1])
	print ("")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created...")
	print ("")
	s.connect((bings_ip, port))
	print ("")
	print ("Successfully connected to Bing.com, The website is up!")
	print ("")
	print ("Pinging Bing.com to check for latency.")
	print ("")
	os.system('ping -c 3 ' + bings_ip)
if answer == "3":
	print ("-"*75)
	print ("Currently monitoring Yahoo.com")
	print (ips[2])
	print ("")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket succesfully created...")
	s.connect((yahoos_ip, port))
	print ("")
	print ("Successfully connected to Yahoo.com, The website is up!")
	print ("")
	print ("Pinging Yahoo.com to check for latency")
	os.system('ping -c 3 ' + yahoos_ip)
if answer == "4":
	print ("-"*75)
	print ("Currently monitoring Yandex.com")
	print (ips[4])
	print ("")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created...")
	s.connect((yandexs_ip, port))
	print ("")
	print ("Successfully connected to Yandex.com, The website is up!")
	print ("")
	print ("Pinging Yandex.com to check for latency")
	print ("")
	os.system('ping -c 3 ' + yandexs_ip)
else:
	exit()
