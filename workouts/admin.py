from django.contrib import admin
from .models import Workout, WorkoutDay, WorkoutDayExercise, Goal, Disability, Exercise, UserInfo, Progress, Friendship
from .models import Post, Reaction, Comment, Follow, Payment

admin.site.register(Workout)
admin.site.register(WorkoutDay)
admin.site.register(WorkoutDayExercise)
admin.site.register(Goal)
admin.site.register(Disability)
admin.site.register(Exercise)
admin.site.register(UserInfo)
admin.site.register(Post)
admin.site.register(Reaction)
admin.site.register(Comment)
admin.site.register(Progress)
admin.site.register(Friendship)
admin.site.register(Follow)
admin.site.register(Payment)