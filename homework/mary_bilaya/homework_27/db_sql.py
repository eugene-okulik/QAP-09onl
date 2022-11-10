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
#print(insert_id_group)

cursor.execute(f"INSERT INTO students (name, second_name, group_id) "
               f"VALUES ('Mary', 'Dubenchuk', {insert_id_group})")
db.commit()
insert_id_student = cursor.lastrowid
#print(insert_id_student)

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
   ('Learning Python', f'{insert_id_student}'),
   ('Python Testing with Selenium', f'{insert_id_student}')
]
cursor.executemany(query, values)
db.commit()
insert_id_book = cursor.lastrowid
#print(insert_id_book)

join_query = f'''SELECT s.name, s.second_name, gr.title as title_group, b.title as book_title 
FROM students s
JOIN `groups` gr ON s.group_id = gr.id
JOIN books b ON s.id= b.taken_by_student_id
WHERE s.id = {insert_id_student}'''
cursor.execute(join_query)
student_data = cursor.fetchall()
for book in student_data:
    all_books = book['book_title'].split(', ')
    books = (', '.join(all_books))





db.close()
