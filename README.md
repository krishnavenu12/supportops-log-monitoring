# SupportOps Log Monitoring System
![CI](https://github.com/krishnavenu12/supportops-log-monitoring/actions/workflows/test.yml/badge.svg)

A simulation tool for real-time log monitoring and alerting using FastAPI and Python.

## Features
- Receive and process logs via API
- Trigger alerts for ERROR and CRITICAL logs
- View active critical alerts via GET endpoint
- Includes CI testing and alert logic
- Resume-worthy and relevant to support engineering roles

## Endpoints
- POST /log → Submit a log entry
- GET /alerts → View active critical alerts
