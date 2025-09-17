import random
import time;
import datetime
import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management Systems")
root.configure(background = 'LightSteelBlue') # Changed from Cadet Blue to LightSteelBlue

Tops = Frame(root, bg='SteelBlue', bd=20, pady=5, relief=RIDGE) # Changed from Cadet Blue to SteelBlue
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('Helvetica', 65, 'bold'), text="Restaurant Management Systems", # Changed font to Helvetica, size 65
                 bd=21, bg='SteelBlue', fg='White', justify=CENTER) # Changed bg to SteelBlue, fg to White
lblTitle.grid(row=0, column=0)

ReceiptCal_F = Frame(root, bg='LightGray', bd=10, relief=RIDGE) # Changed from Powder Blue to LightGray
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F, bg='LightGray', bd=3, relief=RIDGE) # Changed from Powder Blue to LightGray
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F, bg='LightGray', bd=6, relief=RIDGE) # Changed from Powder Blue to LightGray
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F, bg='LightGray', bd=4, relief=RIDGE) # Changed from Powder Blue to LightGray
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='LightSteelBlue', bd=10, relief=RIDGE) # Changed from Cadet Blue to LightSteelBlue
MenuFrame.pack(side=LEFT)

Cost_F = Frame(MenuFrame, bg='LightGray', bd=4) # Changed from Powder Blue to LightGray
Cost_F.pack(side=BOTTOM)

Drinks_F=Frame(MenuFrame, bg='LightCyan', bd=10) # Changed from Cadet Blue to LightCyan
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='LightCyan', bd=10, relief=RIDGE) # Changed from Cadet Blue to LightCyan
Drinks_F.pack(side=LEFT)

Cake_F=Frame(MenuFrame, bg='LightCyan', bd=10, relief=RIDGE) # Changed from Powder Blue to LightCyan
Cake_F.pack(side=RIGHT)

#====================Variable====================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCakes=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()

text_Input = StringVar()
operator = ""

E_Latta=StringVar()
E_Espresso=StringVar()
E_Iced_Latta=StringVar()
E_Vale_Coffe=StringVar()
E_Cappuccino=StringVar()
E_African_Coffee=StringVar()
E_American_Coffee=StringVar()
E_Iced_Cappuccino=StringVar()

E_School_Cake=StringVar()
E_Sunny_AO_Cake=StringVar()
E_Jonathan_YO_Cake=StringVar()
E_West_African_Cake=StringVar()
E_Lagos_Chocolate_Cake=StringVar()
E_Kilburn_Chocolate_Cake=StringVar()
E_Carlton_Hill_Chocolate_Cake=StringVar()
E_Queen_Park_Chocolate_Cake=StringVar()

E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latta.set("0")
E_Vale_Coffe.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")

E_School_Cake.set("0")
E_Sunny_AO_Cake.set("0")
E_Jonathan_YO_Cake.set("0")
E_West_African_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Chocolate_Cake.set("0")
E_Queen_Park_Chocolate_Cake.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))


#====================Function====================

def iExit():
    iExit = tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latta.set("0")
    E_Vale_Coffe.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")

    E_School_Cake.set("0")
    E_Sunny_AO_Cake.set("0")
    E_Jonathan_YO_Cake.set("0")
    E_West_African_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    
    txtLatta.configure(state =DISABLED)
    txtEspresso.configure(state= DISABLED)
    txtIced_Latte.configure(state= DISABLED)
    txtVale_Coffee.configure(state= DISABLED)
    txtCappuccino.configure(state= DISABLED)
    txtAfrican_Coffee.configure(state= DISABLED)
    txtAmerican_Coffee.configure(state= DISABLED)
    txtIced_Cappuccino.configure(state= DISABLED)
    txtSchool_Cake.configure(state= DISABLED)
    txtSunny_AO_Cake.configure(state= DISABLED)
    txtJonathan_YO_Cake.configure(state= DISABLED)
    txtWest_African_Cake.configure(state= DISABLED)
    txtLagos_Chocolate_Cake.configure(state= DISABLED)
    txtKilburn_Chocolate_Cake.configure(state= DISABLED)
    txtCarlton_Hill_Cake.configure(state= DISABLED)
    txtQueen_Park_Chocolate_Cake.configure(state= DISABLED)

