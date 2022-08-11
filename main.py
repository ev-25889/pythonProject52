"""создание JSON пакета с инофрмацией по студентам с выбранными ИД.
"""
import psycopg2
from psycopg2 import Error

import json


try:
# Подключение к существующей базе данных
connection = psycopg2.connect(user="myprojectuser",
# пароль, который указали при установке PostgreSQL
password="password",
host="localhost",
port="5432",
database="myproject")
# Курсор для выполнения операций с базой данных

cursor = connection.cursor()
"""
insert_query = '''INSERT INTO public.human
("ID", "HumanAddressRuID", "HumanAddressStringID", "HumanBasicEmail", "HumanBirthDate", "HumanBirthPlace", "HumanBirthPlaceOKATO", "HumanCitizenshipID", "HumanFirstName", "HumanID", "HumanINN", "HumanLastName", "HumanLogin", "HumanMiddleName", "HumanPhotoContentURL", "HumanPrincipalID", "HumanSNILS", "HumanSex", created_on)
VALUES('f254a0f7-fb8f-48a3-937d-1b6a7a1ee97f', NULL, 'e444692d-91f7-454c-8484-ab540a10bc88', NULL, '1995-02-15', NULL, NULL, '76497526-812d-4246-9c52-799fb92d82aa', 'Яна', NULL, NULL, 'Пономарева', 'ya.e.ponomareva99', 'Эдуардовна', NULL, '3fd40daa-8a71-44a4-aa61-470c2f017d96', NULL, 'Женский', NULL);
'''
cursor.execute(insert_query)
connection.commit()



select_query = 'select s."ID" , s."HumanID" , h."HumanFirstName" , h."HumanMiddleName" , h."HumanLastName" , h."HumanSNILS" , h."HumanINN" , h."HumanBasicEmail" from student s join human h on h."ID"  = s."HumanID";'
cursor.execute(select_query)
mobile_records_one = cursor.fetchone()
print("Вывод первой записи", mobile_records_one)"""

def get_student_info_list(): # Функция, которая создает пакет (список) по всем студентам
select_query = '''select s."ID" , h."HumanLastName", h."HumanFirstName" ,h."HumanMiddleName" ,
h."HumanSNILS", h."HumanINN", h."HumanBasicEmail"
from student s join human h on h."ID"  = s."HumanID";'''
cursor.execute(select_query)

student_id = cursor.fetchall()
all_students_information = list()
for row in student_id: # Список для сохранения информации по одному студенту
one_student_information = list()
for i in range(7):
one_student_information.append(row[i])
one_dict = get_dict_from_list(one_student_information)
all_students_information.append(one_dict)
with open('students.json', 'w') as fp: json.dump(all_students_information, fp, ensure_ascii=False)
return json.dumps(all_students_information, ensure_ascii=False)


# list_of_student_id.append(student_id)
print(all_students_information)

def get_dict_from_list(one_student_information): # функция для преобразования словаря в JSON объект
list_of_keys = ('external_id', 'surname', 'name', 'middle_name', 'snils', 'inn', 'email')
stud_dict = dict(zip(list_of_keys, one_student_information))
# преобразование в JSON в аргументом для неломки кодировки
return stud_dict # json.dumps(stud_dict, ensure_ascii=False)

print(get_student_info_list())
# json_data = json.dump()
# print(json_data)



except (Exception, Error) as error: print("Ошибка при работе с PostgreSQL", error)
finally: if connection: cursor.close()
connection.close()
print("Соединение с PostgreSQL закрыто")


