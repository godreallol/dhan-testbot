import pyotp
from dhanhq import dhanhq
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# YOUR VALUES
CLIENT_ID = "YOUR_CLIENT_ID"

# generate OTP
totp = pyotp.TOTP("YOUR_TOTP_SECRET")
otp = totp.now()

print("Generated OTP:", otp)

# here login automation happens
# extract access token

ACCESS_TOKEN = "GENERATED_TOKEN"

# connect to dhan
dhan = dhanhq(CLIENT_ID, ACCESS_TOKEN)

# place order
response = dhan.place_order(
    security_id="11536",
    exchange_segment="NSE_EQ",
    transaction_type="BUY",
    quantity=1,
    order_type="MARKET",
    product_type="CNC",
    price=0
)

print(response)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://web.dhan.co")