def CostofItem():
    Item1=float(E_Latta.get())
    Item2=float(E_Espresso.get())
    Item3=float(E_Iced_Latta.get())
    Item4=float(E_Vale_Coffe.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_African_Coffee.get())
    Item7=float(E_American_Coffee.get())
    Item8=float(E_Iced_Cappuccino.get())
    
    Item9=float(E_School_Cake.get())
    Item10=float(E_Sunny_AO_Cake.get())
    Item11=float(E_Jonathan_YO_Cake.get())
    Item12=float(E_West_African_Cake.get())
    Item13=float(E_Lagos_Chocolate_Cake.get())
    Item14=float(E_Kilburn_Chocolate_Cake.get())
    Item15=float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16=float(E_Queen_Park_Chocolate_Cake.get())

    PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) + \
                (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)

    PriceofCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) + \
                (Item12 * 1.49) + (Item13 * 1.8) + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 * 1.99)

    DrinksPrice="£", str('%.2f' % (PriceofDrinks))
    CakesPrice="£", str('%.2f' % (PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="£", str('%.2f' % (1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS ="£", str('%.2f' % (PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax="£", str('%.2f' % ((PriceofDrinks + PriceofCakes + 1.59)*0.15))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 1.59)*0.15)
    TC ="£", str('%.2f' % (PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)

def chkLatta():
    if (var1.get() == 1):
        txtLatta.configure(state = NORMAL)
        txtLatta.focus()
        txtLatta.delete('0', END)
        E_Latta.set("")
    elif(var1.get() == 0):
        txtLatta.configure(state = DISABLED)
        E_Latta.set("0")
        
def chkEspresso():
    if (var2.get() == 1):
        txtEspresso.configure(state=NORMAL)
        txtEspresso.focus()
        E_Espresso.set("")
    elif var2.get() == 0:
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
        
def chkIced_Latte():
    if (var3.get() == 1):
        txtIced_Latte.configure(state=NORMAL)
        txtIced_Latte.delete(0, END)
        txtIced_Latte.focus()
    elif var3.get() == 0:
        txtIced_Latte.configure(state=DISABLED)
        E_Iced_Latta.set("0")

def chkVale_Coffee():
    if (var4.get() == 1):
        txtVale_Coffee.configure(state= NORMAL)
        txtVale_Coffee.delete(0,END)
        txtVale_Coffee.focus()
    elif var4.get() == 0:
        txtVale_Coffee.configure(state= DISABLED)
        E_Vale_Coffe.set("0")
        
def chkCappuccino():
    if (var5.get() == 1):
        txtCappuccino.configure(state= NORMAL)
        txtCappuccino.delete(0,END)
        txtCappuccino.focus()
    elif var5.get() == 0:
        txtCappuccino.configure(state= DISABLED)
        E_Cappuccino.set("0")
        
def chkAfrican_Coffee():
    if (var6.get() == 1):
        txtAfrican_Coffee.configure(state= NORMAL)
        txtAfrican_Coffee.delete(0,END)
        txtAfrican_Coffee.focus()
    elif var6.get() == 0:
        txtAfrican_Coffee.configure(state= DISABLED)
        E_African_Coffee.set("0")

def chkAmerican_Coffee():
    if (var7.get() == 1):
        txtAmerican_Coffee.configure(state= NORMAL)
        txtAmerican_Coffee.delete(0,END)
        txtAmerican_Coffee.focus()
    elif var7.get() == 0:
        txtAmerican_Coffee.configure(state= DISABLED)
        E_American_Coffee.set("0")

def chkIced_Cappuccino():
    if (var8.get() == 1):
        txtIced_Cappuccino.configure(state= NORMAL)
        txtIced_Cappuccino.delete(0,END)
        txtIced_Cappuccino.focus()
    elif var8.get() == 0:
        txtIced_Cappuccino.configure(state= DISABLED)
        E_Iced_Cappuccino.set("0")

def chkSchool_Cake():
    if (var9.get() == 1):
        txtSchool_Cake.configure(state= NORMAL)
        txtSchool_Cake.delete(0,END)
        txtSchool_Cake.focus()
    elif var9.get() == 0:
        txtSchool_Cake.configure(state= DISABLED)
        E_School_Cake.set("0")
        
def chkSunny_AO_Cake():
    if (var10.get() == 1):
        txtSunny_AO_Cake.configure(state= NORMAL)
        txtSunny_AO_Cake.delete(0,END)
        txtSunny_AO_Cake.focus()
    elif var10.get() == 0:
        txtSunny_AO_Cake.configure(state= DISABLED)
        E_Sunny_AO_Cake.set("0")

def chkJonathan_YO_Cake():
    if (var11.get() == 1):
        txtJonathan_YO_Cake.configure(state= NORMAL)
        txtJonathan_YO_Cake.delete(0,END)
        txtJonathan_YO_Cake.focus()
    elif var11.get()== 0:
        txtJonathan_YO_Cake.configure(state= DISABLED)
        E_Jonathan_YO_Cake.set("0")
        
def chkWest_African_Cake():
    if (var12.get() == 1):
        txtWest_African_Cake.configure(state= NORMAL)
        txtWest_African_Cake.delete(0,END)
        txtWest_African_Cake.focus()
    elif var12.get() == 0:
        txtWest_African_Cake.configure(state= DISABLED)
        E_West_African_Cake.set("0")

def chkLagos_Chocolate_Cake():
    if (var13.get() == 1):
        txtLagos_Chocolate_Cake.configure(state= NORMAL)
        txtLagos_Chocolate_Cake.delete(0,END)
        txtLagos_Chocolate_Cake.focus()
    elif var13.get() == 0:
        txtLagos_Chocolate_Cake.configure(state= DISABLED)
        E_Lagos_Chocolate_Cake.set("0")
        
def chkKilburn_Chocolate_Cake():
    if (var14.get() == 1):
        txtKilburn_Chocolate_Cake.configure(state= NORMAL)
        txtKilburn_Chocolate_Cake.delete(0,END)
        txtKilburn_Chocolate_Cake.focus()
    elif var14.get() == 0:
        txtKilburn_Chocolate_Cake.configure(state= DISABLED)
        E_Kilburn_Chocolate_Cake.set("0")

def chkCarlton_Hill_Cake():
    if (var15.get() == 1):
        txtCarlton_Hill_Chocolate_Cake.configure(state= NORMAL)
        txtCarlton_Hill_Chocolate_Cake.delete(0,END)
        txtCarlton_Hill_Chocolate_Cake.focus()
    elif var15.get()== 0:
        txtCarlton_Hill_Chocolate_Cake.configure(state= DISABLED)
        E_Carlton_Hill_Chocolate_Cake.set("0")
        
def chkQueen_Park_Cake():
    if (var16.get() == 1):
        txtQueen_Park_Chocolate_Cake.configure(state= NORMAL)
        txtQueen_Park_Chocolate_Cake.delete(0,END)
        txtQueen_Park_Chocolate_Cake.focus()
    elif var16.get()== 0:
        txtQueen_Park_Chocolate_Cake.configure(state= DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")

def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t\t' + Receipt_Ref.get() + '\t\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items \n")
    txtReceipt.insert(END, 'Latta:\t\t\t\t\t' + E_Latta.get() + "\n")
    txtReceipt.insert(END, 'Espresso:\t\t\t\t' + E_Espresso.get() + "\n")
    txtReceipt.insert(END, 'Iced Latta:\t\t\t\t' + E_Iced_Latta.get() + "\n")
    txtReceipt.insert(END, 'Vale Coffe:\t\t\t\t' + E_Vale_Coffe.get() + "\n")
    txtReceipt.insert(END, 'Cappuccino:\t\t\t\t' + E_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'African Coffee:\t\t\t\t' + E_African_Coffee.get() + "\n")
    txtReceipt.insert(END, 'American Coffee:\t\t\t\t' + E_American_Coffee.get() + "\n")
    txtReceipt.insert(END, 'Iced Cappuccino:\t\t\t\t' + E_Iced_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'Coffee Cake:\t\t\t\t' + E_School_Cake.get() + "\n")
    txtReceipt.insert(END, 'Sunny AO Cake:\t\t\t\t' + E_Sunny_AO_Cake.get() + "\n")
    txtReceipt.insert(END, 'Jonathan O Cake:\t\t\t\t' + E_Jonathan_YO_Cake.get() + "\n")
    txtReceipt.insert(END, 'West African C_Cake:\t\t\t\t' + E_West_African_Cake.get() + "\n")
    txtReceipt.insert(END, 'Lagos Chocolate Cake:\t\t\t\t' + E_Lagos_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Kilburn Chocolate Cake:\t\t\t\t' + E_Kilburn_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Carlton Hill Chocolate Cake:\t\t\t\t' + E_Carlton_Hill_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Queens Park Chocolate Cake:\t\t\t\t' + E_Queen_Park_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Cost of Drinks:\t\t\t\t' + CostofDrinks.get() + '\nTax Paid:\t\t\t\t' + PaidTax.get() + "\n")
    txtReceipt.insert(END, 'Cost of Cakes:\t\t\t\t' + CostofCakes.get() + '\nSubTotal:\t\t\t\t' + str(SubTotal.get()) + "\n")
    txtReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get() + '\nTotal Cost:\t\t\t\t' + str(TotalCost.get()))

# =========================================================Drinks=========================================================

Latta = Checkbutton(Drinks_F, text="Latta ", variable=var1, onvalue = 1, offvalue = 0,
                    font=('Verdana',16, 'bold'),bg="LightCyan",command=chkLatta).grid(row=0, sticky=W) # Font and bg changed

Espresso = Checkbutton(Drinks_F, text="Espresso ", variable=var2, onvalue = 1, offvalue = 0,
                       font=('Verdana',16, 'bold'),bg="LightCyan",command=chkEspresso).grid(row=1, sticky=W) # Font and bg changed

Iced_Latte = Checkbutton(Drinks_F, text="Iced Latte ", variable=var3, onvalue = 1, offvalue = 0,
                         font=('Verdana',16, 'bold'),bg="LightCyan",command=chkIced_Latte).grid(row=2, sticky=W) # Font and bg changed

Vale_Coffee = Checkbutton(Drinks_F, text="Vale Coffee", variable=var4, onvalue = 1, offvalue = 0,
                          font=('Verdana',16, 'bold'),bg="LightCyan",command=chkVale_Coffee).grid(row=3, sticky=W) # Font and bg changed

Cappuccino= Checkbutton(Drinks_F, text="Cappuccino", variable=var5, onvalue = 1, offvalue = 0,
                        font=('Verdana',16, 'bold'),bg="LightCyan",command=chkCappuccino).grid(row=4, sticky=W) # Font and bg changed

African_Coffee = Checkbutton(Drinks_F, text="African Coffee", variable=var6, onvalue = 1, offvalue = 0,
                             font=('Verdana',16, 'bold'),bg="LightCyan",command=chkAfrican_Coffee ).grid(row=5, sticky=W) # Font and bg changed

American_Coffee = Checkbutton(Drinks_F, text="American Coffee ", variable=var7, onvalue = 1, offvalue = 0,
                              font=('Verdana',16, 'bold'),bg="LightCyan",command=chkAmerican_Coffee).grid(row=6, sticky=W) # Font and bg changed

Iced_Cappuccino = Checkbutton(Drinks_F, text="Iced Cappuccino", variable=var8, onvalue = 1, offvalue = 0,
                              font=('Verdana',16, 'bold'),bg="LightCyan",command=chkIced_Cappuccino).grid(row=7, sticky=W) # Font and bg changed

#====================Entry Box for Drinks====================
txtLatta = Entry(Drinks_F,font=('arial', 16, 'bold'), textvariable=E_Latta, bd=8,width=6, justify='left',state= DISABLED, bg='AliceBlue') # bg changed
txtLatta.grid(row=0,column=1)
txtEspresso = Entry(Drinks_F,font=('arial', 16, 'bold'), textvariable=E_Espresso, bd=8,width=6, justify='left',state= DISABLED, bg='AliceBlue') # bg changed
txtEspresso.grid(row=1,column=1)
txtIced_Latte = Entry(Drinks_F,font=('arial', 16, 'bold'), textvariable=E_Iced_Latta, bd=8,width=6, justify='left',state= DISABLED, bg='AliceBlue') # bg changed
txtIced_Latte.grid(row=2,column=1)
txtVale_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'), textvariable=E_Vale_Coffe, bd=8,width=6, justify='left',state= DISABLED, bg='AliceBlue') # bg changed
txtVale_Coffee.grid(row=3,column=1)
txtCappuccino = Entry(Drinks_F,font=('arial', 16, 'bold'), textvariable=E_Cappuccino, bd=8,width=6, justify='left',state= DISABLED, bg='AliceBlue') # bg changed
txtCappuccino.grid(row=4,column=1)
txtAfrican_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'), textvariable=E_African_Coffee, bd=8,width=6, justify='left',state= DISABLED, bg='AliceBlue') # bg changed
txtAfrican_Coffee.grid(row=5,column=1)
txtAmerican_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'), textvariable=E_American_Coffee, bd=8,width=6, justify='left',state= DISABLED, bg='AliceBlue') # bg changed
txtAmerican_Coffee.grid(row=6,column=1)
txtIced_Cappuccino = Entry(Drinks_F,font=('arial', 16, 'bold'), textvariable=E_Iced_Cappuccino, bd=8,width=6, justify='left',state= DISABLED, bg='AliceBlue') # bg changed
txtIced_Cappuccino.grid(row=7,column=1)
txtIced_Cappuccino.grid(row=7,column=1)

# =========================================================Cakes=========================================================

SchoolCake = Checkbutton(Cake_F, text="School Cake", variable=var9, onvalue = 1, offvalue = 0,
                         font=('Verdana',16, 'bold'),bg="LightCyan",command=chkSchool_Cake).grid(row=0, sticky=W) # Font and bg changed

Sunny_AO_Cake = Checkbutton(Cake_F, text="Sunday O Cake ", variable=var10, onvalue = 1, offvalue = 0,
                            font=('Verdana',16, 'bold'),bg="LightCyan",command=chkSunny_AO_Cake).grid(row=1, sticky=W) # Font and bg changed

Jonathan_YO_Cake = Checkbutton(Cake_F, text="Jonathan O Cake ", variable=var11, onvalue = 1, offvalue = 0,
                               font=('Verdana',16, 'bold'),bg="LightCyan",command=chkJonathan_YO_Cake).grid(row=2, sticky=W) # Font and bg changed

West_African_Cake = Checkbutton(Cake_F, text="West African Cake ", variable=var12, onvalue = 1, offvalue = 0,
                                font=('Verdana',16, 'bold'),bg="LightCyan",command=chkWest_African_Cake).grid(row=3, sticky=W) # Font and bg changed

Lagos_Chocolate_Cake = Checkbutton(Cake_F, text="Lagos Chocolate Cake", variable=var13, onvalue = 1, offvalue = 0,
                                   font=('Verdana',16, 'bold'),bg="LightCyan",command=chkLagos_Chocolate_Cake).grid(row=4, sticky=W) # Font and bg changed

Kilburn_Chocolate_Cake = Checkbutton(Cake_F, text="Kilburn Chocolate Cake", variable=var14, onvalue = 1, offvalue = 0,
                                     font=('Verdana',16, 'bold'),bg="LightCyan",command=chkKilburn_Chocolate_Cake).grid(row=5, sticky=W) # Font and bg changed

Carlton_Hill_Cake = Checkbutton(Cake_F, text="Carlton Hill Chocolate Cake", variable=var15, onvalue = 1, offvalue = 0,
                                font=('Verdana',16, 'bold'),bg="LightCyan",command=chkCarlton_Hill_Cake).grid(row=6, sticky=W) # Font and bg changed

Queen_Park_Cake = Checkbutton(Cake_F, text="Queen's Park Chocolate Cake", variable=var16, onvalue = 1, offvalue = 0,
                              font=('Verdana',16, 'bold'),bg="LightCyan",command=chkQueen_Park_Cake).grid(row=7, sticky=W) # Font and bg changed

#====================Entry Box for Cakes====================
txtSchool_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED, textvariable=E_School_Cake, bg='AliceBlue') # bg changed
txtSchool_Cake.grid(row=0,column=1)
txtSunny_AO_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED, textvariable=E_Sunny_AO_Cake, bg='AliceBlue') # bg changed
txtSunny_AO_Cake.grid(row=1,column=1)
txtJonathan_YO_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED, textvariable=E_Jonathan_YO_Cake, bg='AliceBlue') # bg changed
txtJonathan_YO_Cake.grid(row=2,column=1)
txtWest_African_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED, textvariable=E_West_African_Cake, bg='AliceBlue') # bg changed
txtWest_African_Cake.grid(row=3,column=1)
txtLagos_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED, textvariable=E_Lagos_Chocolate_Cake, bg='AliceBlue') # bg changed
txtLagos_Chocolate_Cake.grid(row=4,column=1)
txtKilburn_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED, textvariable=E_Kilburn_Chocolate_Cake, bg='AliceBlue') # bg changed
txtKilburn_Chocolate_Cake.grid(row=5,column=1)
txtCarlton_Hill_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED, textvariable=E_Carlton_Hill_Chocolate_Cake, bg='AliceBlue') # bg changed
txtCarlton_Hill_Chocolate_Cake.grid(row=6,column=1)
txtQueen_Park_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=E_Queen_Park_Chocolate_Cake, bg='AliceBlue') # bg changed
txtQueen_Park_Chocolate_Cake.grid(row=7, column=1)

