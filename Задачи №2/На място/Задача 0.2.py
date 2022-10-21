from abc import ABC, abstractmethod
from imp import init_builtin
from this import d

class BaseCounter:
    def __init__(self, initial=0, step=1) -> None:
        self.initial = initial
        self.step = step       

    def get_total(self):
        return self.initial

    @property
    def get_step(self):
        return self.step


class ICounterIncrement(ABC):
    @abstractmethod  
    def increment(self):
        pass

class ICounterDecrement(ABC):
    @abstractmethod
    def decrement(self):
        pass

class Counter(BaseCounter, ICounterIncrement):
    def __init__(self, initial=0, step=1) -> None:
        super().__init__(initial, step)
    
    def increment(self):
        self.initial += self.step

something = Counter()

something.increment()
something.increment()
print(f"Value of something should be: {something.get_total()} with step --> {something.get_step}")

class TwowayCounter(Counter, ICounterDecrement):
    def __init__(self, initial=0, step=1) -> None:
        super().__init__(initial, step)

    def decrement(self):
        self.initial -= self.step

somethingTwoway = TwowayCounter()

somethingTwoway.increment()
somethingTwoway.decrement()
print(f"Value of somethingTwoway should be: {somethingTwoway.get_total()} with step --> {somethingTwoway.get_step}")

class LimitedCounter(BaseCounter, ICounterIncrement):
    def __init__(self, max, initial=0, step=1) -> None:
        super().__init__(initial, step)
        self.max = max

    def increment(self):
        if(self.max > self.initial):
             self.initial += self.step

    def get_max(self):
        return self.max

somethingLimited = LimitedCounter(2)

somethingLimited.increment()
somethingLimited.increment()
somethingLimited.increment()
somethingLimited.increment()
print(f"Value of somethingLimited should be the max value ({somethingLimited.get_max()}): {somethingLimited.get_total()} with step --> {somethingLimited.get_step}")   

class LimitedTwowayCounter(LimitedCounter, ICounterDecrement):
    def __init__(self, max, min, initial=0, step=1) -> None:
        super().__init__(max, initial, step)
        self.min = min

    def decrement(self):
        if(self.min < self.initial): 
            self.initial -= 1

    def get_min(self):
        return self.min


somethingLimitedTwowayCounter = LimitedTwowayCounter(2, 0)

somethingLimitedTwowayCounter.increment()
somethingLimitedTwowayCounter.increment()
somethingLimitedTwowayCounter.increment()
somethingLimitedTwowayCounter.decrement()
somethingLimitedTwowayCounter.decrement()
somethingLimitedTwowayCounter.decrement()
somethingLimitedTwowayCounter.increment()
print("Value of somethingLimitedTwowayCounter should be between the max value " + 
f"({somethingLimitedTwowayCounter.get_max()}) and the min value ({somethingLimitedTwowayCounter.get_min()}): " + 
f"{somethingLimitedTwowayCounter.get_total()} with step --> {somethingLimitedTwowayCounter.get_step}")

class Semaphore(LimitedTwowayCounter):
    def __init__(self, is_available) -> None:
        if(is_available):
            super().__init__(1, 0, 1, 1)
        else:
            super().__init__(1, 0, 0, 1)

    def is_available(self):
        return self.initial > 0

    def wait(self):
        return self.decrement()

    def signal(self):
        return self.increment()

# Клас Semaphore
# Най-простия бинарен семафор - това е LimitedTwowayCounter, който има минимална стойност 0, максимална стойност 1 и стъпка 1. Използва се от процесите в операционнитe системи за синхронизационни цели. (За повече информация: https://skelet.ludost.net)

# Инициализатор с 1 параметър is_available=False. При True началната стойност на брояча е 1, а при False е 0.
# is_available(): връща bool, показващ дали стойността на брояча е над 0
# wait() - прави същото като decrement() на LimitedTwowayCounter
# signal() - прави същото като increment() на LimitedTwowayCounter

somethingSemaphore = Semaphore(False)
somethingSemaphore.signal()
somethingSemaphore.signal()
somethingSemaphore.signal()
print(f"Is somethingSemaphore available: Expected TRUE --> {somethingSemaphore.is_available()}")
somethingSemaphore.wait()
somethingSemaphore.wait()
somethingSemaphore.signal()
somethingSemaphore.wait()
print(f"Is somethingSemaphore available: Expected FALSE --> {somethingSemaphore.is_available()}")
somethingSemaphore.signal()
somethingSemaphore.signal()
print("Value of somethingSemaphore should be between the max value " + 
f"({somethingSemaphore.get_max()}) and the min value ({somethingSemaphore.get_min()}): " + 
f"{somethingSemaphore.get_total()} with step --> {somethingSemaphore.get_step}")