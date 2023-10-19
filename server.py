import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# المفتاح المشترك (يجب مشاركته مع العميل بأمان)
shared_key = b'ThisIsASharedKey'

# إعداد الخادم
host = '127.0.0.1'
port = 12346

# إنشاء مولد عشوائي لل IV (Initialization Vector)
iv = get_random_bytes(16)

# إعداد المشفر باستخدام مفتاح المشترك و IV
cipher = AES.new(shared_key, AES.MODE_CFB, iv)

# انشاء السيرفر
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"server listining {host}:{port}")
    conn, addr = server_socket.accept()

    with conn:
        print(f"{addr}")

        # الرسالة المراد إرسالها
        message = "This is a secret message."

        # تشفير الرسالة
        ciphertext = iv + cipher.encrypt(message.encode('utf-8'))

        # إرسال الرسالة المشفرة إلى العميل
        conn.sendall(ciphertext)
