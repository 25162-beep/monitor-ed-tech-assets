import streamlit as st
import matplotlib.pyplot as plt
import os

LOG_FILE = os.path.join("logs", "results.txt")

def load_logs():
    """Load log entries from results.txt."""
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]

st.title("🔎 Keyword Monitoring Dashboard")
st.markdown("Interactive dashboard for monitoring keyword alerts across websites.")

if st.button("Load Monitoring Results"):
    logs = load_logs()
    if logs:
        # Show raw log entries
        st.subheader("📜 Raw Log Entries (latest 20)")
        for entry in logs[-20:]:
            st.text(entry)

        # Extract summary line
        summary_lines = [line for line in logs if "Monitoring complete" in line]
        if summary_lines:
            st.subheader("✅ Summary")
            st.write(summary_lines[-1])

        # Visualization: count alerts vs checks
        alerts = sum(1 for line in logs if "ALERT" in line)
        checks = sum(1 for line in logs if "Checked" in line)
        categories = ["Alerts", "Checks"]
        counts = [alerts, checks]

        fig, ax = plt.subplots()
        ax.bar(categories, counts, color=["red", "blue"])
        ax.set_title("Keyword Monitoring Results")
        ax.set_ylabel("Number of Entries")
        st.pyplot(fig)
    else:
        st.warning("No logs found yet. Run monitor.py first to generate results.")
