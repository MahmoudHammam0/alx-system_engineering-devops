#creating a custom HTTP header response, but with Puppet.
package { 'nginx':
  ensure => 'installed'
}

file_line { 'add_header':
  match => 'location / {',
  path  => '/etc/nginx/sites-enabled/default',
  line  => 'location / {\n\t\tadd_header X-Served-By $hostname'
}

exec { 'restart':
  command  => 'sudo service nginx restart'
}
