#set the ssh config file without password authentication and with private-key file location
file_line { 'Req-1: no password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line { 'Req-2: PrivateKey':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}
