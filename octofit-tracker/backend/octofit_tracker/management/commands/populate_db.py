from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson.objectid import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.delete()
        Team.objects.delete()
        Activity.objects.delete()
        Leaderboard.objects.delete()
        Workout.objects.delete()

        # Create users
        users = [
            User(username='thundergod', email='thundergod@mhigh.edu', password='password123').save(),
            User(username='metalgeek', email='metalgeek@mhigh.edu', password='password123').save(),
            User(username='zerocool', email='zerocool@mhigh.edu', password='password123').save(),
            User(username='crashoverride', email='crashoverride@mhigh.edu', password='password123').save(),
            User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='password123').save(),
        ]

        # Create teams
        team1 = Team(name='Blue Team', members=[users[0], users[1]]).save()
        team2 = Team(name='Gold Team', members=[users[2], users[3], users[4]]).save()

        # Create activities
        activities = [
            Activity(activity_id=str(ObjectId()), user=users[0], activity_type='Cycling', duration='1:00:00').save(),
            Activity(activity_id=str(ObjectId()), user=users[1], activity_type='Crossfit', duration='2:00:00').save(),
            Activity(activity_id=str(ObjectId()), user=users[2], activity_type='Running', duration='1:30:00').save(),
            Activity(activity_id=str(ObjectId()), user=users[3], activity_type='Strength', duration='0:30:00').save(),
            Activity(activity_id=str(ObjectId()), user=users[4], activity_type='Swimming', duration='1:15:00').save(),
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(leaderboard_id=str(ObjectId()), user=users[0], score=100).save(),
            Leaderboard(leaderboard_id=str(ObjectId()), user=users[1], score=90).save(),
            Leaderboard(leaderboard_id=str(ObjectId()), user=users[2], score=95).save(),
            Leaderboard(leaderboard_id=str(ObjectId()), user=users[3], score=85).save(),
            Leaderboard(leaderboard_id=str(ObjectId()), user=users[4], score=80).save(),
        ]

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event').save(),
            Workout(name='Crossfit', description='Training for a crossfit competition').save(),
            Workout(name='Running Training', description='Training for a marathon').save(),
            Workout(name='Strength Training', description='Training for strength').save(),
            Workout(name='Swimming Training', description='Training for a swimming competition').save(),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))