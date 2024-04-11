import mysql.connector

def add_user():
    db_name = "library_db"
    user = "root"
    password = "Gi0vanna"
    host = "127.0.0.1" 

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )
        cursor = conn.cursor()
        name = input("Who woud you like to enter into your database? ")
        email = input("What is their email? ")
        phone = input("What is their phone number? ")

        new_user = (name, email, phone)

        query = "INSERT INTO User (name, email, phone) VALUES (%s, %s, %s)"

        # execute query with new customer
        cursor.execute(query, new_user)
        conn.commit()
        print("New User was succesfully added")


    
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            conn.close()
            print("MySql connection closed")

add_user()