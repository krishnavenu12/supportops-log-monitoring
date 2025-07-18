# 🛠️ SupportOps Log Monitoring System

![CI](https://github.com/krishnavenu12/supportops-log-monitoring/actions/workflows/test.yml/badge.svg)

A real-time backend system built using FastAPI that mimics a production support environment by simulating log ingestion, severity classification, and alerting. It’s designed to help you learn support engineering workflows like triaging, log monitoring, and backend testing.

---

## 🚀 Features

- 📥 **POST /log** — Submit logs with severity, timestamp, service name
- 🚨 **Automatic Alert Triggering** — For ERROR/CRITICAL logs
- 🔍 **GET /alerts** — Retrieve triggered alerts
- 🧪 **Test Coverage with Pytest**
- 🔄 **CI/CD Integration with GitHub Actions**
- 💡 **Modular Codebase** with FastAPI, reusable alert engine

---

## 🧰 Tech Stack

- **FastAPI** for API and backend logic
- **Python** for core logic and alert engine
- **Pytest** for unit testing
- **GitHub Actions** for CI/CD automation

---

## 📦 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/krishnavenu12/supportops-log-monitoring.git
   cd supportops-log-monitoring
