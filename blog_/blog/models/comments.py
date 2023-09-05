from django.db import models


class Comment(models.Model):
  user = models.ForeignKey("blog.users",on_delete=models.CASCADE)
  post = models.ForeignKey("blog.posts", on_delete=models.CASCADE)
  text = models.TextField("Comment")
  date = models.DateTimeField("Date of create")

  class Meta:
    verbose_name = "Comment"
    verbose_name_plural = "Comments"