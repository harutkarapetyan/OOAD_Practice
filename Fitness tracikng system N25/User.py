from validate_decorators import validate_email, validate_non_empty_string

class User:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.favorite_exercises = []

    def add_favorite_exercise(self, exercise):
        self.favorite_exercises.append(exercise)

    def track_progress(self, exercise, duration):
        print(f"{self.name} completed {exercise.description()} for {duration} minutes.")
