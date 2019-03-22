



class KeyObservable:
    def __init__(self):
        self.__observers = []
    
    def register_observer(self, observer):
        self.__observers.append(observer)
    
    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.on_key_press(self, *args, **kwargs)

            
keySubject = KeyObservable()


class KeyObserver:
    keySubject = keySubject
    def __init__(self):
        keySubject.register_observer(self)
    
    def on_key_press(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)
        
