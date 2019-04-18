
from django.db import models

# Create your models here.
class Grades(models.Model):

    gname = models.CharField(max_length = 20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

    def createStudent(self, name, age, gender, contend,
                      grade, lastT, createT, isD=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime = lastT
        stu.createTime = createT
        return stu

class Student(models.Model):

    #自定义模型管理器
    stuObj = models.Manager()
    stuObj2 = StudentManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey("Grades", on_delete = models.CASCADE)
    def __str__(self):
        return self.sname

    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table: 'students'
        ordering = ['id']

    # 定义一个类方法创建对象
    @classmethod
    def createStudent(cls, name, age, gender, contend,
                      grade,lastT, createT, isD = False):
        stu = cls(sname = name, sage = age, sgender = gender,
                  scontend = contend, sgrade = grade, lastTime = lastT, createTime = createT, isDelete = isD)
        return stu

