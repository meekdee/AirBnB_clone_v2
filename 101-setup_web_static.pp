# File: 101-setup_web_static.pp

# Create directory /data/web_static
file { '/data':
  ensure => 'directory',
}

# Create subdirectories inside /data/web_static
file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

# Create a symbolic link /data/web_static/current pointing to /data/web_static
file { 'data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}
