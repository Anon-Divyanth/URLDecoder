import os
import mechanize
from bs4 import BeautifulSoup
from time import sleep

os.system("clear")
sleep(1)

print ("""\033[1;31m

                (    (         (                                         
                )\ ) )\ )      )\ )                  (          
            (  (()/((()/(     (()/(     (            )\ )   (   
            )\  /(_))/(_))___  /(_))   ))\  (   (   (()/(  ))\  
         _ ((_)(_)) (_)) |___|(_))_   /((_) )\  )\   ((_))/((_) 
  \033[1;32m      | | | || _ \| |        |   \ \033[1;31m(_))  ((_)((_)  \033[1;32m_| |(_))   
        | |_| ||   /| |__      | |) |/ -_)/ _|/ _ \/ _` |/ -_)  
         \___/ |_|_\|____|     |___/ \___|\__|\___/\__,_|\___| 


  Decode \033[4m Bitly,Tiny,google,Rebrandly,Hyperlink,Tiny.C,Phishing \033[0m \033[1;32mand more

          <<<\033[1;31m Find original url don't click Phishing Links\033[1;32m >>>\033[1;0m\n\n\n
""")

sleep(1)
anon = input("\033[1;32m[*] \033[1;31m paste here your short URL :\033[1;32m ")
sleep(1)
print ("\033[1;0m\t Please Wait..\n")
url = 'https://checkshorturl.com'
br = mechanize.Browser()
br.open(url)
br.select_form(name="formulaire")
br['u'] = anon
res = br.submit().read()
soup = BeautifulSoup(res,'html.parser')
table = soup.find('table')
tr = table.find('tr')
print("\033[1;32m[*] Success.,\033[1;0m your URL is succesfully Decoded\n\n\n")
x = "\033[1;31m[*]\033[1;32m original"
sleep(3)
print(x+tr.text)
print("\033[1;0m")
sleep(1)

