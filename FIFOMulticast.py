from MulticastAbstract import MulticastAbstract
import BasicMulticast as m
class FIFOMulticast( MulticastAbstract ):
    def __init__(self,selfnode,NUMOFNODES):
        self.SSEQUENCER = 0
        self.RSEQUENCERS = []
        self.SELFNODE = selfnode
        for a in range(NUMOFNODES):
            self.RSEQUENCERS.append(0)
        self.QUEUE = []

    def multicast(self, group, message):
        self.SSEQUENCER = self.SSEQUENCER + 1
        message = message + " " + str(self.SSEQUENCER)
        a = m.BasicMulticast()
        a.multicast(group,message)

    def deliver(self, source,message):
        self.RSEQUENCERS[source.MYID] = self.RSEQUENCERS[source.MYID] + 1
        a = m.BasicMulticast()
        a.deliver(self.SELFNODE,source,message)