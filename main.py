from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class typer:

    def __init__(self):
        self.timer = 10
        #creates a webdriver chrome object that starts typeracer
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.get("https://play.typeracer.com/")
        time.sleep(5)
        # start a race and locate the typebox element
        self.elem = self.driver.find_element(By.LINK_TEXT, value='Enter a Typing Race').click()
        time.sleep(10)
        


    def get_text(self):
        write_elem = self.wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//span[@unselectable='on']")))
        word_list = []
        for x in write_elem:
            word = x.text
            temp = str(word)
            word_list.append(temp)

        if len(word_list) == 3:
            word_text = f'{word_list[0]}{word_list[1]} {word_list[2]}'
        else:
            word_text = f'{word_list[0]} {word_list[1]}'
        return word_text
        
    def write_text(self, word):
        time.sleep(10)
        type_box = self.driver.find_element(By.CLASS_NAME, "txtInput")
        for x in str(word):
            print(x)
            type_box.send_keys(x)
            time.sleep(1/self.timer)
        time.sleep(2)
        wpm = self.driver.find_element(By.CLASS_NAME, value = "rankPanelWpm-self")
        wpm_count = int((wpm.text).replace(" wpm", ""))
        self.driver.close()
        return wpm_count
        




if __name__ == "__main__":

    start = typer()
    start.write_text(start.get_text())

