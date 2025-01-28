import pyotp
from test_applications.d_365.core.base import Base

class IIFA(Base):
    def __init__(self):
        totp = pyotp.TOTP("kc2k77zbgdn7c7sr")
        self.state["iifa"] = totp.now()
        print(self.state["iifa"] )



    def __call__(self, *args, **kwds):
        totp = pyotp.TOTP("kc2k77zbgdn7c7sr")
        self.state["iifa"] = totp.now()
        print(self.state["iifa"] )

        return self.state["iifa"] 