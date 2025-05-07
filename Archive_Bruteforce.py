import py7zr
import zipfile
import rarfile

def Seven_Zip(file):
    rockyou = open('/home/venom/CreateWordlist/rockyou.txt')
    for i in rockyou:
        i = i.strip('\n')
        with py7zr.SevenZipFile(file,mode='r',password=i) as z7:
            try:
                z7.extractall()
                print('[+]Password Found :',i,'Correct!!')
                break
            except:
                pass
def Zip_file(file):
    rockyou = open('/home/venom/CreateWordlist/rockyou.txt')
    for i in rockyou:
        i = i.strip('\n')
        zFile = zipfile.ZipFile(file)
        try:
            zFile.extractall(pwd=i.encode('utf8'))
            print('[+]Password Found :',i,'Correct!!')
            break
        except:
            pass
def Rar_file(file):
    rockyou = open('/home/venom/CreateWordlist/rockyou.txt')
    for i in rockyou:
        i = i.strip('\n')
        rarF = rarfile.RarFile(file)
        try:
            rarF.extractall(pwd=i.encode('utf8'))
            print('[+]Password Found :',i,'Correct!!')
            break
        except:
            pass
def main():
    file = input("Nama File : ")
    if ".rar" in file and file[-4:] == '.rar':
        print("File is Archive RAR")
        Rar_file(file)
    elif ".zip" in file and file[-4:] == '.zip':
        print("File is Archive ZIP")
        Zip_file(file)
    elif ".7z" in file and file[-3:] == '.7z':
        print("File is Archive 7Zip")
        Seven_Zip(file)
    else:
        print("File not allowing")
    

if __name__ == '__main__':
    main()
