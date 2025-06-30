import requests
import json
import time  


class JobScraper:

    def __init__(self, api_key, query, location, pages=5, delay=1.5):
        self.api_key = api_key
        self.query = query
        self.location = location
        self.pages = pages
        self.delay = delay
        self.base_url = "https//jsearch.p.rapidapi.com/search"
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }
        self.all_jobs = []


    def fetch_jobs(self):
        for page in range(1, self.pages + 1):
            print(f"[INFO] fetching page {page} for '{self.query}' in {self.location}...")
            params = {
                "query": self.query,
                "location": self.location,
                "page": str(page),
                "num_pages": "1"
            }

            try:
                response = requests.get(self.base_url, headers=self.headers, params=params)
                if response.status_code == 200:
                    jobs = response.json().get("data", [])
                    if not jobs:
                        print("[INFO] NO more jobs returned. Stopping early.")
                        break
                    self.all_jobs.extend(jobs)
                else:
                    print(f"[ERROR] Status code {response.status_code} on page {page}")
                    break
            except Exception as e:
                print(f"[EXCEPTION] {e}")
                break

            time.sleep(self.delay)


    def save_to_json(self, filename="job_postings.json"):
        with open(filename, "w") as f:
            json.dump(self.all_jobs, f, indent=4)
        print(f"[INFO] Saved {len(self.all_jobs)} job postings to '{filename}'")
                