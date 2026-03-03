from django.db import models

# Create your models here.

class Professor(models.Model):
    profesorID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    
class Course(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    courseCode = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=255)
    credits = models.IntegerField()
    amountPerCredits = models.IntegerField()
    
class Assignment(models.Model):
    assignmentID = models.AutoField(primary_key=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    totalAmount = models.IntegerField()
    