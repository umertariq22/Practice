from django.db import models
from django.utils import timezone
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    published_at = models.DateTimeField(null=True,blank=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()
    def __str__(self):
        return str(self.pk) + "- " + str(self.title)
    def get_absolute_url(self):
        return reverse("cbv:detail",kwargs={'pk':self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    author = models.CharField(max_length=80)
    text = models.TextField()
    created_at = models.DateTimeField()
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()
    def __str__(self):
        return str(self.pk) + "- " + str(self.article)
