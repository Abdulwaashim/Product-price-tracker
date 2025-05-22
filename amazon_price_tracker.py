#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Email Alert Function ---
def send_email(product_title, product_price, url):
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient_email@gmail.com"
    app_password = "your_app_password_here"

    subject = "🟢 Amazon Price Drop Alert!"
    body = f"The price for '{product_title}' has dropped to ₹{product_price}!\nCheck it here: {url}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Email failed:", e)

# --- Main Function ---
def check_price(url, target_price):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(5)

    # Get product title
    try:
        title = driver.find_element(By.ID, "productTitle").text.strip()
    except:
        title = "Title not found"

    # Get product price
    try:
        price = driver.find_element(By.ID, "priceblock_dealprice").text.strip()
    except:
        try:
            price = driver.find_element(By.ID, "priceblock_ourprice").text.strip()
        except:
            try:
                price = driver.find_element(By.CLASS_NAME, "a-price-whole").text.strip()
            except:
                price = "0"

    driver.quit()

    try:
        price_num = int(price.replace(",", "").split(".")[0])
    except:
        price_num = 0

    # Check price and trigger alert
    print("Product:", title)
    print("Current Price: ₹", price_num)

    if price_num < target_price:
        print(f"💸 Price dropped! Current price ₹{price_num} is below ₹{target_price}!")
        send_email(title, price_num, url)
    else:
        print(f"😕 No drop yet. Current price ₹{price_num} is above ₹{target_price}.")

# --- Call your function here ---
check_price("https://www.amazon.in/dp/B08YYVW968", 350)

