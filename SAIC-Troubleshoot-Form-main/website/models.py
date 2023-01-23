from django.db import models


class Member(models.Model):
    name1=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
    name3=models.CharField(max_length=50)
    name4=models.CharField(max_length=50)
    roll1=models.IntegerField()
    roll2=models.IntegerField()
    roll3=models.IntegerField()
    roll4=models.IntegerField()
    email1=models.EmailField(max_length=200)
    email2=models.EmailField(max_length=200)
    email3=models.EmailField(max_length=200)
    email4=models.EmailField(max_length=200)
    phone1=models.IntegerField()
    phone2=models.IntegerField()
    phone3=models.IntegerField()
    phone4=models.IntegerField()
    tname=models.CharField(max_length=100)
    

    def __str__(self):
        return self.name1 + ' '+self.name2