from pyexpat import model
from random import choices
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from pytz import timezone
# Create your models here.

class WorkCategory(models.Model):
    name = models.CharField(_("نام دسته بندی"), max_length=50)
    
    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(_("نام مهارت"), max_length=50)
    
    def __str__(self):
        return self.name


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(_("نام شرکت یا ارگان"), max_length=50)
    phone = models.CharField(_("شماره تماس"), max_length=50)
    work_category = models.ManyToManyField(WorkCategory, verbose_name=_("دسته بندی شغلی"),null=True,blank=True)
    person_number_from = models.IntegerField(_("تعداد افراد مورد نیاز از"),null=True,blank=True)
    person_number_until = models.IntegerField(_("تعداد افراد مورد نیاز تا"),null=True,blank=True)
    site = models.CharField(_("سایت یا وبلاگ"), max_length=50,null=True,blank=True)
    title = models.CharField(_("موضوع آگهی"), max_length=50,null=True,blank=True)
    state = models.CharField(_("استان"), max_length=50,null=True,blank=True)    
    city = models.CharField(_("شهر"), max_length=50,null=True,blank=True)   
    JOB_TYPE = (
        ('تمام وقت','تمام وقت'),
        ('پاره وقت','پاره وقت'),
        ('کارآموزی','کارآموزی'),
        ('دورکاری','دورکاری'),
    )
    job_type = models.CharField(_("نوع قرارداد"), max_length=50,choices=JOB_TYPE,null=True,blank=True)
    EXPERIENCE = (
        ('مهم نیست','مهم نیست'),
        ('کمتر از سه سال','کمتر از سه سال'),
        ('سه تا شش سال','سه تا شش سال'),
        ('بیشتر از شش سال','بیشتر از شش سال'),
    )
    experience = models.CharField(_("سابقه کار"), max_length=50,choices=EXPERIENCE,null=True,blank=True)
    SALARY = (
        ('توافقی','توافقی'),
        ('از سه میلیون','از سه میلیون'),
        ('از پنج میلیون','از پنج  میلیون'),
    )
    description = models.TextField(_("توضیحات کار"),null=True,blank=True)
    company_introduction = models.TextField(_("معرفی شرکت"),null=True,blank=True)
    skills = models.ManyToManyField(Skill, verbose_name=_("مهارت های مورد نیاز"),null=True,blank=True)
    GENDER = (
        ('مهم نیست','مهم نیست'),
        ('آقا','آقا'),
        ('خانم','خانم'),
    )
    gender = models.CharField(_("جنسیت"), max_length=50,choices=GENDER,null=True,blank=True)
    published = models.DateTimeField(_("زمان ایجاد"), auto_now=False, auto_now_add=True,null=True,blank=True)
    
     
    def get_absolute_url(self):
        return reverse("job-detail", args=[self.pk,])
    
    def __str__(self):
        return self.name
    
    
    
class RequestModel(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, verbose_name="کاربر", on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
