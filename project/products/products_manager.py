# قائمة المنتجات داخل المتجر
products = [

    # بيانات المنتج
    {
        "name": "Laptop",

        "price": 1000
    },

    # بيانات المنتج
    {
        "name": "Phone",

        "price": 500
    },

    # بيانات المنتج
    {
        "name": "Mouse",

        "price": 50
    }
]


# دالة عرض المنتجات
def show_products():

    # عرض عنوان القائمة
    print("قائمة المنتجات")

    # المرور على كل منتج
    for product in products:

        # عرض اسم المنتج
        print(product["name"])

        # عرض السعر
        print(product["price"])


# تشغيل النظام
show_products()