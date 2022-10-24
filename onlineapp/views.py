from select import select
from django.shortcuts import render
from . models import *
import MySQLdb

db=MySQLdb.connect("localhost","root","","onlinedb",3306)
c=db.cursor()

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def adminhome(request):
    return render(request,'adminhome.html')
def addcategory(request):
    msg=""
    if request.method=='POST':
        capname=request.POST.get("catname")
        s="select count(*) from onlineapp_addcategory where name='"+str(capname)+"'"
        c.execute(s)
        d=c.fetchone()
        print(d)
        if d[0]==0:
            try :
                s="insert into onlineapp_addcategory(name) values ('"+str(capname)+"')"
                c.execute(s)
                db.commit()
            except:
                msg="error in insertion"
            else:                
                msg="insertion completed successfully"
        else:
            msg="category already exist"
    s="select * from onlineapp_addcategory"  
    c.execute(s) 
    e= c.fetchall()        
    return render(request,"addcategory.html",{"msg":msg},{"e":e})
def addsubcategory(request):
    return render(request,'addsubcategory.html')
def addbrand(request):
    msg=""
    if request.method=='POST':
        brname=request.POST.get("catname")
        s="select count(*) from onlineapp_Addbrand where name='"+str(brname)+"'"
        c.execute(s)
        d=c.fetchone()
        print(d[0])
        if d[0]==0:
            try :
                s="insert into onlineapp_Addbrand(name) values ('"+str(brname)+"')"
                c.execute(s)
                db.commit()
            except:
                msg="error in insertion"
            else:
                msg="insertion completed successfully"
        else:
            msg="brand already exist"
    s="select * from onlineapp_Addbrand"  
    c.execute(s) 
    br= c.fetchall()   
    
    return render(request,'addbrand.html',{"msg":msg},{"br":br})
def addproduct(request):
    return render(request,'addproduct.html')
def registration(request):
    return render(request,'registration.html')
def login(request):
    return render(request,'login.html')
def userhome(request):
      return render(request,'userhome.html')
def buyproduct(request):
      return render(request,'buyproduct.html')

    


