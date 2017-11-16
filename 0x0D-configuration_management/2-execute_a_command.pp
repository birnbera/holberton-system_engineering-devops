exec { 'kill killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
