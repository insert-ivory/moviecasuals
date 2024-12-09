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


class MovieUserOptions(models.TextChoices):
    UNSPECIFIED = "Unspecified", "Unspecified"
    WANT_TO_WATCH = "Want to Watch", "Want to Watch"
    WATCHED = "Watched", "Watched"
    NEED_TO_REWATCH = "Need to Rewatch", "Need to Rewatch"
    INTERESTED = "Interested", "Interested"
    NOT_INTERESTED = "Not Interested", "Not Interested"
    RECOMMENDED = "Recommended", "Recommended"

