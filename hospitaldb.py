import sqlite3

class Hpdatabase:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.c=self.con.cursor()
        self.c.execute(
        """
        CREATE TABLE IF NOT EXISTS hospitaltwo(
           id INTEGER PRIMARY KEY ,
           fname TEXT NOT NULL,
           lname TEXT NOT NULL,
           gender TEXT NOT NULL,
           dob INTEGER NOT NULL,
           phone INTEGER NOT NULL,
           date TEXT NOT NULL
            
        )
        """
        )
        self.c.execute(
        """
        CREATE TABLE IF NOT EXISTS adddoctors(
            pid INTEGER PRIMARY KEY,
            id INTEGER NOT NULL,
            fname TEXT NOT NULL,
            Lname TEXT NOT NULL,
            specallist TEXT NOT NULL,
            phone INTEGER NOT NULL,
            email TEXT NOT NULL
            
            
        )
        """
        )
        self.con.commit()
        
        self.c.execute("""
                       
              CREATE TABLE IF NOT EXISTS appoinments(
                  pid INTEGER PRIMARY KEY,
                  id INTEGER NOT NULL,
                  date TEXT NOT NULL,
                  time TEXT NOT NULL,
                  reasione TEXT NOT NULL,
                  pations TEXT NOT NULL,
                  doctor TEXT NOT NULL
                  
                  
                  
              )         
                       
                       """)
        self.con.commit()
        
        self.c.execute("""
               CREATE TABLE IF NOT EXISTS bills(
                   pid INTEGER PRIMARY KEY,
                   id INTEGER NOT NULL,
                   pationt TEXT NOT NULL,
                   date TEXT NOT NULL,
                   description TEXT NOT NULL,
                   amount INTEGER NOT NULL
                   
                   
               )        
                       """)
    def insert(self,fname,lname,gender,dob,phone,date):
        sql="""
        INSERT INTO  hospitaltwo VALUES(NULL,?,?,?,?,?,?)
        """
        self.c.execute(sql,(fname,lname,gender,dob,phone,date))
        self.con.commit()
    def select(self):
        self.c.execute("SELECT * FROM hospitaltwo") 
        return self.c.fetchall()  
    def updates(self,id,fname,lname,gender,dob,phone,date,pid):
        sql="""
        UPDATE hospitaltwo set id=?,fname=?,lname=?,gender=?,dob=?,phone=?,date=? WHERE id=?
        """ 
        self.c.execute(sql,(id,fname,lname,gender,dob,phone,date,pid))
        self.con.commit()
    def insertdoc(self,id,fname,lname,specallist, phone, email):
        sql="""
        INSERT INTO adddoctors VALUES(NULL,?,?,?,?,?,?) 
        """
        self.c.execute(sql,(id,fname,lname,specallist, phone, email))  
        self.con.commit() 
    def show_doc(self):
        self.c.execute("SELECT * FROM adddoctors")
        return self.c.fetchall()
    def updatedoc(self,id,fname,lname,specallist, phone, email,ids):
        sql="""
        UPDATE adddoctors set id=?,fname=?,lname=?,specallist=?, phone=?, email=? WHERE id=?
        """
        self.c.execute(sql,(id,fname,lname,specallist, phone, email,ids))
        self.con.commit()
    def inserapplication_detai(self,id,date,time,reasione,pations,doctor):
        sql="""
        INSERT INTO appoinments VAlUES(NULL,?,?,?,?,?,?)
        """  
        self.c.execute(sql,(id,date,time,reasione,pations,doctor))
        self.con.commit()  
    def fetchappoinmets(self):
        self.c.execute("SELECT * FROM  appoinments ") 
        return self.c.fetchall() 
    
    def billinsert(self,id,pationt,date,description,amout):
        sql="""
        INSERT INTO bills VALUES(NULL,?,?,?,?,?)
        """
        self.c.execute(sql,(id,pationt,date,description,amout))
        self.con.commit() 
    def fetchbill(self):
        self.c.execute("SELECT * FROM bills ") 
        return self.c.fetchall()    