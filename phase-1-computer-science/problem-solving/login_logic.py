# اسم المستخدم الصحيح
correct_username = "admin"

# كلمة المرور الصحيحة
correct_password = "1234"

# اسم المستخدم المدخل
username = "admin"

# كلمة المرور المدخلة
password = "1234"

# التحقق من البيانات
if username == correct_username and password == correct_password:

    # طباعة نجاح تسجيل الدخول
    print("تم تسجيل الدخول بنجاح")

# إذا كانت البيانات خاطئة
else:

    # طباعة رسالة خطأ
    print("اسم المستخدم أو كلمة المرور غير صحيحة")