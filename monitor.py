import requests
from bs4 import BeautifulSoup
from googlesearch import search
import datetime
import os

# ---------------- CONFIG ----------------
USE_GOOGLE_SEARCH = False   # Toggle: True = Google search, False = demo mode (fast, fixed URLs)
RESULTS_PER_KEYWORD = 3     # Number of URLs to check per keyword in Google mode
TIMEOUT = 3                 # Seconds before giving up on a slow site
# ----------------------------------------

# Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Load keywords from keywords.txt
with open("keywords.txt") as f:
    keywords = [line.strip() for line in f.readlines() if line.strip()]

# Demo mode URLs (fast, guaranteed matches)
demo_urls = [
    "https://www.python.org/",
    "https://openai.com/",
    "https://www.microsoft.com/"
]

alerts_found = 0
checks_done = 0

def check_url_for_keyword(url, kw):
    """Fetch a URL and check if keyword appears in body, title, or URL."""
    global alerts_found, checks_done
    try:
        response = requests.get(url, timeout=TIMEOUT)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text().lower()
        title = soup.title.string.lower() if soup.title else ""

        checks_done += 1
        if kw.lower() in text or kw.lower() in title or kw.lower() in url.lower():
            alert = f"⚠ ALERT: Keyword '{kw}' found at {url}"
            print(alert)
            alerts_found += 1
            log_entry = f"{datetime.datetime.now()} - {alert}\n"
        else:
            log_entry = f"{datetime.datetime.now()} - Checked {url} for '{kw}' - No match\n"

        with open("logs/results.txt", "a", encoding="utf-8") as log:
            log.write(log_entry)

    except Exception as e:
        print(f"Error fetching {url}: {e}")

# ---------------- MAIN LOOP ----------------
for kw in keywords:
    print(f"\nSearching for keyword: {kw}")
    urls_to_check = demo_urls if not USE_GOOGLE_SEARCH else list(search(kw, num_results=RESULTS_PER_KEYWORD))

    for url in urls_to_check:
        print(f"Checking URL: {url}")
        check_url_for_keyword(url, kw)

# ---------------- SUMMARY ----------------
print(f"\n✅ Monitoring complete. {len(keywords)} keywords checked, {checks_done} URLs scanned, {alerts_found} alerts found.")
