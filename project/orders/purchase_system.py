# قائمة المنتجات داخل المتجر
products = {

    # اسم المنتج وسعره
    "Laptop": 1000,

    # اسم المنتج وسعره
    "Phone": 500,

    # اسم المنتج وسعره
    "Mouse": 50
}


# دالة تنفيذ عملية الشراء
def purchase_product(
        product_name,
        user_balance,
        has_discount
):

    # التحقق هل المنتج موجود
    if product_name not in products:

        # طباعة رسالة خطأ
        print("المنتج غير موجود")

        # إيقاف الدالة
        return

    # الحصول على سعر المنتج
    product_price = products[product_name]

    # إذا يوجد خصم
    if has_discount:

        # تطبيق خصم 20%
        discount_amount = product_price * 0.20

    # إذا لا يوجد خصم
    else:

        # لا يوجد خصم
        discount_amount = 0

    # حساب السعر النهائي
    final_price = (
        product_price - discount_amount
    )

    # التحقق هل الرصيد كافي
    if user_balance >= final_price:

        # خصم السعر النهائي
        remaining_balance = (
            user_balance - final_price
        )

        # طباعة نجاح العملية
        print("تم الشراء بنجاح")

        # طباعة المنتج
        print(product_name)

        # طباعة السعر النهائي
        print(final_price)

        # طباعة الرصيد المتبقي
        print(remaining_balance)

    # إذا الرصيد غير كافٍ
    else:

        # طباعة رسالة خطأ
        print("الرصيد غير كافٍ")


# تشغيل النظام
purchase_product(

    # اسم المنتج
    "Laptop",

    # الرصيد الحالي
    1500,

    # هل يوجد خصم؟
    True
)