
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # link to another model, like models.Model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # limited number of characters in text blog
    title = models.CharField(max_length=200)
    # for long text w/o a limit
    text = models.TextField()
    # date & time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
