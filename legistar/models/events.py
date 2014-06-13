from .base import LegistarODataBase


class Events(LegistarODataBase):
    def list(self, **kwargs):
        return (Event(self.legistar_client, x) for x in self.request("GET", "Events"))


class Event(LegistarODataBase):
    def __init__(self, legistar_client, info, **kwargs):
        super(Event, self).__init__(legistar_client, **kwargs)
        self.info = info
        self.id = self.info.get('EventBodyId', None)

    def _fetch(self, **kwargs):
        return self.request("GET", "Events/%s" % (self.id))

    def event_items(self, **kwargs):
        return self.request("GET", "Events/%s/EventItems" % (self.id))

    def __str__(self):
        return "<Event %s (%s)>" % (self.id, self.info.get("EventBodyName"))
