from server import TcpHandler,Server

HOST = ''
PORT = 8001

def runServer():
    print('서버 시작')

    try:
        server = Server((HOST, PORT), TcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('서버 종료')
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    runServer()