import psycopg2  # Importación necesaria

conn = psycopg2.connect(
    host="localhost",        # En local
    database="ingenieria1",   # Nombre de la base de datos django
    user="postgres",         # Usuario de postgreSql
    password="admin123$%"    # contraseña de postgreSql
)