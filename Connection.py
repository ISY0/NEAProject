import psycopg2

# Checking the connection with the database and ensuring data is inputted correctly 
conn = psycopg2.connect(
    dbname="bwkv4mjzmrnekdcjycl3",
    user="ukjbdjhtvlnzqsu9tnyi",
    password="9L1o8zMjcLcL1p5ouHWlNKLuhebLwi",
    host="bwkv4mjzmrnekdcjycl3-postgresql.services.clever-cloud.com",
    port="50013"
)
cursor = conn.cursor()


cursor.execute("""
        SELECT MAX(Season)
        FROM Season INNER JOIN Player
        ON Player.playerid = Season.playerid
        WHERE Player.Firstname = %s AND Player.Lastname = %s""",("Karl","Anthony-Towns",))
recentseason = cursor.fetchall()


print(recentseason[0][0])