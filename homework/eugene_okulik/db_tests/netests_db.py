import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
   database='qap09'
)

cursor = db.cursor(dictionary=True)
# cursor.execute('select * from students')
# cursor.execute('select * from students where id = 3')
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Dream of the Red Chamber', 15)")
db.commit()
query_id = cursor.lastrowid
print(query_id)
# result = cursor.fetchall()
# result = cursor.fetchone()
# print(result['name'])


db.close()