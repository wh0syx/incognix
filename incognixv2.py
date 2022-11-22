import pyperclip as c
import requests, time, re
from colorama import init, Fore, Back, Style

url = 'https://www.1secmail.com/api/v1/'
update = True

def rainbow():
    init(autoreset=True)
    r = ('\x1b[38;5;160m'+'██╗███╗░░██╗░█████╗░░█████╗░░██████╗░███╗░░██╗██╗██╗░░██╗') 
    a = ('\x1b[38;5;208m'+'██║████╗░██║██╔══██╗██╔══██╗██╔════╝░████╗░██║██║╚██╗██╔╝')
    i = ('\x1b[38;5;220m'+'██║██╔██╗██║██║░░╚═╝██║░░██║██║░░██╗░██╔██╗██║██║░╚███╔╝░')
    n = ('\x1b[38;5;40m' +'██║██║╚████║██║░░██╗██║░░██║██║░░╚██╗██║╚████║██║░██╔██╗░')
    b = ('\x1b[38;5;27m' +'██║██║░╚███║╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║██║██╔╝╚██╗')
    o = ('\x1b[38;5;93m' +'╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝')
    w = ('\x1b[38;5;201m'+'✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶[by wh0syx]✶✶✶✶✶✶✶')
    print('{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}'.format(r,a,i,n,b,o,w))

rainbow()

def get_email_address():
    r = requests.get(url, params={'action': 'genRandomMailbox', 'count': '1'}).json()
    email = r[0]
    c.copy(email)
    print(Fore.GREEN+"Your email address is: {0}".format(Fore.RED+email))
    return str(email)

def get_activation_code(email=get_email_address()):
    login = email.split('@')[0]
    domain = email.split('@')[1]
    print(Fore.GREEN+'Email address '+Fore.RED+'has been copied to the clipboard!'+Fore.GREEN+'\nWaiting your activation code...')
    while update:
        time.sleep(5)
        r = requests.get(url, params={'action': 'getMessages','login': login,'domain':domain}).json()
        if r == []:
            continue
        else:
            lastMessageID = r[0]['id']
            r = requests.get(url, params={'action': 'readMessage','login': login,'domain':domain,'id': lastMessageID}).json()
            activationCode = re.findall('\d+',r['textBody'])
            print("Your code is: {0}".format(activationCode[0]))
            quit()

get_activation_code()