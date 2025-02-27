import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the IMDb reviews page
url = "https://www.rottentomatoes.com/m/inception_the_cobol_job/reviews?type=user"

# Set the User-Agent to avoid being blocked by the website
headers = {"User-Agent":"Mozilla/5.0"}

# Download the page
response=requests.get(url,headers=headers)

# Check if the request was successful
if response.status_code==200:
    print("Download successful")
    print(response.text[:500])
else:
    print("Error downloading page : ",response.status_code)

# Wait for 5 seconds before making the next request
time.sleep(3)
   
# Parse the HTML content
soup=BeautifulSoup(response.text,"html.parser")

# Find all the review elements
rewiews=soup.find_all(reviews = soup.find_all("span", class_="sc-16ede01-2 fDdOeB"))

# Extract the review text
rewiew_text = [review.text.strip() for review in rewiews]

# Display the first 5 reviews
for i,review in enumerate(rewiews[:5]):
    print(f"Review {i+1}:,{review.text.strip()}")
    
# Save the reviews to a CSV file
df=pd.DataFrame(rewiew_text,columns=["Review"])
df.to_csv("reviews.csv",index=False)
    
