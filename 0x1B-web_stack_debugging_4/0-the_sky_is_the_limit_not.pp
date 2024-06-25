# increasing nginx ULIMIT
exec {'fix-ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# restarting Nginx
exec {'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
