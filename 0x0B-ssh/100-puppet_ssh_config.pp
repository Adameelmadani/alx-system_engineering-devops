#Configuring config file
file_line { 'Add new line':
  path   => 'etc/ssh/ssh_config',
  line   => 'Host *
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
