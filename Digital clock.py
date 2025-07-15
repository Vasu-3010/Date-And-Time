from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()
    h=time.strftime('%I')
    m=time.strftime('%M')
    s=time.strftime('%S')
    a=time.strftime("%p")
    
    da=time.strftime('%d')
    mo=time.strftime('%m')
    y=time.strftime('%y')
    d=time.strftime("%a")
    
    lab_hr.config(text=h)
    lab_min.config(text=m)
    lab_sec.config(text=s)
    lab_am.config(text=a)
    
    lab_dt.config(text=da)
    lab_mo.config(text=mo)
    lab_yr.config(text=y)
    lab_day.config(text=d)
    lab_hr.after(200,date_time)



clock=Tk()
clock.title("Digital Clock")
clock.geometry('1000x500')
clock.config(bg='light blue')

lab_hr=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='red',fg='white')
lab_hr.place(x=112,y=40,height=110,width=100)
lab_hr_txt=Label(clock,text="hour",font=('Times New Roman',20,"bold"),bg='red',fg='white')
lab_hr_txt.place(x=112,y=165,height=30,width=100)

lab_min=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='red',fg='white')
lab_min.place(x=334,y=40,height=110,width=100)
lab_min_txt=Label(clock,text="minute",font=('Times New Roman',20,"bold"),bg='red',fg='white')
lab_min_txt.place(x=334,y=165,height=30,width=100)

lab_sec=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='red',fg='white')
lab_sec.place(x=556,y=40,height=110,width=100)
lab_sec_txt=Label(clock,text="Secound",font=('Times New Roman',20,"bold"),bg='red',fg='white')
lab_sec_txt.place(x=556,y=165,height=30,width=100)

lab_am=Label(clock,text="AM",font=('Times New Roman',45,"bold"),bg='red',fg='white')
lab_am.place(x=778,y=40,height=110,width=100)
lab_am_txt=Label(clock,text="AM / PM",font=('Times New Roman',15,"bold"),bg='red',fg='white')
lab_am_txt.place(x=778,y=165,height=30,width=100)


lab_dt=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='red',fg='white')
lab_dt.place(x=112,y=270,height=110,width=100)
lab_dt_txt=Label(clock,text="Date",font=('Times New Roman',20,"bold"),bg='red',fg='white')
lab_dt_txt.place(x=112,y=405,height=30,width=100)

lab_mo=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='red',fg='white')
lab_mo.place(x=334,y=270,height=110,width=100)
lab_mo_txt=Label(clock,text="Month",font=('Times New Roman',20,"bold"),bg='red',fg='white')
lab_mo_txt.place(x=334,y=405,height=30,width=100)

lab_yr=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='red',fg='white')
lab_yr.place(x=556,y=270,height=110,width=100)
lab_yr_txt=Label(clock,text="Year",font=('Times New Roman',20,"bold"),bg='red',fg='white')
lab_yr_txt.place(x=556,y=405,height=30,width=100)

lab_day=Label(clock,text="Day",font=('Times New Roman',40,"bold"),bg='red',fg='white')
lab_day.place(x=778,y=270,height=110,width=100)
lab_day_txt=Label(clock,text="Day",font=('Times New Roman',15,"bold"),bg='red',fg='white')
lab_day_txt.place(x=778,y=405,height=30,width=100)


date_time()
clock.mainloop()