import socket
import json
host= "192.168.10.2"
port = 66
clientInfo = [] #Creation de la variable qui va contenir les information du client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation de socket
try:
   
    client.connect((host, port))  # Connexion au server avec le host et le port
    data = client.recv(1024)
    data = data.decode("utf8")
    print(data)
    print("1. Connexion :")
    print("2. Inscription :")
    print("3. Quitter :")
    choix = int(input("Veuillez choisir s'il vous plait  : "))
    if choix == 1:
        #Le client entre les coordonnées de connexion
        mail = input("veuillez saisir votre address mail :")
        mdp = input("veuillez saisir votre mdp :")
        clientInfo.append(mail)
        clientInfo.append(mdp)
        #On definit le type d'operation
        clientInfo.append("Connexion")
        #On le transforme en JSOn
        messagesend = json.dumps(clientInfo)
        messagesend = messagesend.encode("utf8")
        #On l'envoi au serveur
        client.sendall(messagesend)
        #On recupere la reponse du serveur puis on l'affiche
        data = client.recv(1024)
        data = data.decode("utf8")
        print(data)
    elif choix == 2 :
        #Le client insert les coordonnees
        nom = input("veuillez saisir votre  nom :")
        mail = input("veuillez saisir votre address mail :")
        mdp = input("veuillez saisir votre mdp :")
        mdp1 = input("Confirmer votre mot de passe :")
        if mdp == mdp1 :
                clientInfo.append(nom)
                clientInfo.append(mail)
                clientInfo.append("Inscription")
                clientInfo.append(mdp)
                 #On le transforme en JSOn
                messagesend = json.dumps(clientInfo)
                messagesend = messagesend.encode("utf8")
                #On l'envoi au serveur
                client.sendall(messagesend)
                #On recupere la reponse du serveur puis on l'affiche
                data = client.recv(1024)
                data = data.decode("utf8")
        else:
            print("Les deux mot de passe doivent etre les identiques")
        pass
    elif choix == 3 :
        print("Quitter")
        exit()
    else:
        print("choix inccorect")
        pass

except Exception as e:
    print(e)
finally:
    #On ferme la connection
    client.close()


