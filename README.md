# 🛡️ Dark Web Monitoring for Edtech Assets

> An automated web keyword monitoring and alert system built to protect EdTech platforms from data breaches, credential leaks, and cybersecurity threats.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-59666C?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## 📖 Overview

This project was developed as a final year project at **Yenepoya Institute of Arts, Science, Commerce and Management** in collaboration with **IBM Innovation Centre for Education** and **Nihon Communication Solutions (NCS)**.

The **Web Keyword Monitoring & Alert System** scans websites for sensitive keywords related to EdTech asset exposure — such as leaked student records, credential dumps, or LMS vulnerabilities — and generates real-time alerts classified by risk severity (HIGH, MEDIUM, LOW).

---

## ✨ Features

- 🔍 **Multi-Keyword Scanning** — Load unlimited keywords from a simple `keywords.txt` file
- 🌐 **Dual Scan Modes** — Demo Mode (fixed URLs) and Google Search Mode (dynamic discovery)
- 🧠 **Risk Classification Engine** — Automatically classifies findings as `HIGH`, `MEDIUM`, or `LOW`
- 📊 **Interactive Streamlit Dashboard** — Live scanning, colour-coded results table, bar charts
- 📝 **Timestamped Logging** — All results saved to `logs/results.txt` for auditing
- ⚡ **Robust Error Handling** — Gracefully handles timeouts, broken URLs, and missing content
- 🔎 **Deep Detection** — Checks keyword presence in page body, title, and URL

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/dark-web-monitoring-edtech.git
cd dark-web-monitoring-edtech

# Install dependencies
pip install -r requirements.txt
```

### Running the Dashboard

```bash
streamlit run monitor.py
```

Then open your browser at `http://localhost:8501` and click **▶ Run Monitor Now**.

---

## 📁 Project Structure

```
dark-web-monitoring-edtech/
│
├── monitor.py              # Main application & Streamlit dashboard
├── keywords.txt            # Keyword list with risk classifications
├── requirements.txt        # Python dependencies
│
├── logs/
│   └── results.txt         # Auto-generated scan logs (timestamped)
│
└── README.md
```

---

## 🔑 Keywords Configuration

Edit `keywords.txt` to customise what the system monitors. Each keyword is paired with a risk level in `monitor.py`:

```
database leaked          → HIGH
credentials exposed      → HIGH
data breach              → HIGH
password dump            → HIGH
exam paper leaked        → HIGH
student records exposed  → HIGH
LMS vulnerability        → MEDIUM
unauthorized access      → MEDIUM
phishing attack          → MEDIUM
API key exposed          → MEDIUM
security vulnerability   → MEDIUM
data privacy             → LOW
cyber attack             → LOW
malware detected         → LOW
```

---

## 🖥️ Dashboard Preview

The Streamlit dashboard provides:

| Component | Description |
|-----------|-------------|
| **Metric Cards** | Total checks, HIGH / MEDIUM / LOW alert counts |
| **Results Table** | Colour-coded keyword × URL results with risk ratings |
| **Bar Charts** | Alert distribution and most-detected keywords |
| **Alert Details** | Expandable findings for each match |
| **Log Viewer** | Timestamped log of every scan run |

---

## 📊 Sample Scan Results

From a real scan across **10 cybersecurity websites** (140 total checks):

```
2026-04-30 00:43:35 - 🔴 HIGH RISK   — 'data breach' found at https://haveibeenpwned.com/
2026-04-30 00:43:39 - 🔴 HIGH RISK   — 'data breach' found at https://krebsonsecurity.com/
2026-04-30 00:44:33 - 🟠 MEDIUM RISK — 'unauthorized access' found at https://www.wired.com/category/security/
2026-04-30 00:44:38 - 🟠 MEDIUM RISK — 'phishing attack' found at https://krebsonsecurity.com/

=== SUMMARY ===
Total checks : 140
Alerts found : 7
🔴 HIGH      : 4
🟠 MEDIUM    : 3
🟢 LOW       : 0
```

---

## 🏗️ System Architecture

The system follows a 6-layer modular pipeline:

```
Input Layer     →  Load keywords from file, select scan mode
URL Layer       →  Fixed demo URLs or dynamic Google Search discovery
Scraping Layer  →  HTTP GET via Requests + HTML parsing via BeautifulSoup
Detection Layer →  Case-insensitive matching + risk severity classification
Logging Layer   →  Timestamped writes to logs/results.txt
Output Layer    →  Streamlit dashboard with charts and detailed findings
```

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---------|---------|---------|
| `requests` | latest | HTTP GET requests and timeout handling |
| `beautifulsoup4` | latest | HTML parsing and text extraction |
| `streamlit` | latest | Interactive real-time dashboard |
| `pandas` | latest | Results table and data manipulation |
| `datetime` | stdlib | Log timestamping |
| `os` | stdlib | File path and directory management |

---

## ⚙️ Requirements

**Minimum Hardware:**
- CPU: Dual-core
- RAM: 2 GB
- Storage: 200 MB

**Recommended:**
- CPU: Quad-core
- RAM: 4 GB
- Storage: 500 MB

**Supported OS:** Windows · Linux · macOS

---

## 📋 Requirements File

```txt
requests
beautifulsoup4
streamlit
pandas
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧪 Testing

The system was tested across four areas:

- **Unit Testing** — Keyword loading, URL scanning, HTML parsing
- **Integration Testing** — End-to-end monitoring pipeline
- **Performance Testing** — Large keyword lists, slow-responding websites
- **Error Handling Testing** — Timeouts, invalid URLs, empty keyword files

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| Valid URL | `haveibeenpwned.com` | No crash |
| Timeout | Slow site | Error logged, scan continues |
| Keyword match | `"data breach"` | HIGH alert generated |
| Empty keyword file | (empty) | No crash |

---

## 🔮 Future Development

- [ ] **NLP Integration** — BERT/RoBERTa contextual detection, synonym expansion
- [ ] **Scheduled Monitoring** — Cron jobs for hourly/daily automated scans
- [ ] **Real-Time Alerts** — Email, SMS, Slack, or Telegram notifications
- [ ] **Web Crawling** — Scrapy/Selenium-based deep crawling from seed URLs
- [ ] **Social Media Monitoring** — Twitter/X, Reddit, LinkedIn API integration
- [ ] **Cloud Deployment** — AWS Lambda / Azure Functions / Docker
- [ ] **ML Anomaly Detection** — Isolation Forest, One-Class SVM
- [ ] **Enhanced Reporting** — Grafana dashboards, PDF/Excel exports

---

## 👩‍💻 Author

**Nishma Fathima**
Final Year Project — Yenepoya Institute of Arts, Science, Commerce and Management

| Role | Name |
|------|------|
| Student | Nishma Fathima |
| Industry Mentor | Mr. Shashank |
| Academic Guide | Ms. Suzzana Sharol |

---

## 🏛️ Institution

Developed under the **IBM Innovation Centre for Education** initiative in partnership with **Nihon Communication Solutions (NCS)**.

---

## 📚 References

- [Requests Documentation](https://requests.readthedocs.io)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- Manning, C. D., Raghavan, P., & Schütze, H. — *Introduction to Information Retrieval*, Cambridge University Press
- Feldman, R., & Sanger, J. — *The Text Mining Handbook*, Cambridge University Press

---

## ⚠️ Disclaimer

This tool is developed for **educational and research purposes only**. Always ensure compliance with a website's `robots.txt` and terms of service before scanning. The author and institution are not responsible for any misuse.

---

<p align="center">
  Made with ❤️ for EdTech security awareness · Project 2026
</p>
