# استيراد مكتبة SQLite
import sqlite3


# دالة إنشاء قاعدة البيانات
def setup_database():

    # الاتصال بقاعدة البيانات
    connection = sqlite3.connect(
        "intellisystems.db"
    )

    # إنشاء Cursor
    cursor = connection.cursor()

    # إنشاء جدول المنتجات
    cursor.execute("""

    CREATE TABLE IF NOT EXISTS products (

        id INTEGER PRIMARY KEY,

        name TEXT,

        price REAL
    )

    """)

    # حفظ التغييرات
    connection.commit()

    # إغلاق الاتصال
    connection.close()

    # طباعة نجاح العملية
    print("تم إنشاء قاعدة البيانات")


# دالة إضافة منتج
def add_product():

    # الاتصال بقاعدة البيانات
    connection = sqlite3.connect(
        "intellisystems.db"
    )

    # إنشاء Cursor
    cursor = connection.cursor()

    # إضافة منتج
    cursor.execute("""

    INSERT INTO products (
        name,
        price
    )

    VALUES (?, ?)

    """, (
        "Laptop",
        1000
    ))

    # حفظ التغييرات
    connection.commit()

    # إغلاق الاتصال
    connection.close()

    # طباعة نجاح العملية
    print("تمت إضافة المنتج")


# دالة عرض المنتجات
def show_products():

    # الاتصال بقاعدة البيانات
    connection = sqlite3.connect(
        "intellisystems.db"
    )

    # إنشاء Cursor
    cursor = connection.cursor()

    # جلب المنتجات
    cursor.execute("""

    SELECT * FROM products

    """)

    # تخزين النتائج
    products = cursor.fetchall()

    # المرور على المنتجات
    for product in products:

        # طباعة المنتج
        print(product)

    # إغلاق الاتصال
    connection.close()


# إنشاء قاعدة البيانات
setup_database()

# إضافة منتج
add_product()

# عرض المنتجات
show_products()