from __future__ import absolute_import, unicode_literals, print_function

import logging


logger = logging.getLogger('gro.connection')


class GroConnection(object):
    """
    Manages all the connections to Grooveshark, as a way to put together
    all the API calls.
    
    It needs to get initialized with an API Key and Secret, and it will
    by default do all the requests to the API in that way. Session parameter
    can be set and tell the connection manager put the session id too together
    with the requests, but it isn't in charge of managing the connection.
    """
    def __init__(self, key, secret):
        pass
    
    def request(self, method, params, session=False):
        """
        This is meant to create and make the request to Grooveshark. It isn't
        meant to know anything about session handling, just about the
        form of the request.
        
        :param str method: Name of the method to be called
        :param dict params: The data to be sent as request parameters
        :param bool session: Whether if the session id should or not be
        attached to the request.
        """
        pass
    
    session = str()
    """
    This session id is meant to be kept by the connection manager but organized
    by the session manager in a way to make them separate. 
    """