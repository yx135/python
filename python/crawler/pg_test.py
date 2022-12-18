import psycopg2
def connect():
    conn = None
    try:        
        # Connect to your postgres DB
        conn = psycopg2.connect("host=localhost dbname=movieskydb user=postgres password=root")
        print('connnect')
        # Open a cursor to perform database operations
        cur = conn.cursor()        
    
        #sql="create table filmtab(name varchar(100),star varchar(400),time varchar(30));"
        # Execute a query
        cur.execute("""
           create table request_finger(
            finger char(60)
            )
        """
        )
        # Print Result
        lines=cur.fetchall()
        print(lines)       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()