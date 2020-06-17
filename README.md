# spammer_sms
/* هشدار!
#این اسکریپت فقط با اهداف آموزش پایتون ۳ ساخته شده است و 
هر گونه سو استفاده  یا استفاده نادرست از آن بر عهده ی ما نمی باشد

Spammer  SMS for Termux , linux :

1)linux :

آپدیت و آپگرید مغازن لینوکس :


apt-get update && apt-get upgrade -y
یا 
sudo apt-get update && sudo apt-get upgrade -y

نصب پایتون ۳ و پایپ:

apt-get install python3 python3-pip 
یا
sudo apt-get install python3 python3-pip

نصب گیت هاب :

apt-get install git -y 

یا 
sudo apt-get install git -y

کلون : 
git clone https://github.com/kinguser20204/spammer_sms

وارد پوشه دانلود شده می شویم :
cd spammer_sms && ls 

نصب ماژول های مورد نیاز :


pip3 install requests colorama 

دسترسی گرفتن از فایل اجرایی :
chmod +x spammer_sms.py

اجرا : 
python3 spammer_sms.py

2) termux :

تمام دستورات بصورت یکجا :
pkg update && pkg upgrade && pkg install python git && git clone https://github.com/kinguser20204/spammer_sms  && cd spammer_sms && pip3 install requests colorama && chmod +x spammer_sms.py && python3 spammer_sms.py
