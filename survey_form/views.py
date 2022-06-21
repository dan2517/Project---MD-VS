
from django.shortcuts import  render
import mysql.connector as sql
pf=''
cs=''
lang=''
dev=''
le=''
sug=''


# Create your views here.
def submitaction(request):

    global pf,cs,lang,dev,le,sug
    if request.method=="POST":
        
        m=sql.connect(host="localhost",user="root",passwd="Div@g@r25",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Profession":
                s1=value
            if key=="Cloud_Service":
                s2=value
            if key=="Language":
                s3=value
            if key=="Development":
                s4=value
            if key=="Latest_Experience":
                s5=value
            if key=="Suggestions":
                s6=value

    

        c="insert into feedback Values('{}','{}','{}','{}','{}','{}')".format(pf,cs,lang,dev,le,sug)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'Error.html')
        else:
            return render(request,'Thankyou.html')

    