# كلاس إعدادات التطبيق
class AppConfig:

    # متغير لتخزين النسخة الوحيدة
    instance = None

    # دالة إنشاء الكائن
    def __new__(cls):

        # إذا لم توجد نسخة مسبقًا
        if cls.instance is None:

            # إنشاء نسخة واحدة فقط
            cls.instance = super().__new__(cls)

        # إعادة نفس النسخة دائمًا
        return cls.instance


# إنشاء الكائن الأول
config1 = AppConfig()

# إنشاء الكائن الثاني
config2 = AppConfig()

# التحقق هل نفس النسخة
print(config1 == config2)