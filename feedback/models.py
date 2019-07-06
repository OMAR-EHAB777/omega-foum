from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=200,)
    email = models.EmailField(max_length=200,)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"
        # the new bit we're adding
    def __str__(self):
        return self.name + "-" + self.email