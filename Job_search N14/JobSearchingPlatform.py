from Company import Company
from abc import ABC
from JobPosting import JobPosting
from Application import Application

class JobSearchPlatform(ABC):
    def __init__(self):
        self.job_postings = []
        self.companies = []
        self.applications = []

    def create_company(self, name, contact_info):
        company = Company(name, contact_info)
        self.companies.append(company)
        return company

    def create_job_posting(self, company, title, description, salary):
        job_posting = JobPosting(company, title, description, salary)
        self.job_postings.append(job_posting)
        return job_posting

    def create_application(self, job_seeker, job_posting, resume):
        application = Application(job_seeker, job_posting, resume)
        self.applications.append(application)
        return application

    def view_job_postings(self):
        for job_posting in self.job_postings:
            job_posting.display_job_posting()
