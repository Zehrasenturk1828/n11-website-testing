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

#test_remove_filters
REMOVE_FILTERS_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[1]/section[2]/span")

#test_sorting_filters
DROPDOWN_MENU_XPATH = (By.XPATH, "//*[@id='smartListOption']/div[2]/div/div[1]/span")
PRICE_LOW_XPATH = (By.XPATH,"//*[@id='smartListOption']/div[2]/div/div[2]/div[2]")
PRICE_HIGH_XPATH = (By.XPATH, "//*[@id='smartListOption']/div[2]/div/div[2]/div[3]")
SALES_VOLUME_XPATH = (By.XPATH, "//*[@id='smartListOption']/div[2]/div/div[2]/div[4]")
REVIEWS_XPATH = (By.XPATH, "//*[@id='smartListOption']/div[2]/div/div[2]/div[5]")

#test_Local_advantages_feature
SELECT_LOCATION_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[2]/section/div[1]/div[2]/div[1]/div/span")
CITY_DROPDOWN_XPATH = (By.XPATH, "//*[@id='headerMyLocationCityId']")
DISTRICT_XPATH = (By.XPATH, "//*[@id='headerMyLocationDistrictId']")
ISTANBUL_XPATH = (By.XPATH, "//*[@id='headerMyLocationCityId']/option[41]")
SISLI_XPATH = (By.XPATH, "//*[@id='headerMyLocationDistrictId']/option[36]")
CONFIRM_LOCATION_XPATH = (By.XPATH, "//*[@id='headerSetMyLocationBtn']")
LOCATION_PLACE_XPATH = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[2]/section/div[1]/div[2]/div[1]/div/span")

#product_details
#test_product_detail_check
PRODUCT_XPATH = (By.XPATH, "//*[@id='p-625348535']/div/a/div/img")
SCREENSIZE_XPATH = (By.XPATH, "//*[@id='attribute_3']")
MORE_FEATURES_XPATH = (By.XPATH, "//*[@id='unf-prop']/div/p/span")


#test_changing_product_options
PRODUCT_OPTION_XPATH = (By.XPATH, "//*[@id='unfDetailForm']/div[1]/div[2]/div")
PRODUCT_COLOR_XPATH = (By.XPATH, "//*[@id='renk-0']/label[3]")
PRODUCT_MEMORY_XPATH = (By.XPATH, "//*[@id='dahili-hafiza-1']/label")
SELECT_PRODUCT_XPATH = (By.XPATH, "//*[@id='prop-opt-lb']/div/div[2]/span")
PRODUCT_INFO_XPATH = (By.XPATH, "//*[@id='unfDetailForm']/div[1]/div[2]/div/div/div[1]")


#test_tabs_control
PD_INFO_XPATH = (By.XPATH, "//*[@id='unfTabMenu']/ul/li[1]/a")
INFO_TITLE_XPATH = (By.XPATH, "//*[@id='unf-info']/div/div/h2")

PD_REVIEW_XPATH = (By.XPATH, "//*[@id='unfTabMenu']/ul/li[2]/a")
REVIEW_TITLE_XPATH = (By.XPATH, "//*[@id='unf-review']/div[1]/h3")

PD_SELLER_XPATH = (By.XPATH, "//*[@id='unfTabMenu']/ul/li[3]/a")
SELLER_TITLE_XPATH = (By.XPATH, "//*[@id='unf-sell']/h2")

PD_SHIPMENT_XPATH = (By.XPATH, "//*[@id='unfTabMenu']/ul/li[4]/a")
SHIPMENT_TITLE_XPATH = (By.XPATH, "//*[@id='unf-shipment-details']/div/div[1]")

PD_PAYMENT_XPATH = (By.XPATH, "//*[@id='unf-tab-payment-opt']")
PAYMENT_TITLE_XPATH = (By.XPATH, "//*[@id='unf-inst']")


#product_cart
#test_add_product_to_product_cart
ADD_BASKET_BUTTON_XPATH = (By.XPATH, "//*[@id='unfDetailForm']/div[2]/div[2]/div[1]/button")
POP_UP_XPATH = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div[4]/div/div/div[1]/div[2]")
BASKET_XPATH = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div[4]/a/i")
PROD_INFO_IN_BASKET_XPATH = (By.XPATH, "//*[@id='newCheckout']/div/div[1]/div[1]/div[2]/section/table[2]/tbody/tr/td[1]/div[3]/div[1]/a")


#test_update_cart
SKIRT_XPATH = (By.XPATH, "//*[@id='p-583344327']/div/a/div/img")
SPINNER_UP = (By.CLASS_NAME, "spinnerUp")
PRODUCT_PRICE = (By.XPATH, "//*[@id='newCheckout']/div/div[1]/div[1]/div[2]/section/table[2]/tbody/tr/td[3]/div/div")
TOTAL_PRICE = (By.XPATH, "//*[@id='newCheckout']/div/div[1]/div[2]/div/div/section/div/div[7]/span[2]")
DISCOUNT_PRICE = (By.XPATH, "//*[@id='newCheckout']/div/div[1]/div[2]/div/div/section/div/div[3]/span[2]")
CLICK_BASKET_XPATH = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div[4]/a/i")

#test_remove_product
REMOVE_BUTTON = (By.CLASS_NAME, "removeProd")
DELETE_BUTTON_ID = (By.ID, "deleteBtnDFLB")
EMPTY_BASKET_MESSAGE = (By.XPATH, "//*[@id='wrapper']/div[4]/div/div[1]/div[1]/h2")