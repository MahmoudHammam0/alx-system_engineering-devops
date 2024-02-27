#configures a new Ubuntu machine with Nginx web server
package { 'nginx':
  ensure => 'present'
}

exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell
}

exec { 'install':
  command  => 'sudo apt-get -y install nginx',
  provider => shell
}

exec { 'echo "Hello World!" | sudo tee /var/www/html/index.html':
  provider => shell
}

exec { 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/google.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell
}

exec { 'sudo service nginx restart':
  provider => shell
}
