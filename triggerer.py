class Triggerer:

    def __init__(self, address):
        self.p = ParallelPort(address)

    def send_trigger(self, value, duration = .002):
        self.p.setData(value)
        time.sleep(duration)
        self.p.setData(0)
