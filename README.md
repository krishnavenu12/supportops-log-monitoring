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

---

## 👨‍💻 Author

```md
- **Krishna Venugopal**  
  [GitHub: @krishnavenu12](https://github.com/krishnavenu12)  
  [LinkedIn](https://www.linkedin.com/in/krishna-venugopal-9b073b267/)  
  📫 [krishnakichuz2004@gmail.com](mailto:krishnakichuz2004@gmail.com)

---

## 🤝 Contributing

Contributions are welcome!  
If you have suggestions, bug reports, or feature requests, feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes and commit (`git commit -m 'Add some feature'`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and passes all tests.

---

## 📄 License

This project is licensed for personal, educational, and portfolio use.  
For commercial or production deployment, please contact the author for permission.

© 2025 Krishna Venugopal

---


---

### ✅ Next Steps

- Paste this into your `README.md`
- Save it
- Run:
  ```bash
  git add README.md
  git commit -m "Update full README with author, license, contributing"
  git push

