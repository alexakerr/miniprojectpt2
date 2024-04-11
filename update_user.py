from connect_db import connect_db

def update_user():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            
            updated_user = ("Lex Kerr", 4)

        
            query = "UPDATE User SET name = %s WHERE user_id = %s"


            cursor.execute(query, updated_user)
            conn.commit() 
            print("User details succesfully updated!")

        except Exception as e:
            print(f"and error occurred: {e}") 
        
        finally:
            cursor.close()
            conn.close()
update_user()       


