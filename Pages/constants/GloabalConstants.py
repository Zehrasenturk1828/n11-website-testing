from selenium.webdriver.common.by import By

#ProductCategory
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

#ProductFiltering
#test_searchbutton_function_control
SEARCHBOX_XPATH = (By.XPATH, "/html//input[@id='searchData']")
PRODUCT_NAME = "Telefon"
SEND_BUTTON = (By.XPATH, "/html//header[@id='header']/div[@class='container']//a[@title='ARA']/span[@class='iconsSearch']")
PRODUCT_CATEGORY_PATH = (By.XPATH, "//*[@id='breadCrumb']")
PRODUCT_CATEGORY_PATH_TEXT = ("Ana Sayfa\nElektronik\nTelefon & Aksesuarları\nCep Telefonu\ntelefon")

#test_price_range_filters
PRICE_RANGE_MIN = "5000"
PRICE_RANGE_MIN_XPATH = (By.XPATH, "//*[@id='minPrice']")
PRICE_RANGE_MAX = "10000"
PRICE_RANGE_MAX_XPATH = (By.XPATH, "//*[@id='maxPrice']")
CONFIRM_FILTERS_XPATH = (By.XPATH, "//*[@id='priceSearchButton']")
FILTER_GROUP_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[1]/section[2]/div/div/div")
FILTER_GROUP_TEXT = "5000 TL - 10000 TL"

#test_brand_filters
BRAND_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[1]/section[5]/div/div[2]/div[1]/label/span")
BRAND_FILTER_GROUP_TEXT = "Samsung"

#test_category_filters
CATEGORY_PRODUCT_NAME = "Etek"
CATEGORY_FILTER_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[1]/section[2]/div/ul/li/ul/li/ul/li/ul[1]/li/a")
CATEGORY_BREADCRUMB_TEXT = "Moda\nKadın Giyim & Aksesuar\nEtek\nMidi Etek\netek"

#test_product_rating_filters
PRODUCT_RATING_FILTER_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[1]/section[19]/div/div/div[2]")
PR_FILTER_GROUP_TEXT = "4 yıldız ve üzeri"
COOKIES_XPATH = (By.XPATH,"//*[@id='1d5d7aff-8ee1-4a98-9022-f0e29a5e471c']")


#test_combination_mutliple_filters
DEFACTO_BRAND_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[2]/section/div[1]/div[3]/div/ul/div/div/li[1]/a")
MF_SUBCATEGORY_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[1]/section[2]/div/ul/li/ul/li/ul/li/ul[1]/li/a")