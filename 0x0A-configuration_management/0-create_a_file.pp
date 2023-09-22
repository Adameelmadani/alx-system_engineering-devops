#create new file in /tmp/school with mode 0744, owner, group and content

file { '/tmp/school/0-create_a_file.pp':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
