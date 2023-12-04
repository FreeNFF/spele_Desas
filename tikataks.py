from tkinter import*
from tkinter import messagebox #paziņojumi, ieteikumi



mansLogs=Tk()# loga objekts
mansLogs.title("Desas")


#Disabled - izslēgta poga, Active – uz pogas ir noklikšķināts, Normal – parasts pogas stāvoklis, ir pieejama


##########################################################################################################
global winner, speletajsX, count
count=0
speletajsX=True
winner=False
######################################################################################################

def disableButtons(): #spēle beidzas, pogas izslēgtas
 btn1.config(state=DISABLED) #pogas stāvoklis izslēgts
 btn2.config(state=DISABLED)
 btn3.config(state=DISABLED)
 btn4.config(state=DISABLED)
 btn5.config(state=DISABLED)
 btn6.config(state=DISABLED)
 btn7.config(state=DISABLED)
 btn8.config(state=DISABLED)
 btn9.config(state=DISABLED)
 return

########################################################################################################

def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title('Info par programmu')
    jaunsLogs.geometry("300x300")
    apraksts=Label(jaunsLogs,text='Spēles noteikumi')
    apraksts.grid(row=0,column=2)
    return 


########################################################################################################

def reset():
    global count
    count=0
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""
    return


#######################################################################################################3

def btnClick(button):
    global speletajsX,count#kādi mainīgie tiks izmantoti visā programmā(global mainīgie-izmantoti viša programmā)
    if button["text"]==""and speletajsX==True:#spēlē X spēlētājs
        button["text"]="X"#maina uz X
        speletajsX=False
        count+=1#palielina rūtiņu skaitu
        checkWinner()
    elif button["text"]=='' and speletajsX==False:
        button["text"]='O'
        speletajsX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror('Desas', 'Šeit kāds ir ieklikšķinājis.')
    return

#############################################################################################################

def checkWinner():#funkcija, kas nosaka uzvarētāju
    global winner
    winner=False
    if (btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X" or btn4["text"]=="X"and btn5["text"]=="X" and btn6["text"]=="X" or btn7["text"]=="X"and btn8["text"]=="X" and btn9["text"]=="X" or btn1["text"]=="X"and btn4["text"]=="X" and btn7["text"]=="X" or btn2["text"]=="X"and btn5["text"]=="X" and btn8["text"]=="X" or btn3["text"]=="X"and btn6["text"]=="X" and btn9["text"]=="X" or btn1["text"]=="X"and btn5["text"]=="X" and btn9["text"]=="X" or btn3["text"]=="X"and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        disableButtons()
        messagebox.showinfo("Desas", "1. spēlētajs ir uzvarētājs.")
    elif(btn1["text"]=="O"and btn2["text"]=="O" and btn3["text"]=="O" or btn4["text"]=="O"and btn5["text"]=="O" and btn6["text"]=="O" or btn7["text"]=="O"and btn8["text"]=="O" and btn9["text"]=="O" or btn1["text"]=="O"and btn4["text"]=="O" and btn7["text"]=="O" or btn2["text"]=="O"and btn5["text"]=="O" and btn8["text"]=="O" or btn3["text"]=="O"and btn6["text"]=="O" and btn9["text"]=="O" or btn1["text"]=="O"and btn5["text"]=="O" and btn9["text"]=="O" or btn3["text"]=="O"and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        disableButtons()
        messagebox.showinfo("Desas", "2. spēlētajs ir uzvarētājs.")
    elif count==9 and winner==False:
        disableButtons()
        messagebox.showinfo("Desas", "Neizšķirts.")
    return

################################################################################################################

btn1= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow", command=lambda:btnClick(btn1))
btn2= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="yellow", command=lambda:btnClick(btn2))
btn3= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow", command=lambda:btnClick(btn3))
btn4= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="yellow", command=lambda:btnClick(btn4))
btn5= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow", command=lambda:btnClick(btn5))
btn6= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="yellow", command=lambda:btnClick(btn6))
btn7= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow", command=lambda:btnClick(btn7))
btn8= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24), bg="yellow", command=lambda:btnClick(btn8))
btn9= Button(mansLogs, text="", width=6, height=3,font=('Helvica',24),bg="light yellow", command=lambda:btnClick(btn9))



###########################################################################################################################

#Lielā izvēle
galvenaIzvele=Menu(mansLogs)#izveido galveno izvēli
mansLogs.config(menu=galvenaIzvele)#pievieno galvenajam logam


#Mazā izvēle
opcijas=Menu(galvenaIzvele,tearoff=False)#mazā izvēle
galvenaIzvele.add_cascade(label="Opcijas", menu=opcijas)#lejupkrītošais saraksts
galvenaIzvele.add_command(label="Par programmu",command=infoLogs) # pievieno mazajai izvēlnei


#Komandas
opcijas.add_command(label="Jauna spēle", command=reset)
opcijas.add_command(label="Iziet", command=mansLogs.quit)

############################################################################################################################

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