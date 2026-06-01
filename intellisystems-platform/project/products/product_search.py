# استيراد مكتبة SQLite
import sqlite3


# دالة البحث عن المنتج
def search_product(product_name):

    # الاتصال بقاعدة البيانات
    connection = sqlite3.connect(
        "intellisystems.db"
    )

    # إنشاء Cursor
    cursor = connection.cursor()

    # البحث عن المنتج
    cursor.execute("""

    SELECT * FROM products

    WHERE name = ?

    """, (product_name,))

    # جلب النتيجة
    product = cursor.fetchone()

    # إذا المنتج موجود
    if product:

        # طباعة المنتج
        print(product)

    # إذا المنتج غير موجود
    else:

        # طباعة رسالة خطأ
        print("المنتج غير موجود")

    # إغلاق الاتصال
    connection.close()


# تشغيل النظام
search_product("Laptop")