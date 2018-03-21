from MulticastAbstract import MulticastAbstract
import BasicMulticast as m
class CausalMulticast( MulticastAbstract ):
    def __init__(self,selfnode,NUMOFNODES):

        # Use vector timestamps in liu of sequence numbers. All initated at 0

        self.VECTORTIMESTAMPS = []
        self.SELFNODE = selfnode
        for a in range(NUMOFNODES):
            self.VECTORTIMESTAMPS.append(0)
        self.QUEUE = []

    def multicast(self, group, message):

        # increment self's timestamp before piggybacking onto message

        self.VECTORTIMESTAMPS[self.SELFNODE.MYID] += 1
        message = message + " " + str(self.VECTORTIMESTAMPS)

        # Basic Multicast

        a = m.BasicMulticast()
        a.multicast(group,message)

    # Basic Delivery

    def deliver(self, source,message):
        a = m.BasicMulticast()
        a.deliver(self.SELFNODE,source,message)