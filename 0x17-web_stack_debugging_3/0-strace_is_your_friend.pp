# Manifest to fix issue with LAMP stack serving Wordpress site.
# Issue is a misspelled resource in `wp-settings.php`.
exec {'sed phpp':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin',
}
