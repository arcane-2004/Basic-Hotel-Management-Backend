import mysql.connector as mc

con = mc.connect(host="localhost", user="root", passwd = "mysql")
cursor = con.cursor()

# creating database
cursor.execute('create database if not exists Hotel_Management')
cursor.execute('Use Hotel_Management')
# creating Table

H1,H2,H3,H4,H5 = [],[],[],[],[]

# Hotel1
t1 = "create table if not exists Budget (Customer_Name char(30), Phone_Number varchar(10), Room_Number int(5) " \
     "Not Null Primary key , Address Varchar(50) Not Null, Checkin_Date varchar(10) , Checkin_Time varchar(10),Price int(5))"

cursor.execute(t1)

# Hotel2
t2 = "create table if not exists Economy (Customer_Name char(30), Phone_Number varchar(10), Room_Number int(5) " \
     "Not Null Primary key , Address Varchar(50) Not Null,Checkin_Date varchar(10),Checkin_Time varchar(10),Price int(5))"
cursor.execute(t2)

# Hotel3
t3 = "create table if not exists Elite (Customer_Name char(30), Phone_Number varchar(10), Room_Number int(5) " \
     "Not Null Primary key , Address Varchar(50) Not Null,Checkin_Date varchar(10),Checkin_Time varchar(10),Price int(5))"
cursor.execute(t3)

# Hotel4
t4 = "create table if not exists Royal (Customer_Name char(30), Phone_Number varchar(10), Room_Number int(5) " \
     "Not Null Primary key , Address Varchar(50) Not Null,Checkin_date varchar(20),Checkin_Time varchar(10),Price int(5))"
cursor.execute(t4)

# Hotel5
t5 = "create table if not exists Ultra_Royal (Customer_Name char(30), Phone_Number varchar(10), Room_Number int(5) " \
     "Not Null Primary key , Address Varchar(50) Not Null,Checkin_Date varchar(20),Checkin_Time varchar(10),Price int(5))"
cursor.execute(t5)

# History
t6 = "create table if not exists History (Customer_Name char(30), Phone_Number varchar(10), Room_Number int(5), " \
     " Address Varchar(50) Not Null,Checkin_Date varchar(20),Checkin_Time varchar(10), Price int(5)," \
     "Room_Type char(15) ,Checkout_Date varchar(20) default null )"
cursor.execute(t6)

## Inserting values in list--------------------------------------
cursor.execute("create table if not exists H1 (Room int(5))")
cursor.execute("create table if not exists H2 (Room int(5))")
cursor.execute("create table if not exists H3 (Room int(5))")
cursor.execute("create table if not exists H4 (Room int(5))")
cursor.execute("create table if not exists H5 (Room int(5))")

cursor.execute("select* from H1")
d = cursor.fetchall()
for j in d:
    H1.append(j[0])

cursor.execute("select* from H2")
d = cursor.fetchall()
for j in d:
    H2.append(j[0])

cursor.execute("select* from H3")
d = cursor.fetchall()
for j in d:
    H3.append(j[0])

cursor.execute("select* from H4")
d = cursor.fetchall()
for j in d:
    H4.append(j[0])

cursor.execute("select* from H5")
d = cursor.fetchall()
for j in d:
    H5.append(j[0])

## Giving choise

def list():
    print('We have the following rooms for you!!!!!!!')
    print('1. Budget          ----> Rs. 850\n'
          '2. Economy         ----> Rs. 2000\n'
          '3. Elite           ----> Rs. 5500\n'
          '4. Royal           ----> Rs. 7100\n'
          '5. Ultra Royal     ----> Rs. 10000\n'
          '6. Quit')
    print()

