# configuration file (w/ Puppet)


file_line { 'PasswordAuthentication':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}
file_line { 'IdentityFile':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
}
