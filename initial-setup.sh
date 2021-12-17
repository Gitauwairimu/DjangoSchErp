#!/bin/sh

cd ~

sudo yum -y update

sudo apt install -y epel-release

sudo apt install -y python3 gcc nginx git nano java-1.8.0-openjdk-devel wget

sudo wget -O /etc/apt.repos.d/jenkins.repo \
    https://pkg.jenkins.io/ubuntu/jenkins.repo

sudo add --import https://pkg.jenkins.io/redhat/jenkins.io.key

sudo apt upgrade

sudo apt install -y jenkins

sudo systemctl daemon-reload

sudo systemctl start nginx

sudo systemctl enable nginx

sudo systemctl start jenkins

systemctl status jenkins

sudo systemctl enable jenkins
