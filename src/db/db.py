import psycopg2

def get_db_connection():
    connection = psycopg2.connect(database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5432')
    
    return connection