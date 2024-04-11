from connect_db import connect_db

def fetch_books_by_book_id():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()
            query = """
            SELECT book, date, book.book_id, user, author
            FROM User, Books
            WHERE User.user_id = Orders.book_id;
                        
            """

            cursor.execute(query)

            for order in cursor.fetchall():
                print(order)
            
           
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()
fetch_books_by_book_id()