# =========================================================Totals Cost=========================================================

lblCostofDrinks = Label(Cost_F,font=('Verdana', 13, 'bold'), text="Cost of Drinks", bg="LightGray",fg="black") # Font and bg changed
lblCostofDrinks.grid(row=0, column=0, sticky=W)
txtCostofDrinks = Entry(Cost_F,font=('arial', 14, 'bold'), textvariable=CostofDrinks, bd=7,bg="AliceBlue", # bg changed
                        insertwidth=2, justify=RIGHT)
txtCostofDrinks.grid(row=0, column=1)

lblCostofCakes = Label(Cost_F,font=('Verdana', 13, 'bold'), text="Cost of Cakes ", bg="LightGray",fg="black") # Font and bg changed
lblCostofCakes.grid(row=1, column=0, sticky=W)
txtCostofCakes = Entry(Cost_F,font=('arial', 14, 'bold'), textvariable=CostofCakes, bd=7,bg="AliceBlue", # bg changed
                        insertwidth=2, justify=RIGHT)
txtCostofCakes.grid(row=1, column=1)

lblServiceCharge = Label(Cost_F,font=('Verdana', 13, 'bold'), text="Service Charge ", bg="LightGray",fg="black") # Font and bg changed
lblServiceCharge.grid(row=2, column=0, sticky=W)
txtServiceCharge = Entry(Cost_F,font=('arial', 14, 'bold'), textvariable=ServiceCharge, bd=7,bg="AliceBlue", # bg changed
                        justify=RIGHT)
