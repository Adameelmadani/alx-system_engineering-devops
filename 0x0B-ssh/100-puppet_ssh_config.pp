# Configuring config file
file_line { 'Add new line':
  path => 'etc/ssh/ssh_config',
  line => 'Host 100.25.164.203
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
