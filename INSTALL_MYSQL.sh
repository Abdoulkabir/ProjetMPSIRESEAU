#!/bin/sh
###Installation des dependances pour l'installation de mysql###
###Mis à jour du systeme###
apt update
###installation des packages###
apt install mariadb-client
apt install mariadb-server
###demarrage du service###
systemctl start mariadb.service
