<?php 
echo exec('whoami');
$url_text = $_POST['URL-from-user'];
$command = 'sudo python bbcgoodfood.py https://www.bbcgoodfood.com/recipes/7001/cinnamon-berry-granola-bars';
exec($command);
echo "Run command";
?>