"""
Напишите программу, которая:
    1. Создает группу (даты в запросе можно указывать как строки, т.е. '2022-04-03')
    2. Создает студента с именем и фамилией, такими как вы придумаете и group_id той группы, что вы создали
    3. Создает 2 книги. В колонку taken_by_student_id записывает id вашего студента.
    4. Получает из базы данных данные для студента, которого вы добавили.
    Желательно одним запросом получить и студента и группы и книги (с помощью Join).
    Выводит следующий текст на основании полученных данных:
    Студент Ivan Ivanov учится в группе GPN-001 и взял в библиотеке следующие книги: SQL essentials, Python for dummies
    Весь текст для красоты можно вывести на английском.
"""
import mysql.connector as mysql

db = mysql.connect(
        host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        user='user1',
        passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
        database='qap09'
)

cursor = db.cursor(dictionary=True)
cursor.execute(f"INSERT  INTO `groups` (title, start_date, end_date) VALUES ('QAP-09', '2022-07-01', '2022-12-01')")
db.commit()
group_id = cursor.lastrowid
cursor.execute(f"INSERT INTO students (name, second_name, group_id) VALUES ('Maksim', 'Vajda', {group_id})")
db.commit()
student_id = cursor.lastrowid
query = 'INSERT  INTO books  (title, taken_by_student_id) VALUES (%s, %s)'
books = [
    ('1984', student_id),
    ('TYLL', student_id)
]
cursor.executemany(query, books)
db.commit()
query = f"""
SELECT s.name, s.second_name, g.title as group_title, b.title as book_title  FROM students as s
left join `groups` g 
on g.id = s.group_id
JOIN books b 
on s.id = b.taken_by_student_id 
WHERE s.id = {student_id}
"""
cursor.execute(query)
result = cursor.fetchall()
books = ', '.join([result[books]['book_title'] for books in range(len(result))])
print(f"Student {result[0]['name']} {result[0]['second_name']} "
      f"studies in the {result[0]['group_title']} group and"
      f" borrowed the following books from the library: {books}. ")

db.close()
