from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time  # Import for sleep

# Initialize the WebDriver
driver = webdriver.Firefox()

try:
    # Open the website
    driver.get("https://schedule.vcccd.edu")

    # Wait for the page to load completely
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Ensure the browser window is active
    if not driver.window_handles:
        raise Exception("No browser windows available. Check if the window was closed.")

    # Wait for the combobox to appear and click it
    element = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#site-divinput.divinput"))
    )
    element.click()

    # Wait for the list item to appear and select it
    list_item = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "site-divinput-1"))
    )
    list_item.click()

    # Simulate pressing the 'Escape' key to exit the dropdown
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # Scroll to ensure the search button is visible
    search_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", search_button)

    # Click the search button
    search_button.click()
    print("Search button clicked successfully!")

    # Add a sleep delay for the page to load
    time.sleep(10)  # Wait for 10 seconds

    # Wait for the secondary button on the next page to appear
    secondary_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-secondary"))
    )
    secondary_button.click()  # Click the secondary button
    print("Secondary button clicked successfully!")

    # Print the HTML source of the current page to debug
    print(driver.page_source)  # Prints the full HTML source of the current page

    # Wait for `td.tdhide` elements to appear
    print("Waiting for `td.tdhide` elements to load...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.tdhide"))
    )

    # Extract text from all `td.tdhide` elements
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

except Exception as e:
    # Print the error for debugging
    print(f"An error occurred: {e}")

finally:
    # Close the browser AFTER confirming website interaction
    input("Press Enter to close the browser...")  # Wait for user confirmation
    driver.quit()