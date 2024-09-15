import pandas as pd
import psycopg2
from os import getenv


# "User & Default Database" from Elephant
DBNAME = 'psthuxpu'
USER = 'psthuxpu'

# "Password" from Elephant
PASSWORD = 'zxFmABhuwumP8sRLEpZMr3a47ldLY4F-'

# "Server" from Elephant 
HOST = 'bubble.db.elephantsql.com'

# Create cursor and connection
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()

# Creation of the table and calling all columns
TITANIC_TABLE = '''
CREATE TABLE IF NOT EXISTS titanic_table(
    passenger_id SERIAL PRIMARY KEY,
    survived INT NOT NULL,
    p_class INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    age FLOAT NOT NULL,
    spouse_sibling_aboard INT NOT NULL,
    parents_children_aboard INT NOT NULL,
    fare FLOAT NOT NULL
);
'''

# Calling function that will gather wanted data through queries
def execute_query_pg(curs, conn, query):
    results = curs.execute(query)
    conn.commit()
    return results


df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", '')
df.drop(columns=['Ticket', 'Cabin', 'Embarked'], inplace=True)
df.fillna(0, inplace=True)

# Initializing the connection and cursor from first call of dataset
if __name__ == '__main__':

    execute_query_pg(pg_curs, pg_conn, '''
                    DROP TABLE IF EXISTS titanic_table 
                        ''')
    execute_query_pg(pg_curs, pg_conn, TITANIC_TABLE)

    records = df.values.tolist()
    
    for record in records:
        INSERT_TABLE = f'''
        INSERT INTO titanic_table(passenger_id,survived, p_class, name, sex, age, spouse_sibling_aboard, parents_children_aboard,fare)
        VALUES {tuple(record)};
        '''
        execute_query_pg(pg_curs, pg_conn, INSERT_TABLE)
