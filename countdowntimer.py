from tkinter import *
from threading import Thread
from tkinter.messagebox import showinfo
import time,tkinter.messagebox
from tkinter import messagebox



#class to perform countdown timer
class counter(Thread):
    over=False
    pause=False
    def __init__(self,func):
        Thread.__init__(self)
        self.func=func

    def run(self):
        global t,root
        time.sleep(1)
        finish=False
        while not self.over and not finish:
            if not self.pause:
                finish=self.func()
            time.sleep(1)
        if finish:
            root.event_generate('<<pop>>',when='tail')
            messagebox.showinfo("Time Countdown", "Time's up ")
        t=None
    def kill(self):
        self.over=True
    def paus(self):
        self.pause=True
    def countinue(self):
        self.pause=False

t=None
sec=None
root=Tk()
#root.bind('<<pop>>',lambda event=None:showinfo('Time is up'))
e1=StringVar()
e2=StringVar()

def show():
                                        #displays the time
    global e1,e2,sec
    e1.set('%.2d'%(sec/60))
    e2.set('%.2d'%(sec%60))

def decrese():                          #decrease the entered time by 1
    global sec
    if sec:
        sec-=1;
        show()
        return False
    else:
        return True

def incriment():                        #increase the time by 1
    global sec
    sec+=1;
    show()
    return False

def start_():                           #starts/resumes the timer
    global sec,t
    if t:t.countinue();return
    sec=0;
    show()
    t=counter(incriment)
    t.start()

def countdwn():                         #starts the countdown
    global sec,t
    if t:t.countinue();return
    sec=0
    try:
        sec=int(e1.get())*60
    except Exception:
        pass
    try:
        sec+=int(e2.get())
    except Exception:
        pass
    if not sec: return
    show()
    t=counter(decrese)
    t.start()
    pass

def pause_():                       #pause the timer/countdown
    global t
    t.paus()

def stop_():                        #stops the timer/countdown and sets to 0
    global t,sec
    sec=0;show()
    if t:
        t.kill()
    t=None

en1=Entry(root,textvariable=e1,width=10,justify=RIGHT)
en2=Entry(root,textvariable=e2,width=10)
lb=Label(root,text=":")

#buttons 

startbutton=Button(root,width=10,text='start',command=start_)
countdownbutton=Button(root,width=10,text='countdown',command=countdwn)
pausebutton=Button(root,width=10,text='pause',command=pause_)
stopbutton=Button(root,width=10,text='stop',command=stop_)

#allingnment of widget

en1.grid(row=0,column=0)
lb.grid(row=0,column=1)
en2.grid(row=0,column=2)
startbutton.grid(row=1,column=0)
countdownbutton.grid(row=1,column=2)
pausebutton.grid(row=2,column=0)
stopbutton.grid(row=2,column=2)

#geometry
root.geometry('200x100')
root.geometry('+550+400')
root.title("Time Counter")
root.mainloop()



    
    
