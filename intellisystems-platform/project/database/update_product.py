# استيراد مكتبة SQLite
import sqlite3


# دالة تعديل المنتج
def update_product_price():

    # الاتصال بقاعدة البيانات
    connection = sqlite3.connect(
        "intellisystems.db"
    )

    # إنشاء Cursor
    cursor = connection.cursor()

    # تعديل سعر المنتج
    cursor.execute("""

    UPDATE products

    SET price = ?

    WHERE name = ?

    """, (
        1200,
        "Laptop"
    ))

    # حفظ التغييرات
    connection.commit()

    # إغلاق الاتصال
    connection.close()

    # طباعة نجاح العملية
    print("تم تعديل سعر المنتج")


# تشغيل النظام
update_product_price()