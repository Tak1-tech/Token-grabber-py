import requests #line:1:import requests
import json #line:2:import json
import sys #line:3:import sys
from datetime import datetime #line:5:from datetime import datetime
from colorama import Fore ,init #line:6:from colorama import Fore, init
__version__ =1.9 #line:8:__version__ = 1.9
languages ={'da':'Danish, Denmark','de':'German, Germany','en-GB':'English, United Kingdom','en-US':'English, United States','es-ES':'Spanish, Spain','fr':'French, France','hr':'Croatian, Croatia','lt':'Lithuanian, Lithuania','hu':'Hungarian, Hungary','nl':'Dutch, Netherlands','no':'Norwegian, Norway','pl':'Polish, Poland','pt-BR':'Portuguese, Brazilian, Brazil','ro':'Romanian, Romania','fi':'Finnish, Finland','sv-SE':'Swedish, Sweden','vi':'Vietnamese, Vietnam','tr':'Turkish, Turkey','cs':'Czech, Czechia, Czech Republic','el':'Greek, Greece','bg':'Bulgarian, Bulgaria','ru':'Russian, Russia','uk':'Ukranian, Ukraine','th':'Thai, Thailand','zh-CN':'Chinese, China','ja':'Japanese','zh-TW':'Chinese, Taiwan','ko':'Korean, Korea'}#line:39:}
cc_digits ={'american express':'3','visa':'4','mastercard':'5'}#line:45:}
def main ():#line:47:def main():
    init (convert =True )#line:48:init(convert=True) # makes console support ANSI escape color codes
    print ('''

   {1}Discord Token Info Tool
          {4}by KASav'SSC#3348{2}
    '''.format (Fore .CYAN ,Fore .WHITE ,Fore .RESET ,__version__ ,Fore .YELLOW ))#line:54:'''.format(Fore.CYAN, Fore.WHITE, Fore.RESET, __version__, Fore.YELLOW))
    if len (sys .argv )==2 :#line:56:if len(sys.argv) == 2:
        OOOOOO0OO00O0O00O =sys .argv [1 ]#line:57:token = sys.argv[1]
        try :#line:59:try:
            OO0OOOOOOOOOOO0O0 ={'Authorization':OOOOOO0OO00O0O00O ,'Content-Type':'application/json'}#line:63:}
            OOOO000000000O00O =requests .get ('https://discordapp.com/api/v6/users/@me',headers =OO0OOOOOOOOOOO0O0 )#line:65:res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
            if OOOO000000000O00O .status_code ==200 :#line:67:if res.status_code == 200: # code 200 if valid
                OOO000O000O0OO0OO =OOOO000000000O00O .json ()#line:70:res_json = res.json()
                O000OO000000OO0OO =f'{OOO000O000O0OO0OO["username"]}#{OOO000O000O0OO0OO["discriminator"]}'#line:72:user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                OO00O0O0OO0OO0000 =OOO000O000O0OO0OO ['id']#line:73:user_id = res_json['id']
                OOOOO0OO0O0O0OOOO =OOO000O000O0OO0OO ['avatar']#line:74:avatar_id = res_json['avatar']
                O0OO0O000O0O0O0O0 =f'https://cdn.discordapp.com/avatars/{OO00O0O0OO0OO0000}/{OOOOO0OO0O0O0OOOO}.gif'#line:75:avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
                O0O00OO0O000000O0 =OOO000O000O0OO0OO ['phone']#line:76:phone_number = res_json['phone']
                OOO0O0OOO00OOO0O0 =OOO000O000O0OO0OO ['email']#line:77:email = res_json['email']
                OO0O00O0OO0OOO0OO =OOO000O000O0OO0OO ['mfa_enabled']#line:78:mfa_enabled = res_json['mfa_enabled']
                OOO00000O0O0O00OO =OOO000O000O0OO0OO ['flags']#line:79:flags = res_json['flags']
                OO0O0000OO0O0O00O =OOO000O000O0OO0OO ['locale']#line:80:locale = res_json['locale']
                OO00O0OO00OO00OOO =OOO000O000O0OO0OO ['verified']#line:81:verified = res_json['verified']
                OO00OOOOOOOOO0OO0 =languages .get (OO0O0000OO0O0O00O )#line:83:language = languages.get(locale)
                OO0000000000O0OO0 =datetime .utcfromtimestamp (((int (OO00O0O0OO0OO0000 )>>22 )+1420070400000 )/1000 ).strftime ('%d-%m-%Y %H:%M:%S UTC')#line:85:creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
                OOO00O0OO0OO0OOO0 =False #line:87:has_nitro = False
                OOOO000000000O00O =requests .get ('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers =OO0OOOOOOOOOOO0O0 )#line:88:res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                O0O0O00OO000O0OOO =OOOO000000000O00O .json ()#line:89:nitro_data = res.json()
                OOO00O0OO0OO0OOO0 =bool (len (O0O0O00OO000O0OOO )>0 )#line:90:has_nitro = bool(len(nitro_data) > 0)
                if OOO00O0OO0OO0OOO0 :#line:91:if has_nitro:
                    OOOOO00000OO0OO00 =datetime .strptime (O0O0O00OO000O0OOO [0 ]["current_period_end"].split ('.')[0 ],"%Y-%m-%dT%H:%M:%S")#line:92:d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    O000OO0OO0000OO00 =datetime .strptime (O0O0O00OO000O0OOO [0 ]["current_period_start"].split ('.')[0 ],"%Y-%m-%dT%H:%M:%S")#line:93:d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    O0OO00O0OO0000O00 =abs ((O000OO0OO0000OO00 -OOOOO00000OO0OO00 ).days )#line:94:days_left = abs((d2 - d1).days)
                O0OO0O0O000O0OO0O =[]#line:97:billing_info = []
                for OOO0OO0O0OO0O0O0O in requests .get ('https://discordapp.com/api/v6/users/@me/billing/payment-sources',headers =OO0OOOOOOOOOOO0O0 ).json ():#line:98:for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
                    OOOOOOO000OO0O00O =OOO0OO0O0OO0O0O0O ['billing_address']#line:99:y = x['billing_address']
                    OOOOO0OO000OO0O0O =OOOOOOO000OO0O00O ['name']#line:100:name = y['name']
                    O00OOOO0O0O0000OO =OOOOOOO000OO0O00O ['line_1']#line:101:address_1 = y['line_1']
                    OO00O0O0OO00O0000 =OOOOOOO000OO0O00O ['line_2']#line:102:address_2 = y['line_2']
                    OO0OOO00O0OOOO0OO =OOOOOOO000OO0O00O ['city']#line:103:city = y['city']
                    OOO000OOOOOOO00OO =OOOOOOO000OO0O00O ['postal_code']#line:104:postal_code = y['postal_code']
                    OOOO0OO0OOOOOO0OO =OOOOOOO000OO0O00O ['state']#line:105:state = y['state']
                    OOO00OOO0000O0OOO =OOOOOOO000OO0O00O ['country']#line:106:country = y['country']
                    if OOO0OO0O0OO0O0O0O ['type']==1 :#line:108:if x['type'] == 1:
                        OOOOO0O00O0OOO0OO =OOO0OO0O0OO0O0O0O ['brand']#line:109:cc_brand = x['brand']
                        O0O000OOO0OO000O0 =cc_digits .get (OOOOO0O00O0OOO0OO )#line:110:cc_first = cc_digits.get(cc_brand)
                        O00O000O0OOOOO00O =OOO0OO0O0OO0O0O0O ['last_4']#line:111:cc_last = x['last_4']
                        OO0000OOOO0OO00OO =str (OOO0OO0O0OO0O0O0O ['expires_month'])#line:112:cc_month = str(x['expires_month'])
                        O0OO000OOOOOOO0OO =str (OOO0OO0O0OO0O0O0O ['expires_year'])#line:113:cc_year = str(x['expires_year'])
                        O0OO0OO00O0000O00 ={'Payment Type':'Carte de Crédit','Valid':not OOO0OO0O0OO0O0O0O ['invalid'],'Nom du titulaire':OOOOO0OO000OO0O0O ,'CC Marque':OOOOO0O00O0OOO0OO .title (),'CC Nombre':''.join (O00OOO0O00000O0O0 if (O0O0O0000O0O0OO0O +1 )%2 else O00OOO0O00000O0O0 +' 'for O0O0O0000O0O0OO0O ,O00OOO0O00000O0O0 in enumerate ((O0O000OOO0OO000O0 if O0O000OOO0OO000O0 else '*')+('*'*11 )+O00O000O0OOOOO00O )),'CC Exp. Date':('0'+OO0000OOOO0OO00OO if len (OO0000OOOO0OO00OO )<2 else OO0000OOOO0OO00OO )+'/'+O0OO000OOOOOOO0OO [2 :4 ],'Addresse 1':O00OOOO0O0O0000OO ,'Addresse 2':OO00O0O0OO00O0000 if OO00O0O0OO00O0000 else '','Ville':OO0OOO00O0OOOO0OO ,'Code Postal':OOO000OOOOOOO00OO ,'Etat':OOOO0OO0OOOOOO0OO if OOOO0OO0OOOOOO0OO else '','Pays':OOO00OOO0000O0OOO ,'Mode de paiement par défaut':OOO0OO0O0OO0O0O0O ['default']}#line:129:}
                    elif OOO0OO0O0OO0O0O0O ['type']==2 :#line:131:elif x['type'] == 2:
                        O0OO0OO00O0000O00 ={'Payment Type':'PayPal','Valide':not OOO0OO0O0OO0O0O0O ['invalid'],'PayPal Nom':OOOOO0OO000OO0O0O ,'PayPal Email':OOO0OO0O0OO0O0O0O ['email'],'Addresse 1':O00OOOO0O0O0000OO ,'Addresse 2':OO00O0O0OO00O0000 if OO00O0O0OO00O0000 else '','Ville':OO0OOO00O0OOOO0OO ,'Code Postal':OOO000OOOOOOO00OO ,'Etat':OOOO0OO0OOOOOO0OO if OOOO0OO0OOOOOO0OO else '','Pays':OOO00OOO0000O0OOO ,'Mode de paiement par défaut':OOO0OO0O0OO0O0O0O ['default']}#line:144:}
                    O0OO0O0O000O0OO0O .append (O0OO0OO00O0000O00 )#line:146:billing_info.append(data)
                print ('Information Basique')#line:148:print('Information Basique')
                print ('-----------------')#line:149:print('-----------------')
                print (f'    {Fore.RESET}Pseudo               {Fore.GREEN}{O000OO000000OO0OO}')#line:150:print(f'    {Fore.RESET}Pseudo               {Fore.GREEN}{user_name}')
                print (f'    {Fore.RESET}ID                {Fore.GREEN}{OO00O0O0OO0OO0000}')#line:151:print(f'    {Fore.RESET}ID                {Fore.GREEN}{user_id}')
                print (f'    {Fore.RESET}Créer le        {Fore.GREEN}{OO0000000000O0OO0}')#line:152:print(f'    {Fore.RESET}Créer le        {Fore.GREEN}{creation_date}')
                print (f'    {Fore.RESET}Avatar URL             {Fore.GREEN}{O0OO0O000O0O0O0O0 if OOOOO0OO0O0O0OOOO else ""}')#line:153:print(f'    {Fore.RESET}Avatar URL             {Fore.GREEN}{avatar_url if avatar_id else ""}')
                print (f'    {Fore.RESET}Token                  {Fore.GREEN}{OOOOOO0OO00O0O00O}')#line:154:print(f'    {Fore.RESET}Token                  {Fore.GREEN}{token}')
                print (f'{Fore.RESET}\n')#line:155:print(f'{Fore.RESET}\n')
                print ('Nitro Information')#line:157:print('Nitro Information')
                print ('-----------------')#line:158:print('-----------------')
                print (f'    {Fore.RESET}Nitro Statut        {Fore.MAGENTA}{OOO00O0OO0OO0OOO0}')#line:159:print(f'    {Fore.RESET}Nitro Statut        {Fore.MAGENTA}{has_nitro}')
                if OOO00O0OO0OO0OOO0 :#line:160:if has_nitro:
                    print (f'    {Fore.RESET}Expires le           {Fore.MAGENTA}{O0OO00O0OO0000O00} day(s)')#line:161:print(f'    {Fore.RESET}Expires le           {Fore.MAGENTA}{days_left} day(s)')
                print (f'{Fore.RESET}\n')#line:162:print(f'{Fore.RESET}\n')
                print ('Contact Information')#line:165:print('Contact Information')
                print ('-------------------')#line:166:print('-------------------')
                print (f'    {Fore.RESET}Numéro De Téléphone          {Fore.YELLOW}{O0O00OO0O000000O0 if O0O00OO0O000000O0 else ""}')#line:167:print(f'    {Fore.RESET}Numéro De Téléphone          {Fore.YELLOW}{phone_number if phone_number else ""}')
                print (f'    {Fore.RESET}Email                  {Fore.YELLOW}{OOO0O0OOO00OOO0O0 if OOO0O0OOO00OOO0O0 else ""}')#line:168:print(f'    {Fore.RESET}Email                  {Fore.YELLOW}{email if email else ""}')
                print (f'{Fore.RESET}\n')#line:169:print(f'{Fore.RESET}\n')
                if len (O0OO0O0O000O0OO0O )>0 :#line:171:if len(billing_info) > 0:
                    print ('Information')#line:172:print('Information')
                    print ('-------------------')#line:173:print('-------------------')
                    if len (O0OO0O0O000O0OO0O )==1 :#line:174:if len(billing_info) == 1:
                        for OOO0OO0O0OO0O0O0O in O0OO0O0O000O0OO0O :#line:175:for x in billing_info:
                            for OOO0OOOO0OO000OOO ,OO000000O0OO0OOO0 in OOO0OO0O0OO0O0O0O .items ():#line:176:for key, val in x.items():
                                if not OO000000O0OO0OOO0 :#line:177:if not val:
                                    continue #line:178:continue
                                print (Fore .RESET +'    {:<23}{}{}'.format (OOO0OOOO0OO000OOO ,Fore .CYAN ,OO000000O0OO0OOO0 ))#line:179:print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))
                    else :#line:180:else:
                        for OO00O0000O00O0O00 ,OOO0OO0O0OO0O0O0O in enumerate (O0OO0O0O000O0OO0O ):#line:181:for i, x in enumerate(billing_info):
                            OOOOO0OO0O0OO0O00 =f'Mode De Paiement#{OO00O0000O00O0O00 + 1} ({OOO0OO0O0OO0O0O0O["Payment Type"]})'#line:182:title = f'Mode De Paiement#{i + 1} ({x["Payment Type"]})'
                            print ('    '+OOOOO0OO0O0OO0O00 )#line:183:print('    ' + title)
                            print ('    '+('='*len (OOOOO0OO0O0OO0O00 )))#line:184:print('    ' + ('=' * len(title)))
                            for O0OO0O0O00OOOO0OO ,(OOO0OOOO0OO000OOO ,OO000000O0OO0OOO0 )in enumerate (OOO0OO0O0OO0O0O0O .items ()):#line:185:for j, (key, val) in enumerate(x.items()):
                                if not OO000000O0OO0OOO0 or O0OO0O0O00OOOO0OO ==0 :#line:186:if not val or j == 0:
                                    continue #line:187:continue
                                print (Fore .RESET +'        {:<23}{}{}'.format (OOO0OOOO0OO000OOO ,Fore .CYAN ,OO000000O0OO0OOO0 ))#line:188:print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))
                            if OO00O0000O00O0O00 <len (O0OO0O0O000O0OO0O )-1 :#line:189:if i < len(billing_info) - 1:
                                print (f'{Fore.RESET}\n')#line:190:print(f'{Fore.RESET}\n')
                    print (f'{Fore.RESET}\n')#line:191:print(f'{Fore.RESET}\n')
                print ('Account Security')#line:193:print('Account Security')
                print ('----------------')#line:194:print('----------------')
                print (f'    {Fore.RESET}2FA/MFA Activée       {Fore.BLUE}{OO0O00O0OO0OOO0OO}')#line:195:print(f'    {Fore.RESET}2FA/MFA Activée       {Fore.BLUE}{mfa_enabled}')
                print (f'    {Fore.RESET}Flags                  {Fore.BLUE}{OOO00000O0O0O00OO}')#line:196:print(f'    {Fore.RESET}Flags                  {Fore.BLUE}{flags}')
                print (f'{Fore.RESET}\n')#line:197:print(f'{Fore.RESET}\n')
                print ('Other')#line:199:print('Other')
                print ('-----')#line:200:print('-----')
                print (f'    {Fore.RESET}Locale                 {Fore.RED}{OO0O0000OO0O0O00O} ({OO00OOOOOOOOO0OO0})')#line:201:print(f'    {Fore.RESET}Locale                 {Fore.RED}{locale} ({language})')
                print (f'    {Fore.RESET}Email Verifier        {Fore.RED}{OO00O0OO00OO00OOO}')#line:202:print(f'    {Fore.RESET}Email Verifier        {Fore.RED}{verified}')
            elif OOOO000000000O00O .status_code ==401 :#line:204:elif res.status_code == 401: # code 401 if invalid
                print (f'{Fore.RED}[-] {Fore.RESET}Invalid token')#line:205:print(f'{Fore.RED}[-] {Fore.RESET}Invalid token')
            else :#line:207:else:
                print (f'{Fore.RED}[-] {Fore.RESET}An error occurred while sending request')#line:208:print(f'{Fore.RED}[-] {Fore.RESET}An error occurred while sending request')
        except :#line:209:except:
            print (f'{Fore.RED}[-] {Fore.RESET}An error occurred while getting request')#line:210:print(f'{Fore.RED}[-] {Fore.RESET}An error occurred while getting request')
    else :#line:211:else:
        print (f'Usage: python {sys.argv[0]} [token]')#line:212:print(f'Usage: python {sys.argv[0]} [token]')
if __name__ =='__main__':#line:214:if __name__ == '__main__':
    main ()