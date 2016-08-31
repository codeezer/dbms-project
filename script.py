import MySQLdb

db = MySQLdb.connect(host="localhost",user="root",passwd="sqlroot",db="departmentmodels")

cur = db.cursor()

def addbex(bex):
    file1 = open(bex,'r')


    raw_list = file1.readlines()

    for each in raw_list:
        array = each.split(',')
        roll = '069BEX4'+array[2]
        name = array[3]
        contact = array[4]
        email = array[5]
        if array[2] == 33 or 47 or 44 or 12:
            address = 'Balaju, Kathmandu'
        else:
            address = 'Koteshwor, Random'


    
    	cur.execute("""INSERT INTO student (roll_no, name, address, contact, email, semester_no) VALUES(%s,%s,%s,%s,%s,8);""",(roll, name, address, contact, email))
    	db.commit()

def adddbms(dbms):
    file1 = open(dbms,'r')


    raw_list = file1.readlines()

    for each in raw_list:
        array = each.split(',')
        roll = '069BEX4'+array[2]
    
    	cur.execute("""INSERT INTO studies (roll_no, semester_no, subject_code) VALUES(%s,8,%s);""",(roll,'EX453'))
    	db.commit()

def addbex70(bex70):
    file1 = open(bex70,'r')


    raw_list = file1.readlines()

    for each in raw_list:
        array = each.split(',')
        roll = array[3]
        name = array[4]
        contact = array[5]
        email = array[6].strip()+'@gmail.com'

        if array[3] == '070BEX412' or '070BEX417' or '070BEX424' or '070BEX422':
            address = 'Balaju, Kathmandu'
        else:
            address = 'Koteshwor, Kathmandu'


    
    	cur.execute("""INSERT INTO student (roll_no, name, address, contact, email, semester_no) VALUES(%s,%s,%s,%s,%s,6);""",(roll, name, address, contact, email))
    	db.commit()

def addbct70(bct70):
    file1 = open(bct70,'r')


    raw_list = file1.readlines()

    for each in raw_list:
        array = each.split(',')
        roll = array[1]
        name = array[2]
        contact = array[3]
        email = array[4].strip()+'@gmail.com'

        if array[1].strip() == '070BCT412' or '070BCT417' or '070BCT424' or '070BCT422':
            address = 'Lagankhel, Lalitpur'
        else:
            address = 'Koteshwor, Kathmandu'


    
    	cur.execute("""INSERT INTO student (roll_no, name, address, contact, email, semester_no) VALUES(%s,%s,%s,%s,%s,6);""",(roll, name, address, contact, email))
    	db.commit()



#adddbms('dbms.csv')
#addbex70('bex70.csv')
addbct70('bct70.csv')
