# استيراد نظام تسجيل الدخول
from authentication.login_system import login_user

# استيراد عرض المنتجات
from database.database_products import (
    get_products
)

# استيراد البحث عن منتج
from products.product_search import (
    search_product
)

# استيراد نظام الشراء
from orders.purchase_system import (
    purchase_product
)


# عنوان النظام
print("===== IntelliSystems =====")

# تشغيل تسجيل الدخول
login_user(
    "admin",
    "1234"
)

# عرض قائمة الخيارات
print("\n1 عرض المنتجات")
print("2 البحث عن منتج")
print("3 شراء منتج")

# اختيار المستخدم
user_choice = input(
    "اختر عملية: "
)

# عرض المنتجات
if user_choice == "1":

    get_products()

# البحث عن منتج
elif user_choice == "2":

    product_name = input(
        "اسم المنتج: "
    )

    search_product(product_name)

# شراء منتج
elif user_choice == "3":

    purchase_product(
        "Phone",
        2000,
        True
    )

# إذا الخيار غير صحيح
else:

    print("خيار غير صحيح")