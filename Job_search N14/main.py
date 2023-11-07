from JobSearchingPlatform import JobSearchPlatform
from JobSeeker import JobSeeker

if __name__ == "__main__":
    
    job_search_platform = JobSearchPlatform()
    company1 = job_search_platform.create_company("TechCorp", "techcorp@examplegmail.com")
    company2 = job_search_platform.create_company("FinanceCo", "financeco@examplegmail.com")

    job_posting1 = job_search_platform.create_job_posting(company1, "Software Engineer", "Join our team of developers.", "$17,000 per year")
    job_posting2 = job_search_platform.create_job_posting(company2, "Financial Analyst", "Analyze financial data.", "$14,000 per year")

    job_seeker1 = JobSeeker("Alice", "alice@example.com", "Resume: Alice's qualifications")
    job_seeker2 = JobSeeker("Bob", "bob@example.com", "Resume: Bob's experience")

    application1 = job_search_platform.create_application(job_seeker1, job_posting1, "Alice's application for Software Engineer")
    application2 = job_search_platform.create_application(job_seeker2, job_posting2, "Bob's application for Financial Analyst")

    job_search_platform.view_job_postings()
