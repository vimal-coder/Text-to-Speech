from tkinter import *
import pyttsx3
from PIL import ImageTk ,Image
#--------------------------------------------------------------
window=Tk()
window.geometry("700x360")
window.title("TEXT TO SPEECH CONVERTER")
window.config(bg="powderblue")
window.iconbitmap("text name.ico")
#---------------------------------------------------------------

#code for button function----------------------------------------

def speech():
    voice=entry.get()
    speech=pyttsx3.init()
    speech.say(voice)
    speech.setProperty("rate",200)
    speech.runAndWait()
def clear():
    entry.delete(0,1)
#------------------------------------------------------------------
    

#code for entry function-------------------------------------------
entry=Entry(window,bg="white",font="georgio 15")
entry.place(x=20,y=15,height=150,width=285)
#---------------------------------------------------------------------
#text=tk.Text(window,font="Robote 15",bg="white",relief=GROOVE,wrap=WORD)
#text.insert(END,"TEXT: ")
#text.place(x=20,y=15,width=285,height=290)


#code for frame function--------------------------------------
frame=Frame(window,bg="moccasin",width=380,height=70)
frame.place(x=315,y=15)
#------------------------------------------------------------


#code for label function---------------------------------------------------
label=Label(frame,text="TEXT TO SPEECH CONVERTER",font="arial 18 bold"
            ,height=1,bg="white",fg="black",padx=0,pady=5)
label.place(x=7,y=12)
#--------------------------------------------------------------------------

#code for button------------------------------------------------------------
button=Button(window,bg="lightskyblue",text="SPEAK"
              ,font="arial 12 bold",width=12,height=2,command=speech)
button.place(x=20,y=230)
#button2
button=Button(window,bg="orange",text="CLEAR"
              ,font="arial 12 bold",width=12,height=2,command=clear)
button.place(x=175,y=230)
#--------------------------------------------------------------------------


#code for image adding------------------------------------------------------

img=ImageTk.PhotoImage(Image.open("text control.ico"))
label=Label(window,image=img,bg="powderblue")
label.place(x=380,y=85)
#------------------------------------------------------------------------------


window.mainloop()