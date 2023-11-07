from abc import ABC, abstractmethod

class IJobPosting(ABC):
    @abstractmethod
    def create_job_posting(self, title, description, salary):
        pass


class JobPosting(IJobPosting):
    def __init__(self, company, title, description, salary):
        self.company = company
        self.title = title
        self.description = description
        self.salary = salary

    def create_job_posting(self, title, description, salary):
        return JobPosting(self.company, title, description, salary)

    def display_job_posting(self):
        print(f"Company: {self.company.name}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Salary: {self.salary}\n")
