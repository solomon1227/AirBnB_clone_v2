#!/usr/bin/env bash

# Install and configure nginx web server
apt-get update
#apt-get install -y nginx

#prepare the directory
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<h1>Test file<h1>
<p>This is a simple test file</p>
<h2>the test is sucessful</h2> " > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current

#change ownership to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Edit Nginx configuration file
sed -i '/^server {\n\t/a location \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t }' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart

