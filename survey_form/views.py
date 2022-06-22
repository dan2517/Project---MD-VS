from django.shortcuts import render
import mysql.connector as sql

s1=''

# Create your views here.
def submitaction(request):
    global s1
    if request.method=="POST":
        
        m=sql.connect(host="localhost",user="root",passwd="Div@g@r25",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="s1":
                s1=value
            # if key=="last_name":
            #     ln=value
            
            # if key=="email":
            #     em=value
            # if key=="password":
            #     pwd=value
        
        db="insert into survey(survey-1)) Values('{}')".format(s1)
        cursor.execute(db)
        m.commit()
        

    return render(request,'survey_form.html')