import sys
import socket
import itertools
import string

ip = sys.argv[1]
port = int(sys.argv[2])
abc = string.ascii_lowercase + string.digits

def password():
    for n in range(len(abc)):
        for i in itertools.product(abc, repeat=n+1):
            yield "".join(i)

ip = sys.argv[1]
port = int(sys.argv[2])
address = (ip, port)

with socket.socket() as st:
    st.connect(address)
    generator = password()
    while True:
        pw = next(generator)
        st.send(pw.encode())
        response = st.recv(1024).decode()
        if response == "Connection success!":
            print(pw)
            break

