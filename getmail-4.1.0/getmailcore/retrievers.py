#!/usr/bin/env python2.3
'''Classes implementing retrievers (message sources getmail can retrieve mail
from).

Currently implemented:

  SimplePOP3Retriever
  SimplePOP3SSLRetriever
  MultidropPOP3Retriever
  MultidropPOP3SSLRetriever
  MultidropSDPSRetriever
  SimpleIMAPRetriever -- IMAP, as a protocol, is a FPOS, and it shows.
    The Python standard library module imaplib leaves much up to
    the user because of this.
  SimpleIMAPSSLRetriever - the above, for IMAP-over-SSL.
  MultidropIMAPRetriever
  MultidropIMAPSSLRetriever
'''

__all__ = [
    'SimplePOP3Retriever',
    'SimplePOP3SSLRetriever',
    'MultidropPOP3Retriever',
    'MultidropPOP3SSLRetriever',
    'MultidropSDPSRetriever',
    'SimpleIMAPRetriever',
    'SimpleIMAPSSLRetriever',
    'MultidropIMAPRetriever',
    'MultidropIMAPSSLRetriever',
]

import socket
import poplib
import imaplib
import types

from exceptions import *
from constants import *
from utilities import *
from baseclasses import ConfigurableBase
from _retrieverbases import *

#
# Functional classes
#

#######################################
class SimplePOP3Retriever(POP3RetrieverBase, POP3initMixIn):
    '''Retriever class for single-user POP3 mailboxes.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        {'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : 110},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},
        {'name' : 'use_apop', 'type' : bool, 'default' : False},
    )
    received_from = None
    received_with = 'POP3'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'SimplePOP3Retriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('SimplePOP3Retriever(%s)\n' % self._confstring())

#######################################
class SimplePOP3SSLRetriever(POP3RetrieverBase, POP3SSLinitMixIn):
    '''Retriever class for single-user POP3-over-SSL mailboxes.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        {'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : POP3_ssl_port},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},
        {'name' : 'use_apop', 'type' : bool, 'default' : False},
        {'name' : 'keyfile', 'type' : str, 'default' : None},
        {'name' : 'certfile', 'type' : str, 'default' : None},
    )
    received_from = None
    received_with = 'POP3-SSL'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'SimplePOP3SSLRetriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('SimplePOP3SSLRetriever(%s)\n' % self._confstring())

#######################################
class MultidropPOP3Retriever(MultidropPOP3RetrieverBase, POP3initMixIn):
    '''Retriever class for multi-drop POP3 mailboxes.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        {'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : 110},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},
        {'name' : 'use_apop', 'type' : bool, 'default' : False},
        {'name' : 'envelope_recipient', 'type' : str},
    )
    received_from = None
    received_with = 'POP3'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'MultidropPOP3Retriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('MultidropPOP3Retriever(%s)\n' % self._confstring())

#######################################
class MultidropPOP3SSLRetriever(MultidropPOP3RetrieverBase, POP3SSLinitMixIn):
    '''Retriever class for multi-drop POP3-over-SSL mailboxes.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        {'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : POP3_ssl_port},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},
        {'name' : 'use_apop', 'type' : bool, 'default' : False},
        {'name' : 'envelope_recipient', 'type' : str},
        {'name' : 'keyfile', 'type' : str, 'default' : None},
        {'name' : 'certfile', 'type' : str, 'default' : None},
    )
    received_from = None
    received_with = 'POP3-SSL'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'MultidropPOP3SSLRetriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('MultidropPOP3SSLRetriever(%s)\n' % self._confstring())

#######################################
class MultidropSDPSRetriever(SimplePOP3Retriever, POP3initMixIn):
    '''Retriever class for multi-drop SDPS (demon.co.uk) mailboxes.

    Extend POP3 class to include support for Demon's protocol extensions, known
    as SDPS.  A non-standard command (*ENV) is used to retrieve the message
    envelope.  See http://www.demon.net/helpdesk/products/mail/sdps-tech.shtml
    for details.

    Support originally requested by Paul Clifford for getmail v.2/3.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        {'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : 110},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},
        # Demon apparently doesn't support APOP
        {'name' : 'use_apop', 'type' : bool, 'default' : False},
    )

    received_from = None
    received_with = 'SDPS'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'MultidropSDPSRetriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('MultidropSDPSRetriever(%s)\n' % self._confstring())

    def _getmsgbyid(self, msgid):
        self.log.trace()
        msg = SimplePOP3Retriever._getmsgbyid(self, msgid)

        # The magic of SDPS is the "*ENV" command.  Implement it:
        try:
            msgnum = self._getmsgnumbyid(msgid)
            resp, lines, octets = self.conn._longcmd('*ENV %i' % msgnum)
        except poplib.error_proto, o:
            raise getmailConfigurationError('server does not support *ENV (%s)'
                % o)
        if len(lines) < 4:
            raise getmailOperationError('short *ENV response (%s)' % lines)
        msg.sender = lines[2]
        msg.recipient = lines[3]
        return msg

#######################################
class SimpleIMAPRetriever(IMAPRetrieverBase, IMAPinitMixIn):
    '''Retriever class for single-user IMAPv4 mailboxes.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        {'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : imaplib.IMAP4_PORT},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},

        {'name' : 'mailboxes', 'type' : tuple, 'default' : ('INBOX', )},
        {'name' : 'move_on_delete', 'type' : str, 'default' : None},

        # imaplib.IMAP4.login_cram_md5() requires the (unimplemented)
        # .authenticate(), so we can't do this yet.
        {'name' : 'use_cram_md5', 'type' : bool, 'default' : False},
    )
    received_from = None
    received_with = 'IMAP4'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'SimpleIMAPRetriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('SimpleIMAPRetriever(%s)\n' % self._confstring())

