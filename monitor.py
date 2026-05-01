# monitor.py - Upgraded with risk scoring and better keyword detection

import requests
from bs4 import BeautifulSoup
import datetime
import os

TIMEOUT = 5

# Target URLs — real sites where leaks/sensitive info might appear
TARGET_URLS = [
    "https://haveibeenpwned.com/",
    "https://www.databreaches.net/",
    "https://www.bleepingcomputer.com/",
    "https://krebsonsecurity.com/",
    "https://www.darkreading.com/",
    "https://threatpost.com/",
    "https://www.cisa.gov/news-events/cybersecurity-advisories",
    "https://www.bbc.com/news/technology",
    "https://techcrunch.com/security/",
    "https://www.wired.com/category/security/",
]

# Keywords with risk levels
KEYWORDS = [
    {"term": "database leaked",        "risk": "HIGH"},
    {"term": "credentials exposed",    "risk": "HIGH"},
    {"term": "data breach",            "risk": "HIGH"},
    {"term": "password dump",          "risk": "HIGH"},
    {"term": "exam paper leaked",      "risk": "HIGH"},
    {"term": "student records exposed","risk": "HIGH"},
    {"term": "LMS vulnerability",      "risk": "MEDIUM"},
    {"term": "unauthorized access",    "risk": "MEDIUM"},
    {"term": "phishing attack",        "risk": "MEDIUM"},
    {"term": "API key exposed",        "risk": "MEDIUM"},
    {"term": "security vulnerability", "risk": "MEDIUM"},
    {"term": "data privacy",           "risk": "LOW"},
    {"term": "cyber attack",           "risk": "LOW"},
    {"term": "malware detected",       "risk": "LOW"},
]

os.makedirs("logs", exist_ok=True)
LOG_FILE = "logs/results.txt"

def assess_risk(risk_level, url, keyword):
    return {
        "HIGH":   f"🔴 HIGH RISK   — '{keyword}' found at {url}",
        "MEDIUM": f"🟠 MEDIUM RISK — '{keyword}' found at {url}",
        "LOW":    f"🟡 LOW RISK    — '{keyword}' found at {url}",
    }.get(risk_level, f"🟢 INFO — '{keyword}' found at {url}")

def check_url(url, keyword, risk):
    try:
        response = requests.get(url, timeout=TIMEOUT,
                                headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        text  = soup.get_text().lower()
        title = soup.title.string.lower() if soup.title else ""

        matched = keyword.lower() in text or keyword.lower() in title
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if matched:
            alert = assess_risk(risk, url, keyword)
            entry = f"{timestamp} - {alert}\n"
            print(alert)
        else:
            entry = f"{timestamp} - ✅ No match — '{keyword}' not found at {url}\n"

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)

        return {"url": url, "keyword": keyword, "risk": risk,
                "matched": matched, "timestamp": timestamp}

    except Exception as e:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} - ⚠ Error fetching {url}: {e}\n"
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
        print(entry.strip())
        return {"url": url, "keyword": keyword, "risk": risk,
                "matched": False, "timestamp": timestamp, "error": str(e)}

def run_monitor():
    # Clear old log
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"=== Monitoring Run — {datetime.datetime.now()} ===\n\n")

    results = []
    for kw in KEYWORDS:
        print(f"\nScanning for: [{kw['risk']}] {kw['term']}")
        for url in TARGET_URLS:
            result = check_url(url, kw["term"], kw["risk"])
            results.append(result)

    # Summary
    total   = len(results)
    matched = sum(1 for r in results if r.get("matched"))
    high    = sum(1 for r in results if r.get("matched") and r["risk"] == "HIGH")
    medium  = sum(1 for r in results if r.get("matched") and r["risk"] == "MEDIUM")
    low     = sum(1 for r in results if r.get("matched") and r["risk"] == "LOW")

    summary = (
        f"\n=== SUMMARY ===\n"
        f"Total checks  : {total}\n"
        f"Alerts found  : {matched}\n"
        f"🔴 HIGH       : {high}\n"
        f"🟠 MEDIUM     : {medium}\n"
        f"🟡 LOW        : {low}\n"
    )
    print(summary)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(summary)

    return results

if __name__ == "__main__":
    run_monitor()