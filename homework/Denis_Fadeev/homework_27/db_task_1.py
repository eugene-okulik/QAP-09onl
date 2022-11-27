import mysql.connector as mysql


db = mysql.connect(
   host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
   database='qap09'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('QAP-09', '2022-07-14', '2022-12-13')")
db.commit()
groups_id = cursor.lastrowid
cursor.execute(f"INSERT INTO students (name, second_name, group_id) VALUES ('Denis', 'Fadeev', {groups_id})")
db.commit()
students_id = cursor.lastrowid
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('1984', {students_id}),"
               f" ('Animal Farm', {students_id})")
db.commit()
cursor.execute(f"SELECT name, second_name, g.title as group_title, b.title as book_title from `groups` g "
               f"JOIN students s on g.id = s.group_id "
               f"JOIN books b on b.taken_by_student_id = s.id "
               f"WHERE s.id = {students_id}")
student_info = cursor.fetchall()
books = ', '.join([books['book_title'] for books in student_info])

print(f"Студент {student_info[0]['name']} {student_info[0]['second_name']} "
      f"учится в группе {student_info[0]['group_title']}"
      f" и взял в библиотеке следующие книги: {books}")

db.close()
