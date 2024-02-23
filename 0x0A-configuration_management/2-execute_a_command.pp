#kill the process named killmenow
exec { 'pkill killmenow':
  command => '/usr/bin/pkill killmenow'
}
