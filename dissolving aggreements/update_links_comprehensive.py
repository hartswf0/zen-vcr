import os
import re

def update_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update href links
    content = re.sub(
        r'href="(?!https?://|#)([^"]+)"', 
        r'href="/\1"', 
        content
    )
    
    # Update iframe src links
    content = re.sub(
        r'src="(?!https?://|#)([^"]+)"', 
        r'src="/\1"', 
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all HTML files in the directory
    html_files = [
        f for f in os.listdir(script_dir) 
        if f.endswith('.html') and os.path.isfile(os.path.join(script_dir, f))
    ]
    
    print("Files to be processed:")
    for filename in html_files:
        file_path = os.path.join(script_dir, filename)
        print(f"Processing {filename}")
        update_links(file_path)
    
    print("Link update complete.")

if __name__ == '__main__':
    main()
