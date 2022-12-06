from django.shortcuts import render,redirect
import mysql.connector as sql
fn=''
ln=''
mb=''
em=''
pwd=''
cpwd=''
id=0
a='id'


# Create your views here.
def signup(request):
    global fn,ln,mb,em,pwd,cpwd,id,a
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=='fname':
                fn=value
            if key=='lname':
                ln=value
            if key=='mobile':
                mb=value
            if key=='email':
                em=value
            if key=='password':
                pwd=value
            if key=='cpassword':
                cpwd=value
        if pwd!=cpwd:
            return redirect('/signup')
        elif fn=='' or ln=='' or mb=='' or em=='' or pwd=='' or cpwd=='':
            return redirect('/signup')
        else:
            m=sql.connect(host="localhost",user="root",password="1234",database="authentication")
            cur=m.cursor()
            cur.execute('select count(id) from signupapp_authentication')
            row = cur.fetchone()
            row=row[0]
            id=int(row)+1
            id=str(id)
            c="insert into signupapp_authentication values('{}','{}','{}','{}','{}','{}')".format(id,fn,ln,mb,em,pwd)
            cur.execute(c)
            m.commit()
            return redirect('/login')
        
    return render(request,'signup.html')

    