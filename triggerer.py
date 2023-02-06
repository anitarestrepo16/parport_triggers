from psychopy.parallel import ParallelPort

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
        self.trigger_labels = {}
        for trigger, index in enumerate(trigger_types):
            self.trigger_labels[trigger] = index + 1
        return self.trigger_labels
            

    def send_trigger(self, trigger_type, duration = .002):
        value = self.trigger_labels[trigger_type]
        self.p.setData(value)
        time.sleep(duration)
        self.p.setData(0)
