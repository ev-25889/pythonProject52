
import psycopg2
from psycopg2 import Error

def get_mobile_details(mobile_id):
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
        # SQL-Запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE mobile         ---- шаг 2
                                (ID INT PRIMARY KEY     NOT NULL,
                                MODEL           TEXT    NOT NULL,
                                PRICE           REAL);'''
        # Выполнение команды для создания новой таблицы     ---- шаг 2
        cursor.execute(create_table_query)                  ---- шаг 2
        connection.commit()                                 ---- шаг 2
        print("Таблица успешно создана в PostgreSQL")       ---- шаг 2
        
        # Распечатать сведения о PostgreSQL                 ---- шаг 1
         print("Информация о сервере PostgreSQL")           ---- шаг 1
        print(connection.get_dsn_parameters(), "\n")        ---- шаг 1
        # Выполнение SQL-запроса                            ---- шаг 1
        cursor.execute("SELECT version();")                 ---- шаг 1
        # Получить результат                                ---- шаг 1
        record = cursor.fetchone()                          ---- шаг 1
        print("Вы подключены к - ", record, "\n")           ---- шаг 1
        
        # SQL-запрос для вставки данных в таблицу
        insert_query = '''INSERT INTO mobile (ID, MODEL, PRICE) VALUES (3, 'IPHONE13', 1200) '''
        # Выполнение запроса для вставки
        cursor.execute(insert_query)
        connection.commit()
        print("1 запись успешно вставлена")
        # получить результат
        cursor.execute("SELECT * from mobile")
        record = cursor.fetchall()
        print("Результат", record)
        
        # SQL-запрос на обновление данных в таблице 
        update_query = '''UPDATE mobile SET price = 1500 where id = 3'''
        cursor.execute(update_query)
        connection.commit()
        cursor.execute("select * from mobile")
        print("result", cursor.fetchall())
        
        # SQL-запрос на удаление из таблицы
        delete_query = '''Delete from mobile where id = 2'''
        cursor.execute(delete_query)
        connection.commit()
        count = cursor.rowcount
        print(count, 'delete OK!')
        cursor.execute("select * from mobile")
        print('res', cursor.fetchall())
        
    
        create_table_query = '''CREATE TABLE item (
            item_id serial NOT NULL PRIMARY KEY,
            item_name VARCHAR (100) NOT NULL,
                purchase_item timestamp NOT NULL,
            price INTEGER NOT NULL);'''
    
        cursor.execute(create_table_query)
        connection.commit()
        print('table is ready!')
        
        insert_query = '''insert into mobile (id, model, price) values 
                                            (10, 'model1', 1000),
                                            (20, 'model2', 2000),
                                            (30, 'model3', 3000)'''
        cursor.execute(insert_query)
        connection.commit()
        
        select_query = "select * from mobile where id= %s"
       
        cursor.execute(select_query, (mobile_id,))
        print("выбор строк из таблицы мобайл с помощью курсор.фетчол")
        mobile_records = cursor.fetchall()

        print("выод каждой строки и ее столбцов")
        for row in mobile_records:
            print("ID =", row[0],)
            print("Model =", row[1])
            print("Cena =", row[2], "\n")
        """
        # SQL-запрос на удаление таблиц
        drop_table_query = '''DROP TABLE IF EXISTS mobile, item;'''
        cursor.execute(drop_table_query)
        connection.commit()
        print('таблицы удалены')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

get_mobile_details(10)
get_mobile_details(30)
