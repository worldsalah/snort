# Snort IDS avec Interface Graphique

Ce projet est une interface graphique simple pour afficher les alertes de **Snort**, un système de détection d'intrusion (IDS), en temps réel.

## 📌 Prérequis

Avant de lancer l'application, assurez-vous que **Snort** est installé sur votre machine.

### Installation de Snort (Linux) :
```sh
sudo apt update && sudo apt install snort
```

Vérifiez ensuite la configuration du fichier `/etc/snort/snort.conf` pour être sûr qu'il est bien configuré pour votre interface réseau.

## 🚀 Installation du projet

Clonez ce dépôt et installez les dépendances :
```sh
git clone https://github.com/votre-repo/snort-ids-gui.git
cd snort-ids-gui
pip install -r requirements.txt  # (si des dépendances sont nécessaires)
```

## 🎯 Utilisation

Exécutez le script Python :
```sh
python snort_gui.py
```

### Fonctionnalités :
- Lancer **Snort** avec un simple bouton.
- Voir les alertes en temps réel dans une interface graphique.

## 🛠 Dépannage
- Si Snort ne fonctionne pas, assurez-vous qu'il est correctement installé et configuré.
- Vérifiez que vous avez bien les droits administrateur pour capturer le trafic réseau.
```sh
sudo python snort_gui.py
```

## 🔗 Ressources utiles
- [Documentation officielle Snort](https://www.snort.org/)
- [Forum de support Snort](https://www.snort.org/community)

📌 **Auteur** : Votre Nom  
📅 **Dernière mise à jour** : Février 2025

