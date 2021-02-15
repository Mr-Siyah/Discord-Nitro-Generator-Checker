import random, string
import webbrowser
import time
import requests
import os

os.system("clear")

print("""
███╗░░██╗██╗████████╗██████╗░░█████╗░░░░░░░░██████╗░██╗███████╗████████╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗░░░░░░██╔════╝░██║██╔════╝╚══██╔══╝
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║█████╗██║░░██╗░██║█████╗░░░░░██║░░░
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║╚════╝██║░░╚██╗██║██╔══╝░░░░░██║░░░
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝░░░░░░╚██████╔╝██║██║░░░░░░░░██║░░░
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░
░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
░░██╗░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
╚═██╔═╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚═╝░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
  
  
 
  
  



  
time.sleep(2)

print("Developer  -  MR.SİYAH ")
time.sleep(0.3)

print(" M'N | https://discord.gg/dxF78pPB3S\n")
time.sleep(0.2)

print(" 02/02/21 | https://youtube.com/channel/UCVT2mKGHannnGZXyPjDXCNw\n")
time.sleep(0.2)

num=input('Ne Kadar Nitro Kodu Üretilsin: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Bekle, Senin İçin Üretiyoruz!")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
        	print("Geçersiz | {} ".format(line.strip("\n")))
input("İşte Bitti! 5 Defa Basıp Programı Kapatabilirsin.\n")
input("4")
input("3")
input("2")
input("1")
