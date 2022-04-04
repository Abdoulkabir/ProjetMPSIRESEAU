# ProjetMPSIRESEAU
Ce README dans le but de présenter l’ensemble des aspects fonctionnels lors de la conception de l’environnement de travail (Installation-Mise en Réseau-Implémentation Services (DHCP-DNS-IREDMAIL)) et la réalisation des différents scripts demandés (Installation-Dépendances, Communication CLIENT/SERVEUR, Analyse Paquets et Envoie Mail). Un travail réalisé  qui sera décrite juste ci-dessous.
Le projet consiste à mettre en place un dispositif permettant d’analyser un packet. Nous avons mise en place l'environnement virtuel en simulant un petit réseau constitué d’un SERVEUR avec une adresse fixe ou sera configurées les Services 
-DNS
-	DHCP
-	MAIL
-	Une Base de Données
Une machine cliente qui bénéficiera de l’ensemble des services énumérées ci-dessous et établiera une communication  TCP/IP avec le serveur lors des connetions ou création de comptes.Une communication qui sera générée par nos scripts écrits en python  et sera suivi par une machine kali Man in the middle qui grâce à son outil Wire Shark intégré permettra de voir toutes les informations de communication qui seront analysées, et envoyées par mail à l’Administrateur grâce à un script.
Le travail sera réparti en 5 grandes parties :
-Implémentation et mise en réseau de l’environnement virtuel
-	Implémentation puis tests de nos services DHCP,DNS sur le serveur
-Implémentation et test du script d’installation des dépendances de mysql et iRedMail
-	Mise en place et tests des scripts Client/Serveur pour la connection 
-	 Simulation de Wireshark 
----	Implémentation et Mise en réseau de l’environnement virtuel
Notre environnement est constitué de 3 machines virtuelles installées sur Virtualbox
*Une machine serveur de type Ubuntu 20.04 avec une adresse fixée à 192.168.10.1
*une machine cliente de type Ubuntu 20.04 avec une adresse dynamique mise en réseau avec le serveur 
*Une machine Man In The Middle de type kali linux réputé par ses outils de sécurité intégrés et donc des analyseurs de communications préinstallés comme Wireshark.Elle est aussi mise dans le même réseau Client/serveur et est aussi adressée Dynamiquement
---Implémentation et test du script d’installation des dépendances MYSQL et IREDMAIL
-Pour IREDMAIL nous avons la version 1.5.2. Nous avons d'abord installer les packages de IredMail depuis un depot github avec: 
apt -y install wget 
wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz
Ensuite on extrait le fichier et on se deplace dans le dossier avec:
tar xvf 1.5.2.tar.gz
cd iRedMail-1.5.2
Pour executer le script iredmail Il faut configurer le nom de domain avant l'execution du script
ensuite attribuer les droits
chmod +x iRedMail.sh
execution du script avec:
pwd
bash iRedmail.sh
--Pour MYSQL
Nous avons installer les dependances pour l'installation de mysql
Pour ce faire nous avons d'abord Mise à jour du systeme avec:
apt update
ensuite nous avons proceder à l'installation des packages avec:
apt install mariadb-client
apt install mariadb-server
et enfin le demarrage du service avec:
systemctl start mariadb.service

---Mise en place  des scripts Client/Serveur.
Nous avons mis en place Une base de données MariaDB qui stocke l’ensemble des compte des utilisateurs du service mail avec leur mot de passes et les informations liées à leur compte.Un utilisateur créé tente de se connecter depuis notre machine cliente tout en s'authentifiant au niveau du serveur  avant de pouvoir avoir accés aux service. Raison pour laquelle nous avons implementer nos scripts server.py et client.py