#######################################
class SimpleIMAPSSLRetriever(IMAPRetrieverBase, IMAPSSLinitMixIn):
    '''Retriever class for single-user IMAPv4-over-SSL mailboxes.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        # socket.ssl() and socket timeouts are incompatible in Python 2.3
        #{'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : imaplib.IMAP4_SSL_PORT},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},

        {'name' : 'mailboxes', 'type' : tuple, 'default' : ('INBOX', )},
        {'name' : 'move_on_delete', 'type' : str, 'default' : None},

        {'name' : 'keyfile', 'type' : str, 'default' : None},
        {'name' : 'certfile', 'type' : str, 'default' : None},

        # imaplib.IMAP4.login_cram_md5() requires the (unimplemented)
        # .authenticate(), so we can't do this yet.
        {'name' : 'use_cram_md5', 'type' : bool, 'default' : False},
    )
    received_from = None
    received_with = 'IMAP4-SSL'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'SimpleIMAPSSLRetriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('SimpleIMAPSSLRetriever(%s)\n' % self._confstring())

#######################################
class MultidropIMAPRetriever(MultidropIMAPRetrieverBase, IMAPinitMixIn):
    '''Retriever class for multi-drop IMAPv4 mailboxes.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        {'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : imaplib.IMAP4_PORT},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},

        {'name' : 'mailboxes', 'type' : tuple, 'default' : ('INBOX', )},
        {'name' : 'move_on_delete', 'type' : str, 'default' : None},

        # imaplib.IMAP4.login_cram_md5() requires the (unimplemented)
        # .authenticate(), so we can't do this yet.
        {'name' : 'use_cram_md5', 'type' : bool, 'default' : False},

        {'name' : 'envelope_recipient', 'type' : str},
    )
    received_from = None
    received_with = 'IMAP4'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'MultidropIMAPRetriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('MultidropIMAPRetriever(%s)\n' % self._confstring())

#######################################
class MultidropIMAPSSLRetriever(MultidropIMAPRetrieverBase, IMAPSSLinitMixIn):
    '''Retriever class for multi-drop IMAPv4-over-SSL mailboxes.
    '''
    _confitems = (
        {'name' : 'configparser', 'type' : types.InstanceType, 'default' : None},
        {'name' : 'getmaildir', 'type' : str, 'default' : '~/.getmail/'},

        # socket.ssl() and socket timeouts are incompatible in Python 2.3
        #{'name' : 'timeout', 'type' : int, 'default' : 180},
        {'name' : 'server', 'type' : str},
        {'name' : 'port', 'type' : int, 'default' : imaplib.IMAP4_SSL_PORT},
        {'name' : 'username', 'type' : str},
        {'name' : 'password', 'type' : str, 'default' : None},

        {'name' : 'mailboxes', 'type' : tuple, 'default' : ('INBOX', )},
        {'name' : 'move_on_delete', 'type' : str, 'default' : None},

        {'name' : 'keyfile', 'type' : str, 'default' : None},
        {'name' : 'certfile', 'type' : str, 'default' : None},

        # imaplib.IMAP4.login_cram_md5() requires the (unimplemented)
        # .authenticate(), so we can't do this yet.
        {'name' : 'use_cram_md5', 'type' : bool, 'default' : False},

        {'name' : 'envelope_recipient', 'type' : str},
    )
    received_from = None
    received_with = 'IMAP4-SSL'
    received_by = socket.getfqdn()

    def __str__(self):
        self.log.trace()
        return 'MultidropIMAPSSLRetriever:%s@%s:%s' % (
            self.conf.get('username', 'username'),
            self.conf.get('server', 'server'),
            self.conf.get('port', 'port')
        )

    def showconf(self):
        self.log.trace()
        self.log.info('MultidropIMAPSSLRetriever(%s)\n' % self._confstring())