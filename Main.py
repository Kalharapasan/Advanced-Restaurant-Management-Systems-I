import random
import time;
import datetime
import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management Systems")
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 60, 'bold'), text="Restaurant Management Systems", 
                 bd=21, bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

ReceiptCal_F = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)

Cost_F = Frame(MenuFrame, bg='Powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)

Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)

Cake_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
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

#==================== Drinks ====================
Latta = Checkbutton(Drinks_F, text="Latta", variable=var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='Powder Blue').grid(row=0, sticky=W)
Espresso = Checkbutton(Drinks_F, text="Espresso", variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='Powder Blue').grid(row=1, sticky=W)
Iced_Latta = Checkbutton(Drinks_F, text="Iced Latta", variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='Powder Blue').grid(row=2, sticky=W)
Vale_Coffee = Checkbutton(Drinks_F, text="Vale Coffee", variable=var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='Powder Blue').grid(row=3, sticky=W)
Cappuccino = Checkbutton(Drinks_F, text="Cappuccino", variable=var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='Powder Blue').grid(row=4, sticky=W)
African_Coffee = Checkbutton(Drinks_F, text="African Coffee", variable=var6, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='Powder Blue').grid(row=5, sticky=W)
American_Coffee = Checkbutton(Drinks_F, text="American Coffee", variable=var7, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='Powder Blue').grid(row=6, sticky=W)
Iced_Cappuccino = Checkbutton(Drinks_F, text="Iced Cappuccino", variable=var8, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='Powder Blue').grid(row=7, sticky=W)

#==================== Entry Box for Drinks ====================
txtLatta = Entry(Drinks_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtLatta.grid(row=0,column=1)
txtEspresso = Entry(Drinks_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtEspresso.grid(row=1,column=1)
txtIced_Latta = Entry(Drinks_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtIced_Latta.grid(row=2,column=1)
txtVale_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtVale_Coffee.grid(row=3,column=1)
txtCappuccino = Entry(Drinks_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtCappuccino.grid(row=4,column=1)
txtAfrican_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtAfrican_Coffee.grid(row=5,column=1)
txtAmerican_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtAmerican_Coffee.grid(row=6,column=1)
txtIced_Cappuccino = Entry(Drinks_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtIced_Cappuccino.grid(row=7,column=1)

#==================== Cakes ====================
SchoolCake = Checkbutton(Cake_F, text="School Cake\t\t", variable=var9, onvalue=1, offvalue=0, font=('arial',16, 'bold'), bg='powder blue').grid(row=0, sticky=W)
Sunny_AO_Cake = Checkbutton(Cake_F, text="Sunday O Cake ", variable=var10, onvalue=1, offvalue=0, font=('arial',16, 'bold'), bg='powder blue').grid(row=1, sticky=W)
Jonathan_YO_Cake = Checkbutton(Cake_F, text="Jonathan O Cake ", variable=var11, onvalue=1, offvalue=0, font=('arial',16, 'bold'), bg='powder blue').grid(row=2, sticky=W)
West_African_Cake = Checkbutton(Cake_F, text="West African Cake ", variable=var12, onvalue=1, offvalue=0, font=('arial',16, 'bold'), bg='powder blue').grid(row=3, sticky=W)
Lagos_Chocolate_Cake = Checkbutton(Cake_F, text="Lagos Chocolate Cake", variable=var13, onvalue=1, offvalue=0, font=('arial',16, 'bold'), bg='powder blue').grid(row=4, sticky=W)
Kilburn_Chocolate_Cake = Checkbutton(Cake_F, text="Kilburn Chocolate Cake", variable=var14, onvalue=1, offvalue=0, font=('arial',16, 'bold'), bg='powder blue').grid(row=5, sticky=W)
Carlton_Hill_Cake = Checkbutton(Cake_F, text="Carlton Hill Chocolate Cake", variable=var15, onvalue=1, offvalue=0, font=('arial',16, 'bold'), bg='powder blue').grid(row=6, sticky=W)
Queen_Park_Cake = Checkbutton(Cake_F, text="Queen's Park Chocolate Cake", variable=var16, onvalue=1, offvalue=0, font=('arial',16, 'bold'), bg='powder blue').grid(row=7, sticky=W)

#==================== Entry Box for Cakes====================
txtSchool_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtSchool_Cake.grid(row=0,column=1)
txtSunny_AO_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtSunny_AO_Cake.grid(row=1,column=1)
txtJonathan_YO_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtJonathan_YO_Cake.grid(row=2,column=1)
txtWest_African_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtWest_African_Cake.grid(row=3,column=1)
txtLagos_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtLagos_Chocolate_Cake.grid(row=4,column=1)
txtKilburn_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtKilburn_Chocolate_Cake.grid(row=5,column=1)
txtCarlton_Hill_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtCarlton_Hill_Chocolate_Cake.grid(row=6,column=1)
txtQueen_Park_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'), bd=8,width=6, justify='left',state= DISABLED)
txtQueen_Park_Chocolate_Cake.grid(row=7,column=1)

#====================Totals Cost====================
lblCostofDrinks = Label(Cost_F,font=('arial', 14, 'bold'), text="Cost Of Drinks\t", bg="powder blue",fg="black",)
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks = Entry(Cost_F,font=('arial', 14, 'bold'), bd=7, bg="white", insertwidth=2, justify=RIGHT)
txtCostofDrinks.grid(row=0,column=1)

lblCostofCakes = Label(Cost_F,font=('arial', 14, 'bold'), text="Cost Of Cakes  ", bg="powder blue",fg="black",)
lblCostofCakes.grid(row=1,column=0, sticky=W)
txtCostofCakes = Entry(Cost_F,font=('arial', 14, 'bold'), bd=7, bg="white", insertwidth=2, justify=RIGHT)
txtCostofCakes.grid(row=1,column=1)

lblServiceCharge = Label(Cost_F,font=('arial', 14, 'bold'), text="Service Charge ", bg="powder blue",fg="black",)
lblServiceCharge.grid(row=2,column=0, sticky=W)
txtServiceCharge = Entry(Cost_F,font=('arial', 14, 'bold'), bd=7, bg="white", justify=RIGHT)
txtServiceCharge.grid(row=2,column=1)

#====================Payment Information====================
lblPaidTax = Label(Cost_F,font=('arial', 14, 'bold'), text="\tPaid Tax\t", bd=7, bg="powder Blue",fg="black",)
lblPaidTax.grid(row=0, column=2, sticky=W)
txtPaidTax = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, bg="white", insertwidth=2, justify=RIGHT)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F,font=('arial', 14, 'bold'), text="\tSub Total", bd=7, bg="powder Blue",fg="black",)
lblSubTotal.grid(row=1, column=2, sticky=W)
txtSubTotal = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, bg="white", insertwidth=2, justify=RIGHT)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F,font=('arial', 14, 'bold'), text="\tTotal Cost", bd=7, bg="powder Blue",fg="black",)
lblTotalCost.grid(row=2, column=2, sticky=W)
txtTotalCost = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, bg="white", insertwidth=2, justify=RIGHT)
txtTotalCost.grid(row=2, column=3)

