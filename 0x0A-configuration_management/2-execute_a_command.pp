# Create manifest for kill
exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
