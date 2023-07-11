from django.db import models

# Create your models here.
# Create your models here.
class Job_titles(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    number = models.CharField(max_length=11)
    job_title = models.ForeignKey(to=Job_titles, on_delete=models.CASCADE)
    age = models.IntegerField()
    birthday = models.DateField()
    image = models.ImageField(upload_to='media/')

    
    class Meta:
        ordering = ('first_name',)

