!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
BPF	/usr/lib/python2.7/random.py	/^BPF = 53        # Number of bits in a float$/;"	v
LOG4	/usr/lib/python2.7/random.py	/^LOG4 = _log(4.0)$/;"	v
NV_MAGICCONST	/usr/lib/python2.7/random.py	/^NV_MAGICCONST = 4 * _exp(-0.5)\/_sqrt(2.0)$/;"	v
RECIP_BPF	/usr/lib/python2.7/random.py	/^RECIP_BPF = 2**-BPF$/;"	v
Random	/usr/lib/python2.7/random.py	/^class Random(_random.Random):$/;"	c
SG_MAGICCONST	/usr/lib/python2.7/random.py	/^SG_MAGICCONST = 1.0 + _log(4.5)$/;"	v
SystemRandom	/usr/lib/python2.7/random.py	/^class SystemRandom(Random):$/;"	c
TWOPI	/usr/lib/python2.7/random.py	/^TWOPI = 2.0*_pi$/;"	v
VERSION	/usr/lib/python2.7/random.py	/^    VERSION = 1     # used by getstate\/setstate$/;"	v	class:WichmannHill
VERSION	/usr/lib/python2.7/random.py	/^    VERSION = 3     # used by getstate\/setstate$/;"	v	class:Random
WichmannHill	/usr/lib/python2.7/random.py	/^class WichmannHill(Random):$/;"	c
__all__	/usr/lib/python2.7/random.py	/^__all__ = ["Random","seed","random","uniform","randint","choice","sample",$/;"	v
__getstate__	/usr/lib/python2.7/random.py	/^    def __getstate__(self): # for pickle$/;"	m	class:Random	file:
__init__	/usr/lib/python2.7/random.py	/^    def __init__(self, x=None):$/;"	m	class:Random
__reduce__	/usr/lib/python2.7/random.py	/^    def __reduce__(self):$/;"	m	class:Random	file:
__setstate__	/usr/lib/python2.7/random.py	/^    def __setstate__(self, state):  # for pickle$/;"	m	class:Random	file:
__whseed	/usr/lib/python2.7/random.py	/^    def __whseed(self, x=0, y=0, z=0):$/;"	m	class:WichmannHill	file:
_inst	/usr/lib/python2.7/random.py	/^_inst = Random()$/;"	v
_notimplemented	/usr/lib/python2.7/random.py	/^    def _notimplemented(self, *args, **kwds):$/;"	m	class:SystemRandom
_randbelow	/usr/lib/python2.7/random.py	/^    def _randbelow(self, n, _log=_log, _int=int, _maxwidth=1L<<BPF,$/;"	m	class:Random
_stub	/usr/lib/python2.7/random.py	/^    def _stub(self, *args, **kwds):$/;"	m	class:SystemRandom
_test	/usr/lib/python2.7/random.py	/^def _test(N=2000):$/;"	f
_test_generator	/usr/lib/python2.7/random.py	/^def _test_generator(n, func, args):$/;"	f
betavariate	/usr/lib/python2.7/random.py	/^    def betavariate(self, alpha, beta):$/;"	m	class:Random
betavariate	/usr/lib/python2.7/random.py	/^betavariate = _inst.betavariate$/;"	v
choice	/usr/lib/python2.7/random.py	/^    def choice(self, seq):$/;"	m	class:Random
choice	/usr/lib/python2.7/random.py	/^choice = _inst.choice$/;"	v
expovariate	/usr/lib/python2.7/random.py	/^    def expovariate(self, lambd):$/;"	m	class:Random
expovariate	/usr/lib/python2.7/random.py	/^expovariate = _inst.expovariate$/;"	v
gammavariate	/usr/lib/python2.7/random.py	/^    def gammavariate(self, alpha, beta):$/;"	m	class:Random
gammavariate	/usr/lib/python2.7/random.py	/^gammavariate = _inst.gammavariate$/;"	v
gauss	/usr/lib/python2.7/random.py	/^    def gauss(self, mu, sigma):$/;"	m	class:Random
gauss	/usr/lib/python2.7/random.py	/^gauss = _inst.gauss$/;"	v
getrandbits	/usr/lib/python2.7/random.py	/^    def getrandbits(self, k):$/;"	m	class:SystemRandom
getrandbits	/usr/lib/python2.7/random.py	/^getrandbits = _inst.getrandbits$/;"	v
getstate	/usr/lib/python2.7/random.py	/^    def getstate(self):$/;"	m	class:Random
getstate	/usr/lib/python2.7/random.py	/^    def getstate(self):$/;"	m	class:WichmannHill
getstate	/usr/lib/python2.7/random.py	/^getstate = _inst.getstate$/;"	v
jumpahead	/usr/lib/python2.7/random.py	/^    def jumpahead(self, n):$/;"	m	class:Random
jumpahead	/usr/lib/python2.7/random.py	/^    def jumpahead(self, n):$/;"	m	class:WichmannHill
jumpahead	/usr/lib/python2.7/random.py	/^jumpahead = _inst.jumpahead$/;"	v
lognormvariate	/usr/lib/python2.7/random.py	/^    def lognormvariate(self, mu, sigma):$/;"	m	class:Random
lognormvariate	/usr/lib/python2.7/random.py	/^lognormvariate = _inst.lognormvariate$/;"	v
normalvariate	/usr/lib/python2.7/random.py	/^    def normalvariate(self, mu, sigma):$/;"	m	class:Random
normalvariate	/usr/lib/python2.7/random.py	/^normalvariate = _inst.normalvariate$/;"	v
paretovariate	/usr/lib/python2.7/random.py	/^    def paretovariate(self, alpha):$/;"	m	class:Random
paretovariate	/usr/lib/python2.7/random.py	/^paretovariate = _inst.paretovariate$/;"	v
randint	/usr/lib/python2.7/random.py	/^    def randint(self, a, b):$/;"	m	class:Random
randint	/usr/lib/python2.7/random.py	/^randint = _inst.randint$/;"	v
random	/usr/lib/python2.7/random.py	/^    def random(self):$/;"	m	class:SystemRandom
random	/usr/lib/python2.7/random.py	/^    def random(self):$/;"	m	class:WichmannHill
random	/usr/lib/python2.7/random.py	/^random = _inst.random$/;"	v
randrange	/usr/lib/python2.7/random.py	/^    def randrange(self, start, stop=None, step=1, _int=int, _maxwidth=1L<<BPF):$/;"	m	class:Random
randrange	/usr/lib/python2.7/random.py	/^randrange = _inst.randrange$/;"	v
sample	/usr/lib/python2.7/random.py	/^    def sample(self, population, k):$/;"	m	class:Random
sample	/usr/lib/python2.7/random.py	/^sample = _inst.sample$/;"	v
seed	/usr/lib/python2.7/random.py	/^    def seed(self, a=None):$/;"	m	class:Random
seed	/usr/lib/python2.7/random.py	/^    def seed(self, a=None):$/;"	m	class:WichmannHill
seed	/usr/lib/python2.7/random.py	/^seed = _inst.seed$/;"	v
setstate	/usr/lib/python2.7/random.py	/^    def setstate(self, state):$/;"	m	class:Random
setstate	/usr/lib/python2.7/random.py	/^    def setstate(self, state):$/;"	m	class:WichmannHill
setstate	/usr/lib/python2.7/random.py	/^setstate = _inst.setstate$/;"	v
shuffle	/usr/lib/python2.7/random.py	/^    def shuffle(self, x, random=None):$/;"	m	class:Random
shuffle	/usr/lib/python2.7/random.py	/^shuffle = _inst.shuffle$/;"	v
triangular	/usr/lib/python2.7/random.py	/^    def triangular(self, low=0.0, high=1.0, mode=None):$/;"	m	class:Random
triangular	/usr/lib/python2.7/random.py	/^triangular = _inst.triangular$/;"	v
uniform	/usr/lib/python2.7/random.py	/^    def uniform(self, a, b):$/;"	m	class:Random
uniform	/usr/lib/python2.7/random.py	/^uniform = _inst.uniform$/;"	v
vonmisesvariate	/usr/lib/python2.7/random.py	/^    def vonmisesvariate(self, mu, kappa):$/;"	m	class:Random
vonmisesvariate	/usr/lib/python2.7/random.py	/^vonmisesvariate = _inst.vonmisesvariate$/;"	v
weibullvariate	/usr/lib/python2.7/random.py	/^    def weibullvariate(self, alpha, beta):$/;"	m	class:Random
weibullvariate	/usr/lib/python2.7/random.py	/^weibullvariate = _inst.weibullvariate$/;"	v
whseed	/usr/lib/python2.7/random.py	/^    def whseed(self, a=None):$/;"	m	class:WichmannHill
