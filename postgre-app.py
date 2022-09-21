"""Communication with postgresql database."""

import psycopg2


# Connect to an existing database
conn = psycopg2.connect(
    database='exampledb',
    user='docker',
    password='docker',
    host='0.0.0.0'
)

# Open cursor to perform database operations
cur = conn.cursor()

while True:
    choice = int(input("""What od you want to do?:
1. Show data
2. Add new data
3. Delete data
4. Update data
0. Quit
Your choice: """))

    if choice == 1:
        # Query the database
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()

        if not len(rows):
            print('Empty')
        else:
            for row in rows:
                print(row)
    elif choice == 2:
        # Insert data
        name = input('Give me a name: ')
        age = int(input('Give me an age: '))
        cur.execute(f"INSERT INTO student (name, age) VALUES ('{name}', {age})")
    elif choice == 3:
        print('Delete current data')
        db_id = int(input('Give me an id: '))
        cur.execute(f'DELETE FROM student WHERE id={db_id}')

    elif choice == 4:
        print('Update current data')
        db_id = int(input('Give me an id: '))
        name = input('Give me a name: ')
        age  = int(input('Give me an age: '))
        cur.execute(f"UPDATE student SET name='{name}', age={age} WHERE id={db_id}")
    elif choice == 0:
        print('Have a nice day!')
        break

# Close communication with database
cur.close()
conn.close()
