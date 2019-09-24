#!/usr/bin/env python3
import bs4
import re
import requests
import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#my_url = input('please enter link you want to scrape: ')
##
#https://www.udemy.com/courses/development/software-engineering/?lang=en&price=price-free&ratings=4.0&sort=popularity
##
InputLang = input('Enter Language (en): ')
if InputLang == '':
    Lang = 'en'
else:
    Lang = InputLang
    print(Lang)

InputCost = input('Enter Free or Paid  : ')
if InputCost == '':
        Cost = 'Free'
else:
        Cost = InputCost
        print (Cost)

InputRating = input('Enter Rating 1 - 5 :')
if InputRating == '':
    Rating = '4.0'
else:
    Rating = (InputRating)
    print(Rating)


my_url = 'https://www.udemy.com/courses/development/software-engineering/?lang='+Lang+'&price=price-'+Cost+'&ratings-'+Rating+'sort=popularity'
#open connection to the webpage
uClient = uReq(my_url)
#Grab the info from the page
page_html = uClient.read()
#save the response into var 'page_html'
uClient.close()
# HTML Parse
page_soup = soup(page_html, 'html.parser')

######Newegg scraper setting #######
#grabs products
DescContainer = page_soup.findAll("div",{"class":"item-container"})
CurrentPriceContainer = page_soup.findAll("li",{"class":"price-current"})
#save results to a CSV
filename = "Hard_Drive_Prices.csv"
header = ['Brand','Model','Capacity','Current Price']

#with open(filename, 'w', newline='')as f_output:
#    csv_output = csv.writer(f_output)
#    csv_output.writerow(header)
#    ###Scrape Function for New egg
#  for container in DescContainer:
#        # HardDrive Scraping Vars
#    print (itemPricing)
