

class Triggerer():
    '''
    Attributes:
    - trigger_labels: 
    Methods:
    - 
    '''

    def __init__(self, address, trigger_types):
        '''
        trigger_types: list of strings indicating the flag labels desired
        '''
        self.p = ParallelPort(address)
        self.trigger_labels = 
    
    def set_trigger_labels(self, trigger_types):
        '''
        Map the trigger_types (list of strings with the labels for the flags) onto pin settings.
        
        '''
        trigger_labels = {}
        for trigger, index in enumerate(trigger_types):
            trigger_labels[trigger] = index + 1
        return trigger_labels
            

    def send_trigger(self, value, duration = .002):
        self.p.setData(value)
        time.sleep(duration)
        self.p.setData(0)