#====================Receipt====================
txtReceipt = Text(Receipt_F, width=46, height=12, bg="white", bd=4,font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

#====================Buttons====================
btnTotal = Button(Buttons_F, padx=16,pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="Total", bg="powder blue").grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16,pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="Receipt", bg="powder blue").grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16,pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="Reset", bg="powder blue").grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16,pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="Exit", bg="powder blue").grid(row=0, column=3)

#====================Calculator Display====================
txtDisplay = Entry(Cal_F, width=45, bg="white", bd=4,font=('arial', 12, 'bold'), justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#====================Calculator Buttons====================
btn7 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="7", bg="powder blue").grid(row=2, column=0)
btn8 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="8", bg="powder blue").grid(row=2, column=1)
btn9 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="9", bg="powder blue").grid(row=2, column=2)
btnadd = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="+", bg="powder blue").grid(row=2, column=3)

#====================Calculator Buttons====================
btn4 = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="4", bg="powder blue").grid(row=3, column=0)
btn5 = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="5", bg="powder blue").grid(row=3, column=1)
btn6 = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="6", bg="powder blue").grid(row=3, column=2)
btnSub = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="-", bg="powder blue").grid(row=3, column=3)
#====================Calculator Buttons====================
btn1 = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="1", bg="powder blue").grid(row=4, column=0)
btn2 = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="2", bg="powder blue").grid(row=4, column=1)
btn3 = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="3", bg="powder blue").grid(row=4, column=2)
btnMulti = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="*", bg="powder blue").grid(row=4, column=3)
#====================Calculator Buttons====================
btn0 = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="0", bg="powder blue").grid(row=5, column=0)
btnClear = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="C", bg="powder blue").grid(row=5, column=1)
btnEquals = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="=", bg="powder blue").grid(row=5, column=2)
btnDiv = Button(Cal_F, padx=16,pady=1,bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="/", bg="powder blue").grid(row=5, column=3)




root.mainloop()