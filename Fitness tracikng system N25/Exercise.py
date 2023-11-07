from abc import ABC, abstractmethod

class Exercise(ABC):
    def __init__(self, name, muscle_group):
        self.name = name
        self.muscle_group = muscle_group

    @abstractmethod
    def description(self):
        pass

class CardioExercise(Exercise):
    def __init__(self, name, duration):
        super().__init__(name, "Cardio")
        self.duration = duration

    def description(self):
        return f"Cardio Exercise: {self.name}, Targeted Muscle Group: {self.muscle_group}, Duration: {self.duration} minutes"

class StrengthExercise(Exercise):
    def __init__(self, name, reps, sets):
        super().__init__(name, "Strength")
        self.reps = reps
        self.sets = sets

    def description(self):
        return f"Strength Exercise: {self.name}, Targeted Muscle Group: {self.muscle_group}, Reps: {self.reps}, Sets: {self.sets}"