ask = 'y'
while ask == 'y' or ask == 'Y':
    ask1 = 'y'
    while ask1 == 'y' or ask1 == 'Y':

        print("                        Hotel Pradise Inn                               ")
        print('                       -------------------                           ')
        print()
        print('1. Checkin                2. Checkout              3.Checkin History')
        print('----------------------------------------------------------------------')
        print()
        che = True
        while che:
            use = input('Enter your choice (1,2,3): ')
            if use not in ('1','2','3'):
                print('Choise Invalid.....Please choose again: ')
            else:
                che = False
                use = int(use)

    ## Checkin-------------------------------------------------------

        if use == 1:

            che = True
            while che:
                list()
                print()
                user = input('Chooses Your Room Type (1,2,3,4,5,6): ')
                if user not in ('1', '2', '3', '4', '5', '6'):
                    print('Choise Invalid.....Please choose again: ')
                else:
                    che = False
                    user = int(user)
            if user == 1:
                h = H1
                H = 'H1'
                n = 25
                p = 850
                hotel = 'Budget'
                ask2 = 'n'
            elif user == 2:
                h = H2
                H = 'H2'
                n = 20
                p = 2000
                hotel = 'Economy'
                ask2 = 'n'
            elif user == 3:
                h = H3
                H = 'H3'
                n = 20
                p = 5500
                hotel = 'Elite'
                ask2 = 'n'
            elif user == 4:
                h = H4
                H = 'H4'
                n = 15
                p = 7100
                hotel = 'Royal'
                ask2 = 'n'
            elif user == 5:
                h = H5
                H = 'H5'
                n = 10
                p = 10000
                hotel = 'Ultra_Royal'
                bill = 'bill5'
                ask2 = 'n'
            elif user == 6:
                ask2 = 'no'

            if ask2 == 'n':
                # Hotel details
                print('Total Rooms in Hotel: ', n)
                print('Room Rent: Rs.', p)
                print()
                if h == []:
                    print('All rooms are unoccupied.... ')
                    for i in range(1,n+1):
                        print(i,end = ',')
                    print()
                    print()
                    che = True
                    while che:
                        ask1 = input('Want to continue? (y/n): ')
                        if ask1 == 'y' or ask1 == 'Y' or ask1 == 'n' or ask1 == 'N':
                            che = False


                elif len(h) == n:
                    print('No Vacant Room available!!!!!')
                    print()
                    che = True
                    while che:
                        ask1 = input('Want to select again? (y/n): ')
                        if ask1 == 'y' or ask1 == 'Y' or ask1 == 'n' or ask1 == 'N':
                            che = False
                    if ask1 == 'n' or ask1 == 'N':
                        print('Thanks for visiting.....')
                        print()
                        print()


                else:
                    x = len(h)
                    print(x, 'Rooms are occupied')
                    for i in range(1, n + 1):
                        if i in h:
                            print(i, end=',')
                    print()
                    print('Available Rooms are....')
                    for i in range(1, n + 1):
                        if i in h:
                            pass
                        else:
                            print(i, end=',')
                    print()
                    che = True
                    while che:
                        ask1 = input('Want to continue? (y/n): ')
                        print()
                        if ask1 == 'y' or ask1 == 'Y' or ask1 == 'n' or ask1 == 'N':
                            che = False
                    print('______________________________________________________')
    ## Taking user input:-------------------------------------
                if ask1 == 'y':
                    ask4 = 'n'
                    while ask4 == 'n' or ask4 == 'N':
                        che = True
                        while che:
                            N = ''
                            name = input('Enter customer name: ')
                            print()
                            G = name.split()
                            for i in G:
                                N += i
                            if N.isalpha():
                                che = False
                            else:
                                print('Please enter correct name')
                                print()
                        che = True
                        while che:
                            phone = input('Enter Phone Number: ')
                            print()
                            if phone.isdigit() and len(phone) == 10:
                                che = False
                                phone = int(phone)
                            else:
                                print('Enter correct number')
                                print()

                        che = True
                        while che:
                            num = input('How many rooms to book? : ')
                            print()
                            if num.isdigit():
                                che = False
                                num = int(num)
                        row = []
                        for i in range(num):
                            che = True
                            while che:
                                print('Enter Room Number of Room', (i + 1))
                                room = input('Enter Room Number: ')
                                print()
                                if room.isdigit():
                                    room = int(room)
                                    if room in range(1, n + 1) and room not in h:
                                        if  room not in row:
                                            row.append(room)
                                            che = False
                                        else:
                                            print('Room not available!!!')
                                    else:
                                        print('Room not available!!!')
                                        print()
                                else:
                                    print('Room not available!!!')
                                    print()
                        add = input('Enter Address : ')
                        print()
                        cursor.execute("select curdate()")
                        date = cursor.fetchall()
                        date = date[0][0]
                        cursor.execute("select current_time()")
                        time = cursor.fetchall()
                        time = time[0][0]

                        print()
                        print('______________________________')
                        print('Customer Name: ', name)
                        print('Phone Number: ', phone)
                        print('Room Type: ',hotel)
                        print('Room Rent: ',p)
                        print('Room Number: ', row)
                        print('Address: ', add)
                        print('Checkin date: ', date)
                        print('Checkin Time: ', time)
                        print('______________________________')
                        print()
                        print()
                        che = True
                        while che:
                            ask4 = input('Want to continue? (y/n): ')
                            print()
                            if ask4 == 'y' or ask4 == 'Y' or ask4 == 'n' or ask4 == 'N':
                                che = False

 ## Inserting values in table-----------------------------
                    for i in row:
                        insert = "insert into " + hotel + " values('{}', {}, {}, '{}', '{}','{}',{}) ".format(name,
                                                                                        phone, i, add,date, time, p)
                        insert1 = "insert into History values('{}', {}, {}, '{}', '{}','{}',{},'{}','{}') ".format(name,
                                                                        phone, i, add,date,time,p,hotel,'')
                        insert2 = "insert into " + H + " values({})".format(i)

                        cursor.execute(insert)
                        cursor.execute(insert1)
                        cursor.execute(insert2)
                        con.commit()

                        h.append(i)

                    print()
                    print('Room Successfully Booked............!')
                    print('Thank You.....')
                    print()
                    print('___________________________________________')

