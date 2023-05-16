# Changes the limitations on the holberton user

exec { 'change-os-configuration-for-holberton-user':
  command => 'sudo sed -i "s/hard nofile 5/hard nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'change-os-configuration-for-holberton-user-soft':
  command => 'sudo sed -i "s/soft nofile 4/soft nofile 40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
