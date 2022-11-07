import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('QAP_09Oonl', '2022-11-06', '2023-11-06')")
db.commit()
group_id = cursor.lastrowid
print(group_id)
cursor.execute(f"INSERT INTO students (name, second_name, group_id) VALUES ('Jack', 'Sparrow', {group_id})")
db.commit()
student_id = cursor.lastrowid
print(student_id)
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('The Green Mile', f'{student_id}'),
    ('The Shawshank Redemption', f'{student_id}')
]
cursor.executemany(query, values)
db.commit()
cursor.execute(f'SELECT s.name, s.second_name, g.title as group_title, b.title as book_title FROM students s '
               f'JOIN `groups` g ON s.group_id = g.id JOIN books b ON b.taken_by_student_id = s.id '
               f'WHERE s.id = {student_id}')
result_1 = cursor.fetchone()
result_2 = cursor.fetchone()
print(f"Student {result_1['name']} {result_1['second_name']} studies in the {result_1['group_title']} group and "
      f"borrowed the following books from the library: {result_1['book_title']}, {result_2['book_title']}")
db.close()
