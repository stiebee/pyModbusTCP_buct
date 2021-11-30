# -*- coding: utf-8 -*-

# Python package: Client and Server for ModBus/TCP
#        Version: 0.1.10
#        Website: https://github.com/stiebee/pyModbusTCP_buct
#           Date: 2021-11-30
#        License: MIT (http://http://opensource.org/licenses/mit-license.php)
#    Description: Client/Server ModBus/TCP
#                 Support functions 3 and 16 (class 0)
#                 1,2,4,5,6 (Class 1)
#                 15
#                 43
#                 Forked from https://github.com/sourceperl/pyModbusTCP to support
#                   Encapsulated Interface Transport (function code 0x2b=43)
#        Charset: utf-8

from .constants import VERSION


__all__ = ['constants', 'client', 'server', 'utils']
__title__ = 'pyModbusTCP_buct'
__description__ = 'A simple Modbus/TCP library for Python.'
__url__ = 'https://github.com/stiebee/pyModbusTCP_buct'
__version__ = VERSION
__license__ = 'MIT'
