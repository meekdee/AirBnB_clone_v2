#!/usr/bin/env bash

# Install Nginx if not installed
apt-get update
apt-get -y install nginx

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
if grep -q 'location /hbnb_static' "$config_file"; then
    sed -i 's#location /hbnb_static#location /hbnb_static {\n\talias /data/web_static/current/;\n}#' "$config_file"
else
    sed -i '/^\tlocation \/ {/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$config_file"
fi

# Restart Nginx
service nginx restart
