from connect_db import connect_db

def delete_book():
    conn = connect_db() 
    if conn:
        try:
            cursor = conn.cursor()

    
            book_to_remove = (2, )

            query = "SELECT * FROM Orders WHERE customer_id = %s"
            cursor.execute(query, book_to_remove)
            orders = cursor.fetchall()
   
            if book_to_remove :
                print("Cannot delete book")
            else:
                query = "DELETE FROM Book WHERE book_id = %s"

                # execute that query
                cursor.execute(query, book_to_remove)
                conn.commit()
                print("Book removed succesfully")        

        except Exception as e:
            print(f"error: {e}")

        finally:
            cursor.close()
            conn.close()

delete_book()