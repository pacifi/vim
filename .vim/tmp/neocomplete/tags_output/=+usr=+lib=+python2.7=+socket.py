!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
EBADF	/usr/lib/python2.7/socket.py	/^EBADF = getattr(errno, 'EBADF', 9)$/;"	v
EINTR	/usr/lib/python2.7/socket.py	/^EINTR = getattr(errno, 'EINTR', 4)$/;"	v
_GLOBAL_DEFAULT_TIMEOUT	/usr/lib/python2.7/socket.py	/^_GLOBAL_DEFAULT_TIMEOUT = object()$/;"	v
__all__	/usr/lib/python2.7/socket.py	/^__all__ = ["getfqdn", "create_connection"]$/;"	v
__del__	/usr/lib/python2.7/socket.py	/^    def __del__(self):$/;"	m	class:_fileobject	file:
__doc__	/usr/lib/python2.7/socket.py	/^    __doc__ = _realsocket.__doc__$/;"	v	class:_socketobject
__getattr__	/usr/lib/python2.7/socket.py	/^    __getattr__ = _dummy$/;"	v	class:_closedsocket
__init__	/usr/lib/python2.7/socket.py	/^    def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, _sock=None):$/;"	m	class:_socketobject
__init__	/usr/lib/python2.7/socket.py	/^    def __init__(self, sock, mode='rb', bufsize=-1, close=False):$/;"	m	class:_fileobject
__iter__	/usr/lib/python2.7/socket.py	/^    def __iter__(self):$/;"	m	class:_fileobject	file:
__slots__	/usr/lib/python2.7/socket.py	/^    __slots__ = ["_sock", "__weakref__"] + list(_delegate_methods)$/;"	v	class:_socketobject
__slots__	/usr/lib/python2.7/socket.py	/^    __slots__ = ["mode", "bufsize", "softspace",$/;"	v	class:_fileobject
__slots__	/usr/lib/python2.7/socket.py	/^    __slots__ = []$/;"	v	class:_closedsocket
_closedsocket	/usr/lib/python2.7/socket.py	/^class _closedsocket(object):$/;"	c
_delegate_methods	/usr/lib/python2.7/socket.py	/^_delegate_methods = ("recv", "recvfrom", "recv_into", "recvfrom_into",$/;"	v
_dummy	/usr/lib/python2.7/socket.py	/^    def _dummy(*args):$/;"	m	class:_closedsocket
_fileobject	/usr/lib/python2.7/socket.py	/^class _fileobject(object):$/;"	c
_getclosed	/usr/lib/python2.7/socket.py	/^    def _getclosed(self):$/;"	m	class:_fileobject
_realsocket	/usr/lib/python2.7/socket.py	/^_realsocket = socket$/;"	v
_socketmethods	/usr/lib/python2.7/socket.py	/^    _socketmethods = _socketmethods + ('ioctl',)$/;"	v
_socketmethods	/usr/lib/python2.7/socket.py	/^    _socketmethods = _socketmethods + ('sleeptaskw',)$/;"	v
_socketmethods	/usr/lib/python2.7/socket.py	/^_socketmethods = ($/;"	v
_socketobject	/usr/lib/python2.7/socket.py	/^class _socketobject(object):$/;"	c
accept	/usr/lib/python2.7/socket.py	/^    def accept(self):$/;"	m	class:_socketobject
close	/usr/lib/python2.7/socket.py	/^    def close(self):$/;"	m	class:_fileobject
close	/usr/lib/python2.7/socket.py	/^    def close(self, _closedsocket=_closedsocket,$/;"	m	class:_socketobject
closed	/usr/lib/python2.7/socket.py	/^    closed = property(_getclosed, doc="True if the file is closed")$/;"	v	class:_fileobject
create_connection	/usr/lib/python2.7/socket.py	/^def create_connection(address, timeout=_GLOBAL_DEFAULT_TIMEOUT,$/;"	f
default_bufsize	/usr/lib/python2.7/socket.py	/^    default_bufsize = 8192$/;"	v	class:_fileobject
dup	/usr/lib/python2.7/socket.py	/^    def dup(self):$/;"	m	class:_socketobject
errno	/usr/lib/python2.7/socket.py	/^    errno = None$/;"	v
errorTab	/usr/lib/python2.7/socket.py	/^    errorTab = {}$/;"	v
family	/usr/lib/python2.7/socket.py	/^    family = property(lambda self: self._sock.family, doc="the socket family")$/;"	v	class:_socketobject
fileno	/usr/lib/python2.7/socket.py	/^    def fileno(self):$/;"	m	class:_fileobject
flush	/usr/lib/python2.7/socket.py	/^    def flush(self):$/;"	m	class:_fileobject
getfqdn	/usr/lib/python2.7/socket.py	/^def getfqdn(name=''):$/;"	f
makefile	/usr/lib/python2.7/socket.py	/^    def makefile(self, mode='r', bufsize=-1):$/;"	m	class:_socketobject
meth	/usr/lib/python2.7/socket.py	/^def meth(name,self,*args):$/;"	f
name	/usr/lib/python2.7/socket.py	/^    name = "<socket>"$/;"	v	class:_fileobject
next	/usr/lib/python2.7/socket.py	/^    def next(self):$/;"	m	class:_fileobject
proto	/usr/lib/python2.7/socket.py	/^    proto = property(lambda self: self._sock.proto, doc="the socket protocol")$/;"	v	class:_socketobject
read	/usr/lib/python2.7/socket.py	/^    def read(self, size=-1):$/;"	m	class:_fileobject
readline	/usr/lib/python2.7/socket.py	/^    def readline(self, size=-1):$/;"	m	class:_fileobject
readlines	/usr/lib/python2.7/socket.py	/^    def readlines(self, sizehint=0):$/;"	m	class:_fileobject
ssl	/usr/lib/python2.7/socket.py	/^    def ssl(sock, keyfile=None, certfile=None):$/;"	f
type	/usr/lib/python2.7/socket.py	/^    type = property(lambda self: self._sock.type, doc="the socket type")$/;"	v	class:_socketobject
write	/usr/lib/python2.7/socket.py	/^    def write(self, data):$/;"	m	class:_fileobject
writelines	/usr/lib/python2.7/socket.py	/^    def writelines(self, list):$/;"	m	class:_fileobject
