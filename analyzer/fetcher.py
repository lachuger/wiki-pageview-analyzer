import requests

class PageviewFetcher:
    def __init__(self, article: str, start: str, end: str):
        self.article = article
        self.start = start
        self.end = end
        self.headers = {
                "User-Agent": "wiki-pageview-analyzer/1.0 (your-email@example.com)"
            }

    def fetch(self) -> dict | None:
        try:
            url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{self.article}/daily/{self.start}/{self.end}"
            raw_data = requests.get(url, headers=self.headers)
            if raw_data.status_code == 200:
                return raw_data.json()
            else:
                print(f"Unexpected status: {raw_data.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print (f"Request Exception {e}")
            return None