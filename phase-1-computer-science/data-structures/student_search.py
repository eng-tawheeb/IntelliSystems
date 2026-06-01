# قائمة الطلاب
students = [
    "Ahmed",
    "Ali",
    "Mohammed",
    "Khaled",
    "Sara"
]

# اسم الطالب المطلوب البحث عنه
student_name = "Khaled"

# متغير لمعرفة هل تم العثور
found = False

# البحث داخل القائمة
for student in students:

    # التحقق من اسم الطالب
    if student == student_name:

        # طباعة النجاح
        print("تم العثور على الطالب")

        # تحديث الحالة
        found = True

        # إيقاف البحث
        break

# إذا لم يتم العثور
if not found:

    # طباعة رسالة عدم وجود
    print("الطالب غير موجود")