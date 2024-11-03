import psycopg2  # Для PostgreSQL

# Підключення до бази даних
connection = psycopg2.connect(
    host="localhost",
    database="phonestation",
    user="user",
    password="password"
)

# Створення курсора
cursor = connection.cursor()

# Очищення таблиць перед додаванням нових даних
cursor.execute("TRUNCATE TABLE phones, clients, calls, tariffs RESTART IDENTITY CASCADE;")
connection.commit()
print("Таблиці очищені.")

# Дані для клієнтів
cursor.execute("""
INSERT INTO clients (client_type, address, last_name, first_name, middle_name)
VALUES
('фізична особа', 'вул. Київська, 10', 'Іванов', 'Іван', 'Іванович'),
('відомство', 'вул. Харківська, 20', 'Петров', 'Петро', 'Петрович'),
('фізична особа', 'вул. Львівська, 30', 'Сидоров', 'Сидір', 'Сидорович'),
('фізична особа', 'вул. Полтавська, 40', 'Коваленко', 'Олег', 'Олегович'),
('відомство', 'вул. Дніпровська, 50', 'Шевченко', 'Тарас', 'Григорович');
""")

# Дані для тарифів
cursor.execute("""
INSERT INTO tariffs (call_type, cost_per_minute)
VALUES
('внутрішній', 0.50),
('міжміський', 1.50),
('мобільний', 2.50);
""")

# Дані для телефонів
cursor.execute("""
INSERT INTO phones (phone_number, client_id)
VALUES
('123-456-7890', 1),
('234-567-8901', 2),
('345-678-9012', 3),
('456-789-0123', 4),
('567-890-1234', 5);
""")

# Дані для розмов
cursor.execute("""
INSERT INTO calls (call_date, phone_number, duration_minutes, tariff_code)
VALUES
('2023-01-15', '123-456-7890', 10, 1),
('2023-01-16', '234-567-8901', 20, 2),
('2023-01-17', '345-678-9012', 30, 3),
('2023-01-18', '456-789-0123', 15, 1),
('2023-01-19', '567-890-1234', 25, 2);
""")

# Збереження змін та закриття з'єднання
connection.commit()
cursor.close()
connection.close()

print("Дані успішно додано до таблиць.")
