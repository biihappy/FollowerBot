from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc

class Setup:
    def init(self):
        #warnings.filterwarnings("ignore")
        chrome_options = uc.ChromeOptions()
        #chrome_options.add_argument('--window-size=1036, 674')
        #chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        #chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.headless=True
        chrome_options.add_argument('--headless')
        #chrome_options.add_argument("--log-level=3")
        #chrome_options.add_experimental_option("prefs", {
        #    "profile.default_content_setting_values.notifications": 1
        #})
        #self.browser = uc.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options, )
        self.browser = uc.Chrome(options=chrome_options)

    def close_browser(self):
        self.browser.close()
