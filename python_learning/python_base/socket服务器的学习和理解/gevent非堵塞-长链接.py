import socket
import re
import gevent
from  gevent import monkey

monkey.patch_all()


def service_client(new_socket, request):
    """为这个客户端返回数据"""

    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    # request = new_socket.recv(1024).decode("utf-8")
    # print(">>>"*50)
    # print(request)

    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    # print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    print(ret.group(1))
    if ret:
        file_name = ret.group(1)
        # print("*"*50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2. 返回http格式的数据，给浏览器

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞
    while True:
        # 4. 等待新客户端的链接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
        try:
            # 1.recv_data = none：即客户端关闭的情况下
            # 2.recv_data = data:即客户端发来了数据
            recv_data = new_socket.recv(1024).decode("utf-8")
        except Exception as ret:
            pass
        else:
            if recv_data:  # 当服务器接收到的是客户端发来的数据时
                gevent.joinall([gevent.spawn(service_client, new_socket, recv_data)])
            else:  # 当客户端关闭了，recv_data = none时
                new_socket.close()

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()

