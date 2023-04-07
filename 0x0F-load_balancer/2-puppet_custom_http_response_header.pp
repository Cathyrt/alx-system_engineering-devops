# Nginx web server setup and configuration
class { 'nginx':
  ensure => 'installed',
}

file_line { 'add_custom_header':
  path => '/etc/nginx/nginx.conf',
  line => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
