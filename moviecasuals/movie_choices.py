from django.db import models

class MovieChoices(models.TextChoices):
    ACTION = 'Action', 'Action'
    ADVENTURE = 'Adventure', 'Adventure'
    COMEDY = 'Comedy', 'Comedy'
    DRAMA = 'Drama', 'Drama'
    HORROR = 'Horror', 'Horror'
    SCI_FI = 'Science Fiction (Sci-Fi)', 'Science Fiction (Sci-Fi)'
    FANTASY = 'Fantasy', 'Fantasy'
    THRILLER = 'Thriller', 'Thriller'
    MYSTERY = 'Mystery', 'Mystery'
    ROMANCE = 'Romance', 'Romance'
    ANIMATION = 'Animation', 'Animation'
    DOCUMENTARY = 'Documentary', 'Documentary'
    FAMILY = 'Family', 'Family'
    MUSICAL = 'Musical', 'Musical'
    CRIME = 'Crime', 'Crime'
    OTHERS = 'Other Genres', 'Other Genres'
