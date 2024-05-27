from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(1400, 900)
        self.driver.get("https://www.instagram.com/")

    def login(self, username, password):
        sleep(1)
        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        login_button.click()

        sleep(4)
        save_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        save_button.click()
        alert_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        alert_button.click()

    def find_followers(self, user_name):
        self.driver.get(f"https://www.instagram.com/{user_name}/")

        sleep(3)
        followers_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'フォロワー')]")
        followers_button.click()

    def follow(self):
        sleep(3)
        for i in range(2, 100):
            try:
                follow_button = self.driver.find_element(By.XPATH, f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button")
            except:
                follow_button = self.driver.find_element(By.XPATH, f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[3]/div/button")
                follow_button.send_keys(Keys.END)
                sleep(2)
                follow_button = self.driver.find_element(By.XPATH, f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button")
            finally:
                if follow_button.text == "フォロー":
                    follow_button.click()
                sleep(1)
