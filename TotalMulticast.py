from MulticastAbstract import MulticastAbstract
import BasicMulticast as m
class TotalMulticast( MulticastAbstract ):
    def __init__(self,selfnode):
        self.COUNTER = 0
        self.SELFNODE = selfnode
        self.QUEUE = []

    def multicast(self, group, message):
        a = m.BasicMulticast()
        message = message + " " + str(self.COUNTER)
        a.multicast(group,message)
        
    def deliver(self, source,message):
        a = m.BasicMulticast()
        a.deliver(self.SELFNODE,source,message)
