from connect_db import connect_db

def update_book():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            
            book_id = 3
            book_id = 5 
            new_book_date = "2024-04-05"
            update_info = (new_book_date, book_id, user_id)


            query = "UPDATE Books SET DATE = %s WHERE book_id = %s AND user_id = %s "
            cursor.execute(query, (new_book_date, book_id, user_id) )
        
            conn.commit()
            print("Your book was succesfully updated!")           

        except Exception as e:
            print(f"and error occurred: {e}") 
        
        finally:
            cursor.close()
            conn.close()
update_book()   