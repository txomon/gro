from __future__ import unicode_literals, absolute_import, print_function

class GroException(Exception):
    pass

class GroErrorCodeException(GroException):
    def __init__(self, code, message, *args, **kwargs):
        self.code = code
        self.message = message.decode()
        super(GroException, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Grooveshark Code Exception {}: {}".format(self.code, self.message) + ">"

    def __unicode__(self):
        return "<Grooveshark Code Exception {}: {}".format(self.code, self.message) + ">"

    def __str__(self):
        return "<Grooveshark Code Exception {}: {}".format(self.code, self.message) + ">"

class GroRuntimeException(GroException):
    def __init__(self, message, *args, **kwargs):
        self.message = message.decode()
        super(GroException, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Grooveshark Runtime Exception: {}".format(self.message) + ">"

    def __unicode__(self):
        return "<Grooveshark Runtime Exception: {}".format(self.message) + ">"

    def __str__(self):
        return "<Grooveshark Runtime Exception: {}".format(self.message) + ">"
