import psycopg2

def create_table():
   conn=psycopg2.connect("dbname='database1' user='postgres' password='Azul.1995' host='localhost' port='5432' ") #Argument is the db file, if you don't have a db file, it will be created and connected.
   cur=conn.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")#SQL code goes between ""
                                    #Between () goes the parameters of the table
   conn.commit()
   conn.close()

def insert(item,quantity,price):
   conn=psycopg2.connect("dbname='database1' user='postgres' password='Azul.1995' host='localhost' port='5432' ") #Argument is the db file, if you don't have a db file, it will be created and connected.
   cur=conn.cursor()
   cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
   conn.commit()
   conn.close()


def view():
   conn=psycopg2.connect("dbname='database1' user='postgres' password='Azul.1995' host='localhost' port='5432' ") #Argument is the db file, if you don't have a db file, it will be created and connected.
   cur=conn.cursor()
   cur.execute("SELECT * FROM store")
   rows=cur.fetchall()
   conn.close()
   return rows

def delete(item):
   conn=psycopg2.connect("dbname='database1' user='postgres' password='Azul.1995' host='localhost' port='5432' ") #Argument is the db file, if you don't have a db file, it will be created and connected.
   cur=conn.cursor()
   cur.execute("DELETE FROM store WHERE item=?", (item,))
   conn.commit()
   conn.close()

def update(quantity,price, item):
   conn=psycopg2.connect("dbname='database1' user='postgres' password='Azul.1995' host='localhost' port='5432' ") #Argument is the db file, if you don't have a db file, it will be created and connected.
   cur=conn.cursor()
   cur.execute("UPDATE store  SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
   conn.commit()
   conn.close()

create_table()
insert("Orange", 10, 15)
print(view())
#update(20,15,'Orange')
#delete("Wine Glass")
#print(view()) 