

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



元选项

在模型中定义Meta类

 定义数据表名,推荐使用小写字母,数据表名默认为项目名小写_类名小写

db_table =""

对象的默认排序字段,获取对象的列表时使用,排序会增加数据库的开销

ordering =[]

ordering["id"] 升序

ordering["-id"] 降序

### 模型成员

> 类属性 objects
>
> 是Manager类型的一个对象,作用是与数据库进行交互
>
> 当定义模型累是没有指定管理器,则django为创建一个objects的管理器

自定义管理器manager类

```python
class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

```



#### 创建对象

1. 在自定义管理七类中添加方法创建对象
2.  定义一个方法创建对象

#### 模型查询：

> 查询集

1. 再管理器上调用过滤方法返回查询集
2. 查询集经过过滤器筛选后返回新的查询集，所以可以写成链式调用
3. 惰性执行     创建查询集不会带来数据的访问，直到调用数据时，才会访问数据



>  返回查询集的方法称为过滤器 

1. all()
2. filter()  返回符合条件的数据     filter(key = value)       filter(key = value, key1 = value1)    filter(key = value).filter(key = value)
3. exclude()    过滤符合条件的数据
4. order_by()   排序
5. values()      一条数据就是一个对象（字典），返回一个列表

>  返回单个数据

1. get()    返回一个满足条件的对象，如果没有找到符合条件的对象，会引发 模型类.DoesNotExist异常，如果找到多个对象，会引发模型类.MultipleObjectsReturned异常
2. count()    返回当前查询集中的个数
3. first()	返回查询集中的第一个对象
4. last()         返回查询集中的最后一个对象
5. exists()      判断查询集中是否有数据，有返回True

> 限制查询集

查询返回列表，可以使用下标的方法进行限制，等同于sql中的limit语句，下标不能是负数。

> 查询集的缓存

每个查询集都包含一个缓存，来最小化的对数据库访问

再新建的查询集中，缓存首次为空，第一次对查询集求值，会发生数据缓存，django会将查询出来的数据做一个缓存，以后查询直接使用查询集的缓存。

> 字段查询

实现sql中的where语句，作为方法filter()、exclude()、get()的参数

​	属性名称__比较运算符 = 值

​	外键：属性名_id

​	转义： 类似sql中的like语句，

> 比较运算符

```python
#### 以下四个 在前面加上 i, 就不区分大小写

# exact      判断，大小写敏感    filter(isDelete = False)   iexact

# contains   包含    大小写敏感            icontains

studentList = Student.stuObj.filter(sname__contains = "ass")

# startswith、endswith 以value开头或结尾   大小写敏感     istartswith    iendswith

studentList = Student.stuObj.filter(sname__startswith = "ass")
```

```python
# isnull、 isnotnull   是否为空          filter(sname_isnull = False)
# in  是否包含在范围内   filter(pk__in = [2, 4, 5])
# gt gte  大于、大于等于  filter(sage_gt = 30)
# lt lte  小于、小于等于
# year、month、day、week_day、hour、minute、second   年、月、日、星期、时、分、秒
	filter(sage__year = 2019)
```

> 跨关联查询



查询快捷              pk    代表的主键

> 聚合函数

使用 aggregate()函数返回聚合函数的值

Avg    平均值

Count   个数

Max      最大值  

​	maxAge = studentList = Student.stuObj.aggregate(Max('sage'))

Min         最小值

Sum      求和

> F对象
>
> 可以使用模型的A属性与B属性进行比较
>
> ```python
> g = Grades.objects.filter(ggirlnum__gt=F('gboynum'))
> # 支持F对象的算术运算
> g = Grades.objects.filter(ggirlnum__gt=F('gboynum') + 20)
> ```

> Q对象
>
> 过滤器的方法中的关键字参数，条件为And模式
>
> 使用Q对象进行or查询

### 视图

 视图接受web请求，并响应web请求

视图就是一个python中的函数

相应： 网页，重定向，JSON数据，错误视图

> url配置

