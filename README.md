# python-app-server
#!/bin/bash
sudo yum -y install httpd
cd /var/www/html
echo "healthy" | sudo tee /var/www/html/index.html
cd /home/ec2-user
sudo wget https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
sudo yum -y localinstall mysql57-community-release-el7-11.noarch.rpm
sudo yum -y install mysql
sudo yum -y install python3
sudo yum -y install git
sudo yum install python3-pip
git clone https://github.com/sshariqrizvi15/pythonapp-withoutrds.git
sudo pip3 install -r pythonapp-withoutrds/requirements.txt
nohup python3 /home/ec2-user/pythonapp-withoutrds/app/app.py > output.txt 2>&1  </dev/null &
sudo service httpd start
