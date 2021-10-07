# Sky is the limit, let's bring that limit higher

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/2000/" etc/default/nginx',
  path    => '/bin/:/usr/local/bin/',
}

exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}