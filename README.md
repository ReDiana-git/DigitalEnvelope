# DigitalEnvelope

## 架設環境

### cryptography
安裝請使用
* pip install cryptography
### PyCryptodome
安裝請使用
* pip install pycryptodome<br>
(在jupyter-notebook虛擬環境下，直接安裝會無法抓到lib)
* pip install pycryptodome==3.4.3<br>
(此方式可在最新版windows解決問題，但在ubuntu 20.04 依然會有無法import的問題)

## 目錄檔位置
### input檔
input檔請放到./texts裡面，將名稱改為note.txt。

### output檔
output檔程式自動生成在./texts底下的 output.txt。

### 其他檔案
public_key、private_key、數位信封等密文，皆存放在./keys之下。

##已知問題
目前尚未實作檔案檢測，請在有金鑰的情況下才進行加密。