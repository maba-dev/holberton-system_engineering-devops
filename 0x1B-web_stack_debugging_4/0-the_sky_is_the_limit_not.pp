# Sky is the limit, let's bring that limit higher

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/20000/" etc/default/nginx',
  path    => '/bin/:/usr/local/bin/',
}

exec { 'service nginx restart':
  command => 'service nginx restart',
  path    => '/bin/:/usr/bin/:/usr/sbin/',
}