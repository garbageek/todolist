# Todolist

Test task - Todolist with functional tests based on Selenium.

### Install Chromedriver

```shell
wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

### Install app and libraries

```shell
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-virtualenv xvfb xserver-xephyr
sudo pip3 install django selenium django-bootstrap3 `pyvirtualdisplay
git clone https://github.com/garbageek/todolist
cd todolist/
python3 manage.py makemigrations
python3 manage.py migrate
```

### Run and Test

```shell
python3 manage.py runserver
python3 manage.py test --liveserver=localhost:8082
```
