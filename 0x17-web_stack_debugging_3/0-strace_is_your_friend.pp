#Regex to change the word phpp in php
exec { 'Change of word':
command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
provider => shell
}
