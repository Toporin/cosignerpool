#!/usr/bin/env python3
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2015 Thomas Voegtlin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import os
import sys
import traceback
import plyvel


def run_server(host, port):
    from xmlrpc.server import SimpleXMLRPCServer
    server = SimpleXMLRPCServer((host, port), allow_none=True, logRequests=False)
    server.register_function(delete, 'delete')
    server.register_function(get, 'get')
    server.register_function(put, 'put')
    server.running = True
    while server.running:
        try:
            server.handle_request()
        except KeyboardInterrupt:
            print("Shutting down server")
            sys.exit(0)
        except BaseException as e:
            traceback.print_exc(file=sys.stdout)
    print("server stopped")


def get(key):
    o = db.get(key)
    if o:
        print("get", key, len(o))
    return o


def put(key, value):
    print("put", key, len(value))
    db.put(key, value)


def delete(key):
    db.delete(key)


if __name__ == '__main__':
    my_host = os.environ.get("LISTEN_HOST", "0.0.0.0")
    my_port = os.environ.get("LISTEN_PORT", 80)
    try:
        dbpath = os.environ["DB_PATH"]
    except KeyError as e:
        print("Required variable {} not set".format(e))
        sys.exit(1)

    db = plyvel.DB(dbpath, create_if_missing=True, compression=None)
    run_server(my_host, my_port)
    db.close()
