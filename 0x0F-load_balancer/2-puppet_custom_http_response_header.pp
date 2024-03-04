package { 'nginx':
  ensure => 'installed'
}

file_line { 'add_header':
  match => 'location / {',
  path  => '/etc/nginx/sites-enabled/default',
  line  => "location / {\n\t\tadd_header X-Served-By \"${hostname}\";"
}

exec { 'sudo service nginx restart':
  provider => shell
}