指定根级url配置文件   setting.py中的ROOT_URLCONF

urlpatterns  一个url实例的列表   url对象   正则表达式、视图名称、名称

> url配置的反向解析

如果在视图、模板中使用硬编码，在url配置发生改变时，动态生成链接地址

在使用链接时，通过url配置的名称，动态生成url地址

使用url模板

> 视图函数

定义视图   视图参数  一个HttpRequest的一个实例

​		通过正则表达式获取的参数

一般在views.py文件下定义

>  错误视图
>
> 404  找不到网页   url匹配不成功，在templates目录下定义404.html   》request_path错误网址
>
> ​	配置settings.py    Debug = False    Allowed_hosts = ['*']
>
> 500  在视图代码中出现的错误
>
> 400  错误出现在客户的操作  			



### HttpRequest对象

> path:   请求的完整路经
>
> method:  表示请求的方式，常用的get，post
>
> encoding 表示浏览器提交的数据的编码方式
>
> GET  : 类似字典的对象，包含了get请求的所有参数
>
> POST： 类似字典的对象，包含了post请求的所有参数
>
> FILES :  类似字典的对象，包含了所有上传的文件
>
> COOKIES :  字典，包含所有的cookie
>
> SESSION :   表示当前会话

> 方法： is_ajax()    如果是通过XMLHttpRequest发起的，返回True

> QuertDict对象    request对象中的GET、 POST都属于QuseryDict对象
>
> 方法：   get()   根据键获取值              getlist() 将键的值以列表的形式返回

##### GET     

```
a = request.GET.getlist('a')
```

##### POST

```
name = request.POST.get('name')
```

#### HttpResponse对象

> 给浏览器返回数据        httpresponse对象由程序员创建

> 不调用模板，直接返回数据
>
> 调用模板，使用render方法：render(request, 模板名称，{传到模板的数据})

> 属性：content 内容,charset 编码, status_code, content-type输出类型

> 方法
>
> ​	init:  使用页面内容实例化HttpResponse对象
>
> ​	write(content) ：以文件形式写入
>
> ​	flush():    以文件的形式输出缓冲区 
>
> ​	set_cookie(key, value='', max_age=None,exprise=None)
>
> ​	delete_cookie(key)   删除cookie

> 子类HttpResponseRedirect
>
> ​	重定向   简单方法，from django.shortcuts import redirect
>
> ​	return redirect('/')
>
> 子类JsonResponse
>
> ​	返回json数据，一般用于异步请求
>
> ​	____init____(self, data)      字典对象

### 状态保持

启用session    settings文件中 ，INSTALLED_APPS, MIDDLEWARE 默认启用

使用session	在启用session后，每个httpRequest对象都有一个session属性，一个类似字典的对象

​	get(key, default=None)  	根据键获取session值

​	clear() 	清空所有的会话

​	flush() 	删除当前的会话并删除会话的cookie



设置过期时间 request.session.set_expiry(10)     十秒钟之后过期 

如果不设置，两个星期后过期，

0	关闭浏览器过期

None 	永不过期





存储session的位置

​	数据库，缓存，

用redis存储缓存



### 模板

> 定义模板: 传递变量的值,遵守标识符语法规则,

{{ var }} 如果使用的变量不存在,就是空字符串

在模板中使用点语法,字典查询,属性或者方法,数字索引(调用方法时不能传递参数)

> #### 标签
>
> ​	{% tag %}  
>
> 1. 在输出中创建文本
> 2. 控制逻辑和循环
>
> if,    {% if %}  {% elif  %} {% else %}   {% endif %}
>
> for,   {% for %}  {% empty %} (列表为空或者列表不存在时执行之后的语句)  {% endfor %}
>
> ​	{{ forloop.counter }}   在for里使用,显示当前循环了几次
>
> comment,     注释多行, {% comment %}  {% endcomment %}
>
>  ifequal, ifnotequal 判断是否相等或者不相等, 
>
> ​	{% ifequal 值1 值2 %}    {% endifequal %} 
>
> include, 	加载模板并以标签内的参数渲染    {% include '模板目录' 参数1 参数2 %}
>
> url,     反向解析    {% url ' namespace : name ' p1 p2 %}
>
>  csrf_token,      用于跨站请求伪造保护   {% csrf_token %}
>
> block,  extends,   用于模板的继承
>
> autoescape,   

