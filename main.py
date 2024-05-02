import requests
import uuid

# Replace with your Supabase URL and API key
supabase_url = "https://your-supabase-instance.supabase.io"
api_key = "your-supabase-api-key"

# Set the API key in the headers
headers = {
    "apikey": api_key,
    "Content-Type": "application/json"
}

# Create a new table
table_name = "new_users"
response = requests.post(f"{supabase_url}/rest/v1/tables", headers=headers, json={
    "table_name": table_name,
    "columns": [
        {"name": "id", "type": "bigint", "primary_key": True},
        {"name": "name", "type": "text"},
        {"name": "email", "type": "text", "unique": True},
        {"name": "password", "type": "text"}
    ]
})

if response.status_code == 201:
    print(f"Table '{table_name}' created successfully!")
else:
    print("Error creating table:", response.text)

# Function to generate random data
def generate_random_data():
    name = f"User {uuid.uuid4().hex[:6]}"
    email = f"{uuid.uuid4().hex[:6]}@example.com"
    password = uuid.uuid4().hex[:12]
    return {
        "name": name,
        "email": email,
        "password": password
    }

# Generate random data
form_data = generate_random_data()

# Convert the form data to JSON
json_data = {"data": [form_data]}

# Make the POST request to the new table
response = requests.post(f"{supabase_url}/rest/v1/{table_name}", headers=headers, json=json_data)

# Check if the request was successful
if response.status_code == 201:
    print("Signup successful!")
    print("Name:", form_data["name"])
    print("Email:", form_data["email"])
    print("Password:", form_data["password"])
else:
    print("Error:", response.text)