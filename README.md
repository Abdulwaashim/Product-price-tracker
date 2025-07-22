# 🛒 Product Price Tracker with Email Alerts

This is a Python-based automation project that scrapes Amazon product prices using Selenium and sends you an **email alert** when the price drops below your set threshold.

> 🔔 Never miss a price drop again!

---

## 📌 Features

- ✅ Scrapes product title and price using Selenium
- ✅ Sends email alerts when the price drops
- ✅ Customizable target price and URL
- ✅ Modular code structure with functions
- ✅ Easy to schedule with Windows Task Scheduler

---

## 🚀 Tech Stack

- Python 3.x
- Selenium
- WebDriver Manager
- smtplib (Email)
- Jupyter Notebook / .py Script

---

## 🧠 How It Works

1. You define:
   - Product URL (Amazon.in or Amazon.com)
   - Target price (your threshold)
2. The script:
   - Opens the product page using Selenium
   - Extracts product title and price
   - Sends an email alert if price < target

---

## 🔧 Setup Instructions

### 1. Clone the repo:
```bash
git clone https://github.com/Abdulwaashim/amazon-price-tracker.git
cd amazon-price-tracker
```

### 2. Install dependencies:

```bash
pip install selenium webdriver-manager
```

### 3. Configure Email:
  - Enable 2-Step Verification in your Gmail
  - Create an App Password Google Guide
  - Replace the following in your script:
```bash
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
app_password = "your_generated_app_password"
```

### Run Script
```bash
python amazon_price_tracker.py
```

### Example Output
```bash
Product: boAt Bassheads 105 Wired Earphones
Current Price: ₹399
😕 No drop yet. Current price ₹399 is above ₹350.
```

### 👨‍💻 Author
Abdul Waashim
A passionate self-taught Data Analyst building practical, automation-based Python projects.

