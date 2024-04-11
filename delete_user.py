from connect_db import connect_db

def delete_user():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()
            del_user = (9,) 
            query = "DELETE FROM User WHERE user_id = %s"
            cursor.execute(query, del_user)
            conn.commit()
            print("User succesfully removed")

        except Exception as e:
            print(f"error: {e}")

        finally:
            cursor.close()
            conn.close()

delete_user()




