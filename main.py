import sqlite3
import os.path
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
db_path = os.path.join(BASE_DIR, "modlog.db")
print(db_path)
with sqlite3.connect(db_path) as db:
  pass

#SQL
 

def create_table(Database,Table):
  conn = sqlite3.connect(Database)
  curs = conn.cursor()
  curs.execute(f'CREATE TABLE {Table}(LOG_ID integer primary key AUTOINCREMENT, USER text, AUTHINTRO text)')
  conn.commit()
  conn.close()



def display(Database,Table):
  conn = sqlite3.connect(Table)
  curs = conn.cursor()
  curs.execute('SELECT * FROM {Table}')
  print(curs.fetchall())
  conn.close()



def add_column(Database,Table,Column):
  conn = sqlite3.connect(Database)
  curs = conn.cursor(Database)
  curs.execute('ALTER TABLE {Table} ADD COLUMN {Column}')
  conn.commit()
  conn.close()



def add_data(Database,Table):
  conn = sqlite3.connect(Database)
  curs = conn.cursor()
  curs.execute(f"INSERT INTO {Table} (USER,AUTHINTRO)  Values ('George','TRUE')") 
  conn.commit()
  conn.close()

def del_data(Database,Table):
  conn = sqlite3.connect(Database)
  curs = conn.cursor()  
  curs.execute(f'''DELETE FROM {Table} WHERE x = "x"''')
  conn.commit()
  conn.close()


def update_data(Database, Table):
  conn = sqlite3.connect(Database)
  curs = conn.cursor()
  sql = ''' UPDATE {Table}  SET x = "x"  WHERE x= "x"
  '''
  curs.execute(sql)
  conn.commit()
  conn.close()

def search(Database,Table):
  conn = sqlite3.connect(Database)
  curs = conn.cursor()
  sql = f'''
  SELECT * FROM {Table}
  
  '''
  curs.execute(sql)
  print(curs.fetchall())
  conn.commit()
  conn.close()

def connect(Database):
  if sqlite3.connect(Database):
    print("Connected")
  else:
    
    create_table(name)


database="ModLog"
connect("LOG")


#get or create table 
try:
  create_table(database,"logger")
except:
  print('table already exists')
add_data(database, "logger")
#display_database("example.db")
#del_data("example.db")
#update_data("example.db")
#display_database("example.db")
search(database,"logger")
