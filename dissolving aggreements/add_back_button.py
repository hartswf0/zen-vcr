import os
import re

def add_back_button(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Add back button styles and script
    back_button_style = '''
    <style>
        .back-button {
            position: fixed;
            top: 20px;
            left: 20px;
            text-decoration: none;
            color: #2c3e50;
            font-family: 'Circular Std', Arial, sans-serif;
            font-weight: 300;
            opacity: 0.7;
            transition: all 0.3s ease;
            z-index: 1000;
            padding: 10px;
            border-radius: 5px;
        }
        .back-button:hover {
            opacity: 1;
            background-color: rgba(44, 62, 80, 0.05);
            transform: translateX(-5px);
        }
    </style>
    '''
    
    back_button_html = '''
    <a href="index.html" class="back-button" id="back-button">← Uncontracting™</a>
    '''
    
    # Insert styles before </head>
    if '</head>' in content:
        content = content.replace('</head>', back_button_style + '</head>')
    
    # Insert back button HTML after <body>
    if '<body>' in content:
        content = content.replace('<body>', '<body>' + back_button_html)
    
    # Add interactivity script
    back_button_script = '''
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const backButton = document.getElementById('back-button');
        
        // Subtle hover effect
        backButton.addEventListener('mouseover', function() {
            this.style.transform = 'translateX(-5px)';
            this.style.opacity = '1';
        });
        
        backButton.addEventListener('mouseout', function() {
            this.style.transform = 'translateX(0)';
            this.style.opacity = '0.7';
        });
    });
    </script>
    '''
    
    # Insert script before </body>
    if '</body>' in content:
        content = content.replace('</body>', back_button_script + '</body>')
    
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    base_dir = '/Users/gaia/dissolving aggreements'
    for filename in os.listdir(base_dir):
        if filename.startswith('dis') and filename.endswith('.html'):
            file_path = os.path.join(base_dir, filename)
            add_back_button(file_path)
            print(f"Updated {filename}")

if __name__ == '__main__':
    main()
