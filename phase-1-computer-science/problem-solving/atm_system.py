# الرصيد الحالي للمستخدم
current_balance = 1000

# المبلغ المراد سحبه
withdraw_amount = 300

# التحقق هل الرصيد يكفي
if withdraw_amount <= current_balance:

    # خصم المبلغ من الرصيد
    current_balance -= withdraw_amount

    # طباعة نجاح العملية
    print("تم السحب بنجاح")

    # عرض الرصيد الجديد
    print(current_balance)

# إذا الرصيد غير كافٍ
else:

    # طباعة رسالة خطأ
    print("الرصيد غير كافٍ")