import streamlit as st

st.set_page_config(
    page_title="GRC Practice Lab", page_icon="🛡️", layout="wide"
)

st.title("🛡️ GRC Practice Lab | Cloud Security & Compliance Automation")
st.write(
    "Welcome to my interactive compliance, risk management, and AI governance dashboard!"
)

# Sidebar for GRC Framework Selection
st.sidebar.header("Audit Configuration")
framework = st.sidebar.selectbox(
    "Select Compliance Framework",
    [
        "ISO 27001:2022",
        "NIST AI RMF (AI Framework)",
        "NIST SP 800-53",
        "COBIT 2019",
        "SOC 2 Trust Services",
    ],
)
target_cloud = st.sidebar.selectbox(
    "Target Environment", ["Azure Subscriptions", "AWS Multi-Account", "On-Prem"]
)

# Main Dashboard Layout
col1, col2, col3 = st.columns(3)
col1.metric(
    label="Active Framework", value=framework, delta="Continuous Monitoring"
)
col2.metric(label="Evaluated Controls", value="142 / 150", delta="94.6%")
col3.metric(label="Risk Posture Score", value="Low Risk", delta="Optimized")

st.divider()

st.subheader(f"Control Assessment: {framework}")
st.write(
    f"Running automated compliance verification mapping against {target_cloud}..."
)

# Interactive Scan Trigger
if st.button("Run Compliance Scan"):
  with st.spinner("Executing automated policy checks..."):
    # Simulated control validation results
    st.success("Control frameworks validated successfully!")

    # Display simulated audit findings table based on framework selection
    st.markdown("### Control Evaluation Report")

    if "ISO 27001" in framework:
      audit_data = [
          {
              "Control ID": "A.5.1",
              "Domain": "Information Security Policies",
              "Status": "Passed",
              "Severity": "High",
          },
          {
              "Control ID": "A.9.1",
              "Domain": "Access Control",
              "Status": "Passed",
              "Severity": "Critical",
          },
          {
              "Control ID": "A.12.4",
              "Domain": "Logging and Monitoring",
              "Status": "Warning",
              "Severity": "Medium",
          },
          {
              "Control ID": "A.8.24",
              "Domain": "Use of Cryptography",
              "Status": "Passed",
              "Severity": "High",
          },
      ]
    elif "NIST AI" in framework:
      audit_data = [
          {
              "Control ID": "Govern 1.1",
              "Domain": "AI Risk Governance & Legal",
              "Status": "Passed",
              "Severity": "High",
          },
          {
              "Control ID": "Map 2.3",
              "Domain": "AI System Context & Impacts",
              "Status": "Passed",
              "Severity": "Critical",
          },
          {
              "Control ID": "Measure 2.7",
              "Domain": "Validity & Reliability Testing",
              "Status": "Warning",
              "Severity": "High",
          },
          {
              "Control ID": "Manage 4.2",
              "Domain": "AI Incident Response & Post-Deployment",
              "Status": "Passed",
              "Severity": "Medium",
          },
      ]
    else:
      audit_data = [
          {
              "Control ID": "AC-2",
              "Family": "Access Control",
              "Status": "Passed",
              "Severity": "High",
          },
          {
              "Control ID": "SC-7",
              "Family": "System & Communications",
              "Status": "Passed",
              "Severity": "Critical",
          },
          {
              "Control ID": "AU-6",
              "Family": "Audit & Accountability",
              "Status": "Warning",
              "Severity": "Medium",
          },
          {
              "Control ID": "IA-5",
              "Family": "Identification & Authentication",
              "Status": "Passed",
              "Severity": "High",
          },
      ]

    st.table(audit_data)
