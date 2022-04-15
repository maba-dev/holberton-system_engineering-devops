exec { 'pkill killmenow':
  path    => ['/usr/bin', '/sbin'],
}
