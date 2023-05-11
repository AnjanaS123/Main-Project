from tkinter import *
from tkinter import messagebox
from testBox import *

#---------------Kali SJT


root=Tk()
root.geometry("600x700")
root.configure(background='white')
root.title("Anjana's App")
root.wm_attributes('-transparentcolor','#ab23ff')

Appmodel=PhotoImage(file='modelX1.png')
TitleModel=PhotoImage(file='MG_TITTLE_tst.png')
underlineModel=PhotoImage(file='red-underline-07 copy.png')
playButton=PhotoImage(file='play.png')
pauseButton=PhotoImage(file='pause.PNG')
stopButton=PhotoImage(file='stop copy.png')

key1=StringVar()
key2=StringVar()
key3=StringVar()
key6=StringVar()
key7=StringVar()
key8=StringVar()
key9=StringVar()
key11=StringVar()
key10=StringVar()

option1=StringVar(root)
option1.set(SCALES[0])




def trigger():
    #scales
    print(option1.get())

    #key6=SCALES[txt4.curselection()]
    #--------------------------
    print(key1.get())
    print(key2.get())
    print(key3.get())
    print(key6.get())
    print(key7.get())
    print(key8.get())
    print(key9.get())
    print(key10.get())
    print(key11.get())



    RXtest(num_bars=int(key1.get()),num_notes=int(key2.get()),num_steps=int(key3.get()),pauses=True,key='C',scale=key6.get(),root=int(key7.get()),population_size=int(key8.get()),num_mutations=int(key9.get()),mutation_probability=float(key10.get()),bpm=int(key11.get()))



Label(root,image=Appmodel,bg="white").place(x=18,y=5)
Label(root,image=TitleModel,bg="white").place(x=230,y=0)
Label(root,image=underlineModel,bg='white').place(x=0,y=140)


Label(root,text='Number of Bars:',bg='white',font=('calibre',13,'bold')).place(x=100,y=195)
txt1=Entry(root,textvariable=key1,font=('calibre',13,'normal'))
txt1.insert(0,8)
txt1.place(x=275,y=195)

Label(root,text='Notes per Bars:',bg='white',font=('calibre',13,'bold')).place(x=100,y=230)
txt2=Entry(root,textvariable=key2,font=('calibre',13,'normal'))
txt2.insert(0,"4")
txt2.place(x=275,y=230)

Label(root,text='Number of Steps:',bg='white',font=('calibre',13,'bold')).place(x=100,y=270)
txt3=Entry(root,textvariable=key3,font=('calibre',13,'normal'))
txt3.insert(0,"1")
txt3.place(x=275,y=270)

Label(root,text='Scale:',bg='white',font=('calibre',13,'bold')).place(x=100,y=310)
txt4=OptionMenu(root,option1,*SCALES)
txt4.configure(font=('calibre',13,'normal'))
txt4.place(x=275,y=310)

Label(root,text='Scale Root:',bg='white',font=('calibre',13,'bold')).place(x=100,y=350)
txt5=Entry(root,textvariable=key7,font=('calibre',13,'normal'))
txt5.insert(0,"4")
txt5.place(x=275,y=350)

Label(root,text='Population Size:',bg='white',font=('calibre',13,'bold')).place(x=100,y=390)
txt6=Entry(root,textvariable=key8,font=('calibre',13,'normal'))
txt6.insert(0,"10")
txt6.place(x=275,y=390)

Label(root,text='Number of Mutations:',bg='white',font=('calibre',13,'bold')).place(x=100,y=430)
txt7=Entry(root,textvariable=key9,font=('calibre',13,'normal'))
txt7.insert(0,"2")
txt7.place(x=275,y=430)

Label(root,text='Mutation Probability:',bg='white',font=('calibre',13,'bold')).place(x=100,y=470)
txt8=Entry(root,textvariable=key10,font=('calibre',13,'normal'))
txt8.insert(0,"0.5")
txt8.place(x=275,y=470)

Label(root,text='bpm           :',bg='white',font=('calibre',13,'bold')).place(x=100,y=510)
txt9=Entry(root,textvariable=key11,font=('calibre',13,'normal'))
txt9.insert(0,"128")
txt9.place(x=275,y=510)

#play=Label(image=playButton)
clickMe=Button(root,text=" ",bg='white',image=playButton,command=trigger,borderwidth=0)
#clickMe.configure(font=('calibre',13,'bold'))
clickMe.place(x=215,y=570)

clickMe=Button(root,text=" ",bg='white',image=pauseButton,command=QuitMe(),borderwidth=0)
clickMe.place(x=300,y=570)


def scoot():
    root.destroy()

clickMe=Button(root,text=" ",bg='white',image=stopButton,command=scoot,borderwidth=0)
clickMe.place(x=440,y=580)


root.mainloop()

#---------------Kali SJT