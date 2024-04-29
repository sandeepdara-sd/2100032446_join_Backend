import mysql.connector

conn = mysql.connector.connect(
    host="3306",
    user="root",
    password="password",
    database="safertek"
)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS locations (
                    location_id INT PRIMARY KEY,
                    street_address VARCHAR(255),
                    postal_code VARCHAR(50),
                    city VARCHAR(255),
                    state_province VARCHAR(255),
                    country_id CHAR(2),
                    FOREIGN KEY (country_id) REFERENCES countries(country_id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                    country_id CHAR(2) PRIMARY KEY,
                    country_name VARCHAR(255),
                    region_id INT
                )''')

locations = [
    (1000, '1297 Via Cola di Rie', '989', 'Roma', '', 'IT'),
    (1100, '93091 Calle della Te', '10934', 'Venice', '', 'TT'),
    (1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefecture', 'JP'),
    (1300, '9450 Kamiya-cho', '6823', 'Hiroshima', '', 'UP'),
    (1400, '2014 Jabberwock Rd', '26192', 'Southlake', 'Texas', 'US'),
    (1500, '2011 Interlors Blvd', '99236', 'South San', 'California', 'US'),
    (1600, '2007 Zagora St', '50090', 'South Brun', 'New Jersey', 'US'),
    (1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US'),
    (1800, '147 Spadina Ave', 'MSV 2L7', 'Toronto', 'Ontario', 'CA'),
]

countries = [
    ('AR', 'Argentina', 2),
    ('AU', 'Australia', 3),
    ('BE', 'Belgium', 1),
    ('BR', 'Brazil', 2),
    ('CA', 'Canada', 2),
    ('CH', 'Switzerland', 1),
    ('CN', 'China', 3),
    ('DE', 'Germany', 1),
]

cursor.executemany("INSERT INTO locations VALUES (%s, %s, %s, %s, %s, %s)", locations)
cursor.executemany("INSERT INTO countries VALUES (%s, %s, %s)", countries)

conn.commit()

cursor.execute('''SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
                  FROM locations l
                  JOIN countries c ON l.country_id = c.country_id
                  WHERE c.country_name = 'Canada' ''')

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
