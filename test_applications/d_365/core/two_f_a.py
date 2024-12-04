import pyotp
from test_applications.d_365.core.base import Base

class TwoFA(Base):
    def __init__(self):
        totp = pyotp.TOTP("kc2k77zbgdn7c7sr")
        self.state["2fa"] = totp.now()

    def __call__(self, *args, **kwds):
        totp = pyotp.TOTP("kc2k77zbgdn7c7sr")
        self.state["2fa"] = totp.now()