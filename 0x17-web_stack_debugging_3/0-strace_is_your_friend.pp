# Manifest to fix issue with LAMP stack serving Wordpress site.
# Issue is a misspelled resource in `wp-settings.php`.
exec {'sed phpp':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php',
}
