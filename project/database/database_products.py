# استيراد مكتبة SQLite
import sqlite3


# دالة جلب المنتجات
def get_products():

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

    # عنوان القائمة
    print("قائمة المنتجات")

    # المرور على المنتجات
    for product in products:

        # رقم المنتج
        product_id = product[0]

        # اسم المنتج
        product_name = product[1]

        # سعر المنتج
        product_price = product[2]

        # عرض المنتج
        print(
            product_id,
            product_name,
            product_price
        )

    # إغلاق الاتصال
    connection.close()


# تشغيل النظام
get_products()