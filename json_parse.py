from bs4 import BeautifulSoup
import json

try:
    # Load and parse the HTML file
    with open('Security-Certification-Roadmap9.html', 'r') as file:
        soup = BeautifulSoup(file, 'lxml')
        print("HTML file loaded successfully.")
except FileNotFoundError:
    print("Error: HTML file not found. Please check the file name and location.")
    exit()

# Initialize an empty list to store the certification data
certifications = []

# Extract each certification and print it to confirm
for cert in soup.find_all('a'):
    name = cert.get_text().strip()  # Certification name
    link = cert.get('href')  # Certification link
    details = cert.get('tooltiptext', '').strip()  # Certification details

    # Append to the certifications list
    certifications.append({
        "name": name,
        "link": link,
        "details": details
    })

print(f"Extracted {len(certifications)} certifications.")

# Attempt to save the extracted data to a JSON file
try:
    with open('certifications.json', 'w') as json_file:
        json.dump(certifications, json_file, indent=2)
        print("Certification data has been successfully saved to certifications.json")
except Exception as e:
    print(f"Error saving to JSON: {e}")
