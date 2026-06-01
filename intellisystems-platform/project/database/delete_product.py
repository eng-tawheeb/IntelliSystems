# استيراد مكتبة SQLite
import sqlite3


# دالة حذف المنتج
def delete_product():

    # الاتصال بقاعدة البيانات
    connection = sqlite3.connect(
        "intellisystems.db"
    )

    # إنشاء Cursor
    cursor = connection.cursor()

    # حذف المنتج
    cursor.execute("""

    DELETE FROM products

    WHERE name = ?

    """, ("Laptop",))

    # حفظ التغييرات
    connection.commit()

    # إغلاق الاتصال
    connection.close()

    # طباعة نجاح العملية
    print("تم حذف المنتج")


# تشغيل النظام
delete_product()