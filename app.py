import tkinter as tk
import tkinter.messagebox as msg
import webbrowser
from tkinter import StringVar
from tkinter.filedialog import askdirectory

from ReadDevice import *
#
# Pyinstaller -F app.py 打包exe
#
# Pyinstaller -F -w app.py 不带控制台的打包
# Pyinstaller -F -i apple.ico app.py 不带控制台带图标的打包
#
# Pyinstaller -F -w -i apple.ico app.py 打包指定exe图标打包

def about():
    print('打开我的博客')
    webbrowser.open('https://blog.huochuankeji.com')


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Vbox移动磁盘挂载工具")
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        # 得到屏幕高度
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.master.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.creat_widgets()
        self.pack()

    def creat_widgets(self):
        # 创建一个顶级菜单

        # 加载硬盘信息按钮
        self.load = tk.Button(self, text="磁盘列表", fg="red",
                              command=self.load_devices, justify="left")
        self.quit = tk.Button(self, text="退出", fg="red",
                              command=root.destroy)

        # 加载的磁盘列表
        self.lb = tk.Listbox(self, selectmode=tk.BROWSE, width=80, height=5)
        # 绑定双击事件
        self.lb.bind("<Double-Button-1>", self.bindDoubleLoad)

        self.lb.pack()
        self.load.pack(side=tk.LEFT)
        self.quit.pack(side=tk.RIGHT)

    def bindDoubleLoad(self, event):
        """
        双击选项事件
        :return:
        """
        print(event)
        # 提取点中选项的下标
        print(self.lb.curselection())
        # 提前点中选项下标的值
        print(self.lb.get(self.lb.curselection()))
        print('选中了:' + devices[self.lb.curselection()[0]].caption)
        tip = tk.Tk()
        tip.title('提示')
        showText = '您选中了硬盘:{},是否生成虚拟硬盘'.format(devices[self.lb.curselection()[0]].caption)
        global disk_info
        disk_info = Devices(devices[self.lb.curselection()[0]].caption, devices[self.lb.curselection()[0]].deviceID,
                            devices[self.lb.curselection()[0]].partitions, devices[self.lb.curselection()[0]].size)
        tip.show = tk.Label(tip, text=showText)
        tip.yes = tk.Button(tip, text="确定", command=lambda: self.selectPath(tip=tip))
        self.lb.bind("<Double-Button-1>", self.bindDoubleLoad)

        tip.quit = tk.Button(tip, text="取消", command=tip.destroy)
        tip.show.pack()
        tip.yes.pack(side=tk.LEFT)
        tip.quit.pack(side=tk.RIGHT)

    def load_devices(self):
        """
        加载设备列表
        :return:
        """
        global devices
        devices = readDevices()
        self.lb.delete(0, self.lb.size())
        for tmp in devices:
            self.lb.insert(tk.END, '磁盘名称:{},磁盘ID:{},磁盘大小:{}'.format(tmp.caption, tmp.deviceID, tmp.size))
            print(tmp.caption, tmp.deviceID, tmp.partitions, tmp.size)

    def choose(self, cs):
        path_ = askdirectory()
        path.set(path_)
        print(path.get())
        cs.destroy()
        self.create_disk(path.get())

    def create_disk(self, param):
        tip = tk.Tk()
        tip.geometry("550x168+100+100")
        tip.title('定义磁盘名称')
        tip.lb1 = tk.Label(tip, text="已选择路径:" + param)
        tip.lb1.grid(row=0, column=0)
        tip.lb2 = tk.Label(tip, text="输入磁盘名称:")
        tip.lb2.grid(row=1, column=0)
        tip.et = tk.Entry(tip)
        tip.et.grid(row=1, column=1)
        tip.btn = tk.Button(tip, text="确定", command=lambda: self.run_create(name=tip.et.get(), tip=tip))
        tip.btn.grid(row=3, column=0)

    def run_create(self, name, tip):
        print('创建虚拟硬盘信息:硬盘名称:{},虚拟硬盘ID:{},虚拟硬盘名称:{},存储路径:{}'.format(disk_info.caption, disk_info.deviceID, name,
                                                                    path.get()))
        cmd = vbox_path + ' internalcommands createrawvmdk -filename ' + path.get() + '/' + name + '.vmdk -rawdisk ' + disk_info.deviceID

        print(cmd)
        popen = os.popen(cmd)
        read = popen.read()
        print(read)
        msg_txt = ''
        if 'successfully' in read:
            msg_txt = "操作成功,创建文件:{}".format(name + '.vmdk')
        else:
            msg_txt = "操作成失败,原因:{}".format(read)
        msg.showinfo("操作提示", msg_txt)
        tip.destroy()

    def selectPath(self, tip):
        """
        选择路径
        :return:
        """
        tip.destroy()
        cs = tk.Tk()
        cs.title('选择存放路径')
        cs.lb = tk.Label(cs, text="请选择存放路径:").grid(row=0, column=0)
        cs.bt = tk.Button(cs, text="路径选择", command=lambda: self.choose(cs=cs)).grid(row=1, column=0)
        cs.mainloop()


ww = 600
wh = 200
# 获取配置的vboxmanager路径
t = open('config', encoding='UTF-8')
vbox_path = t.readline()
root = tk.Tk()

abouts = tk.Menu(root)
abouts.add_command(label="我的博客", command=about)
root.config(menu=abouts)

devices = list()
path = StringVar()
disk_info = Devices('', '', '', '')
disk_name = StringVar()
app = Application(master=root)
app.mainloop()
