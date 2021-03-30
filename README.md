<!--
 * @Author: yuanxx
 * @Date: 2021-03-30 09:55:19
 * @LastEditTime: 2021-03-30 09:59:52
 * @Description: 
-->
### VBOX 磁盘挂载工具

> [github 地址](https://github.com/yxx1912008/vbox_disk)

> [我的博客](https://blog.huochuankeji.com)

#### 简介

       平常开发经常要用到VBOX虚拟机,特殊场景下需要使用U盘启动或者挂载移动硬盘启动等。但是vbox挂载硬盘的时候操作起来比较麻烦。因此产生了开发这个工具的念头.
       本来想用javafx开发一个GUI程序，但是因为本来就是一个小工具,并且编译成exe文件的时候Java的包大小不占优势,而且还需要PC安装JRE.因此选用了:Python + Tkinter +Pyinstaller


#### 使用截图

<img src="1.jpg" style="width: 50%; height: 50%"  alt="软件图标" />
<img src="2.jpg" style="width: 50%; height: 50%"  alt="启动界面" />
<img src="3.jpg" style="width: 50%; height: 50%"  alt="加载硬盘列表" />
<img src="4.jpg" style="width: 50%; height: 50%"  alt="选择存放路径" />
<img src="5.jpg" style="width: 50%; height: 50%"  alt="选择存放路径" />
<img src="6.jpg" style="width: 50%; height: 50%"  alt="选择磁盘名称" />
<img src="7.jpg" style="width: 50%; height: 50%"  alt="操作结果" />

#### 当前环境与依赖

```
1.Python 3.8.3
2.pyinstaller 4.2
```


#### 目录结构


```
autousb
├─ app.py #程序入口
├─ apple.ico # 程序图标
├─ config #配置vbox 地址
├─ Devices.py #设备信息 model
└─ ReadDevice.py #读取设备信息工具

```



#### 使用教程

0.使用文本编辑器修改config文件里的路径修改为当前安装的vboxmanager地址 
<img src="config.jpg" style="width: 50%; height: 50%"  alt="软件图标" />

1.以管理员身份运行
<img src="0.jpg" style="width: 50%; height: 50%"  alt="软件图标" />

2.点击磁盘列表 加载系统磁盘
<img src="2.jpg" style="width: 50%; height: 50%"  alt="加载硬盘列表" />

3.选择存放路径
4.选择磁盘名称