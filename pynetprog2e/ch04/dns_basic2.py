#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 4 - dns_basic.py
# Basic DNS query

#import sys, DNS
import sys,dns
import dns.resolver

if len(sys.argv) != 2:
    print >>sys.stderr, 'usage: dns_basic.py <hostname>'
    sys.exit(2)

#DNS.DiscoverNameServers()

#request = DNS.Request()

dnsrecs = ['A','AAAA','MX','NS','CNAME']
#for qt in DNS.Type.A, DNS.Type.AAAA, DNS.Type.CNAME, DNS.Type.MX, DNS.Type.NS:
for qt in dnsrecs:
    #reply = request.req(name=sys.argv[1], qtype=qt)
    try:
        reply = dns.resolver.query(sys.argv[1],qt)
    except dns.resolver.NoAnswer, e:
        print sys.argv[1] + '/' + qt + ':  No Result'
        continue
    #for answer in reply.answers:
    for answer in reply:
        #print answer['name'], answer['classstr'], answer['typename'], \
        #    repr(answer['data'])
        print sys.argv[1] + '/' + qt + ':  ' + str(answer)

