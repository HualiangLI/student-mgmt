from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    用户资料
    '''
    user = models.OneToOneField(User, related_name='related_profile', on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField(max_length=200, verbose_name='姓名')
    is_supervisor = models.BooleanField(default=False, verbose_name='导师')
    is_student = models.BooleanField(default=False, verbose_name='学生')
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='导师', null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = verbose_name = '用户资料'

class Department(models.Model):
    '''
    科室
    '''
    name = models.CharField(max_length=200, verbose_name='名称')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = verbose_name = '科室'

class Student(models.Model):
    '''
    学生
    '''
    Degree = models.TextChoices('学位', '硕士 博士')
    Grade = models.TextChoices('年级', '一年级 二年级 三年级')
    TrainingType = models.TextChoices('培养类别', '学术型 专业型')

    degree = models.CharField(max_length=32, choices=Degree.choices, verbose_name='学位')
    grade = models.CharField(max_length=32, choices=Grade.choices, verbose_name='年级')
    training_type = models.CharField(max_length=32, choices=TrainingType.choices, verbose_name='培养类别')
    research_direction = models.TextField(verbose_name='研究方向')
    graduated_date = models.DateField(verbose_name='毕业时间')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='本月所在科室')

    def __str__(self) -> str:
        return '{name} / {degree} {grade}'
    
    class Meta:
        verbose_name_plural = verbose_name = '学生'
    
class Research(models.Model):
    '''
    科研工作
    '''
    Nature = models.TextChoices('研究性质', '临床研究 临床转化 基础研究')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    nature = models.CharField(max_length=32, choices=Nature.choices, verbose_name='研究性质')
    content = models.TextField(verbose_name='研究内容')
    plan = models.TextField(verbose_name='研究计划')

    def __str__(self) -> str:
        return '{nature}/{content}'
    
    class Meta:
        verbose_name_plural = verbose_name = '科研工作'

class ResearchAchievement(models.Model):
    '''
    科研成果
    '''
    Type = models.TextChoices('成果类型', '已发表文章 注册临床试验 正在写的文章')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    type = models.CharField(max_length=32, choices=Type.choices, verbose_name='成果类型')
    title = models.CharField(max_length=200, verbose_name='标题')
    progress = models.CharField(max_length=200, verbose_name='进度')

    def __str__(self) -> str:
        return '{type}/{title}'
    
    class Meta:
        verbose_name_plural = verbose_name = '科研成果'
