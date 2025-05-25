import pandas as pd

# Load CSV
df = pd.read_csv('./rozee_selenium_jobs.csv', on_bad_lines='skip', encoding='utf-8')

print(df.head())

# Total Jobs Count
total_jobs = len(df)

# Jobs by Company
jobs_by_company = df['Company'].value_counts()

# Jobs by Location
jobs_by_location = df['Location'].value_counts()

# Jobs by Title
jobs_by_title = df['Job Title'].value_counts()

# Remote Jobs Count
remote_jobs = df[df['Location'].str.contains('work from home', case=False, na=False)]
remote_jobs_count = len(remote_jobs)

# Skill Count
from collections import Counter

all_skills = []
df['Skills'] = df['Skills'].fillna('')

for skills in df['Skills']:
    split_skills = [skill.strip() for skill in skills.split(',')]
    all_skills.extend(split_skills)

skill_counter = Counter(all_skills)
top_10_skills = skill_counter.most_common(10)

# Show Results
print("✅ Total Jobs:", total_jobs)
print("\n📌 Jobs by Company:\n", jobs_by_company.head())
print("\n📌 Jobs by Location:\n", jobs_by_location.head())
print("\n📌 Jobs by Title:\n", jobs_by_title.head())
print("\n🏠 Remote Jobs:", remote_jobs_count)
print("\n🔥 Top 10 Skills:\n", top_10_skills)