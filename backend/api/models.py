from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

import uuid

# Create your models here.
class Todo(models.Model):
    
    id = models.UUIDField(
        primary_key=True, 
        unique=True,
        default=uuid.uuid4, 
        editable=False
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Todo, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name = 'Task to Do'
        verbose_name_plural = 'Tasks to Do'
        unique_together = ('title', 'description')