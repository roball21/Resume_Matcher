if __name__ == "__main__":

    from readResume import Reader

    reader = Reader()

    reader.readResume()
    reader.convertToJson()

    from getResumes import JobScraper

    scraper = JobScraper(
        api_key = "3faff2eeb4msh3af6c02186e6849p178b8djsnb125d077b483",
        query = "computer science",
        location = "St Louis, MO"
    )

    scraper.fetch_jobs()
    scraper.save_to_json("st_louis_cs_jobs.json")
