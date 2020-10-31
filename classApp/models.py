from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField(default=0)
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField(default=0.0)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Django Class'
        verbose_name_plural = 'Django Classes'

    def __str__(self):
        return self.title
