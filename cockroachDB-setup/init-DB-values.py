import psycopg2

# connect to database
#ENTER YOUR DB LINK HERE:
DATABASE_URL = ""
conn = psycopg2.connect(DATABASE_URL)

# create a cursor object
cur = conn.cursor()


# attempt each sql statement individually
try:
    conn.cursor().execute("DROP TABLE IF EXISTS people")
    conn.commit()
    conn.cursor().execute("CREATE TABLE IF NOT EXISTS people (firstname varchar(255) PRIMARY KEY, lastname varchar(255),interest varchar(255), position varchar(255),picture varchar(255))")
    conn.commit()
    conn.cursor().execute("INSERT INTO people (firstname, lastname, interest, position,picture) VALUES ('Henry', 'Chen', 'JA Central Ontario', 'Business Student', 'https://i.imgur.com/zWYFcFs.jpg')")
    conn.commit()
    conn.cursor().execute("INSERT INTO people (firstname, lastname, interest, position,picture) VALUES ('Rhea', 'Mangat', 'Western AI', 'Student', 'https://i.imgur.com/hLWVB66.jpg')")
    conn.commit()
    conn.cursor().execute("INSERT INTO people (firstname, lastname, interest, position,picture) VALUES ('Victoria', 'Da Rosa', 'Bill Gates', 'Computer Engineering Student', 'https://i.imgur.com/4xNpeL4.jpg')")
    conn.commit()
    conn.cursor().execute("INSERT INTO people (firstname, lastname, interest, position,picture) VALUES ('Andréa', 'Jackson', 'Ryan Reynolds', 'Schulich Leader', 'https://i.imgur.com/zqH919A.jpg')")
    conn.commit()
    cur.execute("SELECT * FROM people")
    conn.commit()
    print(cur.fetchall())
except Exception as er:
    print("ERROR: ", er)
