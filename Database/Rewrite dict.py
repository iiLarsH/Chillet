import json
import sqlite3

# Function to retrieve code names from SQLite3 table
def get_code_name(name):
    cursor.execute("SELECT code FROM palname_to_code WHERE name = ?", (name,))
    result = cursor.fetchone()
    return result[0] if result else None

# Read the data from the JSON file
with open("csv's/data.json", 'r') as f:
    data = json.load(f)

# Connect to SQLite3 database
conn = sqlite3.connect('Database/Paldata.db')
cursor = conn.cursor()

# Create a new dictionary to store modified data
new_data = {}

# Iterate through the nested dictionary and replace keys and values with code names
for key, value in data.items():
    new_key = get_code_name(key) or key  # If code name not found, use original key
    new_value_dict = {}
    for sub_key, sub_value in value.items():
        new_sub_key = get_code_name(sub_key) or sub_key  # If code name not found, use original sub key
        new_sub_value = get_code_name(sub_value) or sub_value  # If code name not found, use original sub value
        new_value_dict[new_sub_key] = new_sub_value
    new_data[new_key] = new_value_dict

# Close connection to SQLite3 database
conn.close()

# Save the modified data back to the JSON file
with open("csv's/data_modified.json", 'w') as f:
    json.dump(new_data, f, indent=4)
