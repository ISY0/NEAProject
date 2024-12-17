import psycopg2

#checking the connection with the database and ensuring data is inputted correctly 
Database = psycopg2.connect(
    dbname="bwkv4mjzmrnekdcjycl3",
    user="ukjbdjhtvlnzqsu9tnyi",
    password="9L1o8zMjcLcL1p5ouHWlNKLuhebLwi",
    host="bwkv4mjzmrnekdcjycl3-postgresql.services.clever-cloud.com",
    port="50013"
)
cursor = Database.cursor()


cursor.execute("""SELECT * FROM Season 
               WHERE Season = 2003""")
row = cursor.fetchall()
print(row)

