from tkinter import*
import random
import time;
import datetime


root = Tk()
root.title("Adventure Car Hire")
root.geometry('1350x650+0+0')
root.configure(background='black')

icon = PhotoImage(file='adventurelogo.png')
root.tk.call('wm', 'iconphoto', root._w, icon)

Tops = Frame(root, width=1330,height = 100,bg=  "dark orange",  bd=6, relief="raise")
Tops.pack(side=TOP)

img1=PhotoImage(file="adventurelogo.png")

lblInfo=Label(Tops, font=('arial',30,'bold'),bg= "black", fg= "White", text="                                        Adventure Car Hire                                               ",bd=10, anchor='w')
lblInfo.grid(row=0,column=0)

LeftMayFrame = Frame(root, width =1000, height=650, bg= "black",bd=8, relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame = Frame(root, width =350,bg= "dark orange", height=650, bd=8, relief="raise")
RightMayFrame.pack(side=RIGHT)


LeftMayFrame1 = Frame(LeftMayFrame, width =1000, bg= "dark orange",height=225, bd=8, relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2 = Frame(LeftMayFrame, width =1000,bg= "dark orange", height=225, bd=8, relief="raise")
LeftMayFrame2.pack(side=TOP)
LeftMayFrame3 = Frame(LeftMayFrame, width =1000, bg= "dark orange",height=100, bd=8, relief="raise")
LeftMayFrame3.pack(side=TOP)
LeftMayFrame4 = Frame(LeftMayFrame, width =1000, bg= "black",height=100, bd=8, relief="raise")
LeftMayFrame4.pack(side=TOP)


RightMayFrame1 = Frame(RightMayFrame, width =350,bg= "dark orange", height=325, bd=8, relief="raise")
RightMayFrame1.pack(side=TOP)
RightMayFrame2 = Frame(RightMayFrame, width =350, bg= "dark orange",height=325, bd=8, relief="raise")
RightMayFrame2.pack(side=BOTTOM)

#************************************cost of renting  a car***************************************
def CarRentalCost():
    NoofDays = float(NumberofDays.get())
    CarDiscount = float(Discount.get())
    DailyRate = float(DaysRented.get())

    RentalCost = (((NoofDays * DailyRate)* CarDiscount)/100)

    CostofRental ="₦", str('%.1f'%((NoofDays * DailyRate) - RentalCost ))
    Total.set(CostofRental)

    ID = random.randint(51, 95)
    randomID = str(ID)
    CustomerID.set("CAR"+ randomID)

    Inv = random.randint(15, 112)
    invID = str(Inv)
    InvoiceID.set("INV" + invID)

#*************************************************variables*****************************************

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()

CustomerID =StringVar()
DaysRented =StringVar()
Discount =StringVar()
NumberofDays =StringVar()
InvoiceID =StringVar()
Total =StringVar()
Receipt_Ref =StringVar()
DateofOrder=StringVar()
EngineSize=StringVar()
Style=StringVar()
RegisteredYear=StringVar()
ClassID=StringVar()
PlateNumber=StringVar()
MilesBefore=StringVar()
MilesAfter=StringVar()
Make=StringVar()
Model=StringVar()
CarColour=StringVar()
EngineNo=StringVar()
CarColour=StringVar()
CarInsurance=StringVar()
Area=StringVar()
DailyRentalRate=StringVar()
RegistrationNo=StringVar()
IssueBy=StringVar()
PhoneNo=StringVar()
LicenceNo=StringVar()
NumberofDays=StringVar()
Surname=StringVar()
Manual=StringVar()
Street=StringVar()
Firstname=StringVar()
Title=StringVar()
Customer=StringVar()
PostCode=StringVar()

#***************************************************************************************
def qExit():
    qExit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

#*******************************************************************************
def Reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)

    CustomerID.set("")
    DaysRented.set("")
    Discount.set("")
    NumberofDays.set("")
    InvoiceID.set("")
    Total.set("")
    Receipt_Ref .set("")
    DateofOrder.set("")
    EngineSize.set("")
    Style.set("")
    RegisteredYear.set("")
    ClassID.set("")
    PlateNumber.set("")
    MilesBefore.set("")
    MilesAfter.set("")
    Make.set("")
    Model.set("")
    CarColour.set("")
    EngineNo.set("")
    CarInsurance.set("")
    Area.set("")
    DailyRentalRate.set("")
    RegistrationNo.set("")
    IssueBy.set("")
    Manual.set("")
    PhoneNo.set("")
    LicenceNo.set("")
    Surname.set("")
    Street.set("")
    Firstname.set("")
    Title.set("")
    Customer.set("")
    PostCode.set("")
    txtReceipt.delete("1.0",END)

#***********************************************************Receipt********************************************************
def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(108,506)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t'+Receipt_Ref.get() +'\n\nDate:\t'+ DateofOrder.get()+"\n\n")
    txtReceipt.insert(END, " **** Adventure Car Hire **** \n\n")
    txtReceipt.insert(END, "* No 254 Akuje Street, FHA Lugbe,abuja *\n\n")
    txtReceipt.insert(END,'Firstname: \t'+ Firstname.get()+ "\n\n")
    txtReceipt.insert(END,'Surname: \t'+ Surname.get()+ "\n\n")
    txtReceipt.insert(END,'CustomerID: \t'+ CustomerID.get()+ "\n\n")
    txtReceipt.insert(END,'PlateNumber: \t'+ PlateNumber.get()+ "\n\n")
    txtReceipt.insert(END,'Make: \t'+ Make.get()+ "\n\n")
    txtReceipt.insert(END,'DaysRented: \t\t' + DaysRented.get()+ "\n\n")
    txtReceipt.insert(END,'NumberofDays: \t\t' + NumberofDays.get()+ "\n\n")
    txtReceipt.insert(END,'InvoiceID: \t' + InvoiceID.get()+ "\n\n")
    txtReceipt.insert(END,'Discount: \t\t' + Discount.get()+ "\n\n")
    txtReceipt.insert(END,'Total : \t' + Total.get() )

#*****************************************RightFrame1***********************************************************************

chkManual = Checkbutton(RightMayFrame1, text="Manual \t\t", bg= "dark orange",onvalue = 1, offvalue = 0, variable=var1,
                    font=('arial',12,'bold')).grid(row=1, sticky=W)

chkClassID = Checkbutton(RightMayFrame1, text="Class ID \t\t", bg= "dark orange",onvalue = 1, offvalue = 0, variable=var2,
                    font=('arial',12,'bold')).grid(row=2, sticky=W)

chkInvoiceID = Checkbutton(RightMayFrame1, text="Invoice ID \t\t", bg= "dark orange", onvalue = 1, offvalue = 0, variable=var3,
                    font=('arial',12,'bold')).grid(row=3, sticky=W)

chkDailyRate = Checkbutton(RightMayFrame1, text="Daily Rate \t\t",  bg= "dark orange",onvalue = 1, offvalue = 0, variable=var4,
                    font=('arial',12,'bold')).grid(row=4, sticky=W)

chkAutomatic = Checkbutton(RightMayFrame1, text="Automatic \t\t", bg= "dark orange", onvalue = 1, offvalue = 0, variable=var5,
                    font=('arial',12,'bold')).grid(row=5, sticky=W)

chkAirCondition = Checkbutton(RightMayFrame1, text="AirCondition \t\t", bg= "dark orange",onvalue = 1, offvalue = 0, variable=var6,
                    font=('arial',12,'bold')).grid(row=6, sticky=W)

chkInsuranceSold = Checkbutton(RightMayFrame1, text="Insurance Sold \t\t", bg= "dark orange",onvalue = 1, offvalue = 0, variable=var7,
                    font=('arial',12,'bold')).grid(row=7, sticky=W)

chkCustomerDetails = Checkbutton(RightMayFrame1, text="Customer Details \t\t", bg= "dark orange",onvalue = 1, offvalue = 0, variable=var8,
                    font=('arial',12,'bold')).grid(row=8 , sticky=W)


#**************************************************Rightmayframe2*******************************************************************************
txtReceipt=Text(RightMayFrame2, height=22, width=30, bg="white",bd=8,font=('arial',10, 'bold'))
txtReceipt.grid(row=0,column=0)


#*******************************************************************rightmasyframe2*************************************************************
DateofOrder.set(time.strftime("%d/%m/%Y"))
#****************************************************LeftmayFrame1************************************************************************************
lblCustomer = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="Customer",bd=16)
lblCustomer.grid(row=0,column=0,sticky=W)
txtCustomer = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12,width=28,textvariable=Customer,
                    justify='left')                       
