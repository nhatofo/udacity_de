import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    # connect to default database
    """
        Description:This function creates a connection to a postgress database instance, using a conn object 
        to that utilize a python postgress driver connector.
        
        cur: the cursor object. tha executes the the drop and create databese query on postgress via conn 
        object.
        
        Arguments:
             conn, cur on database connection 
        Returns:
             conn, curr on database connection
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
       This funtion use the conn object and cur cursor object to drop tables on specified database
       
       Arguments:
           cur, conn
       return:
           None
    """
    # drop database tables from drop_table_queries, a list with DROP statements
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
     """
       This funtion use the conn object and cur cursor object to create tables on specified database
       
       Arguments:
           cur, conn
       return:
           None
    """
    # create database tables from create_table_queries, a list with INSERT statements
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
     """
       This is the main funtion that assign the object returned by the create_database() to the cur, and conn
       and executes the drop and create database functions by passing cur and conn as arguments.
       and closes the connection.
       
       Arguments:
           cur, conn
       return:
           None
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()