import sys
from analyzer.fetcher import PageviewFetcher
from analyzer.processor import PageviewProcessor
from analyzer.reporter import PageviewReporter

def main():
    if len(sys.argv) != 4:
        print ("Usage: python(3) main.py <article_name> <start_date(YYYYMMDD)> <end_date(YYYYMMDD)>")
        print ("Example: python3 main.py John_Wick 20230215 20230312")

    article = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]


    raw_data = PageviewFetcher(article, start, end).fetch()
    if raw_data is None:
        print("Fetch failed.")
        return

    stats = PageviewProcessor(raw_data).process()
    if stats is None:
        print("Processing failed.")
        return

    PageviewReporter(stats, "reports").generate()

if __name__ == "__main__":
    main()