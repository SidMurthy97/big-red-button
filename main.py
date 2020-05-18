from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import sleep

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()

if __name__ == '__main__':
    
    
    m.click(960, 100, 1)
    sleep(0.5)
    k.type_string('dad')
    sleep(0.5)
    k.tap_key('Return')
    sleep(1.0)
    m.click(1053,826,1)
    
    '''
    for i in range(5000):
        print(m.position())'''