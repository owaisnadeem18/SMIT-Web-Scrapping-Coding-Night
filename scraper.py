from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Set up Selenium Chrome WebDriver (headless for silent background run)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Note: In actual usage, provide path to your local chromedriver if needed
service = Service()
driver = webdriver.Chrome(service=service, options=options)

def scrape_rozee_jobs_with_selenium():
    job_titles = []
    companies = []
    locations = []
    skills_list = []
    dates = []

    for page in range(1, 3):
        url = f"https://www.rozee.pk/job-search/{page}"
        driver.get(url)
        time.sleep(2)  # wait for page to load

        jobs = driver.find_elements(By.CLASS_NAME, "job")
        print(f"Page {page} - Jobs found: {len(jobs)}")

        for job in jobs:
            try:
                title = job.find_element(By.CLASS_NAME, "s-18").text.strip()
            except:
                title = "N/A"

            try:
                company_and_loc = job.find_element(By.CLASS_NAME, "cname").text.strip().split(",")
                company = company_and_loc[0] if len(company_and_loc) > 0 else "N/A"
                location = company_and_loc[1] if len(company_and_loc) > 1 else "N/A"
            except:
                company = "N/A"
                location = "N/A"

            try:
                date = job.find_element(By.CSS_SELECTOR, ".rz-calendar+span").text.strip()
            except:
                date = "N/A"

            try:
                skill_elements = job.find_elements(By.CSS_SELECTOR, ".label.label-default")
                skills = ", ".join([skill.text.strip() for skill in skill_elements if skill.text.strip()])
            except:
                skills = "N/A"

            job_titles.append(title)
            companies.append(company)
            locations.append(location)
            dates.append(date)
            skills_list.append(skills)

    # Save to CSV
    df = pd.DataFrame({
        "Job Title": job_titles,
        "Company": companies,
        "Location": locations,
        "Date Posted": dates,
        "Skills": skills_list
    })

    df.to_csv("rozee_selenium_jobs.csv", index=False)
    return df.head()

scrape_rozee_jobs_with_selenium()
