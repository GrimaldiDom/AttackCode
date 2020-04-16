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
from pymodbus.client.sync import ModbusTcpClient

MODBUS_PKT_SIZE=55
REG_DICT={
    "Flow":         {"offset": 0,    "type": "holding"  },
    "ColdTempIn":   {"offset": 1,    "type": "input"    },
    "ColdTempOut":  {"offset": 4,    "type": "input"    },
    "HotMassFlowIn":{"offset": 3,    "type": "input"    },
    "HotTempIn":    {"offset": 2,    "type": "input"    },
    "Setpoint":     {"offset": 1,    "type": "holding"  },
    "ShellPress":   {"offset": 6,    "type": "input"    },
    "Temperature":  {"offset": 0,    "type": "input"    },
    "TubePress":    {"offset": 5,    "type": "input"    },
    "PID_kp":       {"offset": 2048, "type": "holding"  },
    "PID_td":       {"offset": 2052, "type": "holding"  },
    "PID_tr":       {"offset": 2050, "type": "holding"  },
}

class attack:

    def __init__(self,IP,Port):
        """
            The IP and Port of the computer being attacked.
            If we are attacking a PLC, the IP and Port of the PLC
            should be used while amking an object to this class
        """
        self.ip=IP
        self.port=Port
        # Modbus tcp client
        self.modcli = ModbusTcpClient(IP)

    @staticmethod
    def getReg( reg, index=0 ):
        # Registers are stored without decimal points. Their values represent
        # the number multiplied by 100 so we undo that to get the real value

        # We assume desired register is first element, pass in optional index to change
        return( float( reg[index] ) / 100 )

    def PrintRegisters( self ):
        print("Printing registers...")
        for key in REG_DICT.keys():
            t = REG_DICT[key]["type"]    # Current register type
            o = REG_DICT[key]["offset"]  # Current register offset
            if( t == "input" ):
                data = self.modcli.read_input_registers(o,1,unit=1)
            elif( t == "holding" ):
                data = self.modcli.read_holding_registers(o,1,unit=1)
            else:
                raise Exception("Unknown register type...")

            print( "Register [{}]: {}".format( key, self.getReg(data.registers) ) )

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


if __name__=="__main__":
    attacker = attack( "192.168.56.104", "502" )
    attacker.PrintRegisters()
