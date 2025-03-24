from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Define the custom click method
def click(driver, locator):
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(locator)).click()

try:
    # Open the website
    print("Opening the website...")
    driver.get("https://schedule.vcccd.edu")

    # Wait for the page to load completely
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Page loaded successfully!")

    # Select the term dropdown
    term_dropdown = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTermSelect.form-select.gap-3"))
    )
    select = Select(term_dropdown)
    select.select_by_value("202503")
    print("Spring 2025 term selected successfully!")

    click(driver, (By.CSS_SELECTOR, "input#site-divinput.divinput"))
    click(driver, (By.CSS_SELECTOR, "input#site-divinput.divinput"))
    print("Combo box clicked successfully!")

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li#site-divinput-1.item")))
    element = driver.find_element(By.CSS_SELECTOR, "li#site-divinput-1.item")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # Wait for and interact with the list item
    click(driver, (By.CSS_SELECTOR, "li#site-divinput-1.item"))
    print("List item clicked successfully!")

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn:nth-child(5)")))
    element = driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(5)")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    click(driver, (By.CSS_SELECTOR, "button.btn:nth-child(5)"))
    print("Search button clicked successfully!")

    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#info-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")))
    element = driver.find_element(By.CSS_SELECTOR, "#info-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    click(driver, (By.CSS_SELECTOR, "#info-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)"))
    print("Close button clicked successfully!")

    time.sleep(6)
    elements = driver.find_elements(By.CSS_SELECTOR, "td.tdhide")
    text_content = [element.text for element in elements]

    # Debug: Print all `td.tdhide` elements and their text content
    if elements:
        print(f"Found {len(elements)} `td.tdhide` elements!")
        for element in elements:
            print(element.get_attribute("outerHTML"))  # Debugging: Print HTML content
            print(f"Extracted Text: {element.text}")  # Debugging: Print text content
    else:
        print("No `td.tdhide` elements found!")

    # Write the extracted text to a file
    with open("extracted_text.txt", "w", encoding="utf-8") as file:
        for text in text_content:
            file.write(text + "\n")

    print("Text extracted and saved to 'extracted_text.txt' successfully!")

    elements = driver.find_elements(By.CSS_SELECTOR, "td.tdMeet")
    text_content = [element.text for element in elements]

    # Debug: Print all `td.tdhide` elements and their text content
    if elements:
        print(f"Found {len(elements)} `td.tdMeet` elements!")
        for element in elements:
            print(element.get_attribute("outerHTML"))  # Debugging: Print HTML content
            print(f"Extracted Text: {element.text}")  # Debugging: Print text content
    else:
        print("No `td.tdMeet' elments found!")

    # Write the extracted text to a file
    with open("MeetingTimes_text.txt", "w", encoding="utf-8") as file:
        for text in text_content:
            file.write(text + "\n")

    print("Text extracted and saved to 'MeetingTimes_text.txt' successfully!")

except Exception as e:
    # Handle errors
    print(f"An error occurred: {e}")

finally:
    # Wait for 2 minutes before closing the browser
    print("Waiting for 1 min before closing the browser...")
    time.sleep(60)
    print("Closing the browser...")
    driver.quit()
    print("Browser closed successfully.")

