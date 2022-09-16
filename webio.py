from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import *
import requests, json, time 
from time import sleep






"""


# في input يمكن اظهار المدخل على شكل *** , تفيد بالباسويرد
من خلال :  
type= password





"""



"""



def app ():
	put_text (" Ali AlYassiry .")
	put_text (" Instagram information .")
	put_button ("info User ", onclick=lambda: toast (" ✅ Successful "))

"""


"""
def btn_click (btn_val) :
	put_text (f" You Click {btn_val} button ")

put_buttons ([" thinker ", " User ", " Info "], onclick=btn_click)

"""



"""

def Select () :
	
	# تظهر input ونختار من قائمه منسدله
	
	status = select (" Choose Combo >> ", ["user:pass", "user", "gmail"])

"""


"""

def Radio () :
	
	# تظهر قائمه ونحدد خيار واحد 
	
	answer = radio ("Choose one : ", options= ["A","B","C","D"])
	
	put_text (answer)

"""


"""
def File () :
	# تنزيل ملف بس ما يصير ادخل متغير يحتوي على الشيء المراد حفظه
	
	put_file ("aaay.txt", content= "Ali Alhdam", label= "Download File ")
"""
	





def info_user () :
	
	#معلومات انستا
	
	put_html ('<h1> Information Instagram </h1>')
	html = put_html ('<p><font face="courier" size="-1"> 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: Instagram: @__6e3  <br>&nbsp; &nbsp; &nbsp; &nbsp;  Telegram: @ENG44</font></p>')
	out = output (html)
	put_row (out)
	user = input (" User Instagram : ",
	type= "text",
	placeholder= "Enter username insta",
	help_text= " ادخل يوزر الانستكرام " ,
	required=True)
	# required=True       المستخدم ما يكدر يضغط على سبميت حته يدخل كلمات
	
	
	user = user.strip()
	if user == "" :
		put_text (" Not Find User , \n Check your user , Try again .")
	else:
		out.reset ("")
		#popup ("✅ Successful ")   # تظهر شعار 
		sessionid = "6768402503%3ACY6RxoQWUWCzQj%3A22%3AAYd43NoH9YwkK7x7FOfKOddc6msYYdYD0OUruJX2sw"
		headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		'cookie': "sessionid={};".format(sessionid),
		'origin': 'https://www.instagram.com', 
		'referer': 'https://www.instagram.com/',
		'user-agent': 'Instagram 27.0.0.7.97 Android (23/6.0.1; 640dpi; 1440x2392; LGE/lge; RS988; h1; h1; en_US)',
		'x-asbd-id': '437806',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9X4Q',}
		url = f"https://i.instagram.com/api/v1/users/{user}/usernameinfo/"		
		req_id = requests.get(url,headers=headers).json()
		name = str(req_id['user']['full_name'])
		username =  str(req_id['user']['username'])
		id = str(req_id['user']['pk'])
		following = str(req_id['user']["following_count"])
		followers = str(req_id['user']["follower_count"])
		#email = str(req_id['graphql']['user']['business_email'])
		#phone = str(req_id['graphql']['user']['phone_number'])
		post = str(req_id['user']["media_count"])
		profile_pic_url= str(req_id['user']['profile_pic_url'])
		bio = str(req_id['user']['biography'])
		data = str(requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["data"])
		t = time.localtime()
		current_time = time.strftime('%H:%M:%S', t)
		
		re2 = requests.get(profile_pic_url).content
		with open("profile_img.jpg", "wb") as a:
			a.write(re2) 
		#  images/profile_img.jpg
		#photo1 = open("profile_img.jpg", 'rb')
		put_image(open('profile_img.jpg', 'rb').read()).style('width:200px; height:230px')
		
		
		Info =(f'''
⌯ 𝗜𝗻𝗳𝗼 𝗶𝗻𝘀𝘁𝗮 🌚:<br>
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯<br>
⌯ 𝐍𝐀𝐌𝐄 : {name}<br>
⌯ 𝐔𝐒𝐄𝐑 :  {username}<br>
⌯ 𝖎𝕯 : {id}<br>
⌯ 𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 :  {followers}<br>
⌯ 𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 :  {following}<br>
⌯ 𝐏𝐎𝐒𝐓 : {post}<br>
⌯ Ðﾑｲﾑ : {data}<br>
⌯ 𝐁𝐈𝐎 : {bio}<br>
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [<a href ="https://instagram.com/{username}"> https://instagram.com/{username} </a>]⌯
<br>
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ <br>
⌯ Tele : @ENG44 ''')
		
		print (Info)
		put_html (Info)
		put_text("\n\n\n\n")
		
		def j(x):
		
			word = ""
			result = output (word)
			put_row ([result])
			for k in x:
				word += str(k)
				result.reset (word)
				sleep (0.2)
		
		x = "[~] 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 (المطور) :"
		j(x)
		put_html (f'<••><b> <font face ="courier" size="+0.5"> Instagram : <a href ="https://instagram.com/__6e3">@__6e3</a></b>')
		put_html ('<••><b> <font face ="courier" size="+0.5"> Telegram : <a href ="tg://openmessage?user_id=1009015069">@ENG44 </a></b> ')
	




if __name__=="__main__":
	start_server (info_user,port=8083, debug=False)
	