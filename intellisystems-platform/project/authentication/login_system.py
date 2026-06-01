# قاعدة بيانات المستخدمين المؤقتة
users_database = {

    # اسم المستخدم وكلمة المرور
    "admin": "1234",

    # اسم المستخدم وكلمة المرور
    "ahmed": "5678",

    # اسم المستخدم وكلمة المرور
    "mohammed": "9999"
}


# دالة تسجيل الدخول
def login_user(
        username,
        password
):

    # التحقق هل المستخدم موجود
    if username not in users_database:

        # طباعة رسالة خطأ
        print("اسم المستخدم غير موجود")

        # إيقاف الدالة
        return

    # جلب كلمة المرور الصحيحة
    correct_password = (
        users_database[username]
    )

    # التحقق من كلمة المرور
    if password == correct_password:

        # طباعة نجاح العملية
        print("تم تسجيل الدخول بنجاح")

        # طباعة اسم المستخدم
        print(username)

    # إذا كلمة المرور خاطئة
    else:

        # طباعة رسالة خطأ
        print("كلمة المرور غير صحيحة")


# تشغيل النظام
login_user(

    # اسم المستخدم
    "admin",

    # كلمة المرور
    "1234"
)