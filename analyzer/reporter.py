from pathlib import Path

class PageviewReporter:
    def __init__(self, stats: dict, output_dir: str):
        self.stats = stats
        self.output_dir = output_dir

    def generate(self) -> None:
        """
        Prints to terminal and generates text file based on stats passed by PageviewProcessor
        """
        start = self.stats["start"]
        formatted_start = f"{start[:4]}-{start[4:6]}-{start[6:]}"
        end = self.stats["end"]
        formatted_end = f"{end[:4]}-{end[4:6]}-{end[6:]}"

        lines = []
        lines.append ("Wikipedia Page Report")
        lines.append ("============")
        lines.append (f"Article: {self.stats['article']}")
        lines.append (f"Period: {formatted_start} to {formatted_end}")
        lines.append (f"Total Views: {self.stats['total_views']:,}")
        lines.append (f"Daily Average: {self.stats['average_views']:,}")
        peak = self.stats["peak"]
        peak_date = f"{peak['date'][:4]}-{peak['date'][4:6]}-{peak['date'][6:]}"
        lines.append (f"Peak Day: {peak_date} - {peak['views']:,} views")
        trough = self.stats["trough"]
        trough_date = f"{trough['date'][:4]}-{trough['date'][4:6]}-{trough['date'][6:]}"
        lines.append (f"Trough Day: {trough_date} - {trough['views']:,} views")
        lines.append ("")
        lines.append ("Daily Breakdown:")
        for day in self.stats["daily_breakdown"]:
            date = day["date"]
            formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
            lines.append (f"{formatted_date} - {day['views']:,}")

        report_text = "\n".join(lines)
        print (report_text)
        
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        filename = f"{self.stats['article']}_{self.stats['start']}_{self.stats['end']}.txt"
        output_path = Path(self.output_dir) / filename
        with open(output_path, "w") as f:
            f.write(report_text)