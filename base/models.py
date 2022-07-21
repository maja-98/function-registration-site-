from django.db import models

# Create your models here.
class Family(models.Model):
    family_name = models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return self.family_name
    
class Member(models.Model):
    name = models.CharField(max_length=50,null=False)
    age = models.PositiveIntegerField(null=False)
    gender = models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')])
    family = models.ForeignKey(Family,on_delete=models.CASCADE,null=False)
    attended = models.BooleanField(default=False)
    photo = models.ImageField(null="True",default='avatar.png')
    
    def __str__(self):
        return self.name