import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
   database='qap09'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) "
               "VALUES ('QAP_mary', '2022-07-17', '2022-12-13')")
db.commit()
insert_id_group = cursor.lastrowid

cursor.execute(f"INSERT INTO students (name, second_name, group_id) "
               f"VALUES ('Mary', 'Dubenchuk', {insert_id_group})")
db.commit()
insert_id_student = cursor.lastrowid

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
   ('Learning Python', f'{insert_id_student}'),
   ('Python Testing with Selenium', f'{insert_id_student}')
]
cursor.executemany(query, values)
db.commit()
insert_id_book = cursor.lastrowid

join_query = f'''SELECT s.name, s.second_name, gr.title as title_group, b.title as book_title 
FROM students s
JOIN `groups` gr ON s.group_id = gr.id
JOIN books b ON s.id= b.taken_by_student_id
WHERE s.id = {insert_id_student}'''
cursor.execute(join_query)
student_data = cursor.fetchall()
book_1 = student_data[0]['book_title']
book_2 = student_data[1]['book_title']

print(f"The student {student_data[0]['name']}, {student_data[0]['second_name']} "
      f"has studied in a group {student_data[0]['title_group']} and "
      f"he/she took the next books from the library: {book_1}, {book_2}")

db.close()
