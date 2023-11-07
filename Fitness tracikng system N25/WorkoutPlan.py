class WorkoutPlan:
    def __init__(self, user, exercises, plan_duration):
        self.user = user
        self.exercises = exercises
        self.plan_duration = plan_duration

    def follow_plan(self):
        print(f"{self.user.name}'s {self.plan_duration}-day workout plan:")
        for exercise in self.exercises:
            print(exercise.description())
