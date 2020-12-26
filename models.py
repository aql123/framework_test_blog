from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# 继承了models.Model
class Category(models.Model):
    name = models.CharField('分类',max_length=100)    #字符串类型，最大长度100
    # 美化一下页面
    class Meta:
        verbose_name = '分类'     #页面显示汉语
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name        #把名字返回，汉语显示了

class Tags(models.Model):
    name = models.CharField('标签',max_length=100)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题',max_length=70)
    intro = models.TextField('摘要',max_length=200,blank=True)    #长文档
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类',default='1')     #一对			多关系 外键    为汉语
    tags = models.ManyToManyField(Tags,blank=True)      #多对多关系，blank 可以为空白
    body = models.TextField("内容")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')       #User表 Django自带的
    created_time = models.DateTimeField('发布时间',auto_now_add=True)
    # auto_now_add = True     自动添加时间
    keywords = models.CharField('文章关键词',max_length=120,blank=True,null=True)
    views = models.PositiveIntegerField('阅读量',default=0)
    # 取值范围为非负整数
    top = models.IntegerField(choices=[(0,'否'),(1,'是'),],default=0,verbose_name='是否推荐')
    modified_time = models.DateTimeField('修改时间',auto_now=True)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title