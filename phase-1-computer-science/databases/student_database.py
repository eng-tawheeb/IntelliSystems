# استيراد مكتبة SQLite
import sqlite3

# الاتصال بقاعدة البيانات
connection = sqlite3.connect("students.db")

# إنشاء Cursor للتعامل مع قاعدة البيانات
cursor = connection.cursor()

# إنشاء جدول الطلاب
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (

    id INTEGER PRIMARY KEY,

    name TEXT,

    grade INTEGER
)
""")

# إضافة طالب جديد
cursor.execute("""

INSERT INTO students (name, grade)

VALUES (?, ?)

""", ("Ahmed", 95))

# حفظ التغييرات
connection.commit()

# طباعة نجاح العملية
print("تم حفظ الطالب بنجاح")

# إغلاق الاتصال
connection.close()