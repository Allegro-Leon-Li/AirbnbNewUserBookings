# TravelRecommendationSys
This repository is for EC601 class project. The topic and database is selected from kaggle.com
To get the website running, it's preferable to have Python 3.5 installed, along with pip. Here are some instructions:
1. Install Django by 'pip install django', or by some other methods: https://docs.djangoproject.com/en/1.10/topics/install/ 
2. Install Django-Rest-Framework by 'pip install djangorestframework'. ref: http://www.django-rest-framework.org/#installation
3.Install mysqlclient by 'pip install mysqlclient'. ref: https://pypi.python.org/pypi/mysqlclient
4.Install XGBoost by following the official guide for python install: https://xgboost.readthedocs.io/en/latest/build.html; Please note it is necessary to have gcc installed in your computer in order to build the XGBoost, details please follow the link above.
5.Install MySQL in your own computer and start it as a service on the default port.(i.e. localhost:3306). And then create a database in MySQL called 'ec601db'. Create a user in MySQL called 'ec601' with the password 'password' and give the user permission by sql command "grant all privileges on *.* to 'ec601'@'localhost'". The setup for the MySQL differs in different OS, you can find some instructions online for your case.
6.Use a terminal change to the directory which contains 'manage.py'
7.Type command 'python manage.py makemigrations'. If it shows something like 'nothing to update', make an empty directory called 'migrations' in '{project root}/tutorial/snippets/' and type in terminal 'python manage.py makemigrations snippets'
8.Type command 'python manage.py migrate'
9.Type command 'python manage.py runserver', if there are some error msg appeared in the terminal, probably it's because you are still missing some packages and you can follow the error msg to install it. Otherwise, the server is on, and you can browse '127.0.0.1:8000' to view the website.

We are using Mac and we have installed Anaconda. If you are using Windows, I'm not sure whether you need to install some more dependencies...
The version on the github has a different configuration on MySQL from which is actually in use because we are using AWS RDS database instead of local MySQL and the github version is only configured for building on localhost. So as you are using the source files on our github, it's unavoidable to create the MySQL on your own computer as described in '5.' above.
