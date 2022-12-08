# @author   Lucas Cardoso de Medeiros
# @since    08/12/2022
# @version  1.0

# Create an Automated Amazon Price Tracker

from bs4 import BeautifulSoup
import requests
from notification_manager import NotificationManager


URL = 'https://www.amazon.com.br/dp/B07XC2FWD1?ref_=cm_sw_r_cp_ud_dp_HWRA755262Z0EDFGKMMP'
HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "pt-BR,pt;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
}
FLOOR_PRICE = 620.00


def get_price():
    """Scraping Amazon Product"""
    response = requests.get(url=URL, headers=HEADERS).content
    soup = BeautifulSoup(response, "html.parser")
    product = soup.find(name="span", id="productTitle").getText().strip()
    price_span = soup.find(name="span", class_="a-offscreen").getText()
    current_price = float(price_span.strip("R$").replace(",", "."))
    print(f"Product: {product}")
    print(f"Current price: R${current_price}")
    return current_price


if __name__ == "__main__":
    notification_manager = NotificationManager()
    price = get_price()
    if price < FLOOR_PRICE:
        print("Good deal! Send notification...")
        msg = f"Subject:Instant Price Alert!\n\n" \
              f"Low price alert!\n" \
              f"The product price is now R${price}" \
              f", bellow your target price.\nBuy now on Amazon:\n{URL}\nDon't miss!"
        if notification_manager.send_email(msg=msg):
            print("Notification sent")
    else:
        print("Current price not bellow floor price :(\nKeep looking!")
