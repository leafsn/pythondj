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

