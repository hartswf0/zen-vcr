import os
import re

def add_page_number_and_style(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Add page number styles
    page_number_style = '''
    <style>
        .page-number {
            position: fixed;
            bottom: 20px;
            right: 20px;
            font-family: 'Arial', sans-serif;
            font-size: 1.5rem;
            color: rgba(44, 62, 80, 0.5);
            opacity: 0.7;
            transition: opacity 0.3s ease;
            z-index: 1000;
        }
        .page-number:hover {
            opacity: 1;
        }
    </style>
    '''
    
    # Determine page number based on filename
    page_number = re.search(r'dis(\d+)\.html', os.path.basename(file_path))
    page_number = page_number.group(1) if page_number else '00'
    
    # Add page number HTML
    page_number_html = f'''
    <div class="page-number">0{page_number}</div>
    '''
    
    # Insert styles before </head>
    if '</head>' in content:
        content = content.replace('</head>', page_number_style + '</head>')
    
    # Insert page number HTML before </body>
    if '</body>' in content:
        content = content.replace('</body>', page_number_html + '</body>')
    
    with open(file_path, 'w') as f:
        f.write(content)

def create_interactive_page():
    interactive_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uncontracting™ | Interactive Exploration</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            perspective: 1000px;
            overflow: hidden;
        }

        .interactive-container {
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            padding: 40px;
            text-align: center;
            transform-style: preserve-3d;
            transition: all 0.3s ease;
        }

        .interactive-container:hover {
            transform: scale(1.02) rotateX(2deg) rotateY(2deg);
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 20px;
        }

        .interaction-prompt {
            color: #7f8c8d;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="interactive-container">
        <h1>Uncontracting™ Interactive Space</h1>
        <p class="interaction-prompt">Where interaction becomes the contract</p>
    </div>

    <div class="page-number">07</div>

    <script>
        document.addEventListener('mousemove', (e) => {
            const container = document.querySelector('.interactive-container');
            const { clientX, clientY } = e;
            const { left, top, width, height } = container.getBoundingClientRect();
            
            const centerX = left + width / 2;
            const centerY = top + height / 2;
            
            const angleX = (clientY - centerY) / 20;
            const angleY = -(clientX - centerX) / 20;
            
            container.style.transform = `
                scale(1.02) 
                rotateX(${angleX}deg) 
                rotateY(${angleY}deg)
            `;
        });

        document.querySelector('.interactive-container').addEventListener('mouseleave', (e) => {
            e.target.style.transform = 'scale(1) rotateX(0) rotateY(0)';
        });
    </script>
</body>
</html>
    '''
    
    with open('/Users/gaia/dissolving aggreements/uncontracting-interactive.html', 'w') as f:
        f.write(interactive_html)

def update_html_files():
    # List of HTML files to update
    html_files = [
        'dis1.html', 'dis2.html', 'dis3.html', 'dis4.html', 
        'dis5.html', 'dis6.html', 'dis7.html', 'dis8.html', 
        'dis9.html', 'uncontracting-interactive.html'
    ]

    # Navigation and styling to be added
    navigation_style = '''
    <style>
        .page-number-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
        }

        .page-number {
            width: 50px;
            height: 50px;
            background-color: rgba(44, 62, 80, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            color: #2c3e50;
            opacity: 0.7;
            transition: all 0.3s ease;
            cursor: pointer;
            text-decoration: none;
        }

        .page-number:hover {
            background-color: rgba(44, 62, 80, 0.2);
            opacity: 1;
            transform: scale(1.1);
        }

        .page-number.question-mark:hover::after {
            content: '?';
        }

        .page-number.question-mark:hover {
            background-color: rgba(52, 152, 219, 0.2);
        }
    </style>
    <div class="page-number-container">
        <a href="index.html" class="page-number PAGE_NUMBER_PLACEHOLDER question-mark">PAGE_NUMBER_PLACEHOLDER</a>
    </div>
    '''

    for filename in html_files:
        filepath = os.path.join('/Users/gaia/dissolving aggreements', filename)
        
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Extract page number from filename
        page_number = filename.replace('dis', '').replace('.html', '').replace('uncontracting-interactive', '07')
        
        # Check if navigation already exists
        if '<div class="page-number-container">' not in content:
            # Insert navigation style and element before closing body tag
            content = content.replace('</body>', navigation_style.replace('PAGE_NUMBER_PLACEHOLDER', page_number) + '\n</body>')
        
        with open(filepath, 'w') as file:
            file.write(content)

    print("Updated all pages with navigation and page numbers.")

def main():
    base_dir = '/Users/gaia/dissolving aggreements'
    for filename in os.listdir(base_dir):
        if filename.startswith('dis') and filename.endswith('.html'):
            file_path = os.path.join(base_dir, filename)
            add_page_number_and_style(file_path)
            print(f"Updated {filename}")
    
    create_interactive_page()
    print("Created uncontracting-interactive.html")
    update_html_files()

if __name__ == '__main__':
    main()
