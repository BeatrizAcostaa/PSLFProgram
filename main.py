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
    tdMeet_elements = driver.find_elements(By.CSS_SELECTOR, "td.tdMeet")
    tdMeetDate_elements = driver.find_elements(By.CSS_SELECTOR, "td.tdMeetDate")

    tdMeet_texts = [element.text for element in tdMeet_elements]
    tdMeetDate_texts = [element.text for element in tdMeetDate_elements]

    # Combine the information side by side
    combined_data = zip(tdMeet_texts, tdMeetDate_texts)

    # Write the combined text to a single file
    with open("MeetingTimes_text.txt", "w", encoding="utf-8") as file:
        file.write("td.tdMeet\t\t|\ttd.tdMeetDate\n")
        file.write("-" * 50 + "\n")
        for tdMeet_text, tdMeetDate_text in combined_data:
            file.write(f"{tdMeet_text}\t\t|\t{tdMeetDate_text}\n")

    print("Meeting times data combined and saved to 'MeetingTimes_text.txt' successfully!")

except Exception as e:
    # Handle errors
    print(f"An error occurred: {e}")

finally:
    # Wait for 1 minute before closing the browser
    print("Waiting for 1 minute before closing the browser...")
    time.sleep(60)
    print("Closing the browser...")
    driver.quit()
    print("Browser closed successfully.")