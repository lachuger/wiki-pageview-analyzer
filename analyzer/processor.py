class PageviewProcessor:
    def __init__(self, data: dict):
        self.data = data

    def process(self) -> dict | None:
        """
        Converts JSON fetched by PageviewFetcher into a dictionary

        Args: data (passed from Fetcher)

        Returns: stats (passed to Reporter)
        """
        items = self.data["items"]
        if items:
            article = items[0]["article"]
            start = items[0]["timestamp"][:8]
            end = items [-1]["timestamp"][:8]

            daily_breakdown = [
                {"date": item["timestamp"][:8], "views": item["views"]}
                for item in items
            ]

            total_views = sum(day["views"] for day in daily_breakdown)
            average_views = round(total_views / len (daily_breakdown), 1)
            
            peak = max(daily_breakdown, key=lambda day: day["views"])
            trough = min(daily_breakdown, key=lambda day: day["views"])

            return {
                "article": article,
                "start": start,
                "end": end,
                "total_views": total_views,
                "average_views": average_views,
                "peak": peak,
                "trough": trough,
                "daily_breakdown": daily_breakdown
                }
        else:
            return None