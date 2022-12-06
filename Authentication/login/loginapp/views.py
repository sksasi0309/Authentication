from django.shortcuts import render,redirect
import mysql.connector as sql
em=''
pwd=''

def login(request):
    global em,pwd
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=='email':
                em=value
            if key=='password':
                pwd=value
        if em == '' or pwd == '':
            print('no')
            return redirect('/login')

        else:
            con = sql.connect(host='localhost', user='root', password='1234', database='authentication')
            cur = con.cursor()
            
            cur.execute('select * from signupapp_authentication  where email=%s and password=%s', (em,pwd))
            row = cur.fetchone()
            
            if row == None:
                return redirect('/login')


            else:
                return render(request,'welcome.html')
            con.close()
                
           
    return render(request,'login.html')




        



    