#!/usr/bin/env bash
# setting up web server for static web

#upgrate and install nginx
apt-get upgarde
apt-get -y update
apt-get -y install nginx

# Create folders
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

#Fake html test page
echo "<html>
<head>
  <title>Test Page</title>
</head>
<body>
  <h1>Welcome to the Test Page</h1>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

#Change ownerships
chown -hR ubuntu:ubuntu /data/

#Update the serever to serve /hbnb_static/
sed -i '/server_name/a \
    \    location /hbnb_static/ {\
    \        alias /data/web_static/current/;\
    \        autoindex on;\
    \    }' /etc/nginx/sites-available/default

service nginx restart
