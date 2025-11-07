import psycopg2

conn = psycopg2.connect(database="studentsA3",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port="5433")

db = conn.cursor()

# Create the table if it doesn't exist
db.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);
""")

# insert
insert_query = """
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
"""

db.execute(insert_query)
conn.commit()

print("Table checked and data inserted successfully!")

db.close()
conn.close()

