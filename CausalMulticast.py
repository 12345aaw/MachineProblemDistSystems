from MulticastAbstract import MulticastAbstract
import BasicMulticast as m
class CausalMulticast( MulticastAbstract ):
    def __init__(self,selfnode,NUMOFNODES):
        self.VECTORTIMESTAMPS = []
        self.SELFNODE = selfnode
        for a in range(NUMOFNODES):
            self.VECTORTIMESTAMPS.append(0)
        self.QUEUE = []

    def multicast(self, group, message):
        self.VECTORTIMESTAMPS[self.SELFNODE.MYID] += 1
        message = message + " " + str(self.VECTORTIMESTAMPS)
        a = m.BasicMulticast()
        a.multicast(group,message)

    def deliver(self, source,message):
        a = m.BasicMulticast()
        a.deliver(self.SELFNODE,source,message)