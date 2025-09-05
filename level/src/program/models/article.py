from django.db import models
from .author import Author
from .category import Category

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    categories = models.ManyToManyField(Category, related_name="articles")
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}-{self.created_by.user.username}"

    class Meta:
        ordering = ["title"]
