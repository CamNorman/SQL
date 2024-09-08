import sqlite3
import pandas as pd

# Creating the connection to the database and the cursor
conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()

# load in csv thorugh a pandas dataframe

df = pd.read_csv('titanic.csv')

if __name__ == '__main__':
    # turb the df into a table called 'review'
    df.to_sql('review', conn, if_exists='replace')

# query the table to ensure that the data was truly added
    curs.execute('''SELECT * FROM review''')
    print(curs.fetchall())