txtServiceCharge.grid(row=2, column=1)

# =========================================================Payment Information=========================================================

lblPaidTax = Label(Cost_F,font=('Verdana', 13, 'bold'), text="Paid Tax", bd=7,bg="LightGray",fg="black") # Font and bg changed
lblPaidTax.grid(row=0, column=2, sticky=W)
txtPaidTax = Entry(Cost_F,font=('arial', 14, 'bold'), textvariable=PaidTax, bd=7, bg="AliceBlue", # bg changed
                   insertwidth=2, justify=RIGHT)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F,font=('Verdana', 13, 'bold'), text="Sub Total", bd=7,bg="LightGray",fg="black") # Font and bg changed
lblSubTotal.grid(row=1, column=2, sticky=W)
txtSubTotal = Entry(Cost_F,font=('arial', 14, 'bold'), textvariable=SubTotal, bd=7, bg="AliceBlue", # bg changed
                    insertwidth=2, justify=RIGHT)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F,font=('Verdana', 13, 'bold'), text="Total Cost", bd=7, bg="LightGray",fg="black") # Font and bg changed
lblTotalCost.grid(row=2, column=2, sticky=W)
txtTotalCost = Entry(Cost_F,font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7, bg="AliceBlue", insertwidth=2, # bg changed
                     justify=RIGHT)
