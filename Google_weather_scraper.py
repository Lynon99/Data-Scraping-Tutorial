import requests

from bs4 import *

print("""           .
         .   :   .  
     '.   .  :  .   .'
  ._   '._.-'''-._.'   _.
    '-..'         '..-' 
 --._ /.==.     .==.\ _.--
     ;/_o__\   /_o__\;
-----|`     ) (     `|-----
    _: \_) (\_/) (_/ ;_
 --'  \  '._.=._.'  /  '--
   _.-''.  '._.'  .''-._
  '    .''-.(_).-''.    '
     .'   '  :  '   '.
        '    :   '
             '
""")

# Ask the user what city they would like to query

city_input = str(input("In what city would you like to know the weather?\n"))

# Create the URL that will be used by requests and bs4

url = f"https://www.google.com/search?q=weather+in+{city_input}"

# request the instance using the module

res = requests.get(url).content

# Get the raw HTML/CSS using bs4

soup = BeautifulSoup(res, 'html.parser')

# Getting the temp from google search

temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# Now its time for the time ;)
time_desc = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# Beautifying the data

data = time_desc.split('\n')
time = data[0]
sky = data[1]

# Print results

print(f"Temperature is: {temp}\nTime is: {time}\nSky Description: {sky}")
#Prevents window from closing in pyintaller
block = input('')







