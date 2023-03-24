# %%
import psycopg2


# %%
# DB Connection

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    param_dic = {
        "host": "localhost", #os.environ["HOST"],
        "database": "testApp", #os.environ["DATABASE"],
        "user": "postgres", #os.environ["USER"],
        "password": "anto", #os.environ["PASSWORD"]
    }
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**param_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    print("Connection successful")
    return conn

# %%
# Table Creation
def table_creation_aws():

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS testTable")

    #Creating table as per requirement
    sql ='''CREATE TABLE testTable(
    name CHAR(20) NOT NULL,
    ph_no INT,
    City INT,
    YEAR CHAR(255)
    )'''
    cursor.execute(sql)
    print("Table created successfully........")
    conn.commit()

table_creation_aws()

# %%
def insert_data_aws():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO testTable(name, ph_no, City, YEAR)
     VALUES ('432FGGdfs5sfass', '8', 4, 't2.nano')''')

    conn.commit()
    print("Records inserted........")

    conn.close()

insert_data_aws()


