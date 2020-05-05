from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=10)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )
    votes = models.PositiveIntegerField()
    genres = models.ManyToManyField("Genre", related_name="books")
    qty = models.IntegerField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
   # author2 = models.ForeignKey(to='Author', on_delete=models.CASCADE, related_name='genre')
    book = models.ForeignKey(to='Book',on_delete=models.CASCADE)
    distance =models.IntegerField()

    def __str__(self):
        return self.name