from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''

em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Div@g@r25",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users(First_Name,Last_Name,Email,Password) Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()
    

    return render(request,'signup_page.html')