txtCustomer.grid(row=0,column=1)

lblTitle = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="Title",bd=16)
lblTitle.grid(row=0,column=2,sticky=W)
txtTitle = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12,width=28, textvariable=Title,
                 justify='left')                       
txtTitle.grid(row=0,column=3)

lblFirstname = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="First name",bd=16)
lblFirstname.grid(row=0,column=4,sticky=W)
txtFirstname = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12,width=28, textvariable=Firstname,
                     justify='left')                       
txtFirstname.grid(row=0,column=5)


lblSurname = Label(LeftMayFrame1,font=('arial',10,'bold'), bg= "dark orange",text="Surname",bd=16)
lblSurname.grid(row=1,column=0,sticky=W)
txtSurname = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12,width=28,textvariable=Surname,
                   justify='left')                       
txtSurname.grid(row=1,column=1)


lblStreet = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="Street",bd=16)
lblStreet.grid(row=1,column=2,sticky=W)
txtStreet = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12,width=28, textvariable=Street,
                  justify='left')                        
txtStreet.grid(row=1,column=3)

lblArea = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="Area",bd=16)
lblArea.grid(row=1,column=4,sticky=W)
txtArea = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12, width=28,textvariable=Area,
                justify='left')                       
txtArea.grid(row=1,column=5)


