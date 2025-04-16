import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_user(email, name, password):
    conn=sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO user (email, name, password) VALUES (?, ?, ?)', (email, name, password))
    conn.commit()
    conn.close()
    
def find_user_by_email(email):
    conn=sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password FROM user WHERE email=?',(email,))
    user=cursor.fetchone()
    conn.close()
    return user

def find_user_by_email_and_password(email, password):
    conn=sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password FROM user WHERE email=? AND password=?', (email, password))
    user=cursor.fetchone()
    conn.close()
    return user

def update_user_avatar(user_id, avatar):
    conn=sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('UPDATE user SET avatar=? WHERE id=?',(avatar,user_id))
    conn.commit()
    conn.close()

def find_user_by_id(user_id):
    conn=sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password, avatar, birthday, gender FROM user WHERE id=?',(user_id,))
    user=cursor.fetchone()
    conn.close()
    return user

def update_user(user_id, name, birthday, gender):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE user SET name = ?, birthday = ?, gender = ? WHERE id = ?',(name,birthday,gender,user_id))
    conn.commit()
    conn.close()

def add_field(name, location, capacity, price, quality, description, image_path):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO fields (name, location, capacity, price, quality, description, image_path)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, location, capacity, price, quality, description, image_path))
    conn.commit()
    conn.close()

def get_all_fields():
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT * FROM fields')
    fields = cursor.fetchall()
    conn.close()
    return fields

def get_field_by_id(field_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT * FROM fields WHERE id = ?', (field_id,))
    field = cursor.fetchone()
    conn.close()
    return field

def get_field_schedule(field_id, date):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT time, status, user_id 
        FROM field_schedule 
        WHERE field_id = ? AND date = ?
        ORDER BY time
    ''', (field_id, date))
    schedules = cursor.fetchall()
    conn.close()
    return [{'time': s[0], 'status': bool(s[1]), 'user_id': s[2]} for s in schedules]

def initialize_field_schedule(field_id, date):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    
    # Generate time slots from 6:00 to 22:00
    times = [f"{hour:02d}:00" for hour in range(6, 23)]
    
    # Check if schedule already exists
    cursor.execute('SELECT COUNT(*) FROM field_schedule WHERE field_id = ? AND date = ?', (field_id, date))
    if cursor.fetchone()[0] == 0:
        # Insert new time slots
        for time in times:
            cursor.execute('''
                INSERT INTO field_schedule (field_id, date, time, status)
                VALUES (?, ?, ?, 0)
            ''', (field_id, date, time))
    
    conn.commit()
    conn.close()

def book_field(field_id, date, time, user_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    
    # Check if slot is available
    cursor.execute('''
        SELECT status 
        FROM field_schedule 
        WHERE field_id = ? AND date = ? AND time = ?
    ''', (field_id, date, time))
    result = cursor.fetchone()
    
    if result and not result[0]:
        # Update slot to booked
        cursor.execute('''
            UPDATE field_schedule 
            SET status = 1, user_id = ? 
            WHERE field_id = ? AND date = ? AND time = ?
        ''', (user_id, field_id, date, time))
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False

def cancel_booking(field_id, date, time, user_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE field_schedule 
        SET status = 0, user_id = NULL 
        WHERE field_id = ? AND date = ? AND time = ? AND user_id = ?
    ''', (field_id, date, time, user_id))
    
    success = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return success