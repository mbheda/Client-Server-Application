# Client-Server-Application
Network Architecture

We have used socket programming with the TCP
protocol.
The process involves the client contacting the server,
which must already be active. The client then creates
the socket and asks the user for the server name and
port number of the server. The client then establishes
the connection and requests the file from the server.
It encodes the request and then decodes the reply it
receives from the server.
On the server side, the server first creates a socket and
defines the host name and port number of the server. It
then binds the two. The server socket allows the server
to talk to multiple clients.
