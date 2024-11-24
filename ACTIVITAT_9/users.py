import psycopg2
from db_connect import connexio 

# Funció read_users que llegeix els usuaris des de la base de dades.
def read_users():
    conn, connection = connexio() 
    try:  
        sql_read = '''SELECT id, nom, cognom FROM USERS;'''
        connection.execute(sql_read)
        
        # Recupera tots els registres obtinguts en una llista.
        resultat = connection.fetchall()
        return resultat
    
    # Zona Errors.
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    
    finally:
        connection.close()
        conn.close()