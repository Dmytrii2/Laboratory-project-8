import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="phonestation",
    user="user",
    password="password"
)
cursor = connection.cursor()

# Запит 1
cursor.execute("SELECT * FROM Clients WHERE client_type = 'фізична особа' ORDER BY last_name;")
clients = cursor.fetchall()

# Запит 2
cursor.execute("""
SELECT client_type, COUNT(*)
FROM Clients
GROUP BY client_type;
""")
client_counts = cursor.fetchall()

# Запит 3
cursor.execute("""
SELECT call_id, (duration_minutes * cost_per_minute) AS cost
FROM Calls
JOIN Tariffs ON Calls.tariff_code = Tariffs.tariff_code;
""")
call_costs = cursor.fetchall()

# Закриваємо підключення
cursor.close()
connection.close()