lblPostCode = Label(LeftMayFrame1,font=('arial',10,'bold'), bg= "dark orange",text="Post Code",bd=16)
lblPostCode.grid(row=2,column=0,sticky=W)
txtPostCode = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12,  width=28,textvariable=PostCode,
                    justify='left')                      
txtPostCode.grid(row=2,column=1)

lblLicenceNo = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="Licence No",bd=16)
lblLicenceNo.grid(row=2,column=2,sticky=W)
txtLicenceNo = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12, width=28, textvariable=LicenceNo,
                     justify='left')                        
txtLicenceNo.grid(row=2,column=3)

lblPhoneNo = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="Phone No",bd=16)
lblPhoneNo.grid(row=2,column=4,sticky=W)
txtPhoneNo = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12, width=28, textvariable=PhoneNo,
                     justify='left')                        
txtPhoneNo.grid(row=2,column=5)

lblIssueBy = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="Issue By",bd=16)
lblIssueBy.grid(row=3,column=0,sticky=W)
txtIssueBy = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12, width=28, textvariable=IssueBy,
                   justify='left')                      
txtIssueBy.grid(row=3,column=1)


lblRegistrationNo = Label(LeftMayFrame1,font=('arial',10,'bold'), bg= "dark orange",text="Registration No",bd=16)
lblRegistrationNo.grid(row=3,column=2,sticky=W)
txtRegistrationNo = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12,width=28,textvariable=RegistrationNo,
                          justify='left')                        
txtRegistrationNo.grid(row=3,column=3)

lblDailyRentalRate = Label(LeftMayFrame1,font=('arial',10,'bold'),bg= "dark orange", text="Daily Rental Rate",bd=16)
lblDailyRentalRate.grid(row=3,column=4,sticky=W)
txtDailyRentalRate = Entry(LeftMayFrame1,font=('arial',10,'bold'), bd=12,width=28, textvariable=DailyRentalRate,
                           justify='left')                       
