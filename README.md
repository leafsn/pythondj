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

#直接添加关联的没有的类
>>> grade1 = Grades()
>>> grade1.gname = 'C++'
#执行直接添加到数据库
>>> gr.student_set.create(sname = 'aaa', sgender = True, scontend = '123456', sage = 18)

```



