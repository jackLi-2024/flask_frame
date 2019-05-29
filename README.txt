step1. Modify config.ini
    Please modify the port number and related database parameters according to the actual situation.

step2.Installing CentOS environment dependencies
    sudo yum install -y pcre pcre-devel pcre-static
    sudo yum install -y gcc
    sudo yum install -y python-devel

step3. api
    1. add URI: ./src/run.py
    2. add api: ./src/controller/
    3. operate database: ./src/model/Models/


step4 Note
    1.There may be a system error, and you will get the following error: "\r"
        sudo yum install -y dos2unix
        dos2unix *
        dos2unix */*
        dos2unix */*/*

1. start
	sh start.sh
2. stop
	sh stop.sh

