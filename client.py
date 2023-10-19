import socket
from Crypto.Cipher import AES


shared_key = b'ThisIsASharedKey'


host = '127.0.0.1'
port = 12346

# انشاء العميل
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))

    # استقبال الرسالة المشفرة من الخادم
    received_data = client_socket.recv(1024)

    iv = received_data[:16]

   
    ciphertext = received_data[16:]

    # إعداد المشفر باستخدام المفتاح المشترك و IV
    cipher = AES.new(shared_key, AES.MODE_CFB, iv)

    # فك تشفير الرسالة
    decrypted_message = cipher.decrypt(ciphertext).decode('utf-8')

    print("this message:", decrypted_message)