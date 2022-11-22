'''
1.Создает группу (даты в запросе можно указывать как строки, т.е. '2022-04-03')
2.Создает студента с именем и фамилией, такими как вы придумаете и group_id той группы, что вы создали
3.Создает 2 книги. В колонку taken_by_student_id записывает id вашего студента.
4.Получает из базы данных данные для студента, которого вы добавили. Желательно одним запросом получить и студента и
группы и книги (с помощью Join). Выводит следующий текст на основании полученных данных:
Студент Ivan Ivanov учится в группе GPN-001 и взял в библиотеке следующие книги: SQL essentials, Python for dummies
'''
import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

#  task 1
cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Test_group', '2022-11-17', '2022-12-12')")
db.commit()

#  task 2
group_id = cursor.lastrowid
cursor.execute(f"INSERT INTO `students` (name, second_name, group_id) VALUES ('Andrei', 'Dudin', {group_id})")
db.commit()

#  task 3
student_id = cursor.lastrowid
cursor.execute(
    f"INSERT INTO books (title, taken_by_student_id) VALUES ('Book name1', {student_id}), ('Book name2', {student_id})")
db.commit()

#  task 4
taken_by_student_id = cursor.lastrowid

query = f"""
SELECT s.name , s.second_name , g.title as g_title, b.title FROM students s
JOIN `groups` g on s.group_id  = g.id
JOIN books b on b.taken_by_student_id = s.id
WHERE s.id = {student_id}
"""

cursor.execute(query)
query_result = cursor.fetchall()
db.commit()

print(f"""
Student {query_result[0]['name']} {query_result[0]['second_name']} \
studies in the {query_result[0]['g_title']} group and \
borrowed the following books from the library: {query_result[0]['title']} and {query_result[1]['title']}.
""")
