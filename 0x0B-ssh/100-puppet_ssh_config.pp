# Client-side configuration
file_line{'Configuration':
  path => '/etc/ssh/ssh_config',
  line => 'Host 100.25.164.203
    HostName 100.25.164.203
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
