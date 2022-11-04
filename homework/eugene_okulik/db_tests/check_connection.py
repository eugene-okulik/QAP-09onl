import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
   database='qap09'
)

cursor = db.cursor()
cursor.execute('select * from students')
print(cursor.fetchall())

db.close()
