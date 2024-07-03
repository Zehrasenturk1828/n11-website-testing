from selenium.webdriver.common.by import By
#test_selecting_subcategory
CATEGORY_XPATH = (By.XPATH, "//header[@id='header']/nav[@class='catMenu']/ul/li[1]/a[@title='Moda']")
SUBCATEGORY_XPATH = (By.XPATH, "//header[@id='header']/nav[@class='catMenu']/ul[@class='container']//a[@title='Ayakkabı & Çanta']/img")
RESULT_TEXT = "Moda\nAyakkabı & Çanta"
RESULT_TEXT_CLASS = (By.XPATH, "//*[@id='breadCrumb']")

#test_selecting_maincategory
ADD_MEDIA_SCRRENSHOT_PATH = r'screenshots/ProductCategory/displayedsubcategories.png'
WOMENS_CLOTHING_XPATH = (By.XPATH, "/html//div[@id='contentCategory']//a[@href='https://www.n11.com/kadin-giyim-aksesuar']/img[@alt='KADIN GİYİM']")
BREADCRUMB_TEXT = "Moda\nKadın Giyim & Aksesuar"
BREADCRUMB_XPATH = (By.XPATH, "//*[@id='breadCrumb']")

#test_selecting_brandcategory
BRAND_MAVI_XPATH = (By.XPATH, "/html//div[@id='contentCategory']//div[@class='dynamicPageContainer']/div[4]/a[@title='Mavi']/img[@alt='Mavi']")
SELLER_NAME_XPATH = (By.XPATH, "//*[@id='contentSellerShop']/div/section[1]/div[2]/div[2]/div[1]/div[1]/h1")
BRAND_MAVI_TEXT = "Mavi"
