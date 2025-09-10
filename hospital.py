from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
from hospitaldb import Hpdatabase
class ui_contents(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("hospital managent system")
        self.geometry("1000x500")
        self.ui()
        self.krish=Hpdatabase("hospitalrecordnew.db")
       
      
      
       
    def ui(self):
        
        
        nb=ttk.Notebook(self)
        nb.pack(fill="both",expand=True)
        
        self.pationts=tk.Frame(nb,bg="lightgreen")
        nb.add(self.pationts,text="Pationts")
        
        self.doctor=tk.Frame(nb)
        nb.add(self.doctor,text="Docter")
        
        self.applications=tk.Frame(nb)
        nb.add(self.applications,text="Application")
        
        self.biilling=tk.Frame(nb)
        nb.add(self.biilling,text="Billing")
      
        self.pationst_details()
        self.doctor_ui()
        self.applications_farm() 
        self.pre_billings()
    
        
      
    def pationst_details(self):
        frm=Frame(self.pationts)
        frm.pack(fill="x")
        
        name=Label( frm,text="Fname",font=("times",10,"bold"))
        name.grid(row=0,column=0)
        efname=Entry(frm,font=("times",10,"bold"))
        efname.grid(row=0,column=1,pady=10) 
        
        lname=Label(frm,text="Lname",font=("times",10,"bold")) 
        lname.grid(row=0,column=2)
        elname=Entry(frm,font=("times",10,"bold"))
        elname.grid(row=0,column=3,pady=10)
        
        lgender=Label(frm,text="Gender",font=("times",10,"bold"))
        lgender.grid(row=0,column=4)
        self.gender=ttk.Combobox(frm,values=("male","female"),state="readonly")
        self.gender.grid(row=0,column=5,pady=10)
        
        doblbl=Label(frm,text="DOB(yyyy-mm-dd)",font=("times",10,"bold"))
        doblbl.grid(row=1,column=0,pady=10,padx=20)
        endob=Entry(frm,font=("times",10,"bold"))
        endob.grid(row=1,column=1,pady=10)
        
        lphon=Label(frm,text="Phone",font=("times",10,"bold"))
        lphon.grid(row=1,column=2)
        ephone=Entry(frm,font=("times",10,"bold"))
        ephone.grid(row=1,column=3,pady=10)
        def save():
            selected_gender = self.gender.get() 
            today=datetime.now().strftime("%d/%m/%y,%H:%M:%S")
            id=len(mytree.get_children())+1
            mytree.insert("","end",values=(id,efname.get(), elname.get(), selected_gender,endob.get(),ephone.get(), today))
            self.krish=Hpdatabase("hospitalrecord.db")
            self.krish.insert(efname.get(), elname.get(), selected_gender,endob.get(),ephone.get(), today)
            efname.delete(0,END)
            elname.delete(0,END)
            self.gender.delete(0,END)
            endob.delete(0,END)
            ephone.delete(0,END)
        def show(event):
            efname.delete(0,END)
            elname.delete(0,END)
            self.gender.delete(0,END)
            endob.delete(0,END)
            ephone.delete(0,END)
            id=mytree.focus()
            value=mytree.item(id,"values")
            efname.insert(0,value[1])
            elname.insert(0,value[2])
            self.gender.insert(0,value[3])
            endob.insert(0,value[4])
            ephone.insert(0,value[5])
        def update():
            today=datetime.now().strftime("%d/%m/%y,%H:%M:%S")
            id=mytree.focus()[3]
            val=mytree.focus()
            selected_gender = self.gender.get() 
            mytree.item(val,values=(id,efname.get(), elname.get(),  selected_gender,endob.get(),ephone.get(),today))
            self.krish=Hpdatabase("hospitalrecord.db")
            self.krish.updates(id,efname.get(), elname.get(), selected_gender,endob.get(),ephone.get(),today,id)
            efname.delete(0,END)
            elname.delete(0,END)
            self.gender.delete(0,END)
            endob.delete(0,END)
            ephone.delete(0,END)
            
        
        savebtn=Button(frm,text="Save",font=("times",10,"bold"),width=10,command=save)
        
        savebtn.grid(row=1,column=4,padx=10)
        
        updatebtn=Button(frm,text="Update",font=("times",10,"bold"),width=10,command=update)
        
        updatebtn.grid(row=1,column=5,padx=10)
      
        treefrm=Frame(self.pationts)
        treefrm.pack(side=LEFT,fill="both",expand=True)
       
       
        
        mytree=ttk.Treeview( treefrm)
        mytree['columns']=("ID","Fname","lname","Gender","DOB","Phone","Created")
        mytree.column("#0",width=0,stretch=NO)
        mytree.column("#1",width=150)
        mytree.column("#2",width=150)
        mytree.column("#3",width=150)
        mytree.column("#4",width=150)
        mytree.column("#5",width=150)
        mytree.column("#6",width=150)
        mytree.column("#7",width=150)
        
        mytree.heading("#0",text="")
        mytree.heading("#1",text="ID")
        mytree.heading("#2",text="Fname")
        mytree.heading("#3",text="Lname")
        mytree.heading("#4",text="Gender")
        mytree.heading("#5",text="DOB")
        mytree.heading("#6",text="Phone")
        mytree.heading("#7",text="Created")
        v_scrolbar=ttk.Scrollbar(treefrm,orient="vertical",command=mytree.yview)
        y_scrolbar=ttk.Scrollbar(treefrm,orient="horizontal",command=mytree.xview)
        
        mytree.configure(yscrollcommand=v_scrolbar.set)
      
        
        mytree.pack(side=tk.LEFT,fill="both",expand=True)
        v_scrolbar.pack(side=tk.RIGHT,fill="y")
        mytree.bind("<ButtonRelease-1>",show)
        self.krish=Hpdatabase("hospitalrecord.db")
        value= self.krish.select()
        for i in value:
            id,fname,lname,gender,dob,phone,date=i
            mytree.insert("","end",values=(id,fname,lname,gender,dob,phone,date))
            
    def doctor_ui(self):
        frm=Frame(self.doctor)
        frm.pack(fill="x")
        
        lid=Label(frm,text="ID",font=("times",10,"bold"))
        lid.grid(row=1,column=0,padx=10)
        eid=Entry(frm,font=("times",10,"bold"))
        eid.grid(row=1,column=1)
        
        lfname=Label(frm,text="Fname",font=("times",10,"bold"))
        lfname.grid(row=1,column=2,padx=10)
        efname=Entry(frm,font=("times",10,"bold"))
        efname.grid(row=1,column=3)
        
        lname=Label(frm,text="Lname",font=("times",10,"bold"))
        lname.grid(row=1,column=4,padx=10)
        elname=Entry(frm,font=("times",10,"bold"))
        elname.grid(row=1,column=5)
        
        lspl=Label(frm,text="Specalist",font=("times",10,"bold"))
        lspl.grid(row=1,column=6,padx=10)
        self.espls=Entry(frm,font=("times",10,"bold"))
        self.espls.grid(row=1,column=7)
        
        lphone=Label(frm,text="Phone",font=("times",10,"bold"))
        lphone.grid(row=2,column=0,padx=10)
        self.ephone=Entry(frm,font=("times",10,"bold"))
        self.ephone.grid(row=2,column=1,pady=10)
        
        lspl=Label(frm,text="email",font=("times",10,"bold"))
        lspl.grid(row=2,column=2,padx=10,pady=10)
        self.email=Entry(frm,font=("times",10,"bold"))
        self.email.grid(row=2,column=3,pady=10)
        
        
        def adddoctot():
            mytree.insert("","end",values=( eid.get(),efname.get(), elname.get(),self.espls.get(), self.ephone.get(), self.email.get()))
            self.krish=Hpdatabase("hospitalrecord.db")
            self.krish.insertdoc(eid.get(),efname.get(), elname.get(),self.espls.get(),self. ephone.get(),self. email.get())
            eid.delete(0,END)
            efname.delete(0,END)
            elname.delete(0,END)
            self.espls.delete(0,END)
            self.ephone.delete(0,END)
            self.email.delete(0,END)
        
        def show(event):
            
            
            id=mytree.focus()
            values=mytree.item(id,"values")
            eid.insert(0,values[0])
            efname.insert(0,values[1])
            elname.insert(0,values[2])
            self.espls.insert(0,values[3])
            self.ephone.insert(0,values[4])
            self.email.insert(0,values[5])
        def upsatedoctor():
            id=mytree.focus()
            val=mytree.focus()[3]
            mytree.item(id,values=( eid.get(),efname.get(), elname.get(),self.espls.get(), self.ephone.get(), self.email.get()))
            self.krish=Hpdatabase("hospitalrecord.db")
            self.krish.updatedoc(eid.get(),efname.get(), elname.get(),self.espls.get(), self.ephone.get(), self.email.get(),val)
            eid.delete(0,END)
            efname.delete(0,END)
            elname.delete(0,END)
            self.espls.delete(0,END)
            self.ephone.delete(0,END)
            self.email.delete(0,END)
            
         
         
            
            
            
        adddoc=Button(frm,text="Add doctor",font=("times",10,"bold"),command=adddoctot)
        adddoc.grid(row=2,column=4,padx=10,pady=10)
            
        updatedoc=Button(frm,text="Update doctor",font=("times",10,"bold"),command=upsatedoctor)
        updatedoc.grid(row=2,column=5,pady=10)
        treefrm=Frame(self.doctor)
        treefrm.pack(side=LEFT,fill="both",expand=True,pady=10)
        mytree=ttk.Treeview(treefrm)
        mytree['columns']=('id','fname','lname','specilization','phone','email')
        mytree.column("#0",width=0,stretch=NO)
        mytree.column("#1",width=150)
        mytree.column("#2",width=150)
        mytree.column("#3",width=150)
        mytree.column("#4",width=150)
        mytree.column("#5",width=150)
        mytree.column("#6",width=150)
      
        
        mytree.heading("#0",text="")
        mytree.heading("#1",text="ID")
        mytree.heading("#2",text="fname")
        mytree.heading("#3",text="lname")
        mytree.heading("#4",text="specilization")
        mytree.heading("#5",text="phone")
        mytree.heading("#6",text="email")
        mytree.bind("<ButtonRelease-1>",show)
        
        self.krish=Hpdatabase("hospitalrecord.db")
        value= self.krish.show_doc()
        for i in value:
            pid,id,fname,lname,espls, ephone, email=i
            mytree.insert("","end",values=(id,fname,lname,espls, ephone, email))
        
        
        y_scrolbar=ttk.Scrollbar(treefrm,orient="vertical",command=mytree.yview)
        mytree.configure(yscrollcommand=y_scrolbar.set)
        
        mytree.pack(side=tk.LEFT,fill="both",expand=True)
        y_scrolbar.pack(side=tk.RIGHT,fill="y")
    def applications_farm(self):
        frm=Frame(self.applications) 
        frm.pack(fill="x") 
        pationt=Label(frm,text="pationts",font=("times",15,"bold"))
        pationt.grid(row=0,column=0)
        
        self.krish=Hpdatabase("hospitalrecord.db")
        values=self.krish.select()
        
        value=list(set(i[1] for i in values)) 
        
        pations=ttk.Combobox(frm,font=("times",10,"bold"))
        pations['values']=value  
        pations.grid(row=0,column=1)
        
        dooctor=Label(frm,text="Doctor",font=("times",15,"bold"))
        dooctor.grid(row=0,column=2)
    
        self.krish=Hpdatabase("hospitalrecord.db")
        values=self.krish.show_doc()
        
        value=list(set(i[2] for i in values)) 
        
        doctors=ttk.Combobox(frm,font=("times",10,"bold"))
        doctors['values']=value  
        doctors.grid(row=0,column=3)
        
        date=Label(frm,text="Time HH:MM",font=("times",10,"bold"))
        date.grid(row=0,column=4,padx=4)
        datee=Entry(frm,font=("times",10,"bold"))
        datee.grid(row=0,column=5,padx=4)
        time=Label(frm,text="Date YYYY-MM-DD",font=("times",10,"bold"))
        time.grid(row=0,column=6,padx=4)
        timee=Entry(frm,font=("times",10,"bold"))
        timee.grid(row=0,column=7,padx=4)
        def create_appoinment():
            id=len(mytree.get_children())+1
            mytree.insert("","end",values=(id, datee.get(), timee.get(), reasione.get(),pations.get(),  doctors.get()))
            self.krish=Hpdatabase("hospitalrecord.db")
            self.krish.inserapplication_detai(id, datee.get(), timee.get(), reasione.get(),pations.get(),  doctors.get())
        reasion=Label(frm,text="Reasion",font=("times",10,"bold"))
        reasion.grid(row=1,column=0,padx=4)
        reasione=Entry(frm,font=("times",10,"bold"))
        reasione.grid(row=1,column=1,pady=10,padx=4)
        
        create=Button(frm,text="Create",font=("times",10,"bold"),command=create_appoinment)
        create.grid(row=1,column=2,padx=4)
        
        treefrm=Frame(self.applications)
        treefrm.pack(side=LEFT,fill="both",expand=True)
        mytree=ttk.Treeview(treefrm)
        mytree['column']=("ID","Date","Time","Reasion","patient","Doctor")
        mytree.column("#0",width=0)
        mytree.column("#1",width=150)
        mytree.column("#2",width=150)
        mytree.column("#3",width=150)
        mytree.column("#4",width=150)
        mytree.column("#5",width=150)
        mytree.column("#6",width=150)
        
        mytree.heading("#0",text="")
        mytree.heading("#1",text="ID")
        mytree.heading("#2",text="Data")
        mytree.heading("#3",text="Time")
        mytree.heading("#4",text="Reasion")
        mytree.heading("#5",text="patient")
        mytree.heading("#6",text="Doctor")
        yscrolbar=ttk.Scrollbar(treefrm,orient="vertical",command=mytree.yview)
        mytree.configure(yscrollcommand=yscrolbar.set)
        mytree.pack(side=tk.LEFT,fill="both",expand=True)
        
        yscrolbar.pack(side=tk.RIGHT,fill="y")
        
        self.krish=Hpdatabase("hospitalrecord.db")
        values=self.krish.fetchappoinmets()
        for i in values:
           pid,id,time,date,rasion,pation,Doctor=i
           mytree.insert("","end",values=(id,time,date,rasion,pation,Doctor))
    def pre_billings(self):
        frm=Frame(self.biilling)
        frm.pack(fill="x") 
        
        def addcharge():
            id=len(mytree.get_children())+1
            mytree.insert("","end",values=(id,epation.get(),edates.get(), edes.get(),eamout.get()))
              
            self.krish=Hpdatabase("hospitalrecord.db")
            self.krish.billinsert(id,epation.get(),edates.get(), edes.get(),eamout.get())
            epation.delete(0,END)
            edates .delete(0,END)
            edes.delete(0,END)
            eamout.delete(0,END)
        
        pation=Label(frm,text="Pationts",font=("times",10,"bold")) 
        pation.grid(row=0,column=0)
        
        self.krish=Hpdatabase("hospitalrecord.db")
        values=self.krish.show_doc()
        
        value=list(set(i[2] for i in values))  
        
        epation=ttk.Combobox(frm,font=("times",10,"bold"))
        epation['values']=value
        epation.grid(row=0,column=1) 
        
        date=Label(frm,text="Date YYYY-MM-DD",font=("times",10,"bold")) 
        date.grid(row=0,column=2,padx=3)
        
        edates=Entry(frm,font=("times",10,"bold"))
        edates.grid(row=0,column=3,padx=3)
        
        amout=Label(frm,text="Amount",font=("times",10,"bold"))
        amout.grid(row=0,column=4,padx=3)
        
        eamout=Entry(frm,font=("times",10,"bold"))
        eamout.grid(row=0,column=5,padx=3)
        
        description=Label(frm,text="Description",font=("times",10,"bold"))
        description.grid(row=0,column=6,padx=3)
        
        edes=Entry(frm,font=("times",10,"bold"))
        edes.grid(row=0,column=7,padx=3)
        
        addchard=Button(frm, text="Add Charge",font=("times",10,"bold"),command=addcharge)
        addchard.grid(row=0,column=8)
        
        treefrm=Frame(self.biilling)
        treefrm.pack(side=LEFT,fill="both",expand=True,pady=10)
        
        mytree=ttk.Treeview(treefrm)
        mytree['column']=("id","pationt","date","descriptin","amout")
        mytree.column("#0",width=0,stretch=NO)
        mytree.column("#1",width=150)
        mytree.column("#2",width=150)
        mytree.column("#3",width=150)
        mytree.column("#4",width=150)
        mytree.column("#5",width=150)
        
        
        mytree.heading("#0",text="")    
        mytree.heading("#1",text="ID")    
        mytree.heading("#2",text="Pationt")    
        mytree.heading("#3",text="Date")    
        mytree.heading("#4",text="Description")    
        mytree.heading("#5",text="Amout")
        
        yscrolbar=ttk.Scrollbar(treefrm,orient="vertical",command=mytree.yview)
        mytree.configure(yscrollcommand=yscrolbar.set)
        
        mytree.pack(side=tk.LEFT,fill="both",expand=True)  
        yscrolbar.pack(side=tk.RIGHT,fill="y")  
        
        self.krish=Hpdatabase("hospitalrecord.db")
        values=self.krish.fetchbill() 
        for i in values:
            pid,id,pationt,date,description,amount=i
            mytree.insert("","end",values=(id,pationt,date,description,amount))
           
            
                    
kri=ui_contents()
kri.mainloop()
