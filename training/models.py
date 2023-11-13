from django.db import models

# Create your models here.


class Course(models.Model):
    image = models.ImageField(upload_to='cources', default='')
    title = models.CharField(max_length=70, default='')
    method_of_teaching = models.CharField(max_length=50, default='Online')
    duration = models.CharField(max_length=200, default="")
    number_of_lessons = models.IntegerField()
    payment = models.CharField(max_length=50, default='$')
    app = models.CharField(max_length=50, default='Zoom')

    def __str__(self):
        return self.title


class Track(models.Model):
    number_of_testimonials = models.IntegerField()
    number_of_instructors = models.IntegerField()


class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimony', default='')
    name = models.CharField(max_length=100, default='')
    summary_of_testimoney = models.TextField()
    def __str__(self):
        return self.name 
    

#students registration info model
class Student(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=200, blank=False, null=False, default='')
    country = models.CharField(max_length=200, blank=False, null=False, default='')   
    expectation = models.CharField(max_length=200, blank=False, null=False, default='')
    def __str__(self):
        return self.first_name