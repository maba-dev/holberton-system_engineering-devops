# change requests limit

exec { 'Change limite number':
  command => 'sed -i s/15/4096/g /etc/default/nginx',
  path    => '/bin/:/usr/local/bin/',
}

exec { 'restart service nginx':
  command => 'service nginx restart',
  path    => '/bin/:/usr/bin/:/usr/sbin/',
}
