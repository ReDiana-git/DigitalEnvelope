import myRSA as rsa
import myAES as aes


def mode1(name):
    rsa.makekeys(name)
    return


def mode2(name):
    aes.encoder(name)
    return


def mode3(name):
    aes.decoder(name)
    return


name = input('請輸入你的名稱：')
while 1:
    mode = input('工作模式 1:產生金鑰 2:產生數位信封並加密文件 3:解密文件 4:退出程式')
    if mode == "1":
        mode1(name)
    elif mode == "2":
        mode2(name)
    elif mode == "3":
        mode3(name)
    elif mode == "4":
        break
    else:
        print('輸入錯誤，請重新輸入')