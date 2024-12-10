from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image

def capture_website_snapshot(url, output_file="snapshot.png", browser_path="chromedriver"):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run browser in headless mode
    chrome_options.add_argument("--window-size=1920,1080")  # Set window size
    
    # Initialize WebDriver
    service = Service(browser_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Load the website
        driver.get(url)
        
        # Take screenshot
        screenshot = driver.get_screenshot_as_file(output_file)
        print(f"Snapshot saved as {output_file}")
        
        # Optionally, crop to visible area using Pillow (if needed)
        with Image.open(output_file) as img:
            cropped = img.crop((0, 0, img.width, img.height))  # Adjust cropping as needed
            cropped.save(output_file)
        
    finally:
        driver.quit()

# Example usage
capture_website_snapshot("https://example.com", "example_snapshot.png", browser_path="path/to/chromedriver")
