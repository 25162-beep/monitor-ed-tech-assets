# dashboard.py - Upgraded Streamlit dashboard with live monitoring

import streamlit as st
import matplotlib.pyplot as plt
import datetime
import os
import sys

# So dashboard can import monitor.py from same folder
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from monitor import run_monitor, KEYWORDS, TARGET_URLS

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "results.txt")

st.set_page_config(page_title="Keyword Monitor", page_icon="🔎", layout="wide")
st.title("🔎 Keyword Threat Monitoring Dashboard")
st.caption("Final Year Project — Automated Web Keyword & Data Leak Detection")

# Sidebar info
with st.sidebar:
    st.subheader("⚙ Configuration")
    st.write(f"**Keywords monitored:** {len(KEYWORDS)}")
    st.write(f"**Target URLs:** {len(TARGET_URLS)}")
    st.write(f"**Total checks per run:** {len(KEYWORDS) * len(TARGET_URLS)}")
    st.markdown("---")
    st.subheader("🎯 Risk Levels")
    st.markdown("🔴 **HIGH** — Critical data exposure")
    st.markdown("🟠 **MEDIUM** — Significant security concern")
    st.markdown("🟡 **LOW** — Worth monitoring")
    st.markdown("🟢 **INFO** — General finding")

col1, col2 = st.columns([2,1])
with col1:
    st.info("Click Run to scan all target URLs for sensitive keywords in real time.")
with col2:
    run_btn = st.button("▶ Run Monitor Now", use_container_width=True)

if run_btn:
    with st.spinner("Scanning websites for keywords... this may take 30-60 seconds..."):
        results = run_monitor()

    st.success(f"✅ Scan complete — {len(results)} checks performed")

    # Metrics
    matched = [r for r in results if r.get("matched")]
    high    = [r for r in matched if r["risk"] == "HIGH"]
    medium  = [r for r in matched if r["risk"] == "MEDIUM"]
    low     = [r for r in matched if r["risk"] == "LOW"]

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Checks",    len(results))
    m2.metric("🔴 HIGH Alerts",  len(high))
    m3.metric("🟠 MEDIUM Alerts",len(medium))
    m4.metric("🟡 LOW Alerts",   len(low))

    # Results table
    st.subheader("📋 All Findings")
    RISK_EMOJI = {"HIGH": "🔴 HIGH", "MEDIUM": "🟠 MEDIUM", "LOW": "🟡 LOW"}

    import pandas as pd
    df = pd.DataFrame([{
        "Keyword":   r["keyword"],
        "Risk":      RISK_EMOJI.get(r["risk"], r["risk"]),
        "URL":       r["url"],
        "Match":     "✅ FOUND" if r.get("matched") else "❌ Not found",
        "Time":      r["timestamp"],
    } for r in results])
    st.dataframe(df, use_container_width=True)

    # Charts
    st.subheader("📊 Charts")
    c1, c2 = st.columns(2)

    with c1:
        fig, ax = plt.subplots()
        labels = ["HIGH", "MEDIUM", "LOW", "No Match"]
        values = [len(high), len(medium), len(low),
                  len(results) - len(matched)]
        colors = ["#B71C1C", "#F44336", "#FFC107", "#4CAF50"]
        ax.bar(labels, values, color=colors)
        ax.set_title("Alerts by Risk Level")
        ax.set_ylabel("Count")
        st.pyplot(fig)

    with c2:
        kw_matches = {}
        for r in matched:
            kw_matches[r["keyword"]] = kw_matches.get(r["keyword"], 0) + 1
        if kw_matches:
            fig2, ax2 = plt.subplots()
            ax2.barh(list(kw_matches.keys()), list(kw_matches.values()),
                     color="#E24B4A")
            ax2.set_title("Most Detected Keywords")
            ax2.set_xlabel("Times Found")
            plt.tight_layout()
            st.pyplot(fig2)
        else:
            st.info("No keyword matches found in this scan.")

    # Detailed alerts
    if matched:
        st.subheader("🚨 Alert Details")
        for r in matched:
            risk_color = {"HIGH":"🔴","MEDIUM":"🟠","LOW":"🟡"}.get(r["risk"],"🟢")
            with st.expander(f"{risk_color} [{r['risk']}] '{r['keyword']}' found at {r['url']}"):
                st.code(
                    f"Keyword   : {r['keyword']}\n"
                    f"Risk      : {r['risk']}\n"
                    f"URL       : {r['url']}\n"
                    f"Timestamp : {r['timestamp']}"
                )
    else:
        st.info("No keyword matches found in this scan — all clear.")