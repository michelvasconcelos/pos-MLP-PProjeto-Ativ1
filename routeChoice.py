from typing import Type
from routes import IRoute
from safeRoute import SafeRoute
from unsafeRoute import UnsafeRoute
from safestRoute import SafestRoute

class Choice():
    def __init__(self, route_option: Type[IRoute]) -> None:
        self.route_option = route_option
        
    def choice(self):
        self.route_option.path()
        
safe = Choice(UnsafeRoute())
safe.choice()
safe = Choice(SafeRoute())
safe.choice()
safe = Choice(SafestRoute())
safe.choice()