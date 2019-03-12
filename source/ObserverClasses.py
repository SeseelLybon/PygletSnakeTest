



class KeyObservable:
    def __init__(self):
        self.__observers = []
    
    def register_observer(self, observer):
        self.__observers.append(observer)
    
    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.on_key_press(self, *args, **kwargs)

class KeyObserver:
    def __init__(self, observable):
        observable.register_observer(self)
    
    def on_key_press(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)
        
keySubject = KeyObservable()


if "__name__" == "__main__":
    subject = Observable()
    observer = Observer(subject)
    subject.notify_observers('test')