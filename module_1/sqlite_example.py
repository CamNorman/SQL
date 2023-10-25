import sqlite3
import queries as q

# step 1
# connect to database
connection = sqlite3.connect('rpg_db.sqlite3')
# step 2
# its like a bank teller
cursor = connection.cursor()
# step 3

# step 4 EXECUTE
results = cursor.execute(q.SELECT_ALL).fetchall()
print(results[:5])
