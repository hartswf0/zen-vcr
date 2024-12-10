import os
import re

def update_links(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace relative links with root-relative links
    # Ensure links to HTML files start with /
    content = re.sub(r'href="([^"]+\.html)"', r'href="/\1"', content)
    
    # Preserve external links and anchor links
    
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    html_files = [
        'dis1.html', 'dis2.html', 'dis3.html', 'dis4.html', 
        'dis5.html', 'dis6.html', 'dis7.html', 'dis8.html', 
        'dis9.html', 'index.html', 'uncontracting-interactive.html'
    ]
    
    for filename in html_files:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        update_links(file_path)
        print(f"Updated links in {filename}")

if __name__ == '__main__':
    main()
