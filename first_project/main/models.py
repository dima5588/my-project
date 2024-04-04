# from django.db import models

# Create your models here.
#
# class Cars(models.Model):
#     title = models.CharField(max_length=150)
#     price = models.DecimalField(max_digits=12, decimal_places=2)
#     image = models.ImageField(upload_to='images/')
#     phone = models.CharField(max_length=25)
#     description = models.CharField(blank=True, max_length=255)
#     owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = 'Машина'
#         verbose_name_plural = 'Машины'
#
#     def __str__(self):
#         return f'{self.title}'

from django .db import models

class Teachebr(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f'Mr/Mrs {self.first_name} {self.last_name}'

class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Students, related_name='groups', blank=True)

