import psycopg


class UserConnection():
    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=admin host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()
            
    
    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM users
                               """)
            return data.fetchall()
        
        
    def read_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute(""" 
                SELECT * FROM users WHERE id = %s
                               """, (str(id),))
            return data.fetchone()
    
    def write(self, data):
        # working in context "with" helps closing the connection when there's an error or after the execution is done
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "users"(name, phone) VALUES(%(name)s, %(phone)s)
                        """, data)
        self.conn.commit()
        
        
    def delete(self, id: int):
        with self.conn.cursor() as cur:
            cur.execute(""" 
                DELETE FROM users WHERE id = %s
                        """, (str(id),))
        self.conn.commit()
            
            
    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE users SET name = %(name)s, phone = %(phone)s WHERE id = %(id)s """, data)
        self.conn.commit()
            
    def __def__(self):
        self.conn.close()