txtDailyRentalRate.grid(row=3,column=5)

#********************************************leftmayframe2**************************************************************88
lblEngineNo = Label(LeftMayFrame2,font=('arial',10,'bold'), bg= "dark orange",text="Engine No",bd=16)
lblEngineNo.grid(row=0,column=0,sticky=W)
txtEngineNo = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28, textvariable=EngineNo,
                      justify='left')                       
txtEngineNo.grid(row=0,column=1)

lblStyle = Label(LeftMayFrame2,font=('arial',10,'bold'),bg= "dark orange", text="Style",bd=16)
lblStyle.grid(row=0,column=2,sticky=W)
txtStyle = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28,textvariable=Style,
                        justify='left')
txtStyle.grid(row=0,column=3)

lblRegisteredYear = Label(LeftMayFrame2,font=('arial',10,'bold'),bg= "dark orange", text="Registered Year",bd=16)
lblRegisteredYear.grid(row=0,column=4,sticky=W)
txtRegisteredYear = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28, textvariable=RegisteredYear,
                          justify='left')                       
txtRegisteredYear.grid(row=0,column=5)


lblClassID = Label(LeftMayFrame2,font=('arial',10,'bold'), bg= "dark orange",text="Class ID",bd=16)
lblClassID.grid(row=1,column=0,sticky=W)
txtClassID = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28, textvariable=ClassID,
                   justify='left')                      
txtClassID.grid(row=1,column=1)


lblPlateNumber = Label(LeftMayFrame2,font=('arial',10,'bold'), bg= "dark orange",text="Plate Number",bd=16)
lblPlateNumber.grid(row=1,column=2,sticky=W)
txtPlateNumber = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28,textvariable=PlateNumber,
                          justify='left')                         
txtPlateNumber.grid(row=1,column=3)

lblMilesBefore = Label(LeftMayFrame2,font=('arial',10,'bold'),bg= "dark orange", text="Miles Before",bd=16)
lblMilesBefore.grid(row=1,column=4,sticky=W)
txtMilesBefore = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28,textvariable=MilesBefore,
                       justify='left')                       
txtMilesBefore.grid(row=1,column=5)


lblMilesAfter = Label(LeftMayFrame2,font=('arial',10,'bold'), bg= "dark orange",text="Miles After",bd=16)
lblMilesAfter.grid(row=2,column=0,sticky=W)
txtMilesAfter = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28, textvariable=MilesAfter,
                      justify='left')                      
txtMilesAfter.grid(row=2,column=1)

lblMake = Label(LeftMayFrame2,font=('arial',10,'bold'),bg= "dark orange", text="Make",bd=16)
lblMake.grid(row=2,column=2,sticky=W)
txtMake = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28,textvariable=Make,
                justify='left')                      
txtMake.grid(row=2,column=3)

lblModel = Label(LeftMayFrame2,font=('arial',10,'bold'),bg= "dark orange", text="Model",bd=16)
lblModel.grid(row=2,column=4,sticky=W)
txtModel = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28, textvariable=Model,
                 justify='left')
txtModel.grid(row=2,column=5)

lblEngineSize = Label(LeftMayFrame2,font=('arial',10,'bold'),bg= "dark orange", text="Engine Size",bd=16)
lblEngineSize.grid(row=3,column=0,sticky=W)
txtEngineSize= Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28, textvariable=EngineSize,
                      justify='left')                      
txtEngineSize.grid(row=3,column=1)


lblCarColour = Label(LeftMayFrame2,font=('arial',10,'bold'),bg= "dark orange", text="Car Colour",bd=16)
lblCarColour.grid(row=3,column=2,sticky=W)
txtCarColour = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28,textvariable=CarColour,
                     justify='left')                       
txtCarColour.grid(row=3,column=3)

