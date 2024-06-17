from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    target_url = "https://passport2.chaoxing.com/login"
    driver = webdriver.Chrome()
    driver.get(target_url)

    fanyi_id = "18508205503"
    fanyi_pwd = "jmh+2937703346"
    user_name = "姜美恒"
        # WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "showlogintext")))
    if login_success := WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "lg-title"))):
        print("Page open successfully!")
    else:
        print("Page open failed!")
        exit(1)
