import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',password='*****',database='sboutique')
mycur=mycon.cursor()
def space():
    for i in range(1):
                      print()                       
def addpro():
                n=int(input('enter no of items to insert  '))
                qry='select pro_id,pro_nam from products;'
                mycur.execute(qry)
                prolist=mycur.fetchall()
                pidl=[]
                pnl=[]
                for i in prolist:
                    pidl.append(i[0])
                    pnl.append(i[1])               
                for j in range(n):
                   t=()
                   proid=int(input('enter product no.  '))
                   if proid in pidl:
                      print('Product of this serial no already exists.......continue further from product no',pidl[-1])
                   else:
                    pnam=input('Name of product (id):  ')
                    pprice=input('price  ')
                    pstk=input('numbers In stock  ')
                    t=(proid,pnam,pprice,pstk)
                    print("PRODUCT ADDED")
                    qry='insert into products values(%s,%s,%s,%s);'
                    val=t
                    mycur.execute(qry,val)
                    mycon.commit()
def cust_ac():
                 print("TO CREATE YOUR OWN ACCOUNT,please enter the details..")
                 ask='Y'
                 qry='select cust_id from customer;'
                 mycur.execute(qry)
                 d=mycur.fetchall()
                 l=[]
                 for i in d:
                    l.append(i[0])
                 while ask in 'yY':
                        t=()
                        custid=int(input('Enter your customer id...   '))
                        if custid in l:
                             print ('This Customer Id already exists....Try creating a new one')
                        else:
                            cnam=input('First Name   ')
                            clnam=input('Last Name   ')
                            cphno=input('Phone Number   ')
                            cadrs=input('Your Address   ')
                            t=(custid,cnam,clnam,cphno,cadrs)
                            qry='insert into customer values(%s,%s,%s,%s,%s,NULL,NULL);'
                            val=t
                            mycur.execute(qry,val)
                            mycon.commit()
                            print('CUSTOMER DETAILS ENTERED') 
                            ask =input('do you want to continue ...........enter Y or N  ')
                            if ask not in  ('Y','y'):
                               space()
                               break
def addemp():
   n=[]
   ne=int(input('enter the no. of employees to add  '))
   for i in range(1,ne+1):
      t=()
      print('enter employee id(8 characters)  ')
      idd=int(input(str(i)+')    '))
      print('enter employee name  ')
      nam=input(str(i)+')    ')
      print('enter employee last name  ')
      lnam=input(str(i)+')    ')
      print('enter employee contact no.  ')
      conno=int(input(str(i)+')    '))
      print('enter employee adress  ')
      adrs=input(str(i)+')    ')
      t=t+(idd,nam,lnam,conno,adrs)
      n.append(t)
      print('EMPLOYEE '+str(i)+'DETAILS ADDED')
   print('ALL EMPLOYEE DETAILS ADDED !! ')
   qry='insert into employee values(%s,%s,%s,%s,%s);'
   for i in range(len(n)):
         val=n[i]
         mycur.execute(qry,val)
         mycon.commit()
   space()
