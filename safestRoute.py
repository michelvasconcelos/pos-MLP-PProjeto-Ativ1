from routes import IRoute

class SafestRoute(IRoute):
    def __init__(self):
        self.risk = 'super safe'
        self.distance = 'longest'

    def path(self):
        print(f'You took the {self.distance} route but got home {self.risk}! :-)')

#SafestRoute().path()