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
Pour IREDMAIL nous avons la version 1.5.2. Nous avons d'abord installer les packages de IredMail depuis un depot github avec 
apt -y install wget avant de  il faut d’abord donner les droits d’exécution du script avec chmod+x Install_IREDMAIL_DEPENDENCIES.sh , puis l’exécuter avec la commande bash Install_IREDMAIL_DEPENDENCIES.sh 