def sign_in():
   try:
       print('  '*8+'''TO SIGN IN TO YOUR ACCOUNT .....
                          ENTER YOUR CUSTOMER ID''')
       ask=int(input('     id:   '))
       qry='select cust_id from customer;'
       mycur.execute(qry)
       d=mycur.fetchall()
       l=[]
       for i in d:
         l.append(i[0])
       if ask in l:
          print('NOW YOU ARE SIGNED IN TO YOUR ACCOUNT !!')
          while True:
                space()
                print(''' CHOOSE WHAT TO DO
                                                                                                 OR ENTER   "Back"  TO GO BACK......
                         1) Show Bookings
                         2)  Book a product
                         3)  Book an Appointment
                         4)  Update Self Details
                         5)  Cancel booked products or appointments
                         6)  Delete Account''')
                ccc=input('enter choice______     ')
                if ccc=='1':
                   qry2='select bkd_apmt  from customer where cust_id = %s;'
                   qry='select bkd_pro  from customer where cust_id = %s;'
                   val=(ask,)
                   mycur.execute(qry,val)
                   s =mycur.fetchone()
                   val2=(ask,)
                   mycur.execute(qry2,val2)
                   s2 =mycur.fetchone()
                   if s[0] is None:
                      print('you have not booked products yet')
                   else:
                     d=s[0].split('_')
                     print('Booked products')
                     for bkditems in d:
                        print('     ',bkditems)
                   if s2[0] is None:
                          print('you have not booked any appointments yet')
                   else:
                     dic={}
                     d2=s2[0].split('_')
                     try:
                          enam=()
                          for i in d2:  
                            qry='select e_nam from employee where emp_id =%s'
                            val=(i,)
                            mycur.execute(qry,val)
                            enam=enam+(mycur.fetchone(),)
                          print('You have booked appointments with ......')
                          for i in range (len(d2)):
                                 print(d2[i],enam[i][0])
                     except Exception:
                            print()
                elif ccc=='2':
                   qry='select pro_nam from products;'
                   mycur.execute(qry)
                   prolist=mycur.fetchall()
                   pl=[]
                   for i in prolist:
                      pl.append(i[0])
                   v=input('enter the product id to book products')
                   qt=input('enter the quantity')
                   if v in pl:
                      qry='select bkd_pro from customer where cust_id=%s;'
                      mycur.execute(qry,(ask,))
                      pr=mycur.fetchone()
                      prl=pr[0]
                      if prl is None:
                         qry='update customer set bkd_pro=%s where cust_id=%s;'
                         val=(v+'_',ask)
                         mycur.execute(qry,val)
                         mycon.commit()
                         print('Your Product is booked !!') 
                      else:
                         prl1=prl+v
                         qry2='update customer set bkd_pro=%s  where cust_id=%s;'
                         val2=(prl1+'_',ask)
                         mycur.execute(qry2,val2)
                         mycon.commit()
                         print('Your Product is booked !!') 
                   else:
                      print('This product does not exists...Please write the correct product id!!')   
                if ccc=='3':
                   qry='select emp_id,CONCAT(e_nam," ",e_lnam) as "Name of employee" from employee;'
                   mycur.execute(qry)
                   elist=mycur.fetchall()
                   print('The following is the list of members available to serve your purpose ---')
                   for i in elist:
                      print(i[0]," "*4,i[1])
                   v=input('enter the employee id to book Appointment  ')
                   qry='select bkd_apmt from customer where cust_id=%s;'
                   mycur.execute(qry,(ask,))
                   pr=mycur.fetchone()
                   prl=pr[0]
                   if prl is None:
                      qry='update customer set bkd_apmt=%s where cust_id=%s;'
                      val=(v+'_',ask)
                      mycur.execute(qry,val)
                      mycon.commit()
                      print('Your Appointment is booked !!')
                   else:
                      prl1=prl+v
                      qry2='update customer set bkd_apmt=%s  where cust_id=%s;'
                      val2=(prl1+'_',ask)
                      mycur.execute(qry2,val2)
                      mycon.commit()
                      print('Your Appointment is booked !!')
                if ccc=='4':
                           print('''HERE'S THE WAY TO UPDATE YOUR DETAILS
                                      YOUR EXISTING RECORD IS;''')
                           qry='select cust_id,c_nam,c_lnam,c_phno,c_adrs from customer where cust_id =%s'
                           mycur.execute(qry,(ask,))
                           clist=mycur.fetchone()
                           flds=['NAME','LAST NAME','PHONE NO.','ADDRESS']
                           dic={}
                           for i in range(4):
                                  dic[flds[i]]=clist[i+1]
                           updt=print('''enter the choice to update existing records
                                              1. NAME
                                              2. LAST NAME
                                              3. CONTACT NO.
                                              4.YOUR ADDRESS''')
                           for i in range(len(clist)):
                                 updtc=int(input('enter choice   '))
                                 print(updtc)
                                 upval=input('enter'+flds[updtc-1]+'   ')
                                 dic[flds[updtc-1]]=upval
                                 yn=input('Do you want to continue?? y or n  ')
                                 if yn in 'Nn':
                                        break
                           print('YOUR DETAILS ARE UPDATED ')
                           updtl=tuple(dic.values())+(ask,)
                           qry='update customer set c_nam=%s,c_lnam=%s,c_phno=%s ,c_adrs=%s where cust_id=%s;'
                           val=(updtl)
                           mycur.execute(qry,val)
                           mycon.commit()
                if ccc=='5':
                   try:
                       w=input('''TO CANCEL PRODUCTS ENTER,P or
TO CANCEL APPOINTMENTS ENTER ,AP........       ''')
                       if w in'pP':
                              qry='select bkd_pro from customer where cust_id=%s'
                              mycur.execute(qry,(ask,))
                              bp=mycur.fetchone()
                              bpl=bp[0]
                              print('YOUR BOOKING(/S)',bpl)
                              if bpl is None:
                                     print('you have no bookings to cancel')
                              else:
                                     print('''To cancel all products; enter A
       OR enter the product code to cancel.....   ''')
                                     cw=input('____   ')
                                     if cw in 'Aa':
                                            qry='update customer set bkd_pro=NULL where cust_id=%s'
                                            mycur.execute(qry,(ask,))
                                            mycon.commit()
                                            print('ALL BOOKINGS DELETED')
                                     elif cw in bpl:
                                            x=(bpl[0:-1]).split('_')
                                            x.remove(cw)
                                            print(x)
                                            st=''
                                            for i in x:
                                                   st=st+i+'_'
                                            print(st)
                                            qry='update customer set bkd_pro=%s where cust_id=%s'
                                            val=(st,ask)
                                            mycur.execute(qry,val)
                                            mycon.commit()
                                            print('DONE !!!')      
                       if w.lower()=='ap':
                              qry='select bkd_apmt from customer where cust_id=%s;'
                              mycur.execute(qry,(ask,))
                              bp=mycur.fetchone()
                              bpl=bp[0]
                              if bpl is None:
                                     print('You have no appointments')
                              else:
                                     print('Your booking(s):  ',bpl)
                                     print('''To cancel all appointments; enter A
       OR enter the employee code to cancel.....    ''')
                                     cw=input('___   ')
                                     if cw in 'Aa':
                                            qry='update customer set bkd_apmt=NULL where cust_id=%s'
                                            mycur.execute(qry,(ask,))
                                            mycon.commit()
                                            print('ALL APPOINTMENTS DELETED')
                                     elif cw in bpl:
                                            x=(bpl[0:-1]).split('_')
                                            x.remove(cw)
                                            st=''
                                            for i in x:
                                                   st=st+i+'_'
                                            qry='update customer set bkd_apmt=%s where cust_id=%s'
                                            val=(st,ask)
                                            mycur.execute(qry,val)
                                            mycon.commit()
                                            print('APPOINTMENT CANCELLED !!!')                      
                   except Exception:
                      print('Some Problem in Updating Your Details....Try Again')
                if ccc=='6':
                       print('WRITE YES IF YOU REALLY WANT TO DEACTIVATE YOUR ACCOUNT')
                       d_n=input('enter   : ')
                       if d_n.lower()=='yes':
                            qry ='delete from customer where cust_id=%s'
                            mycur.execute(qry,(ask,))
                            mycon.commit()
                            print('Account Deleted !!')
                if ccc.lower()=='back':
                   print("SUCCESSFULLY  LOGGED OUT")
                   print("THANKYOU BELOVED CUSTOMER FOR TRUSTING US ....WE HOPE YOU HAVE A HAPPY DAY")
                   space()
                   break 
       else:
            print('This Account does not exist.....')
   except Exception:
          print('Some error occured!! try later')
