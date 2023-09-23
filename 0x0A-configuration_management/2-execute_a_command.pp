#execute command pkill to kill killmenow process
exec { 'pkill killmenow':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
}
