from connect_db import connect_db

def fetch_author():
    conn = connect_db()
    if conn:
        try:
 
            query = "SELECT * FROM Author"

            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)

        finally:
            cursor.close()
            conn.close()
fetch_author()
