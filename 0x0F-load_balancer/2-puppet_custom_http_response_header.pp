exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'present'
}

file_line { 'add_header':
  match => 'http {',
  path  => '/etc/nginx/nginx.conf',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";"
}

exec { 'run':
  command  => '/usr/sbin/service nginx restart'
}