def emp_sign_in():
    try:   
       print('ENTER YOUR EMPLOYEE ID TO SIGN IN TO YOUR ACCOUNT')
       ask=input('____   ')
       qry='select emp_id from employee;'
       mycur.execute(qry)
       d=mycur.fetchall()
       lis=[]
       for i in d:
         lis.append(i[0])
       if ask in lis:
          print('NOW YOU ARE SIGNED IN TO YOUR ACCOUNT !!')
          while True:
                space() 
                print(''' CHOOSE WHAT TO DO:                                                        OR ENTER "Back" TO GO BACK
                         1)Update delivered records or attented appointments
                         2.)Check Today's bookings and appointments''')
                ccc=input('enter choice   ')
                if ccc=='1':
                       print('''To update delivered records:
                                   Type:  A
To update attended appointments:
                                   Type:  B''')
                       c1=input('enter...   ')
                       if c1 in 'Aa':
                              k=input('enter customer id')
                              qry='select bkd_pro from customer where cust_id=%s;'
                              mycur.execute(qry,(k,))
                              bp=mycur.fetchone()
                              bpl=bp[0]
                              if bpl is None:
                                     print('no bookings')
                              else:
                                     print('All booking(s):  ',bpl)
                                     cw=input('enter product code to cancel the delivered product   ')
                                     if cw in bpl:
                                            x=(bpl[0:-1]).split('_')
                                            x.remove(cw)
                                            st=''
                                            for i in x:
                                                   st=st+i+'_'
                                            qry='update customer set bkd_pro=%s where cust_id=%s;'
                                            val=(st,k)
                                            mycur.execute(qry,val)
                                            mycon.commit()
                                            print('DELETED.....')
                                            qry2='update products set pro_stk=pro_stk -1 where pro_nam=%s;'
                                            mycur.execute(qry2,(cw,))
                                            mycon.commit()
                                     else:
                                          print('enter the correct code')
                       if c1 in 'Bb':
                         k=int(input('enter customer id'))
                         qry='select bkd_apmt from customer where cust_id=%s;'
                         mycur.execute(qry,(k,))
                         bp=mycur.fetchone()
                         bpl=bp[0]
                         if bpl is None:
                                     print("You don't have any appointments with this customer ")
                         elif str(ask) in bpl:
                                            x=(bpl[0:-1]).split('_')
                                            x.remove(str(ask))
                                            st=''
                                            for i in x:
                                                   st=st+i+'_'
                                            qry='update customer set bkd_apmt=%s where cust_id=%s;'
                                            val=(st,k)
                                            mycur.execute(qry,val)
                                            mycon.commit()
                                            print('APPOINTMENT CANCELLED !!!')
                                     
                elif ccc=='2':
                 qry='select cust_id from customer;'
                 mycur.execute(qry)
                 d=mycur.fetchall()
                 l=[]
                 for i in d:
                    l.append(i[0])
                 datalist=[]
                 dataid=[]
                 for j in l:
                    query='select bkd_apmt from customer where cust_id=%s;'
                    value=(j,)
                    mycur.execute(query,value)
                    data=mycur.fetchone()
                    if data[0] is None:
                       m=''
                    else:
                      if ask in data[0]:
                             listt=data[0].split('_')
                             que='select cust_id,c_nam from customer where cust_id=%s;'
                             mycur.execute(que,(j,))
                             data2=mycur.fetchone()
                             datalist.append(data2[1])
                             dataid.append(data2[0])
                      else:
                          n=''
                 if datalist ==[]:
                    print('You have no bookings with any customer')
                 else:
                    print('''You have bookings with customers''')
                    for f in range(len(datalist)):
                      print(datalist[f],'with id',dataid[f])
                elif ccc.lower()=='back':
                   print("SUCCESSFULLY  LOGGED OUT")
                   break
                  
       else:
            print('Enter the correct id')                         
    except Exception:
           print('Give the right ,required input')
    
