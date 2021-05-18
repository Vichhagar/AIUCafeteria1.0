from django.db import models

class Food(models.Model):

    DAYS = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )

    foodId = models.AutoField(primary_key=True)
    foodImage = models.ImageField(upload_to='images/', null=True, blank=True)
    foodName = models.CharField(max_length=100)
    foodManufactureDate = models.DateTimeField(null=True, blank=True)
    foodExpirationDate = models.DateTimeField(null=True, blank=True)
    foodPrice = models.IntegerField(default=0)
    foodAvailableDay = models.CharField(max_length=20, choices=DAYS, null=True, blank=True)

    def __str__(self):
        return f"{self.foodName}"

    def save(self, *args, **kwargs):
        print("Hi")
  
        super(Food, self).save(*args, **kwargs)


class Vote(models.Model):
    voteId = models.AutoField(primary_key=True)
    foodId = models.ForeignKey(Food, on_delete=models.CASCADE, related_name ='food_related')
    upVote = models.IntegerField(default=0)
    downVote = models.IntegerField(default=0)

    def __str__(self):
        return f"upVote {self.upVote}"
