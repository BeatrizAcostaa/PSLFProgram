from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Firefox()

try:
    # Open the website
    driver.get("https://schedule.vcccd.edu")

    # Ensure the browser window is active
    if not driver.window_handles:
        raise Exception("No browser windows available. Check if the window was closed.")

    # Wait for the combobox to appear and click it
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#site-divinput.divinput"))
    )
    element.click()

    # Wait for the list item to appear and select it
    list_item = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "site-divinput-1"))
    )
    list_item.click()

    # Simulate pressing the 'Escape' key to exit the dropdown
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # Scroll to ensure the search button is visible
    search_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", search_button)

    # Click the search button
    search_button.click()
    print("Search button clicked successfully!")

    # Wait for the secondary button on the next page to appear
    secondary_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-secondary"))
    )
    secondary_button.click()  # Click the secondary button
    print("Secondary button clicked successfully!")

    # Wait for the next step or element after clicking the secondary button
    # Example: Wait for content update or a new element
    new_content = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "new-content-id"))  # Replace with the actual ID or selector of the new element
    )
    print("New content loaded successfully!")

except Exception as e:
    # Print the error for debugging
    print(f"An error occurred: {e}")

finally:
    # Close the browser AFTER confirming website interaction
    input("Press Enter to close the browser...")  # Wait for user confirmation
    driver.quit()
