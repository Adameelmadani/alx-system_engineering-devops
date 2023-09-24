#Configuring config file
file_line { 'Add new line':
  ensure => present,
  path   => 'etc/ssh/ssh_config',
  line   => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no",
}
