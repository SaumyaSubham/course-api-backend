from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instances')
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()
    custom_course_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course.title} ({self.year} - Semester {self.semester})"
