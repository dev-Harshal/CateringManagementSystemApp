from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.


class Users(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    category_image = models.ImageField(upload_to='CategoryImages',null=True,blank=True)

    def __str__(self):
        return self.title

class Option(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    option_title = models.CharField(max_length=100,null=True,blank=True)
    option_image = models.ImageField(upload_to='OptionImages',null=True,blank=True)

    def __str__(self):
        return self.option_title
    
class Dish(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    option = models.ForeignKey(Option,on_delete=models.CASCADE,null=True,blank=True)
    dish_image = models.ImageField(upload_to="DishImages/",null=True,blank=True)
    dish_name = models.CharField(max_length=100,null=True,blank=True)
    dish_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.dish_name
    


class UsersCartItem(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
