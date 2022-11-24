from django.db import models

class Resume(models.Model):
    title = models.CharField(max_length=250)
    anons  = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоный'
