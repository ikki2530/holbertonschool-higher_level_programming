service mysql start
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
sudo pip3 install jsonschema==3.0.1
sudo pip3 install pathlib2
sudo apt-get install -y python3-lxml
sudo pip3 install flask_cors
sudo pip3 install flasgger

#data
curl -o 100-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
cat 100-dump.sql | mysql -uroot -p