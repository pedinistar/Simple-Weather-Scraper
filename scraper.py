from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def get_weather():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    city = input("Enter the city: ")

    try:
        search_bar = driver.find_element(By.NAME, "q")
        search_bar.send_keys(f"Weather in {city}")
        search_bar.send_keys(Keys.ENTER)
        sleep(2)

        temperature = driver.find_element(By.ID, "wob_tm").text
        condition = driver.find_element(By.ID, "wob_dc").text

        print(f"Current weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
        return
    except:
        print("Error: Could not retrieve weather data")
    finally:
        driver.quit()


if __name__ == "__main__":
    get_weather()
