from getResumes import JobScraper

if __name__ == "__main__":
    scraper = JobScraper(
        api_key = "3faff2eeb4msh3af6c02186e6849p178b8djsnb125d077b483",
        query = "computer science",
        location = "St Louis, MO",
        pages = 5,
        delay = 1.5
    )

    scraper.fetch_jobs()
    scraper.save_to_json("st_louis_cs_jobs.json")