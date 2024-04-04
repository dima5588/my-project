from django.contrib import admin

from main.models import Teacher, Students, Group

admin.site.register(Teacher)
# admin.site.register(Students)
admin.site.register(Group)


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('stud_full_name')

    def student_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    def groups_list(self, obj):
        print(obj, '!!!!!!!!!!!!!!')
        return 'Dima viper'

    gtk


