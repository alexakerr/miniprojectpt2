from connect_db import connect_db

def add_book():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            # set order information into variables
            book_id = 8
            borrow_date = "2024-04-05"

            query = "INSERT INTO Books (date, book_id) VALUES (%s, %s)"
            # execute query
            cursor.execute(query, (borrow_date, book_id))
            #              query, tuple with the above order information
            conn.commit()
            print(f"Book was succesfully added.")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()
add_book()