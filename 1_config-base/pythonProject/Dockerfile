FROM ubuntu:24.04
LABEL authors="Joy HEURTAUX"
LABEL mail="joy.heu@outlook.fr"

# Mettre à jour les paquets et installer sudo
# Créer un utilisateur nommé "student" avec un mot de passe
# Ajouter l'utilisateur au groupe sudo pour qu'il puisse utiliser sudo si nécessaire

RUN apt-get update && apt-get install -y sudo curl && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    useradd -m -s /bin/bash student && echo "student:password" | chpasswd && \
    echo "student ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    usermod -aG sudo student

# Définir l'utilisateur par défaut pour le conteneur
USER student

# Définir le répertoire de travail par défaut
WORKDIR /home/student