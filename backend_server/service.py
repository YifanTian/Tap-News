""" Backend service """
import operations
import pyjsonrpc

SERVER_HOST = 'localhost'
SERER_PORT = 4040

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """ RPC request handler """
    @pyjsonrpc.rpcmethod
    def add(self, num1, num2):
        """ Test method """
        print "add is called with %d and %d" % (num1, num2)
        return num1 + num2

    """ Get news summaries for a user """
    @pyjsonrpc.rpcmethod
    def getNewsSummariesForUser(self, user_id, page_num):
        return operations.getNewsSummariesForUser(user_id, page_num)

    """ Log user news clicks """
    @pyjsonrpc.rpcmethod
    def logNewsClickForUser(self, user_id, news_id):
        print('rpc method log news click')
        return operations.logNewsClickForUser(user_id, news_id)

# Threading HTTP Server
HTTP_SERVER = pyjsonrpc.ThreadingHttpServer(
    server_address=(SERVER_HOST, SERER_PORT),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server on %s%d" % (SERVER_HOST, SERER_PORT)

HTTP_SERVER.serve_forever()
