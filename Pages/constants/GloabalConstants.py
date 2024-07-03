from selenium.webdriver.common.by import By
CATEGORY_XPATH = (By.XPATH, "//header[@id='header']/nav[@class='catMenu']/ul/li[1]/a[@title='Moda']")
SUBCATEGORY_XPATH = (By.XPATH, "//header[@id='header']/nav[@class='catMenu']/ul[@class='container']//a[@title='Ayakkabı & Çanta']/img")
RESULT_TEXT = "Moda Ayakkabı & Çanta"
RESULT_TEXT_CLASS = (By.XPATH, "//*[@id='breadCrumb']")