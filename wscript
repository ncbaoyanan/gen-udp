## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('gen-udp', ['applications', 'internet'])
    module.source = [
        'model/general-udp-client.cc',
        'model/general-udp-server.cc',
        'helper/general-udp-client-server-helper.cc',
        ]

   ## module_test = bld.create_ns3_module_test_library('mms')
   ## module_test.source = [
   ##     'test/mms-client-server-test.cc',
   ##     ]

    headers = bld.new_task_gen(features=['ns3header'])
    headers.module = 'gen-udp'
    headers.source = [
        'model/general-udp-client.h',
        'model/general-udp-server.h',
        'helper/general-udp-client-server-helper.h',
        ]

   # bld.ns3_python_bindings()
