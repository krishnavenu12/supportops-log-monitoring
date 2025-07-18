# 🛠️ SupportOps Log Monitoring System

![CI](https://github.com/krishnavenu12/supportops-log-monitoring/actions/workflows/test.yml/badge.svg)

A real-time backend system built using FastAPI for simulating log ingestion, severity classification, and automatic alerting. Mimics real-world support environments and is integrated with GitHub Actions for CI/CD.

---

## 🚀 Features

- 🔍 API to submit and review logs (`/log`, `/alerts`)
- 🚨 Alerts triggered for ERROR/CRITICAL entries
- 🧪 Unit tests with `pytest`
- 🔄 CI/CD with GitHub Actions
- 📦 Clean modular Python backend (`app/`, `tests/`)

---

## 📦 How to Run

```bash
uvicorn app.main:app --reload
