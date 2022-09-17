
import pywebio
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import *
import requests, json, time , random
from time import sleep



def app():
	
	Choose = radio ("أختر شكل الكومبو : ", options= ["User","User : Password","Email", "Email : Password"])
	#put_text (Choose)
	put_html (f"<center><h2>New Combo {Choose}</h2></center>")
	put_html ('<p><font face="courier" size="-1"> 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: Telegram: @ENG44</font></p><br><hr>')
	
	if str(Choose) == "User":
		
		numb =0
		
		data = input_group ("iD & Token",[
			input ("iD Telegram", name="iD", type="text", help_text=" (*) أدخل ايدي حساب التلكرام"),
			input ("Token Bot", name="token", type="text", help_text="(*) ادخل توكن البوت"),
			input ("Name New File 📎", name="name_file", type="text", help_text="(*) ادخل اسم للملف  [مثلاً user.txt]")
			])
		
		iD = data["iD"]
		token = data["token"]
		name_file = data["name_file"]
		
		if ".txt" in name_file :
			pass
		else:
			name_file = str(name_file+".txt")
		
		#put_text (iD) ; put_text(data["token"]); put_text (data["name_file"])
	
		
		
		file = open (name_file,"w")
		word='qwert.yui12467opasdfghjpoiye1298765wqassf.fghjkllmnbbv123567899cxzklzxcvbnm'
		wor ='qwertyuiopasdfghjpoiyewqassfghjkllmnbbvcxzklzxcvbnm'
		dot = "_."
		
		for k in range(999):
			rng = ("".join(random.choice(word)for i in range(int(random.randint(1,8)))))
			rng1 = ("".join(random.choice(wor)for i in range(1)))
			rng2 = ("".join(random.choice(wor)for i in range(1)))
			
			user = str(rng1+rng+rng2)
			numb+=1
			put_text (f"[{numb}] {user}")
			file.write (str(user)+"\n")
			
		file.close()
		sleep (3)
		requests.get ("https://api.telegram.org/bot"+str(data["token"])+"/sendDocument?chat_id="+str(data["iD"])+f"&caption=File Name : `{name_file}`&parse_mode=markdown", files={"document": open(name_file, "rb")})
		#put_text (x.text)
		sleep (5)
		clear()
		
		put_html (f"<center><h2>New Combo {Choose}</h2></center>")
		put_html ('<p><font face="courier" size="-1"> 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: Telegram: @ENG44</font></p><br><hr>')
		
		put_row ([put_markdown (f"[✅] Successful Send File `{name_file}` to Bot Telegram ")], [toast ("✅ تم أرسال الملف الى بوت التلكرام ")])
			
	
	
	
	
	
	elif str(Choose) == "User : Password":
		
		numb =0
		
		data = input_group ("iD & Token",[
			input ("iD Telegram", name="iD", type="text", help_text=" (*) أدخل ايدي حساب التلكرام"),
			input ("Token Bot", name="token", type="text", help_text="(*) ادخل توكن البوت"),
			input ("Name New File 📎", name="name_file", type="text", help_text="(*) ادخل اسم للملف  [مثلاً user.txt]")
			])
		
		iD = data["iD"]
		token = data["token"]
		name_file = data["name_file"]
		
		if ".txt" in name_file :
			pass
		else:
			name_file = str(name_file+".txt")
		
		#put_text (iD) ; put_text(data["token"]); put_text (data["name_file"])
	
		
		
		file = open (name_file,"w")
		word='qwert.yui12467opasdfghjpoiye1298765wqassf.fghjkllmnbbv123567899cxzklzxcvbnm'
		wor ='qwertyuiopasdfghjpoiyewqassfghjkllmnbbvcxzklzxcvbnm'
		dot = "_."
		word_pas = ("1122334455","qwer1234","Aa123Aa123","12345qwert","12345678910")
		
		
		for k in range(999):
			rng = ("".join(random.choice(word)for i in range(int(random.randint(1,3)))))
			rng1 = ("".join(random.choice(wor)for i in range(1)))
			rng2 = ("".join(random.choice(wor)for i in range(1)))
			pas = ("".join(random.choice(word_pas)for i in range(1)))
			user = str(rng1+rng+rng2+":"+pas)
			numb+=1
			put_text (f"[{numb}] {user}")
			file.write (str(user)+"\n")
			
		file.close()
		sleep (3)
		requests.get ("https://api.telegram.org/bot"+str(data["token"])+"/sendDocument?chat_id="+str(data["iD"])+f"&caption=File Name : `{name_file}`&parse_mode=markdown", files={"document": open(name_file, "rb")})
		#put_text (x.text)
		sleep (5)
		clear()
		
		put_html (f"<center><h2>New Combo {Choose}</h2></center>")
		put_html ('<p><font face="courier" size="-1"> 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: Telegram: @ENG44</font></p><br><hr>')
		
		put_row ([put_markdown (f"[✅] Successful Send File `{name_file}` to Bot Telegram ")], [toast ("✅ تم أرسال الملف الى بوت التلكرام ")])
			
	
	
	
	
	
	
	
		
		
	elif str(Choose) == "Email":
		
		numb =0
		
		data = input_group ("iD & Token",[
			input ("iD Telegram", name="iD", type="text", help_text=" (*) أدخل ايدي حساب التلكرام"),
			input ("Token Bot", name="token", type="text", help_text="(*) ادخل توكن البوت"),
			input ("Name New File 📎", name="name_file", type="text", help_text="(*) ادخل اسم للملف  [مثلاً user.txt]"),
			select ("أختر نوع الدومين : ", ["@gmail.com","@yahoo.com","@hotmail.com"], name="domain")
			])
		
		iD = data["iD"]
		token = data["token"]
		name_file = data["name_file"]
		domain = data["domain"]
		
		if ".txt" in name_file :
			pass
		else:
			name_file = str(name_file+".txt")
		
		#put_text (iD) ; put_text(data["token"]); put_text (data["name_file"])
	
		
		file = open (name_file,"w")
		word='qwertui12467opasdfgh.jpoiye1298765wqassfghjkllm.nbbv123567899cxzklxcvbnm'
		wor ='qwertyuiopasdfghjpoiyewqassfghjkllmnbbvcxzklzxcvbnm'
		nber = "12345678900987654321"
		dot = "_."
		
		for k in range(999):
			rng = ("".join(random.choice(word)for i in range(int(random.randint(3,9)))))
			rng1 = ("".join(random.choice(wor)for i in range(1)))
			rng2 = ("".join(random.choice(wor)for i in range(1)))
			rng3 = ("".join(random.choice(nber)for i in range(2)))
			
			user = str(rng1+rng+rng3+domain)
			numb+=1
			put_text (f"[{numb}] {user}")
			file.write (str(user)+"\n")
			
		file.close()
		sleep (3)
		requests.get ("https://api.telegram.org/bot"+str(data["token"])+"/sendDocument?chat_id="+str(data["iD"])+f"&caption=File Name : `{name_file}`&parse_mode=markdown", files={"document": open(name_file, "rb")})
		#put_text (x.text)
		sleep (6)
		clear()
		
		put_html (f"<center><h2>New Combo {Choose}</h2></center>")
		put_html ('<p><font face="courier" size="-1"> 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: Telegram: @ENG44</font></p><br><hr>')
		
		put_row ([put_markdown (f"[✅] Successful Send File `{name_file}` to Bot Telegram ")], [toast ("✅ تم أرسال الملف الى بوت التلكرام ")])
		
	

	
	elif str(Choose) == "Email : Password":
		
		numb =0
		
		data = input_group ("iD & Token",[
			input ("iD Telegram", name="iD", type="text", help_text=" (*) أدخل ايدي حساب التلكرام"),
			input ("Token Bot", name="token", type="text", help_text="(*) ادخل توكن البوت"),
			input ("Name New File 📎", name="name_file", type="text", help_text="(*) ادخل اسم للملف  [مثلاً user.txt]"),
			select ("أختر نوع الدومين : ", ["@gmail.com","@yahoo.com","@hotmail.com"], name="domain")
			])
		
		iD = data["iD"]
		token = data["token"]
		name_file = data["name_file"]
		domain = data["domain"]
		
		if ".txt" in name_file :
			pass
		else:
			name_file = str(name_file+".txt")
		
		#put_text (iD) ; put_text(data["token"]); put_text (data["name_file"])
	
		
		file = open (name_file,"w")
		word='qwertui12467opasdfgh.jpoiye1298765wqassfghjkllm.nbbv123567899cxzklxcvbnm'
		wor ='qwertyuiopasdfghjpoiyewqassfghjkllmnbbvcxzklzxcvbnm'
		nber = "12345678900987654321"
		word_pas = ("1122334455","qwer1234","Aa123Aa123","12345qwert","12345678910")
		
		dot = "_."
		
		for k in range(999):
			rng = ("".join(random.choice(word)for i in range(int(random.randint(3,9)))))
			rng1 = ("".join(random.choice(wor)for i in range(1)))
			rng2 = ("".join(random.choice(wor)for i in range(1)))
			rng3 = ("".join(random.choice(nber)for i in range(2)))
			pas = ("".join(random.choice(word_pas)for i in range(1)))
			
			user = str(rng1+rng+rng3+domain+":"+pas)
			numb+=1
			put_text (f"[{numb}] {user}")
			file.write (str(user)+"\n")
			
		file.close()
		sleep (3)
		requests.get ("https://api.telegram.org/bot"+str(data["token"])+"/sendDocument?chat_id="+str(data["iD"])+f"&caption=File Name : `{name_file}`&parse_mode=markdown", files={"document": open(name_file, "rb")})
		#put_text (x.text)
		sleep (6)
		clear()
		
		put_html (f"<center><h2>New Combo {Choose}</h2></center>")
		put_html ('<p><font face="courier" size="-1"> 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: Telegram: @ENG44</font></p><br><hr>')
		
		put_row ([put_markdown (f"[✅] Successful Send File `{name_file}` to Bot Telegram ")], [toast ("✅ تم أرسال الملف الى بوت التلكرام ")])
		
		






if __name__=="__main__":
	start_server (app, port=7070, debug=False)
	#auto_open_webbrowser=True  امر التشغيل بدون بورت مع هذه الامر ، يفتح المتصفح بسرعه
	#remote_access=True