txtTotalCost.grid(row=2, column=3)

#====================Receipt====================
txtReceipt = Text(Receipt_F, width=46, height=12, bg="GhostWhite", bd=4,font=('Consolas', 11, 'bold')) # Font and bg changed
txtReceipt.grid(row=0, column=0)

#====================Buttons====================
btnTotal = Button(Buttons_F, padx=16,pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), width=4, # Font, fg, bg changed
                  text="Total", command=CostofItem, bg="SteelBlue").grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16,pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), width=4, # Font, fg, bg changed
                    text="Receipt",command=Receipt, bg="SteelBlue").grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16,pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), width=4, # Font, fg, bg changed
                  text="Reset", command=Reset, bg="SteelBlue").grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16,pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), width=4, # Font, fg, bg changed
                 text="Exit", command=iExit,bg="SteelBlue").grid(row=0, column=3)

#====================Calculator Display====================
txtDisplay = Entry(Cal_F, width=45, bg="GhostWhite", bd=4,font=('arial', 12, 'bold'), justify=RIGHT) # bg changed
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")


#====================Calculator Display====================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(Cal_F, width=45, bg="GhostWhite", bd=4, font=('arial', 12, 'bold'), justify=RIGHT, textvariable=text_Input) # bg changed
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#====================Calculator Buttons====================
btn7 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="7", bg="SteelBlue", command=lambda:btnClick(7)).grid(row=2, column=0)
btn8 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="8", bg="SteelBlue", command=lambda:btnClick(8)).grid(row=2, column=1)
btn9 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="9", bg="SteelBlue", command=lambda:btnClick(9)).grid(row=2, column=2)
btnadd = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
                width=4, text="+", bg="SteelBlue", command=lambda:btnClick("+")).grid(row=2, column=3)