def employer():
 while True:
   print()
   print('''Enter Your Choice:                                                     OR ENTER "Back" TO GO BACK
                    1)View and Update Product Details
                    2)Add a New Product
                    3)Add  a New Employee
                    4)Remove an Employee''')
   ccc=input('Enter _____  ')
   if ccc=='1':
                       qry='select * from products;'
                       mycur.execute(qry)
                       d=mycur.fetchall()
                       dic={}
                       for i in d:
                              dic[i[0]]=i[1:]
                       print('_'*80)
                       print ("{:<17} {:<22} {:<23} {:<19}".format('Product id','Product name(A)','Price(B)','Stock(C)'))
                       print('_'*80)
                       for k, v in dic.items():
                            a, b, c = v
                            print ("{:<17} {:<22} {:<23} {:<19}".format(k, a, b, c))
                       print('_'*80)
                       print('DO YOU WANT TO UPDATE ,ENTER YES ......')
                       ccc_1=input('----  ')
                       try:
                              if ccc_1.lower() =='yes':
                                     ccc_3=int(input('enter product id...  '))
                                     ccc_2=input('Enter the name of field to update:   ')
                                     if ccc_2 in'Aa':
                                            ccc_4=input('enter new name   ')
                                            qry1='select pro_nam from products ;'
                                            mycur.execute(qry1)
                                            names=mycur.fetchall()
                                            nam=[]
                                            for i in names:
                                                    nam.append(i[0])
                                            if ccc_4 in nam:
                                                   print('this product name already exists...try giving another one')
                                            else:
                                                   qry2='update products set pro_nam=%s where pro_id=%s;'
                                                   val=(ccc_4,ccc_3)
                                                   mycur.execute(qry2,val)
                                                   mycon.commit()
                                                   print('UPDATION EXECUTED')
                                     elif ccc_2 in'Bb':
                                            ccc_4=input('enter new price  ')
                                            qry='update products set pro_price=%s where pro_id=%s;'
                                            val=(ccc_4,ccc_3)
                                            mycur.execute(qry,val)
                                            mycon.commit()
                                            print('UPDATION EXECUTED')
                                     elif ccc_2 in'Cc':
                                            ccc_4=input('enter new stock  ')
                                            qry='update products set pro_stk=%s where pro_id=%s;'
                                            val=(ccc_4,ccc_3)
                                            mycur.execute(qry,val)
                                            mycon.commit()
                                            print('UPDATION EXECUTED')                            
                       except Exception:
                             print('Give the right ,required input')
   elif ccc=='2':
      addpro()
   elif ccc=='3':
      addemp()
   elif ccc=='4':
                   qry='select emp_id,CONCAT(e_nam," ",e_lnam) as "Name of employee" from employee;'
                   mycur.execute(qry)
                   elist=mycur.fetchall()
                   print('The following is the list of employees ')
                   for i in elist:
                      print(i[0]," "*4,i[1])
                   y_n=input('Do You Really want to Remove Employee?....enter yes or no')
                   if y_n.lower()=='yes':
                     ans=input('Enter Employee Code')
                     qry='delete from employee where emp_id=%s;'
                     mycur.execute(qry,(ans,))
                     mycon.commit()
                     print('Employee Details Removed')
                   else:
                      print()
   if ccc.lower()=="back":
      break
print('WELCOME !!!')
while True:
   print(''' PLEASE SELECT YOUR CHOICE TO ENTER AS                                                    enter  "exit" to leave the program
   (A).CUSTOMER
   (B).EMPLOYEE
   (C).EMPLOYER''')
   Q=input('Enter...    ')
   try:
       if Q in 'aA':
           print('DEAR CUSTOMER.......WE WELCOME YOU WITH DEEPEST GRATITUDE !!!')
           print('''Select what to do----
       1]Create Account
       2]Sign In into existing account''')
           q=input('enter-   ')
           if q =='1':
                 cust_ac()
           elif q=='2':
               sign_in()
           else:
               print('Enter correct choice')
       if Q in 'bB':
           print("DEAR EMPLOYEE.......HERE'S HOW TO GET STARTED !!!")
           emp_sign_in()
       if Q in 'cC':
           print('MOST WELCOME .......')
           employer()
       elif Q.lower()=="exit":
          print("THANKYOU FOR VISITING !! HAVE A FRUITFUL DAY !! ")
          break   
   except Exception:
       print('Give the right input')
   space()
