from .disability import Disability
from .goal import Goal
from .workout import Workout
from .workout_day import WorkoutDay
from .exercise import Exercise
from .workout_day_exercise import WorkoutDayExercise
from .user_info import UserInfo
from .post import Post
from .reaction import Reaction
from .comment import Comment
from .progress import Progress
from .friendship import Friendship
from .followers import Follow

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .user_payment import Payment
from .calories import FoodCalories

@receiver(post_save, sender=User)
def create_user_info(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)