### Checkout--------------------------------------------------------
        if use == 2:
            che = True
            while che:
                list()
                print()
                user = input('Chooses Your Room Type(1,2,3,4,5,6): ')
                print()
                if user not in ('1', '2', '3', '4', '5', '6'):
                    print('Choise Invalid.....Please choose again: ')
                    print()
                else:
                    che = False
                    user = int(user)

            if user == 1:
                h = H1
                H = 'H1'
                hotel = 'Budget'
                n = 25
                ask2 = 'n'
            elif user == 2:
                h = H2
                H = 'H2'
                hotel = 'Economy'
                n = 20
                ask2 = 'n'
            elif user == 3:
                h = H3
                H = 'H3'
                hotel = 'Elite'
                n = 20
                ask2 = 'n'
            elif user == 4:
                h = H4
                H = 'H4'
                hotel = 'Royal'
                n = 15
                ask2 = 'n'
            elif user == 5:
                h = H5
                H = 'H5'
                hotel = 'Ultra_Royal'
                n = 10
                ask2 = 'n'
            elif user == 6:
                ask2 = 'no'

            if ask2 == 'n' :
                query1 = "select* from "+ hotel
                cursor.execute(query1)
                data = cursor.fetchall()
                print()
                print('---------------------------------------------------------------')
                for i in data:
                    print(i)
                print()
                print('---------------------------------------------------------------')