#====================Calculator Buttons====================
btn4 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="4", bg="SteelBlue", command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="5", bg="SteelBlue", command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="6", bg="SteelBlue", command=lambda:btnClick(6)).grid(row=3, column=2)
btnSub = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
                width=4, text="-", bg="SteelBlue", command=lambda:btnClick("-")).grid(row=3, column=3)
#====================Calculator Buttons====================
btn1 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="1", bg="SteelBlue", command=lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="2", bg="SteelBlue", command=lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="3", bg="SteelBlue", command=lambda:btnClick(3)).grid(row=4, column=2)
btnMulti = Button(Cal_F, padx=16, pady=1, bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
                  width=4, text="*", bg="SteelBlue", command=lambda:btnClick("*")).grid(row=4, column=3)
#====================Calculator Buttons====================
btn0 = Button(Cal_F, padx=16,pady=1,bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
              width=4, text="0", bg="SteelBlue", command=lambda:btnClick(0)).grid(row=5, column=0)
btnClear = Button(Cal_F, padx=16,pady=1,bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
                  width=4, text="C", bg="SteelBlue", command=btnClear).grid(row=5, column=1)
btnEquals = Button(Cal_F, padx=16,pady=1,bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
                   width=4, text="=", bg="SteelBlue", command=btnEquals).grid(row=5, column=2)
btnDiv = Button(Cal_F, padx=16,pady=1,bd=7, fg="White", font=('Verdana', 14, 'bold'), # Font, fg, bg changed
                width=4, text="/", bg="SteelBlue", command=lambda:btnClick("/")).grid(row=5, column=3)

root.mainloop()
