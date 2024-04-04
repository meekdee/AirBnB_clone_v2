#!/usr/bin/env bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration
sudo sed -i '/root \/var\/www\/html;/ a\
\
    location /hbnb_static {\
        alias /data/web_static/current/;\
        # If the requested file is not found, return a 404 error\
        error_page 404 = /404.html;\
    }' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
