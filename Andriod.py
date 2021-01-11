import os
import time
import zipfile
import shutil

def get_pic():
    num = input('''    请输入想要的截图数:''')
    num = int(num)+2
    picture = os.popen('adb shell "ls /sdcard/DCIM/Screenshots"')
    text = picture.read()
    pic_list = text.split('\n')

    
    for i in range(2,num):
        i = -int(i)
        pic_name = pic_list[i]
        print(pic_name)
        os.system("adb pull /sdcard/DCIM/Screenshots/"+pic_name)

def pull_log(mode):
    if os.path.exists('./Log'):
        shutil.rmtree('./Log')
    if os.path.exists('./Log.zip'):
        os.remove('./Log.zip')
    os.system('adb pull /sdcard/Android/data/'+mode+'/files/Log' )
    
def zip_log():
    zip_filename='Log.zip'
    dir_name = './Log'
    if os.path.exists(dir_name):
        with zipfile.ZipFile(zip_filename, 'w',compression=zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(dir_name):
                for single_file in files:
                    if single_file != zip_filename:
                        filepath = os.path.join(root, single_file)
                        z.write(filepath)
            z.close()
           
        
        print("压缩成功")
    else:
        print('未拉取到日志')
def get_log():
    pack = input('''        =============================\n
         1.row主干\n
         2.row分支\n
         3.CN\n
         4.线上（pub、pre）\n
         请输入你要拉取日志的对应数字回车键确认(无需删除之前的文件会自动删除)\n
         
         =============================\n    
         日志：''')
    if pack == '1':
        mode = 'com.riotgames.internal.wildrift.trunk'
    elif pack == '2':
        mode = 'com.riotgames.internal.wildrift.test'
    elif pack == '3':
        mode = 'com.tencent.lolm'
    elif pack == '4':
        mode = 'com.riotgames.league.wildrift'
    pull_log(mode)
    zip_log()
    
if __name__ == '__main__':
    
    a = input('''        =========================\n
        1.提取照片\n
        2.提取日志\n
        =========================\n
        请输入数字：''')
    if a == '1':
        get_pic()
    elif a == '2':
        get_log()
    
    input("点击任意按键退出")