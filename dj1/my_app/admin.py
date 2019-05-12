from django.contrib import admin


# Register your models here.
from .models import Grades, Student, Text
# @admin.register(Student)

###  注册
class StudentInfo(admin.TabularInline):
    model = Student
    extra = 2

# 自定义页面
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]
    # 列表页属性
    list_display = ['pk', 'gname','gdate', 'ggirlnum', 'isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    # t添加修改页属性
    # fields = ['gname','gdate', 'ggirlnum', 'gboynum', 'isDelete']
    fieldsets = [
        ('num', {'fields': ['ggirlnum', 'gboynum']}),
        ('base', {'fields': ['gname', 'gdate', 'isDelete']})
    ]
    # 执行动作的位置下边
    actions_on_top = False
    actions_on_bottom = True
admin.site.register(Grades, GradesAdmin)


class StudentAdmin(admin.ModelAdmin):
    #方法实现男女显示
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    #设置页面列的名称
    gender.short_description = '性别'
    # 列表页属性
    list_display = ['pk', 'sname', 'sage', 'scontend', gender, 'isDelete']
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 5

    # 执行动作的位置下边
    actions_on_top = False
    actions_on_bottom = True
admin.site.register(Student, StudentAdmin)

# 站点注册Text
admin.site.register(Text)

