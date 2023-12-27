# Flask installation from pip3

package { ['python-pip3']:
  ensure => installed,
}

package { 'flask' :
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python-pip3']
}
