import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
   database='qap09'
)

cursor = db.cursor(dictionary=True)
cursor.execute(f"INSERT INTO `groups` (title, start_date, end_date) "
               f"VALUES ('Group_1', '2022-01-01', '2022-31-01')")
db.commit()
group_id = cursor.lastrowid

cursor.execute(f"INSERT INTO `students` (name, second_name, group_id) "
               f"VALUES ('Tanya', 'Shevchuk', {group_id})")
db.commit()
student_id = cursor.lastrowid

cursor.execute(f"INSERT INTO `books` (title, taken_by_student_id) "
               f"VALUES ('Book Name', { student_id }), ('Book Name 2', { student_id })")
db.commit()
book_id = cursor.lastrowid

cursor.execute(f"SELECT s.name, s.second_name, gr.title as title_group, b.title as book_title "
               f"FROM `students` s "
               f"JOIN `groups` gr ON s.group_id = gr.id "
               f"JOIN `books` b ON s.id= b.taken_by_student_id "
               f"WHERE s.id = { student_id }")
user_info = cursor.fetchall()
books = ', '.join([books['book_title'] for books in user_info])
student_data = cursor.fetchall()

print(f"The student {user_info[0]['name']}, {user_info[0]['second_name']} "
      f"studied in a group {user_info[0]['title_group']} and "
      f"took the next books from the library: {books}")
db.close()
