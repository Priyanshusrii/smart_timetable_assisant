import sqlite3

def timetable():
    # 1. SETUP CONNECTION (Must be inside the function)
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor() 

    # 2. CREATE TABLE
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            day TEXT NOT NULL,
            time TEXT NOT NULL,
            room TEXT
        )
    ''')

    # 3. YOUR DATA (Example list)
    sample_classes = [
        #Monday

        ('Free lecture/Library','Monday','9:30 AM - 11:20 AM','Library'),

        ('Class Test','Monday','12:20 PM - 1:15 PM','N/A'),

        ('DBMS','Monday','1:15 PM - 2:30 PM','Class 306'),

        ('Free lecture/Self study','Monday','2:30 PM - 3:35 PM','Library'),

        ('Basic Eng','Monday','3:25 PM - 4:20 PM','Class 309'),



    #Tuesday

        ('SSAD','Tuesday','9:30 AM - 10:25 AM','New class 211'),

        ('Free Lecture/Self study','Tuesday','10:25 AM - 11:20 AM','N/A'),

        ('DBMS[lab]','Tuesday','12:20 PM - 2:10 PM','Lab 607/710'),

        ('Aiml[lab]','Tuesday','2:30 PM - 4:20 PM ','Lab 708/709 '),

        

    #Wednesday

        ('BM', 'Wednesday', '9:30 AM - 10:25 AM', 'Class 604'),

        ('Free Lecture / Self Study', 'Wednesday', '10:25 AM - 11:20 AM', 'N/A'),

        ('Data Visualization', 'Wednesday', '12:20 PM - 2:10 PM', 'Lab 704/705'),

        ('AI/ML', 'Wednesday', '2:30 PM - 3:25 PM', 'New Class 208'),

        ('BE 2', 'Wednesday', '3:25 PM - 4:20 PM', 'New Class 208'),



    # THURSDAY

        ('IPDC 1', 'Thursday', '9:30 AM - 10:25 AM', 'Class 305'),

        ('BM', 'Thursday', '10:25 AM - 11:20 AM', 'Class 308'),

        ('Free Lecture / Self Study', 'Thursday', '12:20 PM - 02:10 PM', 'Cafeteria'),

        ('SSAD Lab', 'Thursday', '02:30 PM - 04:20 PM', 'Lab 712/713'),



    # FRIDAY

        ('IPDC 1', 'Friday', '9:30 AM - 10:25 AM', 'New Class 210'),

        ('BM', 'Friday', '10:25 AM - 11:20 AM', 'New Class 210'),

        ('AI/ML', 'Friday', '12:20 PM - 1:15 PM', 'New Class 210'),

        ('SSAD', 'Friday', '1:15 PM - 2:10 PM', 'New Class 210'),

        ('Free Lecture / Self Study', 'Friday', '2:30 PM - 4:20 PM', 'N/A'),



    # SATURDAY

        ('SSAD', 'Saturday', '9:30 AM - 10:25 AM', 'Class 304'),

        ('Data Visualization', 'Saturday', '10:25 AM - 11:20 AM', 'Class 603'),

        ('BM', 'Saturday', '12:20 PM - 1:15 PM', 'Class 604'),

        ('AI/ML', 'Saturday', '1:15 PM - 2:10 PM', 'Class 604')
        ]
        

    # 4. RESET AND FILL
    
    cursor.execute("DELETE FROM classes") 
    cursor.executemany('INSERT INTO classes (subject, day, time, room) VALUES (?, ?, ?, ?)', sample_classes)

    # 5. COMMIT AND CLOSE
    conn.commit()
    conn.close()
    print("✅ Database Arranged Successfully!")


if __name__ == "__main__":
    timetable()