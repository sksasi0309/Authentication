import smtplib
import math, random
from django.shortcuts import render,redirect
import mysql.connector as sql

em=''
sotp=''
rotp=''
npwd=''
ncpwd=''
# Create your views here.

def sendotp(request):
    global em,sotp
    if request.method=='POST':
        d=request.POST
        for key,value in d.items():
            if key=='email':
                em=value
                print(em)
        
        sotp=otpsend()
        print('done')
        return redirect('/OTP')
    return render(request,"reset.html")


def OTP(request):
    global rotp
    if request.method=='POST':
        d=request.POST
        for key,value in d.items():
            if key =='otp':
                rotp=value
        if sotp == rotp:
            return redirect('/resetpassword')
        else:
            return redirect('/OTP')
    return render(request,"OTP.html")


def pwd(request):
    global npwd,ncpwd
    if request.method== 'POST':
        d=request.POST
        for key,value in d.items():
            if key=='password':
                npwd=value
            if key =='cpassword':
                ncpwd =value
        if npwd =='' or ncpwd =='':
            return redirect('/resetpassword')
        elif npwd !=ncpwd:
            return redirect('/resetpassword')
        else:
            m=sql.connect(host="localhost",user="root",password="1234",database="authentication")
            cursor=m.cursor()
            c="update signupapp_authentication  set password='{}' where email='{}'".format(npwd,em)
            cursor.execute(c)
            m.commit()
            return redirect('/login')
    return render(request,'resetpassword.html')


def resend_otp(request):
    global sotp
    sotp=otpsend()
    return redirect('/OTP')
    
    
def otpsend():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("ENTER YOUR MAIL ID", "ENTER MAIL PASSWORD")
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]
    s.sendmail("ENTER FROM MAIL ID", em, OTP)
    print('sent')
    return OTP

    

