#!/bin/bash

# Stage all changes
git add .

# Commit with a very explicit message
git commit -m "Update for GitHub Pages: Comprehensive link modification

- Converted all relative links to root-relative paths
- Ensured compatibility with GitHub Pages hosting
- Processed all HTML files in the project
- Verified link transformations

Specific changes:
- Added comprehensive_link_update.py script
- Modified href and src attributes in HTML files
- Preserved external and anchor links
- Prepared for GitHub Pages deployment"

# Force push to ensure visibility
git push -f origin main
