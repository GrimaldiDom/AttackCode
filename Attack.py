# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:43:48 2020

@author: Rishabh Das


Please include change_data_label(label) function call before doing each attack
This function call lets the data logger know that some kind of attack is
being performed on the system.

"""
import socket
import threading
import pickle

class attack:

    def __init__(self,IP,Port):
        """
            The IP and Port of the computer being attacked.
            If we are attacking a PLC, the IP and Port of the PLC
            should be used while amking an object to this class
        """
        self.IP=IP
        self.Port=Port


    def change_data_label(self,label,IP,Port):
        """
            calling this function changes the data label
        """
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (self.IP,int(self.Port) )
        client_sock.connect(address)
        dat = pickle.dumps("Change|"+str(label))
        client_sock.send(dat)

    def attack_1(self,label):
        """
            The label can be either an integer or an categorical value.
            Be consistent with the data type you choose
        """
        #Write each attacks in different functions
        print("Performing attack 1!")

    def attack_2(self,label):
        """
            The label can be either an integer or an categorical value.
            Be consistent with the data type you choose
        """
        #Write each attacks in different functions
        print("Performing attack 2!")

    def attack_3(self,label):
        """
            The label can be either an integer or an categorical value.
            Be consistent with the data type you choose
        """
        #Write each attacks in different functions
        print("Performing attack 3!")

    def attack_4(self,label):
        """
            The label can be either an integer or an categorical value.
            Be consistent with the data type you choose
        """
        #Write each attacks in different functions
        print("Performing attack 4!")

    def Normal_operation_1(self,label):
        """
            The label can be either an integer or an categorical value.
            Be consistent with the data type you choose
        """
        #Write each attacks in different functions
        print("Performing Normal Operation 1")

    def Normal_operation_2(self,label):
        """
            The label can be either an integer or an categorical value.
            Be consistent with the data type you choose
        """
        #Write each attacks in different functions
        print("Performing Normal Operation 2 ")


#----------------------------------------------------
#        Example Call
# attacker=attack(PLCIP,PLCport)
# attacker.change_data_label("CommandInjection",IPaddress of the logger1,4321)
# attacker.change_data_label("CommandInjection",IPaddress of the logger2,4321)
# attacker.attack_1("CommandInjection")




# attacker.change_data_label("ResponseInjection",IPaddress of the logger1,4321)
# attacker.change_data_label("ResponseInjection",IPaddress of the logger2,4321)
# attacker.attack_2("ResponseInjection")