lblCarInsurance = Label(LeftMayFrame2,font=('arial',10,'bold'), bg= "dark orange",text="Car Insurance",bd=16)
lblCarInsurance.grid(row=3,column=4,sticky=W)
txtCarInsurance = Entry(LeftMayFrame2,font=('arial',10,'bold'), bd=12,width=28, textvariable=CarInsurance,
                        justify='left')                       
txtCarInsurance.grid(row=3,column=5)

#*******************************************************LeftmayFrame3***************************************************88
lblCustomerID = Label(LeftMayFrame3,font=('arial',10,'bold'), bg= "dark orange",text="Customer ID",bd=16)
lblCustomerID.grid(row=0,column=0,sticky=W)
txtCustomerID = Entry(LeftMayFrame3,font=('arial',10,'bold'), bd=12,width=30,textvariable=CustomerID,
                      justify='left')                      
txtCustomerID.grid(row=0,column=1)

lblDaysRented = Label(LeftMayFrame3,font=('arial',10,'bold'),bg= "dark orange", text="Car Price",bd=16)
lblDaysRented.grid(row=0,column=2,sticky=W)
txtDaysRented = Entry(LeftMayFrame3,font=('arial',10,'bold'), bd=12,width=30, textvariable=DaysRented,
                      justify='left')                      
txtDaysRented.grid(row=0,column=3)

lblDiscount = Label(LeftMayFrame3,font=('arial',10,'bold'),bg= "dark orange", text="Discount",bd=16)
lblDiscount.grid(row=0,column=4,sticky=W)
txtDiscount = Entry(LeftMayFrame3,font=('arial',10,'bold'), bd=12,width=30,textvariable=Discount,
                    justify='left')                      
txtDiscount.grid(row=0,column=5)


lblNumberofDays = Label(LeftMayFrame3,font=('arial',10,'bold'), bg= "dark orange",text="Number of Days",bd=16)
lblNumberofDays.grid(row=1,column=0,sticky=W)
txtNumberofDays = Entry(LeftMayFrame3,font=('arial',10,'bold'), bd=12,width=30, textvariable=NumberofDays,
                        justify='left')
txtNumberofDays.grid(row=1,column=1)


lblInvoiceID = Label(LeftMayFrame3,font=('arial',10,'bold'),bg= "dark orange", text="Invoice ID", bd=16)
lblInvoiceID.grid(row=1,column=2,sticky=W)
txtInvoiceID = Entry(LeftMayFrame3,font=('arial',10,'bold'), bd=12,width=30,textvariable=InvoiceID,
                     justify='left')                       
txtInvoiceID.grid(row=1,column=3)

lblTotal = Label(LeftMayFrame3,font=('arial',10,'bold'),bg= "dark orange", text="Total", bd=16)
lblTotal.grid(row=1,column=4,sticky=W)
txtTotal = Entry(LeftMayFrame3,font=('arial',10,'bold'), bd=12,width=30, textvariable=Total,
                 justify='left')
                       
txtTotal.grid(row=1,column=5)
#****************************************************************buttons***************Leftmayframe4*****************************

btnTotal = Button(LeftMayFrame4, text='Total', padx=8, pady=8, bd=8, bg="tan",fg="black",
                  font=('arial',16,'bold'), width= 18, height=1,command=CarRentalCost).grid(row=0,column=0)

btnReceipt = Button(LeftMayFrame4, text='Receipt', padx=8, pady=8,bg="tan", bd=8, fg="black",
                  font=('arial',16,'bold'), width= 18, height=1,command = Receipt).grid(row=0,column=1)

btnReset = Button(LeftMayFrame4, text='Reset', padx=8, pady=8,bg="tan", bd=8, fg="black",
                  font=('arial',16,'bold'), width= 18, height=1,command = Reset).grid(row=0,column=2)

btnExit = Button(LeftMayFrame4, text='Exit', padx=8, pady=8, bd=8, bg="red",fg="black",
                  font=('arial',16,'bold'), width= 18, height=1,command=qExit).grid(row=0,column=3)




root.mainloop()
