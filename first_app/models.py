from django.db import models

# Create your models here.
class StudentData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    
    def __str__(self):
        return self.name

# Case: Ekjon student onekgula course eksathe nite pare
# relation: one to many
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentData, on_delete=models.CASCADE, related_name='course', default=None)
    course_name = models.CharField(max_length=20)
    marks = models.IntegerField()
    
    def __str__(self):
        return self.course_name