if __name__ == "__main__": 

    from getApplications import JobScraper
    from readResume import Reader
    from openaiConnection import EmbeddingAndComparison

    # step 1: scrape job postings

    scraper = JobScraper(
        api_key = "3faff2eeb4msh3af6c02186e6849p178b8djsnb125d077b483",
        query = "computer science",
        location = "St Louis, MO"
    )

    scraper.fetch_jobs()
    scraper.save_to_json("st_louis_cs_jobs.json")

    
    # step 2: extract keywords and convert to text

    reader = Reader()
    reader.readResume()
    reader.keywords_to_text()
    reader.convertToJson()

    # step 3: embed and compare

    comparison = EmbeddingAndComparison(
        resume_file="userResume.json",
        jobs_file="st_louis_cs_jobs.json"
    )
    comparison.run()