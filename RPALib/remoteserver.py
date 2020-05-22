from twisted.web import xmlrpc, server, resource
from twisted.internet import reactor, endpoints

class RemoteServer(xmlrpc.XMLRPC):
    
    def __init__(self):
        self.names = ['add', 'numbers_should_be_equal']
        self.args = {}
        self.args['add'] = ['x', 'y']
        self.args['numbers_should_be_equal'] = ['x', 'y']
        super().__init__()

    def xmlrpc_get_keyword_names(self):
        return self.names

    def xmlrpc_get_keyword_arguments(self, name):
        return self.args[name]
    
    def xmlrpc_run_keyword(self, name, args, kwargs=None):
        print(name)
        print(args)
        if name == "add":
            return self.xmlrpc_add(int(args[0]), int(args[1]))
        elif name == "numbers_should_be_equal":
            return self.xmlrpc_numbers_should_be_equal(int(args[0]), int(args[1]))
        

    def xmlrpc_add(self, x, y):
        resp = {}
        resp['output'] = str(x+y)
        resp['status'] = "PASS"
        resp['return'] = x+y
        resp['error'] = ""
        resp['traceback'] = ""
        print(resp)
        return resp

    def xmlrpc_numbers_should_be_equal(self, x, y):
        resp = {}
        if x == y:
            resp['status'] = "PASS"
            resp['return'] = "TRUE"
        else:
            resp['status'] = "FAIL"
            resp['error'] = "Numbers are not equal"
            resp['return'] = "FALSE"
        resp['return'] = ""
        resp['error'] = ""
        resp['traceback'] = ""
        return resp


if __name__ == '__main__':
    r = RemoteServer()
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 7080)
    endpoint.listen(server.Site(r))
    reactor.run()