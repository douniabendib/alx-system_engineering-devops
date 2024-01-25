# INcrease the ULIMIT value
exec {'24: Too many open files':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->
exec {'Restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
