#creating a custom HTTP header response, but with Puppet.
exec {'apt-get update':
  command => '/usr/bin/apt-get update'
}

->package {'nginx':
  ensure => installed
}

->file_line { 'add_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";"
}

->exec {'restart':
  command => '/usr/sbin/service nginx restart'
}