## Taking user input----------------------------------------------------
                if h ==[]:
                    print('No booking in hotel')
                    print()
                else:
                    che = True
                    while che:
                        name = input('Enter customer name: ')
                        print()
                        N =''
                        G = name.split()
                        for i in G:
                            N += i
                        if N.isalpha():
                            che = False
                        else:
                            print('Please enter correct name')
                            print()

                    che = True
                    while che:
                        num = input('How many rooms were booked? : ')
                        print()
                        if num.isdigit():
                            che = False
                            num = int(num)
                    row = []
                    for i in range(num):
                        che = True
                        while che:
                            print('Enter Room Number of Room', (i + 1), ' : ')
                            room = input('Enter Room Number: ' )
                            print()
                            if room.isdigit():
                                room = int(room)
                                if room in h:
                                    che = False
                                    row.append(room)
                                else:
                                    print('Room not booked!!!')
                                    print()
                            else:

                                print('Enter correct room number!!!')
                                print()

                    query2 = "select customer_name from " + hotel
                    cursor.execute(query2)
                    data = cursor.fetchall()
                    x = (name,)
                    if x in data:
                        roomout = []
                        priceout = 0
                        for i in row:
                            query3 = "select* from " + hotel + " where customer_name = '{}' and room_number ={}".format(
                                name, i)
                            cursor.execute(query3)
                            data = cursor.fetchall()
                            query4 = "delete from " + hotel + " where customer_name = '{}' and room_number = {}".format(
                                name, i)

                            cursor.execute(query4)
                            con.commit()
                            if data[0][2] not in roomout:
                                roomout.append(data[0][2])
                                priceout += data[0][6]
                        nameout = name
                        date = data[0][4]
                        time = data[0][5]
                        cursor.execute("select sysdate()")
                        dateout = cursor.fetchall()
                        dateout = dateout[0][0]

                        for a in roomout:
                            h.remove(a)
                            cursor.execute("delete from " + H + " where Room = {}".format(a))
                            con.commit()

                        for i in row:
                            query5 = "update History set Checkout_date ='{}' where Customer_name = '{}' and " \
                                     "Room_Number = {} and Checkin_Date = '{}' ".format(dateout,nameout,i,date)
                            cursor.execute(query5)
                            con.commit()

    ## Printing bill-----------------------------------------------------------
                        print()
                        print('------------------------------------------------')
                        print('                Bill          ')
                        print('          The Paradise Inn            ')
                        print('         -------------------            ')
                        print('Customer name : ', nameout,'\n'
                              'Room Type : ',hotel,'\n'
                              'Room : ',roomout,'\n'
                              'Checkin Date : ',date,'\n'
                              'Checkin Time : ',time,'\n'
                              'Checkout Date : ',dateout,'\n'
                              'Total amount to pay : Rs.',priceout)
                        print()
                        print('Thanks for visiting!!!!!')
                        print('------------------------------------------------')

    ### Checkin Detail_______________________________________________________________
        if use == 3:
            cursor.execute("select* from history")
            data = cursor.fetchall()
            print('________________________________________________________________')
            for i in data:
                print(i)
            print('________________________________________________________________')
            print()

            print('Search by: \n'
                  '           1.Name      2.Date of Checking      3.Exit  ')
            print()
            che = True
            while che:
                user = input('Enter your choice (1,2,3): ')
                print('------------------------------------------------------------')
                print()
                if user not in ('1', '2','3'):
                    print('Choise Invalid.....Please choose again: ')
                else:
                    che = False
                    user = int(user)
            if user == 3:
                pass
            if user == 1:
                che = True
                while che:
                    N = ''
                    name = input('Enter customer name: ')
                    print()
                    G = name.split()
                    for i in G:
                        N += i
                    if N.isalpha():
                        che = False
                    else:
                        print('Please enter correct name')
                        print()
                print('____________________________________________________________________________________')

                query5 = "select* from history where Customer_Name ='{}' ".format(name)
                cursor.execute(query5)
                data = cursor.fetchall()
                for i in data:
                    print(i)
                print('_______________________________________________________________________________________')
                print()

                che = True
                while che:
                    ask2 = input('want to enter checkin date? (y/n) : ')
                    print()
                    if ask2 == 'y' or ask2 == 'Y' or ask2 == 'n' or ask2 == 'N':
                        che = False
                        if ask2 == 'n' or ask2 == 'N':
                            print('Thank you...........')
                            print()

                if ask2 == 'y' or ask2 == 'Y':
                    date = input('Enter checkin date (in format YYYY-MM-DD) : ')
                    print()
                    print('______________________________________________________________________________________')

                    query5 = "select* from history where Customer_Name = '{}' and Checkin_Date ='{}' ".format(name,date)
                    cursor.execute(query5)
                    data = cursor.fetchall()

                    for i in data:
                        print(i)
                    print('______________________________________________________________________________________')
                    print()

                    che = True
                    while che:
                        ask1 = input('Press (y) to exit : ')
                        if ask1 == 'y' or ask1 == 'Y' or ask1 == 'n' or ask1 == 'N':
                            che = False

     ###search by date
            elif user == 2:
                date = input('Enter checkin date (in format YYYY-MM-DD) : ')
                print()
                print('______________________________________________________________________________________')

                query5 = "select* from history where Checkin_Date ='{}' ".format(date)
                cursor.execute(query5)
                data = cursor.fetchall()

                for i in data:
                    print(i)
                print('______________________________________________________________________________________')
                print()

                che = True
                while che:
                    ask1 = input('Press (y) to exit : ')
                    if ask1 == 'y' or ask1 == 'Y' or ask1 == 'n' or ask1 == 'N':
                        che = False