> #### 过滤器
>
> ​	语法: {{ var|过滤器 }}           在变量被显示前修改它
>
>  	1. upper   大写
>  	2. lower   小写
>
> 过滤器可以传递参数,参数用引号引起来
>
> 3. join    列表|join : '#'	 用一个符号把列表中的成员连起来
>
> 4. default       如果一个表里没有提供,或者值为false, 空,可以使用默认值,	{{ var | default : ' default ' }}
>
> 5. date    根据给定格式转换日期为字符串            {{ dateVal | date : 'y-m-d' }}
>
> 6. escape     HTML转义
>
> 7. 加减乘除        
>
>      add      {{num | add:10 }}
>
>      widithradtio   {% num widthratio num 1 5 %}   (num/1*5)
>
>    divisibleby 模运算

> #### 注释
>
>  	1. 单行注释	{{# 注释内容 #}}
>  	2. 多行注释   {% comment %}

> 反向解析   名称空间url

> 模板继承
>
>   可以减少页面内容的重复定义,页面重用
>
> block标签	在父母版中预留区域,子模板去填充
>
> ​	{% block 标签 %}    {% endblock 标签名 %}
>
> extends标签    继承模板,需要写在模板文件的第一行
>
> ​	{% extend 父模板路径  %}

> **HTML**转义
>
> ​	将传入的html代码字符串转义为 html 代码渲染
>
>  	1. {{ code | safe }}
>
> 2. {% autoescape off %}  {{ code }}  {% endautoscape %}

> #### CSRF 
>
> 跨站请求伪造, 某些恶意网站包含链接,表单,按钮,根据js进行攻击
>
> 防止 {% csrf_token %}

> ### 验证码
>
> 在用户注册, 登录页面的时候使用,为了防止暴力请求,减轻服务器的压力
>
> 

### 静态文件

配置setting文件   STATICFILES_DIRS = []



#### 中间件

​	一个轻量级,底层的插件,可以介入到django的请求和相应 一个Python类

​	方法: __ __init__ __ 不需要传参,服务器

 	1. process_request(self, request) 在执行视图之前被调用,每个请求上都会调用,返回None或者HttpResponse
 	2. process_view(self, request, view_fun, view_args, view_lwargs)  调用视图之前执行,返回None或者HttpResponse
 	3. process_template_response(self, request, response) 在试图刚好执行完后调用,每个请求都会调用,返回一个HttpResponse对象
 	4. process_response(self, request, response) 所有相应返回浏览器之前调用,每个请求都会调用,返回一个HttpResponse对象
 	5. process_exception(self, request, exception) 当视图抛出异常时调用,返回一个HttpResponse对象

在工程目录下创建一个middleware,创建app目录建立Python文件,

​	from django.utils.deprecation import MiddlewareMixin

​	配置settings.py MIDDLEWARE  中添加'middleware.myapp.myMiddle'



#### 上传图片

在static目录下创建upfile目录用于存储

settings.py 配置 MDEIA_ROOT =os.path.join(BASE_DIR, 'static/upfile')

上传文件需加enctype="multipart/form-data"

### 分页

1. >  paginator对象
   >
   > Paginator(列表, 整数)
   >
   > 属性
   >
   > ​	count 对象总数
   >
   > ​	num_pages 页面总数
   >
   > ​	page_range(页码列表)
   >
   > 方法: page(num) 获取一个page对象, 如果提供的页码不存在,会抛出InvalidPage异常
   >
   > 异常:
   >
   > ​	InvalidPage 当想page()传递一个个无效的页码时抛出
   >
   > ​	pageNotAnInteger   当向page()传递的不是一个整数时抛出
   >
   > ​	EmptyPage     页面没有数据是抛出
2. >  page对象
   >
   > Paginator对象的page()方法赶回得到page对象
   >
   > 属性:
   >
   > ​       object_list   当前页上所有的数据列表
   >
   > ​       number  当前页的页码值
   >
   > ​       paginator   当前page对象关联的paginator对象
   >
   > 方法:
   >
   > ​      has_next()    是否有下一页
   >
   > ​      has_previous()    是否有上一页
   >
   > ​      has_other_pages()   是否有上一页或下一页
   >
   > ​     next_page_number()   返回下一页的页码,不存在抛出InvalidPage异常
   >
   > ​     previous_page_number()  返回上一页的页码,不存在抛出InvalidPage异常
   >
   > ​     len()  
   >
   > ```python
   > from django.core.paginator import Paginator
   > def stupage(request, pageid):
   >     allList = Student.objects.all()
   >     paginator = Paginator(allList, 3)
   >     page = paginator.page(pageid)
   >     return render(request, 'my_app/studentpage.html', {'students':page})
   > ```
   >
   > ```html
   > <body>
   >     <table>
   >         {% for stu in students %}
   >         <tr>
   >             <td>{{stu.sname}}</td>
   >             <td>{{stu.sage}}</td>
   >             <td>{{stu.sgender}}</td>
   >         </tr>
   >          {% endfor %}
   >     </table>
   >     <ul>
   >         {% for index in students.paginator.page_range %}
   >             {% if index == students.number %}
   >                 {{index}}
   >             {% else %}
   >             <li>
   >                 <a href="/myapp/stupage/{{ index }}/">{{index}}</a>
   >             </li>
   >             {% endif %}
   >         {% endfor %}
   >     </ul>
   > </body>
   > ```

###　Ajax

```python
from django.http import JsonResponse
def studentsinfo(request):
    stus = Student.objects.all()
    list = []
    for stu in stus:
        list.append([stu.sname,stu.sage,stu.sgender])
    return JsonResponse({'data':list})
```

```js
$.ajax({
    type: 'get',
    url: '/myapp/studentsinfo/',
    dataType: 'json',
    success:function (data, status) {
        console.log(data)
        var d = data.data;
        for (var i =1; i < d.length; i++) {
            document.write('<p>' + d[i][0] + '---'+ d[i][1] + '</p>');
        }
    }
```

### 富文本

​	pip install django-tinymce

​	在站点中使用

```
# 配置settings.py文件    INSTALLED_APP添加tinymce
TINYMCE_DEFAULT_CONFIG = {
    'theme' : 'advanced',
    'width' : 600,
    'height': 400,
}

#富文本
from  tinymce.models import HTMLField
class Text(models.Model):
    str = HTMLField()
    
# 站点注册Text
admin.site.register(Text)
```

自定义视图中使用

```html
<script src="/static/tiny_mce/tiny_mce.js"></script>
<script>
    tinyMCE.init({
        'mode' : 'textareas',
        'theme': 'advanced',
        'width' : 800,
        'height' : 400,
    })
</script>

<form>
    <textarea name="str">123</textarea>
</form>
```

​	

### celery 

 网站每隔一段时间更新一次,

 	将耗时的操作放到celery中执行

​	使用celery定时执行

celery

​	任务: 本质是一个Python函数,将耗时操作封装成一个函数

​	队列: 将要执行的任务放队列里

​	工人: 负责执行队列中的任务

​	代理: 负责调度

安装: 

​	pip install celery

​	pip install celery-with-redis

​	pip install django-celery

配置settings.py

​	INSTALLED_APP   添加 djcelery

```python
# celery
import djcelery
djcelery.setup_loader()  # 初始化
BROKER_URL='redis://:123456@127.0.0.1:6379/0'
CELERY_IMPORTS = ('my_app.task')
```

​	创建my_app/task.py

​	执行迁移,生成celery需要的数据表

​	在工程目录下的_____init_____.py中添加

​	