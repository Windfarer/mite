class Maybe:
    def __init__(self, val=None):
        if val is None:
            val = {}
        self.val = val
        self.err = None

    def do(self, func):
        if isinstance(self, Nothing):
            return self
        try:
            val = func(self.val)
        except Exception as e:
            return Nothing(self.val, repr(e), func.__name__)
        return Just(val)


class Just(Maybe):
    def unwrap(self):
        return self.val


class Nothing(Maybe):
    def __init__(self, val, error=None, func=None):
        self.val = val
        self.err = {"error": error, "func": func}

    def unwrap(self):
        return self.val
