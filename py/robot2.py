class Robot:
    count = 0

    def __init__(self, name='dummy'):
        self.name = name
        self.count += 1
        
    def __del__(self):
        self.count -= 1

    def talk(self):
        print('Hi. I am %s.'%self.name)
        
    def walk(self, step):
        print('Sorry. No legs.')
        
    def run(self, dist, speed=10):
        print('Must go %dm at %dm/s speed.'%(dist, speed))
        print('Sorry. No legs.')

if __name__ == '__main__':
    asimo = Robot('asimo')
    print( dir(asimo) )
    asimo.talk()