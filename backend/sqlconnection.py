import mysql
import os, time
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("DATABASE_NAME"))

class SQLconnect:
    def __init__(self):
        self.sql = self._connect()
        
        
    def _connect(self) -> mysql.MySQLConnection | None:
        for attempt in range(1, 6):
            try:
                
                conn = mysql.connect(
                    user=os.getenv("DATABASE_USER"),
                    host=os.getenv("DATABASE_HOST"),
                    database=os.getenv("DATABASE_NAME"),
                    passwd=os.getenv("DATABASE_PASSWORD"),
                    port=int(os.getenv("MYSQLPORT", 3306)),
                    connection_timeout=10,
                    autocommit=False,
                )
                
                
                print(f"[DB] Connected on attempt {attempt}")
                return conn
            except Exception as e:
                wait = 2 ** (attempt - 1)
                print(f"[DB] Attempt {attempt} failed: {e}  — retrying in {wait}s")
                time.sleep(wait)

        print("[DB] All connection attempts failed.")
        return None
    
    def _ping(self):
        if not self.sql:
            print("[DB] No active connection object to ping. Attempting fresh reconnect...")
            self.sql = self._connect()
            return self.sql is not None and self.sql.is_connected()

        try:
            # Reconnects automatically if connection was dropped
            self.sql.ping(reconnect=True, attempts=5, delay=2)
            return True
        except Exception as e:
            print(f"[DB] Ping failed:")
            return False

_sql = SQLconnect()


class UserManager:
    def __init__(self):
        pass
    
    def validate_user(self, username_or_email, password, role):
        conn = _sql._ping()
        cur = conn.cursor()
        
        result = cur.execute("""
                    SELECT * FROM users WHERE role = ?
                    """)
        
        cur.close()
        
    def add_user(self, data, add_by):
        pass
    
    def delete_user(self, id, delete_by):
        pass
    
    def update_user(self, id, update_by):
        pass
    
    
class FormManager:
    def add_form(self, data):
        pass
    
    def validate_form(self, form_id, validate_by):
        if not "sub.validate" in validate_by.get("permissions"):
            return {"denied":"x"}
        pass
    
    def edit_form(self, from_id, edit_by):
        if not "sub.edit" in edit_by.get("permissions"):
            return
        
        pass
    
    def delete_form(self, form_id, deleted_by):
        pass
    
    def see_all_form(self, user):
        if not "forms.read" in user.get("permissions"):
            return
        
        pass
    
    
    
    
        
usermanage = UserManager()
formvalidation = FormManager()

        