#Configuring config file
file_line { 'Add new line':
  path   => 'etc/ssh/ssh_config',
  line   => 'Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
