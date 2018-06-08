import sqlite3

def connect():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , title TEXT , author TEXT , year INTEGER , isbn INTEGER)")
    connection.commit()
    connection.close()

def insert(title , author , year , isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title , author, year, isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from book")
    rows = cursor.fetchall()
    connection.close()
    return rows

def search(title="", author="" , year="" , isbn=""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?" , (title,author,year , isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id = ?" , (id,))
    connection.commit()
    connection.close()

def update(id , title , author , year ,  isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title = ? , author = ? , year = ? , isbn = ? WHERE ID = ?", (title , author, year , isbn, id))
    connection.commit()
    connection.close()



connect()
#insert("The Sun" , "John Smith" , 1918 , 91238123671231)
#delete(3)
#update(4 , "The Moon" , "John Smooth" , 1917 , 82361236192831)
#print(view())
#print (search(author="John Smith"))
