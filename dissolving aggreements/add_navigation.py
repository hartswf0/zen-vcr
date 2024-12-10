import os
import re

def add_navigation_to_html(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Add navigation styles
    style_pattern = re.compile(r'(</head>)', re.IGNORECASE)
    navigation_styles = '''
    <style>
        .site-navigation {
            background-color: #2c3e50;
            padding: 10px 0;
            text-align: center;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }
        .site-navigation a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-weight: bold;
            transition: color 0.3s ease;
        }
        .site-navigation a:hover {
            color: #3498db;
        }
    </style>
    '''
    content = style_pattern.sub(navigation_styles + r'\1', content)
    
    # Add navigation HTML
    body_pattern = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
    navigation_html = '''
    <!-- Site Navigation -->
    <div class="site-navigation">
        <a href="index.html">Home</a>
        <a href="dis1.html">Page 1</a>
        <a href="dis2.html">Page 2</a>
        <a href="dis3.html">Page 3</a>
        <a href="dis4.html">Page 4</a>
        <a href="dis5.html">Page 5</a>
        <a href="dis6.html">Page 6</a>
        <a href="dis7.html">Page 7</a>
        <a href="dis8.html">Page 8</a>
        <a href="dis9.html">Page 9</a>
    </div>
    '''
    content = body_pattern.sub(r'\1' + navigation_html, content)
    
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    html_files = [f for f in os.listdir('.') if f.startswith('dis') and f.endswith('.html')]
    html_files.append('index.html')
    
    for file in html_files:
        print(f"Processing {file}...")
        add_navigation_to_html(file)
    
    print("Navigation added to all HTML files.")

if __name__ == '__main__':
    main()
