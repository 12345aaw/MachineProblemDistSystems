from MulticastAbstract import MulticastAbstract
import unicast as u
class BasicMulticast( MulticastAbstract ):
    RECEIVED = []
    def multicast(self, group, message):
        for i in range(len(group)):
            u.unicast_send(group[i],message)
    def deliver(self, selfnode, source,message):
        u.unicast_receive(selfnode, source, message)