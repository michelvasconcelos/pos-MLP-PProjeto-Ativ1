from routes import IRoute

class UnsafeRoute(IRoute):
    def __init__(self):
        self.risk = 'robbed'
        self.distance = 'shortest'

    def path(self):
        print(f'You took the {self.distance} route and got {self.risk}! :-(')

#UnsafeRoute().path()