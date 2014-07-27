from __future__ import absolute_import, unicode_literals, print_function
from collections import OrderedDict

import unittest
import hmac
import mock

from gro import Connection

class TestConnection(unittest.TestCase):
    def test_gro_initialization(self):
        k, s = 'key', 'secret'
        gro = Connection(k, s)
        self.assertEqual(gro.key, k)
        self.assertEqual(gro.secret, s)
        self.assertIsNone(gro.session)

    def test_compose_payload_no_session(self):
        k, s = 'key', 'secret'
        msg = {}
        gro = Connection(k, s)
        gro.compose_payload(msg,False)
        self.assertDictEqual(msg, {'header': {'wsKey': k}})

    def test_compose_payload_with_session(self):
        k, s, sess = 'key', 'secret', 'session'
        msg = {}
        gro = Connection(k, s)
        gro.session = sess
        gro.compose_payload(msg, True)
        self.assertDictEqual(
            msg,
            {'header': {'wsKey': k, 'sessionID': sess}}
        )

    def test_signature(self):
        secret, payload = 'secret', 'payload'
        gro = Connection('key', secret)
        signature = gro.sign_request(payload)
        self.assertEqual(
            signature,
            hmac.new(
                secret.encode(),
                payload.encode()
            ).hexdigest()
        )

    @mock.patch('gro.connection.requests')
    def test_request(self, m_req):
        meth = 'oneMethod'
        params = {'first': '1'}

        m_sr = mock.Mock()
        m_cp = mock.Mock()
        m_c = mock.Mock()
        gro  = Connection('key', 'secret')

        gro.compose_payload = m_cp
        gro.sign_request = m_sr
        gro.connection = m_c

        md = OrderedDict()
        md['method'] = meth
        md['parameters'] = params
        md['header'] = {'wsKey': 'key'}
        m_cp.return_value = md

        m_sr.return_value = 'signature'

        m_c.send.return_value.json.return_value = {}

        gro.request(meth, params)
        m_cp.assert_called_once_with(
            {'method': 'oneMethod', 'parameters': {'first': '1'}},
            False,
        )
        m_sr.assert_called_once_with(
            '{"method": "oneMethod", "parameters": {"first": "1"}, "header": {"wsKey": "key"}}'
        )
        m_req.Request.assert_called_once_with(
            'POST',
            'https://api.grooveshark.com/ws3.php',
            data='{"method": "oneMethod", "parameters": {"first": "1"}, "header": {"wsKey": "key"}}',
            params={u'sig': u'signature'}
        )
        m_c.prepare_request.assert_called_once_with(
            m_req.Request.return_value
        )
        m_c.send.assert_called_once_with(m_c.prepare_request.return_value)