from pyexpat import model
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.

class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("نام و نام خانوادگی"), max_length=50)
    state = models.CharField(_("استان"), max_length=50)
    city = models.CharField(_("شهر"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    phone = models.CharField(_("شماره تلفن"), max_length=50)
    birth_year = models.CharField(_("سال تولد"), max_length=50)
    GENDER = (
        ('آقا','آقا'),
        ('خانم','خانم'),
    )
    gender = models.CharField(_("جنسیت"), max_length=50,choices=GENDER)
    # skils
    about_me = models.TextField(_("متن درباره من"))
    experience = models.TextField(_("سوابق شغلی"))
    education = models.TextField(_("سوابق تحصیلی"))
    
    