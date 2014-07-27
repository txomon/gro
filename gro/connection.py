from __future__ import absolute_import, unicode_literals, print_function

import hmac
import logging

import requests
from gro.exception import GroErrorCodeException, GroRuntimeException


try:
    import simplejson as json
except ImportError:
    import json

logger = logging.getLogger('gro.connection')


class Connection(object):
    """
    Manages all the connections to Grooveshark, as a way to put together
    all the API calls.
    
    It needs to get initialized with an API Key and Secret, and it will
    by default do all the requests to the API in that way. Session parameter
    can be set and tell the connection manager put the session id too together
    with the requests, but it isn't in charge of managing the connection.
    """

    def __init__(self, key, secret):
        assert isinstance(key, unicode)
        assert isinstance(secret, unicode)
        self.key = key
        self.secret = secret
        self.protocol = 'https'
        self.host = 'api.grooveshark.com'
        self.endpoint = '/ws3.php'
        self.connection = requests.Session()

    def request(self, method, params=None, session=False):
        """
        This is meant to create and make the request to Grooveshark. It isn't
        meant to know anything about session handling, just about the
        structure of the request.
        
        :param str method: Name of the method to be called
        :param dict params: The data to be sent as request parameters
        :param bool session: Whether if the session id should or not be
        attached to the request.
        """
        msg = {'method': method}
        if params:
            msg['parameters'] = params
        msg = self.compose_payload(msg, session)
        msg_str = json.dumps(msg)
        signature = self.sign_request(msg_str)

        request = requests.Request(
            'POST',
            self.protocol + '://' + self.host + self.endpoint,
            data = msg_str,
            params = {'sig': signature},
        )
        prep_req = self.connection.prepare_request(request)
        response = self.connection.send(prep_req).json()
        if 'errors' in response:
            raise GroErrorCodeException(
                response['errors'][0]['code'],
                response['errors'][0]['message'],
            )
        return response

    session = None
    """
    This session id is meant to be kept by the connection manager but organized
    by the session manager in a way to make them separate.

    :type str:
    """

    def sign_request(self, payload):
        """
        Sign request with for the given payload. Returns signature

        :param str payload: Payload to sign
        :return str: Signature
        """
        hash = hmac.new(self.secret.encode())
        hash.update(payload)
        return hash.hexdigest()

    def compose_payload(self, message, session):
        """
        Add all the needed headers to the message
        :param message:
        :return:
        """
        assert isinstance(message, dict)
        message['header'] = {'wsKey': self.key}
        if session:
            if not self.session:
                self.create_session()
            message['header']['sessionID'] = self.session
        return message

    def create_session(self):
        response = self.request('startSession')
        if not response.get('result',{}).get('success', False):
            raise GroRuntimeException(
                response.get('result',{}).get('success', False),
                response.get('result',{})
            )
        self.session = response['result']['sessionID']

    def ping_service(self):
        response = self.request('pingService')
        return response