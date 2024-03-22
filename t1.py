import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import sys


def get_foreign_exchange_rate(date, currency_code):
    chrome_driver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    s = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=s)

    try:
        driver.get("https://www.boc.cn/sourcedb/whpj/")
        time.sleep(2)

        date_input = driver.find_element(By.CLASS_NAME, "pjrq")
        print("输入的日期", date_input)
        date_input.send_keys(date)

        currency_select = driver.find_element(By.ID, "pjname")
        print("输入的货币", currency_select)
        currency_select.send_keys(currency_code)

        query_button = driver.find_element(By.CLASS_NAME, "search_btn")
        print("按钮", query_button)
        driver.execute_script("arguments[0].click", query_button)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "BOC_main publish")))
        exchange_rate = driver.find_element(By.XPATH, "//td[text()='现汇卖出价']/following-sibling::td[2]").text

        with open("result.txt", "w") as file:
            file.write(f"{date} {currency_code} 现汇卖出价: {exchange_rate}")
        return exchange_rate

    except Exception as e:
        print("异常:", e)
        return None

    finally:
        driver.quit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <date> <currency_code>")
        sys.exit(1)

    date = sys.argv[1]
    currency_code = sys.argv[2]
    # print(date,currency_code)

    exchange_rate = get_foreign_exchange_rate(date, currency_code)
    if exchange_rate:
        print(exchange_rate)