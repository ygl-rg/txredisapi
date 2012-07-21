#!/usr/bin/env python
# coding: utf-8

"""
Configure your redis instance to accept authentication (requirepass directive)
before running this example, otherwise all commands will raise ResponseError
"""

import txredisapi as redis

from twisted.internet import defer
from twisted.internet import reactor


@defer.inlineCallbacks
def main():
    rc = yield redis.Connection()
    print rc
    a = yield rc.auth('el_bonito')
    print a
    yield rc.set("foo", "bar")
    v = yield rc.get("foo")
    print "foo:", repr(v)

    yield rc.disconnect()


if __name__ == "__main__":
    main().addCallback(lambda ign: reactor.stop())
    reactor.run()
