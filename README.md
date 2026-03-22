# 🚀 EC2 Scheduler (Auto Start/Stop Automation)

## 📌 Overview

This project automates the starting and stopping of AWS EC2 instances based on defined schedules.
It helps optimize cloud costs by ensuring instances only run when needed.

---

## ⚙️ Features

* Start EC2 instances automatically
* Stop EC2 instances automatically
* Logging for tracking operations
* Can be scheduled using cron jobs
* Reduces AWS cost significantly

---

## 🛠 Tech Stack

* Python
* AWS EC2
* Boto3
* Linux (Cron)

---

## 📂 Project Structure

```bash
ec2-scheduler/
│
├── script/
│   └── ec2_scheduler.py
├── config/
│   └── config.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 How It Works

The script:

1. Checks current time
2. Compares with defined schedule
3. Starts or stops EC2 instances accordingly

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure AWS

```bash
aws configure
```

### 3. Run script

```bash
python script/ec2_scheduler.py
```

---

## ⏰ Automation using Cron

Edit cron:

```bash
crontab -e
```

Example (run every 5 minutes):

```bash
*/5 * * * * python /home/ec2-user/ec2-scheduler/script/ec2_scheduler.py
```

---

## 📊 Use Cases

* Office-hour based EC2 usage
* Dev/Test environments
* Cost optimization in AWS

---

## 💡 Future Improvements

* Add Slack/Email alerts
* Use AWS Lambda instead of cron
* Add tagging-based filtering

---

## 👨‍💻 Author

Raj Sharma
