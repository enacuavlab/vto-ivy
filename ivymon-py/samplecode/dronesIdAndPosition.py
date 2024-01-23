#!/usr/bin/env python3

# TODO: pip3 install ivy-python
import logging
from ivy import ivy

# le point de rendez-vous
#DEFAULTBUS = "224.255.255.255:2010" # sur n'importe quel réseau pour parler avec un mac
DEFAULTBUS = "192.168.1.255:2010"   # sur le réseau recherche dans le labo drones
# DEFAULTBUS="127.255.255.255:2010"   # en local sur ma machine


class MonNom():
    def __init__(self):
        self.bus = ivy.IvyServer('Mon Nom', 'Mon Nom est pret') # le nom de l'agent
        ivy.ivylogger.setLevel(logging.ERROR)
        self.bus.bind_msg(self.my_answer, '^datalink REMOTE_GPS_LOCAL ([0-9]+) [^ ]+ ([0-9.-]+) ([0-9.-]+) ([0-9.-]+)')
            # un abonnement spécifique
            # une expression rationnelle compatible perl (PCRE) regexp
            # pour tout recevoir, c'est '(.*)'
        self.bus.start(DEFAULTBUS)

    def my_answer(self, agent, *args):
        # dans args, il y a autant de valeurs que de couples de () dans l'abonnement
        print("id: ", args[0], " x: ", args[1], " y: ", args[2], " z: ", args[3])


if __name__ == "__main__":
    t = MonNom()
