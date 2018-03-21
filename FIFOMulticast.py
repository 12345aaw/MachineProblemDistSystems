from MulticastAbstract import MulticastAbstract
import BasicMulticast as m
class FIFOMulticast( MulticastAbstract ):
    def __init__(self,selfnode,NUMOFNODES):

        # send and receive sequence numbers. All initiated at 0.

        self.SSEQUENCER = 0
        self.RSEQUENCERS = []
        self.SELFNODE = selfnode
        for a in range(NUMOFNODES):
            self.RSEQUENCERS.append(0)
        self.QUEUE = []

    def multicast(self, group, message):

        # increment send sequencer and piggyback it on to message

        self.SSEQUENCER = self.SSEQUENCER + 1
        message = message + " " + str(self.SSEQUENCER)

        # Basic multicast

        a = m.BasicMulticast()
        a.multicast(group,message)

    # Basic delivery

    def deliver(self, source,message):
        a = m.BasicMulticast()
        a.deliver(self.SELFNODE,source,message)