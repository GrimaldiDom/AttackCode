import time

class AttackTask():

    def __init__( self, function, pkt_per_sec ):
        self.function = function
        self.sleep_time = 1/pkt_per_sec
        self._running = True

    def terminate( self ):
        self._running = False

    def run( self ):
        while( self._running ):
            # This runs the lambda function that was passed in
            self.function()
            time.sleep( self.sleep_time )
