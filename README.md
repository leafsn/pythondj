### Django

```shell
#创建django项目
django-admin startporject dj1

#创建APP
python3 manage.py startapp my_app

#生成迁移文件
python3 manage.py makemigrations

#执行迁移生成数据库表
python manage.py migrate
```

生成迁移文件可能报错

```shell
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11.None
## 解决方法
找到到文件中注释掉
 if version < (1, 3, 3):
    raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
```
> 测试数据操作 进入Python shell
```shell
    python3 manage.py shell
    
# 引入包
>>> from  my_app.models import Grades, Student
>>> from django.utils import timezone
>>> from datetime import * 

# 查询所有数据:
>>> Grades.objects.all()

# 查询出来某一个对象
>>> Grades.bojects.get(pk = 2)

# 创建对象数据
>>> grade = Grades()
>>> student = Student()

# 添加数据
>>> grade.gname = 'python'
>>> grade.save()

# 再次 修改数据 模型对象.属性 = 新值
>>> grade.gname = 'java'
>>> grade.save()

# 删除数据 模型对象.delete()(物理删除,数据库里被删除)
>>> grade.delete()

#获取关联对象的集合 对象名.关联的类名小写_set.all()
>>> grade.student_set.all()

>>> student.sgrade = grade
#直接添加关联的没有的类
>>> gr = Grades.objects.get(pk = 1)
#执行直接添加到数据库
>>> gr.student_set.create(sname = 'aaa', sgender = True, scontend = '123456', sage = 18)

```

### 启动服务器

> python manage.py runserver ip:port   ip默认本机,port默认8000

```shell
>>> python manage.py runserver localhost:8000
```

### admin站点管理

1. 内容发布
   1. 负责添加,修改,删除内容
2. 公告访问



> ##### 添加管理
>
> 在settings.py中添加 django.contrib.admin 默认是已经添加



> ##### 创建管理用户
>
> python3 mange.py createsuperuser  
>
> 依次输入用户名,邮箱,密码



> ##### 管理数据表
>
> 修改admin.py 的文件

```python
from .models import Grades, Student

# 注册
admin.site.register(Grades)

admin.site.register(Student)
```

> 自定义管理页面

``` python
## 列表页属性
class GradesAdmin(admin.ModelAdmin):
    # 添加学生 StudentInfo  下面定义
    inlines = [StudentInfo]
    
    #显示字段
    list_display = []
    #过滤字段
    list_filter = []
    #搜索字段
    search_fields = []
    #分页显示条数
    list_per_page = 5

    ## 添加修改页
    # 属性的先后顺序
    fields = []
    # 给属性分组, 不能与fields同时使用
    fieldsets =[
        (),
        (),
    ]
    # 执行动作的位置下边
    actions_on_top = False
    actions_on_bottom = True

#创建grade 直接添加两个student 
class StudentInfo(admin.TabularInline):
    model = Student
    extra = 2
## 注册自定义页面
admin.site.register(Grades, GradesAdmin)
 
## 布尔显示问题
#方法实现男女显示
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    #设置页面列的名称
    gender.short_description = '性别'

```

> 使用装饰器注册
>
> @admin.register(Student)
>
> 注释  admin.site.register(Grades, GradesAdmin)





### 视图的基本使用



配置模板路径   修改settings.py文件下的templates

path运用正则匹配   引入 re_path