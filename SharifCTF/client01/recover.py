with open('file','rb') as f1:
    with open('decoded_file.png','wb') as f2:
        b = f1.read(1)
        f2.write(b)
        f2.write('\x50')
        while True:
            b=f1.read(1)
            if b:
                f2.write(b)
            else: break
