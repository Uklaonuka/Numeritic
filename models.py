from django.db import models
from time import strptime


class Users(models.Model):
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Sex = models.CharField(max_length=32, default="Не указан")
    Date_of_birth = models.DateField()
    Login = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    Role = models.IntegerField(max_length=1)
    Code = models.IntegerField(max_length=6, null=True)
    Title = models.CharField(max_length=64, null=True)
    Price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        if self.Role == 1:
            return self.First_name + " " + self.Last_name + " " + self.Surname + " (Сотрудник)"
        else:
            return self.First_name + " " + self.Last_name + " " + self.Surname


class Talons(models.Model):

    Id_of_patient = models.IntegerField(default=0)
    Id_of_doctor = models.IntegerField()
    Title = models.CharField(max_length=255)
    DataTime = models.DateTimeField()
    Status = models.BooleanField(default=False)
    Price = models.FloatField()

    class Meta:
        verbose_name_plural = 'Талоны'

    def __str__(self):
        return self.Title + " - " + str(self.DataTime)[:16]


class Items(models.Model):
    Name = models.CharField(max_length=255)
    patient = models.IntegerField()
    doctor = models.IntegerField()
    DataTime = models.DateTimeField()
    Complaint = models.TextField()
    Temperature = models.FloatField()
    Recommendations = models.TextField()
    Analysis = models.TextField(null=True)
    Anamnesis = models.CharField(max_length=255, null=True)
    Diagnosis = models.CharField(max_length=255, null=True)
    Mkb = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = 'История болезней'


class Analysis(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.FloatField()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Исследования'

