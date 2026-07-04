import mysql.connector
import pandas as pd 

try:
    conn = mysql.connector.connect(host = "localhost" , user="root" , password="" , database = "mysql_python")
except:
    print("Could Not Connect to the Database !!")
else:
    print("Sucessfully connected with the database")

def execute_query(conn,query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)

        if cursor.description: 
            results = cursor.fetchall() 
            print("Query Results")
            for row in results:
                print(row)
        else:
            # Only INSERT, UPDATE, DELETE, and CREATE need a commit
            conn.commit()
        
    except mysql.connector.Error as err:
        print(f"There was a problem with the query! Error: {err}")
    else:
        print("Query Run Successfull")

def fetch_as_dataframe(conn, query):
    try:
        df = pd.read_sql(query, conn)
        print("\n--- Pandas DataFrame View ---")
        print(df.to_string(index=False)) 
    except Exception as e:
        print(f"Pandas read error: {e}")
