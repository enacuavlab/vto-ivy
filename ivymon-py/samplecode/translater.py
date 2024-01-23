#!/usr/bin/env python3

# TODO: pip3 install ivy-python
import logging
from ivy import ivy

DEFAULTBUS = "224.255.255.255:2010"
# DEFAULTBUS="127.255.255.255:2010"


class Translater():
    def __init__(self):
        self.bus = ivy.IvyServer('Translater', 'IvyTranslater READY')
        ivy.ivylogger.setLevel(logging.ERROR)
        self.bus.bind_msg(self.my_answer, '^hello (.*)')
        self.bus.start(DEFAULTBUS)

    def my_answer(self, agent, firstgroup):
        self.bus.send_msg("bonjour " + firstgroup)


if __name__ == "__main__":
    t = Translater()
