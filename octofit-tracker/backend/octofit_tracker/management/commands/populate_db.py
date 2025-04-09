from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", password="password123")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", password="password456")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha")
        team2 = Team.objects.create(name="Team Beta")

        # Create test activities
        Activity.objects.create(user=user1, activity_type="Running", duration=30, date="2025-04-08")
        Activity.objects.create(user=user2, activity_type="Cycling", duration=45, date="2025-04-07")

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=100)
        Leaderboard.objects.create(team=team2, score=80)

        # Create test workouts
        Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
        Workout.objects.create(name="Squats", description="Do 15 squats")

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
