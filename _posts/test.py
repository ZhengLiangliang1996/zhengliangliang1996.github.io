import os
import re
import glob

# Directory containing the .md files
directory = '2019'

# Regex pattern to find markdown image links
pattern = re.compile(r'\!\[.*\]\((.*?)\)')

# Function to create replacement HTML string
def create_replacement(link):
    return f'''<p align="center">
  <img src="{link}" alt="screenshot" width="80%" height="auto">
</p>'''

# Function to process each file
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(pattern, lambda m: create_replacement(m.group(1)), content)
    
    if content != new_content:
        print(f"Updated file: {filepath}")
    else:
        print(f"No changes made to file: {filepath}")

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Loop over all .md files in the directory
for root, _, files in os.walk(directory):
        for filename in files:
            # Process only .md files
            if filename.endswith(".md"):
                print("process file: ", filename)
                process_file(os.path.join(root, filename))


        
