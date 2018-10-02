from django.db import models


class Articles(models.Model):
    author = models.TextField()
    title = models.TextField()
    article = models.TextField()
    published_time = models.DateTimeField()

    def __str__(self):
        return str(self.pk) + "- " + self.title


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    author = models.TextField()
    text = models.TextField()
    publish_time = models.DateTimeField()

    def __str__(self):
        return str(self.pk) + "- " + str(self.article)
