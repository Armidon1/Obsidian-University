# 🐍 Python Socket Documentation
### Index

1. **Introduction & Basics** (Creation, TCP/UDP)
    
2. **Advanced Performance** (Selectors/Non-blocking)
    
3. **Security** (SSL/TLS)
    
4. **Addressing** (IPv4, IPv6, Unix, Bluetooth)
    
5. **Reliability** (Error Handling & Shutdowns)
    

## 1. Introduction to Sockets

A **socket** is an endpoint in a communication channel. Sockets allow two programs to communicate, either on the same machine or over a network. Python provides access to the BSD socket interface via the built-in `socket` module.

To use it, you must first import the module:

Python

```
import socket
```

## 2. Creating a Socket

The primary method to create a socket is the `socket()` constructor.

Python

```
s = socket.socket(socket_family, socket_type, protocol=0)
```

### Key Parameters:

1. **Address Family (`socket_family`):** Determines the network layer protocol.
    
    - `socket.AF_INET`: IPv4 (The most common).
        
    - `socket.AF_INET6`: IPv6.
        
    - `socket.AF_UNIX`: Local inter-process communication (Unix only).
        
2. **Socket Type (`socket_type`):** Determines the transport layer protocol.
    
    - `socket.SOCK_STREAM`: **TCP** (Reliable, connection-oriented).
        
    - `socket.SOCK_DGRAM`: **UDP** (Unreliable, connectionless).
        

---

## 3. TCP Sockets (Connection-Oriented)

TCP is used when you need reliable data delivery (e.g., HTTP, SSH). It requires a "handshake" to establish a connection.

### A. Server-Side Methods

A server waits for a client to connect.

| **Method**           | **Description**                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `bind((host, port))` | Associates the socket with a specific network interface and port number.                                          |
| `listen(backlog)`    | Enables the server to accept connections. `backlog` is the number of unaccepted connections allowed in the queue. |
| `accept()`           | Blocks execution and waits for a connection. Returns a new socket object (for the client) and the address.        |
| `close()`            | Closes the socket connection.                                                                                     |

### B. Client-Side Methods

A client initiates the connection.

|**Method**|**Description**|
|---|---|
|`connect((host, port))`|Connects to a remote server.|

### C. Data Transfer (Both)

|**Method**|**Description**|
|---|---|
|`send(bytes)`|Sends data. Returns the number of bytes sent. **Note:** Does not guarantee all data is sent at once.|
|`sendall(bytes)`|Repeatedly calls `send()` until all data is sent. (Recommended).|
|`recv(bufsize)`|Receives data. `bufsize` is the max amount of data to read at once (e.g., 1024 or 4096 bytes).|

### Example: Simple TCP Server & Client

**Server Code (`server.py`):**

```Python
import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Non-privileged port

# Using 'with' automatically closes the socket at the end
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    
    conn, addr = s.accept() # Blocks until a client connects
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Echo the data back to client
            conn.sendall(data) 
```

