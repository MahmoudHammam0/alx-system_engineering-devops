#find the issue on Apache returning a 500, fix it and then automate it
$file = '/var/www/html/wp-settings.php'
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file}",
  path    => ['/bin','/usr/bin']
}
