from tkinter import*
from tkinter import messagebox #paziņojumi, ieteikumi



mansLogs=Tk()# loga objekts
mansLogs.title("Desas")

######################################################################################################

def btnClick(button):
    global speletajsX,count#kādi mainīgie tiks izmantoti visā programmā(global mainīgie-izmantoti viša programmā)
    if button["text"]==""and speletajsX==True:#spļē X spēlētājs
        button["text"]="X"#maina uz X
        speletajsX=False
        count+=1#palielina rūtiņu skaitu

#############################################################################################################


btn1= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow")
btn2= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="yellow")
btn3= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow")
btn4= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="yellow")
btn5= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow")
btn6= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="yellow")
btn7= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow")
btn8= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24), bg="yellow")
btn9= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow")



###########################################################################################################################

btn1.grid(row=0,column=0)
btn2.grid(row=1,column=0)
btn3.grid(row=2,column=0)
btn4.grid(row=0,column=1)
btn5.grid(row=1,column=1)
btn6.grid(row=2,column=1)
btn7.grid(row=0,column=2)
btn8.grid(row=1,column=2)
btn9.grid(row=2,column=2)









mansLogs.mainloop()