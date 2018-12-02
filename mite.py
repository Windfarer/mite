import zmq
import pickle


class Sink:
    def __init__(self, bind_addr="tcp://*:6667"):
        self.context = zmq.Context()

        self.receiver = self.context.socket(zmq.PULL)
        self.receiver.bind(bind_addr)

    def __iter__(self):
        while True:
            data = self.receiver.recv_pyobj()
            yield data


class Ventilator:
    def __init__(self, bind_addr="tcp://*:6666"):
        self.context = zmq.Context()

        # Socket to send messages on
        self.sender = self.context.socket(zmq.PUSH)
        self.sender.bind(bind_addr)

    def send(self, data):
        return self.sender.send_pyobj(data)


class Worker:
    def __init__(self,
                 upstream_addr="tcp://localhost:6666",
                 downstream_addr="tcp://localhost:6667",
                 pipeline=None):
        self.context = zmq.Context()

        self.receiver = self.context.socket(zmq.PULL)
        self.receiver.connect(upstream_addr)

        self.sender = self.context.socket(zmq.PUSH)
        self.sender.connect(downstream_addr)

        assert callable(pipeline)
        self.pipeline = pipeline

    def run(self):
        while True:
            data = self.receiver.recv_pyobj()
            result = self.pipeline(data)
            self.sender.send_pyobj(result)
