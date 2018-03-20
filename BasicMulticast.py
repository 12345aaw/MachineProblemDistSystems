from MulticastAbstract import MulticastAbstract
import unicast as u

class BasicMulticast( MulticastAbstract ):
    RECEIVED = []
    def multicast(self, group, message):
        for i in group:
            u.unicast_send(group[i],message)
    def deliver(self, source,message):
        u.receive()