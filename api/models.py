from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.





class Cosmetics(models.Model):

    name=models.CharField(unique=True,max_length=100)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    image=models.ImageField(upload_to='image',null=True)
    
    def __str__(self):
        return self.name


class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Cosmetics,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    product=models.ForeignKey(Cosmetics,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField(max_length=200)

    def __str__(self):
        return self.comment
    
