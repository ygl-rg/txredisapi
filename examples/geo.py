# coding: utf-8
from __future__ import print_function, absolute_import
import os.path as os_path
#curr_dir = os_path.dirname(os_path.abspath(__file__))
import sys
#sys.path.append(os_path.dirname(curr_dir))
import time
from twisted.internet import defer
from twisted.python import log
from twisted.internet import reactor
from .. import txredisapi as redis

HOST = 'localhost'
PORT = 6379

N = 10000


@defer.inlineCallbacks
def test_geoadd():
    key = 'test'
    conn = yield redis.Connection(HOST, PORT)
    start = time.time()
    for i in xrange(N):
        res = yield conn.geoadd(key, i*0.0001,i*0.0001+0.09,'{0}{1}'.format(key,i))
        #log.msg(res)
    print("done geoadd: %.4fs." % ((time.time() - start) / N))


@defer.inlineCallbacks
def test_geohash():
    key = 'test'
    conn = yield redis.Connection(HOST, PORT)
    start = time.time()
    for i in xrange(N):
        res = yield conn.geohash(key, '{0}{1}'.format(key,i))
        #log.msg(res)
    print("done geohash: %.4fs." % ((time.time() - start) / N))


@defer.inlineCallbacks
def test_geopos():
    key = 'test'
    conn = yield redis.Connection(HOST, PORT, charset=None, convertNumbers=False)
    start = time.time()
    for i in xrange(N):
        res = yield conn.geopos(key, '{0}{1}'.format(key,i))
        #log.msg(res)
    print("done geopos: %.4fs." % ((time.time() - start) / N))


@defer.inlineCallbacks
def test_georadius():
    key = 'test'
    conn = yield redis.Connection(HOST, PORT, charset=None, convertNumbers=False)
    start = time.time()
    for i in xrange(N):
        res = yield conn.georadius(key, 0.0002, 0.0002, 1, 'km', 'COUNT', 1)
        #log.msg(res)
    print("done georadius: %.4fs." % ((time.time() - start) / N))


@defer.inlineCallbacks
def test_georadiusbymember():
    key = 'test'
    conn = yield redis.Connection(HOST, PORT, charset=None, convertNumbers=False)
    start = time.time()
    for i in xrange(N):
        res = yield conn.georadiusbymember(key, '{0}{1}'.format(key, i), 5, 'km', 'COUNT', 1, 'DESC')
        #log.msg(res)
    print("done georadiusbymember: %.4fs." % ((time.time() - start) / N))


@defer.inlineCallbacks
def run():
    try:
        #yield test_geoadd()
        #yield test_geohash()
        yield test_georadiusbymember()
        reactor.stop()
    except:
        log.err()

if __name__ == "__main__":
    log.startLogging(sys.stdout)
    run()
    reactor.run()
