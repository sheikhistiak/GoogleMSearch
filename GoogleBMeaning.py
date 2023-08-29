from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome WebDriver with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Provide the path to your ChromeDriver executable
# driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)
# Set up ChromeDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Maximize the browser window
driver.maximize_window()

# Define the search query
search_query = "Dhoom meaning"

# Navigate to Google search
driver.get(f"https://www.google.com/search?q={search_query}")

wait = WebDriverWait(driver, 20)  # Adjust the timeout as needed

# Find and extract data using the given complex CSS selector or XPATH
complex_IndxXpath = "(//div[@class='wHYlTd sY7ric'])[1]"
try:
    found_Element = driver.find_element(By.XPATH, complex_IndxXpath)
    noun_data_element1 = wait.until(
        EC.presence_of_element_located((By.XPATH, complex_IndxXpath))
    )
    noun_complex_data1 = noun_data_element1.text

    print(f"""Search results for "{search_query}" is: \n {noun_complex_data1}\n""")

    # Find and click the element with tl_select attribute
    select_lang_element1 = wait.until(
        EC.presence_of_element_located((By.ID, "tl_select"))
    )
    select_lang_element1.click()

    # Use the Select class to interact with the dropdown options
    select = Select(select_lang_element1)
    # Select a specific option by value, text, or index
    select.select_by_value("bn")  # Select the option with value "bn"
    time.sleep(2)
    # Find and click the element by its index using XPath or CSS
    lang_element_CSS = ".Dwmjg"  # Replace with the actual XPath Or CSS
    lang_element_transl = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, lang_element_CSS))
    )
    print("Meaning in Bangla\n" + lang_element_transl.text)

except NoSuchElementException:
    # If the first element is not found, try to find another element
    another_CSS_select = "div[class='V3FYCf'] b"
    try:
        another_meaning1 = driver.find_element(By.CSS_SELECTOR, another_CSS_select)

        print(f"Search results for {search_query} is: \n {another_meaning1.text}.")
    except NoSuchElementException:
        print("Both elements not found")

# Add a time delay before closing the WebDriver
time.sleep(5)  # Adjust the delay time as needed

# Close the WebDriver
driver.quit()
