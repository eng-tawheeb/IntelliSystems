# قائمة المنتجات داخل المتجر
products = [

    # المنتج الأول
    {
        # اسم المنتج
        "name": "Laptop",

        # سعر المنتج
        "price": 1000
    },

    # المنتج الثاني
    {
        # اسم المنتج
        "name": "Phone",

        # سعر المنتج
        "price": 500
    },

    # المنتج الثالث
    {
        # اسم المنتج
        "name": "Mouse",

        # سعر المنتج
        "price": 50
    }
]


# دالة ترتيب المنتجات
def sort_products_by_price():

    # ترتيب المنتجات حسب السعر
    sorted_products = sorted(

        # قائمة المنتجات
        products,

        # الترتيب حسب السعر
        key=lambda product:
        product["price"]
    )

    # عرض عنوان القائمة
    print("ترتيب المنتجات")

    # المرور على المنتجات
    for product in sorted_products:

        # عرض اسم المنتج
        print(product["name"])

        # عرض السعر
        print(product["price"])


# تشغيل النظام
sort_products_by_price()