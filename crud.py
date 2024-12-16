import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Bhejiput_761029',
        database='indigo'
    )
    mycursor = conn.cursor()
    print('Connection Established.')
except:
    print('Connection Error.')

# Creating Database in the db server:
# mycursor.execute('CREATE DATABASE indigo')
# conn.commit()

# create table:
# airport -> airport_id | code | name
# mycursor.execute(
#     """
#     CREATE TABLE airport(
#         airport_id INT PRIMARY KEY,
#         code VARCHAR(10) NOT NULL,
#         city VARCHAR(50) NOT NULL,
#         name VARCHAR(255) NOT NULL
#     )
#     """
# )
# conn.commit()

# insert data to the table:
# mycursor.execute(
#     """
#     INSERT INTO airport VALUES
#     (1, 'DEL', 'New Delhi','IGIA'),
#     (2, 'CCU', 'KOLKATA', 'NSCA'),
#     (3, 'BOM', 'Mumbai','CSMA')
#     """
# )
# conn.commit()

# Search/Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)
for i in data:
    print(i[3])

# Update:
mycursor.execute(
    """ 
    UPDATE airport
    SET name = 'Bombay'
    WHERE airport_id = 3
    """
)
conn.commit()

mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)
for i in data:
    print(i[3])

# delete
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)
for i in data:
    print(i[3])
