from google.appengine.ext import ndb


class Vehicle(ndb.Model):
    brand = ndb.StringProperty()
    type = ndb.StringProperty()
    regno = ndb.StringProperty()
    #datum_vpis = ndb.DateTimeProperty(auto_now_add=True)
