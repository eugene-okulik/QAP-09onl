import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
   database='qap09'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('QAPy09', '2022-07-14', '2022-12-05')")
db.commit()
group_id = cursor.lastrowid
cursor.execute(f"INSERT INTO students (name, second_name, group_id) VALUES ('Pavel', 'Malashko', { group_id })")
db.commit()
student_id = cursor.lastrowid
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Riki tiki tavi', { student_id }),"
               f" ('Crane cry', { student_id })")
db.commit()
cursor.execute(f"SELECT name, second_name, g.title as group_title, b.title as book_title from `groups` g "
               f"JOIN students s on g.id = s.group_id "
               f"JOIN books b on b.taken_by_student_id = s.id "
               f"WHERE s.id = { student_id }")
user_info = cursor.fetchall()
books = ', '.join([books['book_title'] for books in user_info])

print(f"Student whose name is { user_info[0]['name'] } { user_info[0]['second_name'] } "
      f"is studying in the group { user_info[0]['group_title'] }"
      f" and he took the next books: { books }")
