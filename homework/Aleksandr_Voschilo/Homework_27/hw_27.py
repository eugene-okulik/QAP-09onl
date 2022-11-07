import mysql.connector as mysql


db = mysql.connect(
   host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
   database='qap09'
)


cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('QAP-QAP', '2022-05-11', '2027-05-11')")
db.commit()
group_id = cursor.lastrowid
cursor.execute(f"INSERT INTO students (name, second_name, group_id) values ('Jim', 'Carry', {group_id})")
db.commit()
student_id = cursor.lastrowid
query = "INSERT INTO books (title, taken_by_student_id) values (%s, %s)"
values = [
   ('Witcher', student_id),
   ('Witcher 2', student_id)
]
cursor.executemany(query, values)
db.commit()
query_student_data = f"SELECT s.name, s.second_name, g.title as group_title, b.title as book_title" \
                     f" from students as s" \
          f" join `groups` as g" \
          f" on s.group_id = g.id" \
          f" join books as b" \
          f" on s.id = b.taken_by_student_id" \
          f" where s.group_id = {group_id}"
data_student = cursor.execute(query_student_data)
result = cursor.fetchall()
list_of_books = [result[i]['book_title'] for i in range(len(result))]
print(f"Student {result[0]['name']} {result[0]['second_name']} studies in the {result[0]['group_title']}"
      f" and borrowed the following books from the library: {', '.join(list_of_books)}")

db.close()
