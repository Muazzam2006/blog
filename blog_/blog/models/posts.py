from django.db import models


class Post(models.Model):
  title = models.CharField("Title", max_length=50)
  description = models.TextField("Description")
  date = models.DateTimeField(("Date of create"))
  user = models.ForeignKey( "blog.users", on_delete=models.CASCADE)

  class Meta:
    verbose_name = "Post"
    verbose_name_plural = "Posts"



