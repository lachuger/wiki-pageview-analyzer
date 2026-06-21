# Wikipedia Pageview Analyzer

> A simple python-based wikipedia article pageview analyzer

---

## What It Does

This fun little tool will take any wikipedia article and a date range and spits out page view data for that article. Current stats include total views over a date range, average daily views, peak and trough days, and a full daily breakdow

---

## Installation

```bash
git clone lachuger/wiki-pageview-analyzer
cd wiki-pageview-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py <article> <start_date> <end_date>
```

Dates must be formatted as `YYYYMMDD`. Multi-word article names use underscores.

**Examples:**

```bash
python main.py Chess 20250101 20250131
python main.py Magnus_Carlsen 20250101 20250131
```

---

## Output

The report is printed to the terminal and saved to `reports/` as a `.txt` file
named after the article and date range.
