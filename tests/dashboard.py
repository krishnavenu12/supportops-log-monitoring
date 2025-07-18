import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"

st.set_page_config(page_title="SupportOps Log Monitor", layout="wide")
st.title("🛡️ SupportOps Log Monitoring System")

# Fetch logs
try:
    logs = requests.get(f"{API_URL}/logs").json().get("logs", [])
except Exception as e:
    st.error(f"❌ Couldn't fetch logs: {e}")
    logs = []

# Add New Log
st.header("➕ Add New Log")
with st.form("add_log_form"):
    timestamp = st.text_input("Timestamp (YYYY-MM-DDTHH:MM:SS)", placeholder="2025-07-18T10:00:00")
    severity = st.selectbox("Severity", ["INFO", "WARNING", "ERROR", "CRITICAL"])
    service = st.text_input("Service Name")
    message = st.text_area("Log Message")
    submitted = st.form_submit_button("Add Log")
    if submitted:
        if not timestamp or not service or not message:
            st.warning("All fields are required.")
        else:
            res = requests.post(f"{API_URL}/logs", json={
                "timestamp": timestamp,
                "severity": severity,
                "service": service,
                "message": message
            })
            if res.status_code == 200:
                st.success("✅ Log added successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to add log.")

# Display logs
st.header("📋 Logs")

if logs:
    df = pd.DataFrame(logs)

    # Highlight CRITICAL logs
    def highlight_critical(row):
        return ['background-color: red; color: white' if row['severity'] == 'CRITICAL' else '' for _ in row]

    st.dataframe(df.style.apply(highlight_critical, axis=1), use_container_width=True)

    # Update/Delete
    for index, row in df.iterrows():
        with st.expander(f"📝 Log ID {row['id']} - {row['service']}"):
            new_timestamp = st.text_input(f"Timestamp_{row['id']}", value=row["timestamp"])
            new_severity = st.selectbox(f"Severity_{row['id']}", ["INFO", "WARNING", "ERROR", "CRITICAL"], index=["INFO", "WARNING", "ERROR", "CRITICAL"].index(row["severity"]))
            new_service = st.text_input(f"Service_{row['id']}", value=row["service"])
            new_message = st.text_area(f"Message_{row['id']}", value=row["message"])
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Update Log {row['id']}"):
                    res = requests.put(f"{API_URL}/logs/{row['id']}", json={
                        "timestamp": new_timestamp,
                        "severity": new_severity,
                        "service": new_service,
                        "message": new_message
                    })
                    if res.status_code == 200:
                        st.success("✅ Log updated.")
                        st.rerun()
                    else:
                        st.error("❌ Failed to update log.")
            with col2:
                if st.button(f"Delete Log {row['id']}"):
                    res = requests.delete(f"{API_URL}/logs/{row['id']}")
                    if res.status_code == 200:
                        st.success("🗑️ Log deleted.")
                        st.rerun()
                    else:
                        st.error("❌ Delete failed.")
else:
    st.warning("⚠️ No logs to display.")

# Chart
if logs:
    st.subheader("📊 Log Summary")
    col1, col2 = st.columns(2)
    with col1:
        count_by_severity = df["severity"].value_counts().reset_index()
        count_by_severity.columns = ["severity", "count"]
        st.plotly_chart(px.pie(count_by_severity, names="severity", values="count", title="Logs by Severity"))
    with col2:
        count_by_service = df["service"].value_counts().reset_index()
        count_by_service.columns = ["service", "count"]
        st.plotly_chart(px.bar(count_by_service, x="service", y="count", title="Logs by Service"))
