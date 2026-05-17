# contact_form_automation.py
# QA Intern Assignment - Part 2: UI Automation
# Author: Dulangi Thennakoon
# Framework: Selenium WebDriver (Python)
# Website: https://safora.se/en/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    print("Starting Selenium Automation...")
    
    # Path to ChromeDriver (ensure chromedriver.exe is in the same folder)
    service = Service("chromedriver.exe")  
    
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Safora website
        driver.get("https://safora.se/en/")
        print("Website loaded successfully")
        
        # Step 2: Navigate to Contact Us page
        contact_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact")))
        contact_link.click()
        time.sleep(2)
        print("Navigated to Contact Us page")
        
        # Step 3: Fill Out Contact Form
        name_field = driver.find_element(By.NAME, "name")
        name_field.clear()
        name_field.send_keys("Dulangi Thennakoon")
        
        email_field = driver.find_element(By.NAME, "email")
        email_field.clear()
        email_field.send_keys("dulangilakshani12@gmail.com")
        
        message_field = driver.find_element(By.NAME, "message")
        message_field.clear()
        message_field.send_keys("Hello, I am testing the contact form automation from Safora website.")
        
        print("Form fields filled successfully")
        
        # Step 4: Submit Form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(3)
        
        # Step 5: Verify Success Message
        try:
            success_msg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".success-message, .alert-success")))
            print(f"Success message found: {success_msg.text}")
        except Exception:
            if "thank you" in driver.page_source.lower():
                print("Success message detected in page content")
            else:
                print("Warning: Success message not found")
        
        # Step 6: Test Validation (Empty Fields)
        print("\nTesting form validation (empty fields)...")
        driver.refresh()
        time.sleep(1)
        
        name_field.clear()
        email_field.clear()
        message_field.clear()
        submit_button.click()
        time.sleep(2)
        
        if "required" in driver.page_source.lower() or "error" in driver.page_source.lower():
            print("Validation errors detected as expected")
        else:
            print("Warning: Validation errors not detected")
        
        print("\n" + "="*50)
        print("AUTOMATION TEST COMPLETED SUCCESSFULLY!")
        print("="*50)
        
    except Exception as e:
        print(f"\nAutomation Failed: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        driver.quit()
        print("Browser closed")

if __name__ == "__main__":
    main()