In particular, what s.accept returns? A tuple of 2 values, which is stored properly inside [[Sockets in Python#What is conn after calling s.accept()?|conn]] and [[Sockets in Python#What is addr after calling s.accept()?|addr]]. See the links to understand better what are those values. 
What does  [[Sockets in Python##What does s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)|s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)]]?

**Client Code (`client.py`):**

```Python
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, World!') # Note the b'' for bytes
    data = s.recv(1024)

print(f"Received: {data.decode('utf-8')}")
```

---

## 4. UDP Sockets (Connectionless)

UDP is used when speed is prioritized over reliability (e.g., Video streaming, Gaming). There is no `listen()`, `accept()`, or `connect()`.

|**Method**|**Description**|
|---|---|
|`sendto(bytes, address)`|Sends data to a specific target address `(ip, port)`.|
|`recvfrom(bufsize)`|Receives data and the address of the sender. Returns `(data, address)`.|

### Example: Simple UDP Interaction

```Python
# UDP Server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
data, addr = s.recvfrom(1024) # Wait for a packet
print(f"Message from {addr}: {data}")

# UDP Client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"Hello UDP", ('127.0.0.1', 9999))
```

---

## 5. Advanced Concepts

### Blocking vs. Non-Blocking

- **Blocking (Default):** Functions like `accept()` or `recv()` stop the program until an event occurs.
    
- **Non-Blocking:** The function returns immediately. If no data is available, it raises a `BlockingIOError`. You can set this via `s.setblocking(False)`.
    

### Handling Multiple Connections

Real-world servers handle many clients simultaneously. You generally use one of two approaches:

1. **Threading:** Create a new thread for every client `accept()`ed.
    
2. **Selectors (I/O Multiplexing):** The modern, efficient way. It monitors multiple sockets and triggers events only when a socket is "readable" or "writable."
    

```Python
import selectors
sel = selectors.DefaultSelector()
# This allows a single thread to manage many connections efficiently
```

---
Here is the **Advanced Chapter** for your documentation regarding the `selectors` module.

This approach is much more efficient than threading because it allows a **single thread** to monitor many sockets. It waits for "events" (like "ready to read" or "ready to write") rather than pausing execution while waiting for a specific client.

### Documentation: Handling Multiple Clients with Selectors

To implement this, we use the `selectors` module (High-level I/O multiplexing).

**The Logic Flow:**

1. **Register** the main listening socket to watch for **READ** events (incoming connections).
    
2. **Loop** forever calling `sel.select()`. This blocks until _something_ happens.
    
3. If the event is on the **listening socket**, we `accept()` the new client.
    
4. If the event is on a **client socket**, we `recv()` or `send()` data.
    

#### The Server Code (`multi_server.py`)

```Python
import socket
import selectors
import types

# 1. Create the Default Selector
sel = selectors.DefaultSelector()

HOST = '127.0.0.1'
PORT = 65432

def accept_wrapper(sock):
    """Callback for new connections"""
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    
    # CRITICAL: Set to non-blocking mode
    conn.setblocking(False)
    
    # Create an object to hold data for this specific connection
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    
    # Register the socket to be monitored for READING (receiving data)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    """Callback for existing connections"""
    sock = key.fileobj
    data = key.data
    
    # 1. Handle Reads
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data # Add to output buffer (echo)
        else:
            # Empty bytes means the client closed the connection
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    
    # 2. Handle Writes
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb} to {data.addr}")
            sent = sock.send(data.outb)  # Send data
            data.outb = data.outb[sent:] # Remove sent bytes from buffer

# Main Setup
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print(f"Listening on {HOST}:{PORT}")
lsock.setblocking(False)

# Register the listening socket (Only interested in READ events initially)
sel.register(lsock, selectors.EVENT_READ, data=None)

# The Event Loop
try:
    while True:
        # Blocks until one or more sockets are ready
        events = sel.select(timeout=None)
        
        for key, mask in events:
            if key.data is None:
                # If data is None, it's our listening socket (per line 57)
                accept_wrapper(key.fileobj)
            else:
                # It's an existing client socket
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
```

### Testing the Code

To see this work, you don't need a complex client script. You can simply open **two or three separate terminal windows** and run the basic client code we wrote in the previous section in each window simultaneously.

The server will handle all of them at the same time without "pausing" for one to finish.

---

### Key Takeaways for your Documentation

- **`conn.setblocking(False)`**: This is mandatory for selectors. If you forget this, one slow client can freeze the whole server.
    
- **`types.SimpleNamespace`**: A handy class to attach custom data (like buffers) to a specific socket.
    
- **`sel.select()`**: The heart of the program. It asks the OS: _"Wake me up when one of these sockets is ready to do something."_
    

This covers the "hard part" of Python sockets!

---
## 🧵 Multithreaded Server Implementation

This is the classic approach to network programming. It is easier to reason about than `selectors` because you can write standard **blocking** code (the code stops and waits for data), but the server remains responsive because that waiting happens in a separate thread.

#### The Architecture

1. **Main Thread:** Sits in an infinite loop. Its **only** job is to wait for `server.accept()`.
    
2. **Worker Threads:** Whenever a new client connects, the main thread creates a new thread, hands over the specific **client socket** to it, and immediately goes back to listening.
    

![Immagine di multithreaded server architecture](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRjMZ18Vz8oAYvi5AGhrRaWc5uAGjWVSEwjIodYALYgFPdLBquiziXa8A5fIGkaZ6iEuT8uEiMlRYuRegCXqk0IuFcI_g0tquC1q14FLbuL9m6_cHA)

#### The Python Code

We use the standard `threading` module.

```Python
import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    """
    This function runs inside a separate thread.
    It handles the conversation for a SINGLE client.
    """
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        try:
            # This is a BLOCKING call, but it only blocks THIS thread.
            # The main server loop is free to accept other people.
            msg = conn.recv(1024)
            
            if not msg:
                # Empty bytes means the client disconnected
                break
            
            print(f"[{addr}] {msg.decode('utf-8')}")
            conn.sendall(b"Message received")
            
        except ConnectionResetError:
            break
            
    conn.close()
    print(f"[DISCONNECT] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    
    while True:
        # 1. The main thread blocks here waiting for a new connection
        conn, addr = server.accept()
        
        # 2. Create a new thread object
        # target = the function to run
        # args = a tuple of arguments to pass to that function
        thread = threading.Thread(target=handle_client, args=(conn,addr),
													     daemon=True)
        
        # 3. Start the thread (executes handle_client in background)
        thread.start()
        
        # 4. Optional: Print active connections (minus main thread)
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
```

### 🔍 Key Implementation Details for your Documentation

1. Arguments (args)

Notice args=(conn, addr). When you spin up a thread, you must pass the specific socket object returned by accept(). If you used the global server socket inside the thread, everything would break.

2. Daemon Threads (Optional)

You can set thread.daemon = True before starting it.

- **True:** If you kill the main server program (CTRL+C), all client threads die immediately.
    
- **False (Default):** The program will hang until every single client disconnects, even if the main server has stopped.
    

### ⚖️ Threading vs. Selectors (The CS Perspective)

Since you are studying Cybersecurity/CS, you should document the trade-off:

|**Feature**|**Threading**|**Selectors (Non-blocking)**|
|---|---|---|
|**Complexity**|Low. Logic is linear and easy to read.|High. Requires state management and callbacks.|
|**Memory Usage**|**High.** Each thread requires its own stack memory (approx 8MB default on some OS).|**Low.** Only one thread manages everything.|
|**Context Switching**|High CPU overhead switching between threads.|Very low overhead.|
|**Scalability**|Good for < 1,000 clients. Struggles at 10k+.|Excellent. Can handle C10k (10,000 connections).|

**Recommendation:** Use **Threading** for simple protocols or file transfer servers where logic is complex. Use **Selectors** (or `asyncio`) for chat servers or high-concurrency APIs.

---

## 6. Best Practices Checklist

1. **Always send Bytes:** Sockets transmit bytes, not strings. Use `.encode('utf-8')` to send and `.decode('utf-8')` to read strings.
    
2. **Use Context Managers:** Use the `with` statement so sockets close automatically, preventing resource leaks.
    
3. **Handle Partial Sends:** In TCP, `send()` might not send the whole message. Use `sendall()` to be safe.
    
4. **Handle Buffering:** TCP is a stream. `recv(1024)` might receive half a message or two messages stuck together. You must implement a protocol (like message headers) to know where a message ends.
    
5. **Address Reuse:** When restarting a server, you might get an "Address already in use" error. Use this option to fix it:
    
    ```Python
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ```
    

---

Here is the final major section for your documentation. This is critical because standard sockets send data in **plaintext** (readable by anyone intercepting the network). To secure it, we wrap the socket in **SSL/TLS**.

## 7. Security: Implementing SSL/TLS

Standard sockets are insecure. To encrypt the data, Python uses the `ssl` module to wrap a standard TCP socket. This functions similarly to HTTPS on the web.

### Prerequisites: Certificates

To use [[SSL]], the server needs a Certificate and a Private Key.

For testing purposes, you can generate a self-signed certificate using OpenSSL in your terminal:

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

- `key.pem`: Your private key (Keep secret).
    
- `cert.pem`: Your public certificate (Shared with client).
    

---

### The `SSLContext`

Modern Python uses the `ssl.SSLContext` object to configure security settings (protocol versions, certificates, etc.) before wrapping the socket.

![Immagine di TLS handshake diagram](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTT_Cm4KywZ-nqKHmF0zQq6SrnDIyK5H2nwZ9NwF-rXZsBXuE5EcsjiaI2tawfgQGcnDZHGbxIK9_a7-reqQKnjyhHyDdUJdR7fIcBlE6yphJaG5f4)

### A. Secure Server Code

The server must load its certificate and private key to prove its identity.

```Python
import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443 # Common port for secure traffic

# 1. Create the SSL Context
# Purpose.CLIENT_AUTH means we are a server authenticating clients (standard)
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

# 2. Load the Server's Certificate and Private Key
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

# 3. Create the standard TCP Socket
bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bindsocket.bind((HOST, PORT))
bindsocket.listen(5)
print(f"Secure server listening on {HOST}:{PORT}")

while True:
    newsocket, fromaddr = bindsocket.accept()
    
    # 4. Wrap the socket with SSL
    # server_side=True is critical here
    try:
        conn = context.wrap_socket(newsocket, server_side=True)
        print(f"SSL connection established from: {fromaddr}")
        
        data = conn.recv(1024)
        print(f"Received encrypted data: {data}")
        conn.sendall(b"Secure Hello!")
        
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    finally:
        # Closing the wrapper closes the underlying socket
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
```

### B. Secure Client Code

The client must verify the server's certificate.

**Note:** If using a self-signed certificate (like in this example), the client will reject it by default because it's not from a trusted authority (like Google or DigiCert). We must explicitly tell the client to trust our `cert.pem` or disable verification (for testing only).

```Python
import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

# 1. Create SSL Context
context = ssl.create_default_context()

# OPTION A: For Real Production (Verify the cert)
# context.load_verify_locations('cert.pem') # Trust this specific cert

# OPTION B: For Local Testing (Disable verification - UNSAFE)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# 2. Connect
# We create a standard socket...
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ...and immediately wrap it
# server_hostname is required for SNI (Server Name Indication)
ssl_sock = context.wrap_socket(s, server_hostname=HOST)

ssl_sock.connect((HOST, PORT))

ssl_sock.sendall(b"This message is encrypted!")
data = ssl_sock.recv(1024)
print(f"Received: {data.decode('utf-8')}")

ssl_sock.close()
```

---

### Key Concepts for Documentation

|**Concept**|**Description**|
|---|---|
|**`ssl.wrap_socket`**|The function that takes a plain socket and returns an encrypted SSLSocket.|
|**Handshake**|The process where client and server swap keys and agree on encryption methods. This happens automatically during the `wrap_socket` (server) or `connect` (client) phase.|
|**PEM File**|The standard file format for storing keys and certificates.|
|**SNI (Server Name Indication)**|An extension that allows the client to tell the server which hostname it is trying to connect to (handled by `server_hostname`).|


--- 
Here is the **Address Families & Formatting** section for your documentation. This explains exactly what arguments you pass to `bind()` or `connect()` depending on the socket family.

## 8. Address Families: Hosts and Ports

The arguments you pass to socket methods depend entirely on the **Address Family** (`socket.AF_*`) you chose when creating the socket.

### A. socket.AF_INET (IPv4)

This is the most common standard for the internet. It expects a **tuple** of two items: `(host, port)`.

|**Host Parameter**|**Description**|**Use Case**|
|---|---|---|
|`'127.0.0.1'`|**Loopback Address.** The socket is only accessible from the _same_ computer.|Local testing, internal IPC.|
|`'localhost'`|Same as above (resolves to 127.0.0.1).|Readable local testing.|
|`'0.0.0.0'` (Server)|**INADDR_ANY.** Binds to **all** available network interfaces (Wi-Fi, Ethernet, etc.).|Production servers accessible by others.|
|`''` (Empty String)|Same as `'0.0.0.0'`.|Shortcut for binding to all interfaces.|
|`'192.168.1.x'`|**Private IP.** Binds to a specific network card (e.g., only your Wi-Fi card, not Ethernet).|Restricting access to a specific LAN.|
|`'8.8.8.8'`|**Public IP.** Connects to a specific remote server.|Client connecting to the internet.|
|`'google.com'`|**Hostname.** Python will perform a DNS lookup to find the IP automatically.|Client connecting to a website.|

**The Port Parameter:**

- **Type:** Integer (0–65535).
    
- **0:** Tells the OS to assign an available random port (useful for ephemeral clients).
    
- **1–1023:** "Privileged ports" (requires Administrator/Root access).
    
- **1024–65535:** User ports (safe for your Python scripts).
    

**Example:**

```Python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080)) # Tuple (Host, Port)
```

---

### B. `socket.AF_INET6` (IPv6)

The modern internet standard. It expects a tuple of four items: (host, port, flowinfo, scopeid).

Note: You can usually just provide the first two (host, port) and omit the rest.

|**Host Parameter**|**Description**|
|---|---|
|`'::1'`|**Loopback.** Equivalent to `127.0.0.1`.|
|`'::'`|**INADDR_ANY.** Equivalent to `0.0.0.0` (Listen on all interfaces).|

**Example:**

```Python
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# Connect to localhost IPv6 on port 8080
s.connect(('::1', 8080, 0, 0)) 
```

---

### C. `socket.AF_UNIX` (Unix Domain Sockets)

Used for **Inter-Process Communication (IPC)** on the _same machine_. This is faster than TCP/IP because it avoids the network stack overhead. It is standard on Linux/macOS and available on Windows 10/11 (newer builds).

**The "Host" and "Port":**

- **No Port:** Unix sockets do not use ports.
    
- **Address:** The address is a **file system path** (string).
    

|**Address Parameter**|**Description**|**OS Support**|
|---|---|---|
|`'/tmp/mysocket'`|**File Path.** Creates a physical file on the disk to act as the socket.|Linux, macOS, Windows.|
|`'\0abstract'`|**Abstract Namespace.** Starts with a null byte. Does not create a file on disk. Auto-cleaned when closed.|Linux Only.|

**Example:**

```Python
import os
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Standard File Path
socket_path = '/tmp/demo_socket'

# Ensure the file doesn't already exist before binding
if os.path.exists(socket_path):
    os.remove(socket_path)

s.bind(socket_path)
```

---

### D. `socket.AF_BLUETOOTH` (Bluetooth)

Python can even handle Bluetooth Low Energy or standard Bluetooth (RFCOMM).

- **Protocol:** Usually `socket.BTPROTO_RFCOMM`.
    
- **Address:** A tuple of `(mac_address, channel)`.
    

**Example:**

```Python
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
# Target Bluetooth MAC address and channel 1
s.connect(('00:11:22:33:44:55', 1))
```

---

### Summary Table for Documentation

|**Family**|**Address Format**|**Example**|
|---|---|---|
|**`AF_INET`**|`(host, port)`|`('192.168.1.5', 80)`|
|**`AF_INET6`**|`(host, port, flow, scope)`|`('::1', 8080, 0, 0)`|
|**`AF_UNIX`**|`path` (string)|`'/tmp/mysoc'`|
|**`AF_BLUETOOTH`**|`(mac, channel)`|`('00:11:22:33:44:55', 1)`|

This covers the "How" and "Where" of connecting sockets.

---

Network programming is inherently fragile. Cables get unplugged, servers crash, and Wi-Fi drops. A robust application must handle these failures gracefully without crashing.

## 9. Error Handling & Exceptions

In Python 3.3+, most socket errors raise **`OSError`** or its subclasses.

### A. Common Exceptions

You should wrap your socket calls in `try...except` blocks to catch these specific issues.

|**Exception Class**|**Description**|**Cause**|
|---|---|---|
|**`ConnectionRefusedError`**|Connection failed.|The server is not running, or the port is wrong.|
|**`TimeoutError`**|The operation took too long.|Network congestion, firewall blocking, or server is hanging.|
|**`AddressInUseError`** (errno 98/48)|Could not bind to port.|The server crashed but didn't release the port, or another program is using it.|
|**`BrokenPipeError`**|Error writing to socket.|You tried to `send()` data, but the other side has already closed the connection.|
|**`ConnectionResetError`**|Connection forcibly closed.|The remote peer crashed or hard-closed the connection while you were waiting to read.|

### B. Handling "Address Already in Use"

This is the most common error during development (OSError: [Errno 98] Address already in use).

If you restart your server script quickly, the OS might keep the port "reserved" for a timeout period (TIME_WAIT state).

**The Fix:** Set the `SO_REUSEADDR` option _before_ binding.

```Python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Level: SOL_SOCKET, Option: SO_REUSEADDR, Value: 1 (True)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
```

### C. Timeouts

By default, socket operations are **blocking** (they wait forever). If a packet gets lost, your program freezes. You should always set a timeout.

```Python
s.settimeout(5.0) # Raise socket.timeout if no response after 5 seconds

try:
    data = s.recv(1024)
except socket.timeout:
    print("The server is taking too long to respond!")
except OSError as e:
    print(f"Network error: {e}")
```

---

## 10. Graceful Shutdown

Simply calling `.close()` immediately kills the socket. Data still in the network buffer might be lost.

![Immagine di TCP connection termination](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcRn2Q5x9dD6aFe8w4pmR-ViiRupfKkwnJmPawIb1JSFRPZmUgTt8S62E6iY46F9CJ9mU0s1XPgKRXl6liU_a8jiyYn0N0SrN-7uoqBTpmiI1INV6kM)

Getty Images

The correct way to end a conversation is the **Shutdown-then-Close** dance:

1. **`s.shutdown(how)`**: Tells the other side "I am done sending/receiving," but keeps the channel open just long enough to flush buffers.
    
    - `socket.SHUT_RD`: "I will stop reading."
        
    - `socket.SHUT_WR`: "I will stop writing" (sends a FIN packet).
        
    - `socket.SHUT_RDWR`: "I stop both."
        
2. **`s.close()`**: Releases the OS resource.
    

**Example:**

```Python
def graceful_exit(sock):
    try:
        # Tell the other side we are done writing
        sock.shutdown(socket.SHUT_RDWR)
    except OSError:
        # Socket might already be closed/broken, ignore
        pass
    finally:
        sock.close()
```

---

# EXTRA STUFF
## What is addr after calling s.accept()?

###  `addr` is the "Caller ID"

If `conn` is the open phone line, `addr` is the **Caller ID** on your screen. It tells you **who** is calling before (or while) you talk to them.

Technically, addr is a tuple containing: (Client_IP_Address, Client_Port_Number).

Example: ('203.0.113.45', 54321)

Here are the three main ways you use it in real-world scripts:

### 1. Logging and Auditing

This is the most common use. You need to record who visited your server for debugging or security analysis.

```Python
conn, addr = server.accept()
# addr[0] is the IP string
# addr[1] is the Port integer
print(f"New connection from IP: {addr[0]} on Port: {addr[1]}")
```

### 2. Authentication (Allow/Deny Lists)

Since you are studying **Cybersecurity**, this is critical. You can check `addr` immediately after acceptance to decide if you want to talk to them or hang up instantly.

```Python
conn, addr = server.accept()
client_ip = addr[0]

trusted_ips = ['192.168.1.50', '127.0.0.1']

if client_ip not in trusted_ips:
    print(f"ALARM: Unauthorized connection attempt from {client_ip}")
    conn.close() # Hang up immediately
else:
    print("Authorized user connected.")
    # Proceed to handle_client...
```

### 3. Rate Limiting (Anti-DDoS)

You can use `addr` to track how many times a specific IP has connected in the last minute. If `addr[0]` connects 100 times in 1 second, your script can add them to a "blocklist."

---

### ⚠️ A Note on the Port (`addr[1]`)

You might wonder: _"Why do I care about the client's port (e.g., 54321)?"_

Usually, you don't.

- Your server is on a fixed port (e.g., 80).
    
- The client's OS picks a random, temporary port (called an **Ephemeral Port**) to verify that the return traffic comes back to the right browser tab.
    
- You mostly ignore `addr[1]`, but it is useful in logs to distinguish between two different connections coming from the exact same computer (same IP, different ephemeral ports).
    

## What is conn after calling s.accept()?

### `conn`: The Connected Socket Object

While `addr` is just information (a tuple), `conn` is the actual **tool** used to communicate. It is a full-fledged socket object created specifically for **one** specific client session.

#### 1. Definition

- **What it is:** A new socket object returned by `server.accept()`.
    
- **Purpose:** It acts as the dedicated "pipe" or "channel" between your server and **that specific client**.
    
- **Lifespan:** It exists only as long as the conversation with that client lasts. Once the conversation is over, `conn` is closed and destroyed.
    

#### 2. The Golden Rule

> **The Server Socket (`server`) listens, but the Connection Socket (`conn`) talks.**

You must **never** try to send data using the main `server` socket. You only send data through `conn`.

#### 3. Key Methods Used on `conn`

|**Method**|**Description**|
|---|---|
|**`conn.recv(bufsize)`**|**Receive Data.** Reads bytes sent by the client. The code usually blocks (waits) here until data arrives.|
|**`conn.sendall(bytes)`**|**Send Data.** Pushes bytes back to this specific client. (Use this instead of `send()` to ensure the whole message goes through).|
|**`conn.close()`**|**Hang Up.** Closes the connection with this client, freeing up the port for them.|
|**`conn.settimeout(seconds)`**|**Safety.** Sets a timer. If the client doesn't send data within X seconds, `recv()` raises an error so your server doesn't freeze.|
|**`conn.getpeername()`**|**Info.** Returns the address of the remote client (essentially returns `addr` again).|

#### 4. Security Context (SSL/TLS)

If you are implementing encryption (as discussed in previous notes), `conn` is the object that gets "wrapped."

- The `server` socket stays plain TCP.
    
- The `conn` socket is handed to `context.wrap_socket(conn, ...)` to magically transform it into an encrypted channel.
    

#### 5. Code Example: Life of a `conn`

```Python
# 1. conn is born here
conn, addr = server.accept() 

with conn: # 'with' ensures conn.close() happens automatically at the end
    print(f"Connected to {addr}")
    
    # 2. conn works here
    data = conn.recv(1024) 
    conn.sendall(b"I received your message")

# 3. conn dies here (Automatic close)
```

## What does s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)?
**Is it indispensable?**
- The short answer is: **Technically no, but practically it is indispensable.**
- If you remove that line, your server will work perfectly the **first time** you run it.

However, the problem arises when you **stop** the server (e.g., using CTRL+C) and try to restart it immediately. Without that line, you will almost certainly get this error:

> `OSError: [Errno 98] Address already in use`

You would have to wait 60 to 120 seconds before you can restart the server.

---

### 🕵️‍♂️ Why does this happen? (Cybersecurity Context)

This happens because of how the **TCP** protocol is designed.

When you close a TCP connection (sending the `FIN` packet), the port is not released immediately. It enters a "phantom" state called **TIME_WAIT**.

1. **The Purpose:** The Operating System keeps the port "reserved" for a short while (usually 2 minutes) to ensure that any delayed packets traveling in the network have arrived or expired.
    
2. **The Problem:** During this time, the OS prevents any new application from **binding** to that same port to avoid confusion between old packets and new ones.
    

### 🛠 What does that line do?

```Python
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

You are literally telling the Operating System:

"I know this port is in the TIME_WAIT state and looks busy, but let me reuse it immediately anyway."

- `SOL_SOCKET`: Indicates the option is at the general socket level.
    
- `SO_REUSEADDR`: The specific flag ("Reuse Address").
    
- `1`: Stands for `True` (enable the option).
    

### ✅ Conclusion for your documentation

Include it **always** in your development and production servers. Without it, debugging becomes a nightmare because you have to wait minutes between every test run.