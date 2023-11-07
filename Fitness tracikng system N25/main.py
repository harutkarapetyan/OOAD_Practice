from Exercise import CardioExercise, StrengthExercise
from User import User
from WorkoutPlan import WorkoutPlan


if __name__ == "__main__":
    cardio_exercise = CardioExercise("Running", 30)
    strength_exercise = StrengthExercise("Push-Ups", 15, 3)

    user1 = User("Alice", "alice@examplegmail.com")
    user2 = User("Bob", "bob@examplegmail.com")

    user1.add_favorite_exercise(cardio_exercise)
    user2.add_favorite_exercise(strength_exercise)

    workout_plan1 = WorkoutPlan(user1, [cardio_exercise, strength_exercise], 7)
    workout_plan2 = WorkoutPlan(user2, [strength_exercise, cardio_exercise], 5)

    user1.track_progress(cardio_exercise, 30)
    user2.track_progress(strength_exercise, 15)

    workout_plan1.follow_plan()
    workout_plan2.follow_plan()
