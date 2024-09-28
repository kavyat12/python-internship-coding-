import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)
mycursor=mydb.cursor()

class Student:
    def __init__(self,name,vid,citizen,course,status):
        self.name=name
        self.vid=vid
        self.citizen=citizen
        self.course=course
        self.status=status
        
        
    def __str__(self):
        return f'{self.name},{self.citizen}'
    
class VisaOfficer:
    def createDB():
        try:
            mycursor.execute('create database intrvisa')
            print('DB created succefully')
        except Exception:
            print('Not created successfully')
            
    
    def useDB():
        try:
            mycursor.execute('use intrvisa')
            print('Using DB succefully')
        except Exception:
            print('Not Using DB  successfully')
            
    
    def addStudentRecord():
        try:
            mycursor.execute('create table stuDet(name varchar(20),vid int(10), citizen varchar(20), course varchar(10), status varchar(10))')
            print('Created Table  succefully')       
        except Exception:
            print('issue while creating table')
        else:
            print('No issues working fine')
            
            
            
    def insertStudentRecord(name, vid, citizen, course, status):
        try:
            sql = 'INSERT INTO stuDet (name, vid, citizen, course, status) VALUES (%s, %s, %s, %s, %s)'
            mycursor.execute(sql, (name, vid, citizen, course, status))
            mydb.commit()
            print('Inserted successfully')
        except Exception:
            print('Issue while import mysql.connector')
        else:
            print('No issues working fine')
            
            
    def readStudentRecord(vid):
        try:
            # Correct SQL syntax for SELECT statement
            sql = 'SELECT * FROM stuDet WHERE vid = %s'
            mycursor.execute(sql, (vid,))
            
            # Fetch one result
            record = mycursor.fetchone()
            
            if record:
                print('Read successfully:', record)
            else:
                print('Could not read, no record found.')
        except Exception as e:
            print('Issue while reading:', e)
        else:
            print('No issues, working fine.')
        
        
    def updateStudentRecord(name, vid, citizen, course, status):
        try:
            sql = 'UPDATE stuDet SET name = %s, citizen = %s, course = %s, status = %s WHERE vid = %s'
            mycursor.execute(sql, (name, citizen, course, status, vid))
            mydb.commit()
            if mycursor.rowcount > 0:
                print('Updated successfully')
            else:
                print('No records were updated (check if the vid exists)')
        except Exception as e:
            print('Issue while updating:', e)
        else:
            print('No issues working fine')
            
            
            
    def deleteStudentRecord(vid):
        try:
            sql = 'DELETE FROM stuDet WHERE vid = %s'
            mycursor.execute(sql, (vid,))
            mydb.commit()  
            
            if mycursor.rowcount > 0:
                print('Deleted successfully')
            else:
                print('No records were deleted (check if the vid exists)')
        except Exception as e:
            print('Issue while deleting:', e)
        else:
            print('No issues; working fine')
            


            
vo=VisaOfficer
#vo.createDB()
vo.useDB()
vo.addStudentRecord()
vo.insertStudentRecord("sirisha",1,"india","CSE","F1" )
vo.insertStudentRecord("kavya",2,"india","PHD","F1" )
vo.insertStudentRecord("renuka",3,"germany","doctor","F1") 
vo.insertStudentRecord("megha",4,"canada","MCA","F1" )
vo.readStudentRecord(4)
vo.updateStudentRecord("lakshana",5,"australia","PHD","F1")
vo.deleteStudentRecord(3)


