import mysql.connector

def connect_db():
    db_name = "e_commerce_db"
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

        print("Connected Succesfully")
        return conn     


    
    except mysql.connector.Error as e:
        print(f"Error: {e}")

#     finally:
#         # close out the connection
#         if conn and conn.is_connected():
#             conn.close()
#             print("MySql connection closed")

# connect_db()