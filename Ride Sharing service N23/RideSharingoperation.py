from abc import ABC, abstractmethod

class RideSharingOperation(ABC):
    @abstractmethod
    def request_ride(self, passenger, destination):
        pass

    @abstractmethod
    def accept_ride(self, ride):
        pass

    @abstractmethod
    def complete_ride(self, ride):
        pass