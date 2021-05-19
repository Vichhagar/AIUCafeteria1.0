from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    foodAddDate = models.DateTimeField(null=True, blank=True, auto_now=True)
    foodPrice = models.IntegerField(default=0)
    foodAvailableDay = models.CharField(max_length=20, choices=DAYS, null=True, blank=True)

    def __str__(self):
        return f"{self.foodName}"






class Vote(models.Model):
    voteId = models.AutoField(primary_key=True)
    foodId = models.OneToOneField(Food, on_delete=models.CASCADE)
    upVote = models.IntegerField(default=0)
    downVote = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.foodId}"

    @receiver(post_save, sender=Food)
    def setVoter(sender, instance, created, **kwargs):
        if created:
            
            # vote = Vote.objects.create(food=kwargs['instance'])
            print("YES?!")

            
