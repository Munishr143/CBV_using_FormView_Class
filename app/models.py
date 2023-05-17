from django.db import models

# Create your models here.

#from django.db.models import Q
from django.core import validators

class Student(models.Model):
    Sid=models.IntegerField(primary_key=True)
    Sname=models.CharField(max_length=30, validators=[validators.RegexValidator('[A-Z]')])
    Sage=models.IntegerField(validators=[validators.MinValueValidator(3)])
    Saddress=models.TextField(max_length=200)

    # class Meta:
    #     constraints=[
    #         models.CheckConstraint(check=Q(Sage__gte=3), name='Sage_gt3')
    #     ]

    def __str__(self) -> str:
        return self.Sname
    
