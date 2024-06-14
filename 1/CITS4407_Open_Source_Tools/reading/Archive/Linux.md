# 一、一些基础知识

上世纪70年代美国贝尔实验室：晶体管、太阳能电池、通信卫星、有声电影...



## **网络连接的三种模式**

**1.桥接**

![image-20211119173220818](Linux.assets\image-20211119173220818.png)

**2.NAT**

![image-20211119174407959](Linux.assets\image-20211119174407959.png)

**3.主机模式**

独立的系统，和外界没有关系



## 虚拟机快照

> 如果在使用虚拟机系统时，想要回到原先的某一个状态，也就是说担心可能有些误操作造成系统异常，需要回到原先某个正常运行状态，vmware提供这样的功能，就叫**快照管理**



## vmtools

> 可以在windows和centos共享文件夹

安装步骤：

1. 进入centos

2. 弹出，在“虚拟机”选项卡中点击“重新安装VMware Tools”（如果是灰色则关闭vmware重新进入，并在虚拟机开机后，还没有开机完成前点击）

   ![image-20211119191235751](Linux.assets\image-20211119191235751.png)

3. 进入VMware Tools得到一个安装包![image-20211119191518447](Linux.assets\image-20211119191518447.png)

4. 拷贝到/opt

   ![image-20211119191828340](Linux.assets\image-20211119191828340.png)

5. 使用解压命令tar，得到一个安装文件

   ![image-20211119192005373](Linux.assets\image-20211119192005373.png)

6. 进入该vm解压的目录，/opt目录下

   ![image-20211119192103648](Linux.assets\image-20211119192103648.png)

7. 安装./vmware-install.pl

   ![image-20211119192234414](Linux.assets\image-20211119192234414.png)

8. 全部使用默认设置即可(一直回车)，即安装成功

9. 注意：安装vmtools需要有<font color="red">gcc</font>（在安装centos的时候选项会选择安gcc，在终端输入gcc -v可以检验有无gcc）



**设置共享文件夹**

![image-20211119192744946](Linux.assets\image-20211119192744946.png)

在mnt目录下即可找到

![image-20211119193046711](Linux.assets\image-20211119193046711.png)

![image-20211119193126657](Linux.assets\image-20211119193126657.png)





# 二、基本操作



## 指定运行级别

> init 数字0-6

运行级别说明：

0. 关机
1. 单用户（找回丢失密码）
2. 多用户状态没有网络服务
3. 多用户状态有网络服务
4. 系统未使用保留给哟洪湖
5. 图形界面
6. 系统重启

常用的运行级别是3和5

例：切换到无界面模式

~~~
init 3
~~~



## 图形界面和控制台的切换

Ctrl+Alt+F1 图形界面

Ctrl+Alt+F2 命令行界面

从F2到F6可以在多个控制台之间切换



## 找回root密码

1. 在开机的时候进入这个界面按e（要快一点，不然5s后就闪过去了）

   ![image-20211120101213283](Linux.assets\image-20211120101213283.png)

2. 向下移动到”Linux16“开头那一行的末尾，加上init=/bin/sh

   ![image-20211120100502173](Linux.assets\image-20211120100502173.png)

3. 按Ctrl+x，进入单用户模式

4. 在光标闪烁的位置中输入：mount -o remount,rw / （注意每个单词间有空格），按回车

   ![image-20211120100752533](Linux.assets\image-20211120100752533.png)

5. 输入passwd，按回车。输入密码，然后再次确认密码

   ![image-20211120100900430](Linux.assets\image-20211120100900430.png)

6. 接着输入：touch /.autorelabel，按回车

7. 继续输入：exec /sbin/init，按回车（此过程有点长，耐心等待），即可

   ![image-20211120101118061](Linux.assets\image-20211120101118061.png)



## 命令提示符含义

[root @localhost root] #

当前用户名@Linux主机名 当前目录名 命令提示符

#是管理员命令提示符，$是普通用户的命令提示符



## vi和vim

> vi 或 vim 文件名

**正常模式**

进入便是默认的一般模式

**插入模式**

按下i,I,o,O,a,A,r,R任何一个字母即进入编辑模式

**命令行模式**

按下esc，再输入

:wq	保存并退出

:q    退出

:q！  强制退出并不保存



**快捷键**

* 拷贝当前行 **yy**，拷贝当前行向下的5行 **5yy**，粘贴 **p**
* 删除当前行 **dd**，删除当前行向下的5行 **5dd**
* 查找某个单词，在命令行模式下 **/关键字**，回车查找，输入**n**查找下一个
* 设置文件的行号，在命令行模式下 **set nu**，取消行号 **set nonu**
* 光标移动到文档的最末行 **G**，最首行 **gg**
* 撤销，在一般模式下 **u**
* 移动到第20行，在一般模式下**,20 shift+g**





## 重启和关机

**重启**

reboot

或者

shutdown -r now



**关机**

halt

或者

shutdown -h now



shutdown -h 1 "还有一分钟要关机了" 



sync 把内存的数据同步到磁盘



## 创建文件夹

> mkdir /home/y/work

mkdir -m 在创建目录时设定权限模式

mkdir -p 创建目录结构中指定的每一个目录，如果目录不存在则创建该目录，如果目录已存在也不会被覆盖

mkdir -v 或--verbose，每次创建新目录都显示信息



例：在当前目录键work1和work2，在/tmp目录下创建www目录

~~~
mkdir work1 work2 /tmp/www
~~~

例：创建多级目录，/home/animal/tiger

![image-20211120103621019](Linux.assets\image-20211120103621019.png)



## 切换路径

> cd /home/y



## 显示当前路径

> pwd



## 创建文件

在当前路径下

> touch file1



## 拷贝文件

> cp file1 /home/y/work2

将当前目录下的file1复制到work2目录里



cp -a 保留链接、文件属性，复制目录时可递归地复制目录

cp -f 如果目标文件或目录已经存在，则将其覆盖，并不做提示(force)

cp -i 如果目标文件或目录已经存在，则对用户进行提示，可以用字母y确认，其他字母都是否认

cp -r 复制目录，实现将源目录下的文件和子目录一起复制到目标目录中



## 剪切文件

> mv 文件名 路径

例：把当前目录的hello.csv剪切到当前目的python文件夹里

~~~
mv hello.csv ./python
~~~

例：把当前目录下的文件hello.txt剪切到上一级目录的子目录java目录里

~~~
mv hello.txt ../java
~~~

例：把文件hello.txt移动到上一级目录

~~~
mv hello.txt ..
~~~



## 重命名文件

> mv 旧文件名 新文件名





## 删除文件

> rm file1



rm -f 强制删除文件或目录(force)

rm -i 对用户进行提示(inform)，可以用字母y确认，其它字母是否认

rm -r 删除目录，将指定目录下的所有文件及其子目录一并删除



例：删除文件file

~~~
rm file
~~~

例：删除目录work

```
rm -r work
```

例：强制删除目录work

~~~
rm -rf work
~~~





## 删除文件夹

会询问

> rm -r /home/y/work1

不会询问(f代表force)

> rm -rf /home/y/work1



## 查看文件内容

**cat**

> cat [选型] 文件名

常用选项 -n 显示行号



一般会带上管道命令 cat ... | more，按回车下一行，空格下一页



**more**

空格：向下翻一页

enter：向下翻一行

q：离开more

Ctrl+F：向下滚动一屏

Ctrl+B：返回上一屏

=：输出当前行的行号

:f：输出文件名和当前行的行号



**less**

less用来分屏查看文件内容，功能和more类似，但比more强大，支持各种显示终端。less指令在显示文件内容时，并不是一次将整个文件加载之后才显示，而是根据显示需要加载内容，对心事大型文件具有较高的效率

空白键：向下翻动一页

[pagedown]：向下翻动一页

[pageup]：向上翻动一页

/字串：向下搜寻【字串】的功能；n：向下查找；N：向上查找

?字串：向上搜寻【字串】的功能；n：向上查找；N：向下查找

q：离开less



**echo**

> echo [选项] [输出内容]

echo输出内容到控制台

例：用echo指令输出环境变量

~~~
echo $PATH
~~~

例：用echo输出Hello World

~~~
echo "Hello World"
~~~





**head**

用于显示文件的开头部分内容，默认前10行



例：查看/etc/profile前5行

~~~
head -n 5 /etc/profile
~~~

![image-20211120110749389](Linux.assets\image-20211120110749389.png)



**tail**

用于显示文件的最后部分内容，默认后10行

例：查看/etc/profile后5行

~~~
tail -n 5 /etc/profile
~~~

![image-20211120110925942](Linux.assets\image-20211120110925942.png)

> tail -f 文件名

实时追踪该文档的更新

![image-20211120111430128](Linux.assets\image-20211120111430128.png)





## 查找文件

### find

> 从指定目录向下递归地遍历其各个子目录，将满足条件的文件或者目录显示在终端

find -name <查询方式>：按照指定的文件名查找模式查找文件

find -user <用户名>：查找属于指定用户名的所有文件

find -size <文件大小>：按照指定的文件大小查找文件



例：找出/var/log目录下所有后缀是.log的文件

~~~
find /var/log -name '*.log'
~~~

例：查找/home目录下的hello.txt文件

~~~
find /home -name hello.txt
~~~

例：查找/opt下，用户名为root的文件

~~~
find /opt -user root | more
~~~

例：查找整个linux系统下大于200M的文件（+n 大于  -n 小于  n 等于，单位有k，M，G）

~~~
find / -size +200M
~~~





### **locate**

> locate 搜索文件

locate指令可以快速定位文件路径。locate指令利用事先建立的系统中所有文件名称及路径的locate数据库实现快速定位给定的文件。

locate无序遍历整个文件系统，查询速度较快。

为了保证查询结果的准确度，管理员必须顶起更新locate时刻。

由于locate指令基于数据库进行查询，所以第一次运行前必须使用updatedb指令创建locate数据库。

例：用locate指令快速定位hello.txt文件所在位置

~~~
updatedb
locate hello.txt
~~~

<img src="Linux.assets\image-20211120115755922.png" alt="image-20211120115755922"  />



### grep

> grep [选项] 查找内容 源文件

grep过滤查找，管道符“|”，表示前一个命令的处理结果输出传递给后面的命令处理。

常用选项：

* -n 显示匹配行及行号
* -i 忽略字母大小写

例：在hello.txt中查找“yes”所在行并显示行号

~~~
// 写法一
cat /home/hello.txt | grep "yes"
// 写法二
grep -n "yes" hello.txt
~~~

<img src="Linux.assets\image-20211120140650638.png" alt="image-20211120140650638" style="zoom:67%;" />

<img src="Linux.assets\image-20211120140505772.png" alt="image-20211120140505772" style="zoom: 67%;" />

<img src="Linux.assets\image-20211120140609008.png" alt="image-20211120140609008" style="zoom:67%;" />



## 修改时间

> date

例：将时间改为2021年9月29日9时26分14秒

~~~
data -s "2021-9-29 9:26:14"
~~~



## 查看磁盘用量

> df -h /path/

path是路径



## 设置别名

> alias [别名]='[命令]'

例：将“cat /etc/named.conf”设置为别名 name,然后再取消别名

~~~
alias name='cat /etc/named.conf'
~~~

~~~
unalias name
~~~





## 重定向

> \> 覆盖
>
> \>\> 追加

例：将列表的内容写入文件a.txt

~~~
ls -l > a.txt
~~~

例：将列表内容追加到文件aa.txt的末尾

~~~
ls -al >> aa.txt
~~~

例：将b.txt的内容覆盖到c.txt

~~~
cat b.txt > c.txt
~~~

例：追加内容到d.txt

~~~
echo "内容" >> 文件
~~~

例：将日历信息追加到/home/mycal文件中

~~~
cal >> /home/mycal
~~~



## 软链接

> ln -s [原文件或目录] [软链接名]

修改软连接里的内容，源文件会变；修改源文件的内容，软连接内容也会变

类似于windows的快捷方式

例：在/home目录下创建一个软链接myroot,链接到/root目录

~~~
ln -s /root /home/myroot
~~~

![image-20211120112944947](Linux.assets\image-20211120112944947.png)

例：删除软链接myroot

~~~
rm /home/myroot
~~~



## history指令

查看已经执行过的历史命令

例：显示最近执行的10个指令

~~~
history 10
~~~

![image-20211120113236956](Linux.assets\image-20211120113236956.png)

例：执行历史编号为15的指令

~~~
!15
~~~



## date指令

**显示时间**

date：显示当前时间

date +%Y：显示当前年份

date +%m：显示当前月份

date +%d：显示当前是哪一天

date "+%Y-%m-%d %H:%M:%S"：显示年月日时分秒



**设置日期**

> date -s 字符串时间

例：时间设置为2020-11-01 22:22:22

~~~
date -s "2020-11-01 22:22:22"
~~~



## cal指令

> cal

显示本月日历

例：显示2019年日历

~~~
cal 2019
~~~





## which指令

可以查看某个指令在哪个目录下，比如ls、reboot在哪个目录

![image-20211120115919240](Linux.assets\image-20211120115919240.png)



## 压缩与解压



### gzip/gunzip

> gzip 文件名
>
> gunzip 文件名.gz

gzip用于压缩文件

gunzip用于解压文件

例：将/home下的hello.txt文件压缩

~~~
gzip /home/hello.txt
~~~

例：将/home下的hello.txt.gz文件进行解压

~~~
gunzip /home/hello.txt.gz
~~~

<img src="Linux.assets\image-20211120141111550.png" alt="image-20211120141111550" style="zoom: 67%;" />



### zip/unzip

> zip [选项] xxx.zip /路径
>
> unzip [选项] xxx.zip 

zip用于压缩文件，unzip用于解压文件，在项目打包发布中很常用

常用选项：

* -r：递归压缩，压缩目录

* -d<目录>：指定解压后文件的存放目录

例：将/home下的所有文件压缩成myhome.zip

~~~
zip -r myhome.zip /home
~~~

![image-20211120142053724](Linux.assets\image-20211120142053724.png)

![image-20211120141932893](Linux.assets\image-20211120141932893.png)

例：将myhome.zip解压到/opt/tmp目录下

~~~
unzip -d /opt/tmp /home/myhome.zip
~~~

![image-20211120142108717](Linux.assets\image-20211120142108717.png)

<img src="Linux.assets\image-20211120142145058.png" alt="image-20211120142145058" style="zoom:67%;" />



### tar

> tar [选项] xxx.tar.gz 打包的内容

tar是打包指令，最后打包后的文件是.tar.gz的文件

常用选项：

* -c：产生.tar打包文件
* -v：显示详情信息
* -f：指定压缩后的文件名
* -z：打包同时压缩
* -x：解包.tar文件

例：压缩多个文件，将/home/pig.txt和/home/cat.txt压缩成pc.tar.gz

~~~
tar -zcvf pc.tar.gz /home/pig.txt /home/cat.txt
~~~

<img src="Linux.assets\image-20211120143214993.png" alt="image-20211120143214993" style="zoom: 67%;" />

例：将/home的文件夹压缩成myhome.tar.gz

~~~
tar -zcvf myhome.tar.gz /home
~~~

例：将pc.tar.gz解压到当前目录

~~~
tar -zxvf pc.tar.gz
~~~

例：将myhome.tar.gz解压到/opt/tmp2目录下

~~~
tar -zxvf myhome.tar.gz -C /opt/tmp2
~~~



## 以树状显示目录结构

> tree /目录

* 注意：如果没有tree，则用yum install tree安装



## 文件权限

**查看文件所有者**

> ls -ahl 或 ll

<img src="Linux.assets\image-20211120145014485.png" alt="image-20211120145014485" style="zoom:67%;" />



**修改文件所有者**

> chown 用户名 文件名

例：用root创建apple.txt，然后将其所有者修改成tom

![image-20211120145338031](Linux.assets\image-20211120145338031.png)

![image-20211120145320525](Linux.assets\image-20211120145320525.png)





## cut

- 作用：从文件的每一行中剪切文本字段并将这些字段写至标准输出。
- 常用参数：
  - `-d`：指定字段分隔符。
  - `-f`：指定要剪切的字段或字段范围。
- 示例：
  - `cut -d ',' -f 1,3 file.csv`：从逗号分隔的csv文件中剪切第1和第3个字段。
  - `cut -d ' ' -f 2-5 file.txt`：从空格分隔的文本文件中剪切第2到第5个字段



cut, sort, head, tail, uniq这几个命令的例子都用random_data.csv表示

```csv
ID,Name,Score
1,Alice,85
2,Bob,92
3,Charlie,78
4,Daniel,95
5,Emma,88
6,Frank,80
7,Grace,91
8,Henry,87
9,Ivy,93
10,Jack,82
```

**提取CSV文件的第二列（Name列）**

~~~shell
cut -d ',' -f 2 random_data.csv
~~~

Name
Alice
Bob
Charlie
Daniel
Emma
Frank
Grace
Henry
Ivy
Jack





## sort

- 作用：对文件的行进行排序。
- 常用参数：
  - `-t`：指定字段分隔符。
  - `-k`：指定按照哪个字段进行排序。
  - `-n`：按照数值顺序进行排序。
- 示例：
  - `sort -t ',' -k 3,3n file.csv`：按照逗号分隔的csv文件中的第3个字段进行数值顺序排序。
  - `sort -t ' ' -k 2,2r file.txt`：按照空格分隔的文本文件中的第2个字段进行逆序排序

**按分数（Score列）对CSV文件进行升序排序**

~~~shell
sort -t ',' -k 3 -n random_data.csv
~~~

ID,Name,Score
3,Charlie,78
6,Frank,80
10,Jack,82
1,Alice,85
8,Henry,87
5,Emma,88
7,Grace,91
2,Bob,92
9,Ivy,93
4,Daniel,95



##  head

- 作用：显示文件的开头若干行。
- 常用参数：
  - `-n`：指定显示的行数。
- 示例：
  - `head -n 10 file.txt`：显示文本文件的前10行。

##  tail

- 作用：显示文件的结尾若干行。
- 常用参数：
  - `-n`：指定显示的行数。
- 示例：
  - `tail -n 5 file.csv`：显示csv文件的最后5行。

##  uniq

- 作用：从文件或输入中去除重复的行，并可显示重复行出现的次数。
- 常用参数：
  - `-c`：显示每行重复出现的次数。
- 示例：
  - `uniq -c file.txt`：显示文本文件中每行出现的次数。





# 三、树形目录结构

> ***在Linux世界里，一切皆文件***



**/bin** 存放系统常用命令，目录中的文件都是可执行的、普通用户可以使用的命令

**/dev** 设备文件存储目录，比如声卡、磁盘文件

**/boot** 存放Linux内核及引导系统程序文件

**/etc** 存放系统配置文件，某些服务器的配置文件也在这里

**/home** 普通用户主目录的默认存放位置

**/lib** 库文件存放目录

**/tmp** 临时文件目录

**/usr** 存放系统程序的目录

**/var/log** 存放系统日志文件

**/etc/init.d** 存放系统或服务器启动的脚本

**/usr/bin** 存放可执行程序的目录，普通用户有权限执行；当从系统自带的软件包安装一个程序时，其可执行文件大多会放在这个目录中

**/usr/sbin** 存放可执行程序的目录，只有root权限才能执行

**/usr/local** 存放用户自编译安装软件，一般是通过源码包安装的软件，如果没有特别指定安装目录的话，一般是安装在这个目录中

**/usr/share** 存放系统共用文件的目录

**/usr/src** 存放内核源码的目录

**/mnt** 让用户临时挂载别的文件系统

**/opt** 给主机额外安装软件所存放的目录，例如oracle数据库...











# 四、查看系统

查看Linux内核版本的命令：uname –r或uname –a。
查看文件系统的磁盘空间大小和剩余空间大小的命令：df 。
显示系统已经运行了多长时间的命令：uptime。
查看当前系统内存的使用情况的命令：free。
查询有关CPU的详细硬件信息命令：cat  /proc/cpuinfo。
查看CPU的使用情况和正在运行的进程情况的命令：top。
查看登录日志信息的命令：last。
查看登录用户信息的命令：w [用户名]。
显示月历或年历的命令： cal。
显示或设置当前日期和时间的命令：date。











# 五、用户与用户组

Linux用户分为三种：

1. **超级用户**：最高管理权限
2. **普通用户**：只能对自己目录下的文件进行访问修改，具有登录系统的权限
3. **虚拟用户**：也叫“伪”用户，这类用户最大的特点是不能登陆系统，它们的存在主要是方便系统管理，满足对应的系统进程对文件属主的要求。例如系统默认的bin、adm、nobody用户等



用户和用户组的对应关系有：**一对一**、**一对多**、**多对一**和**多对多**。



## 1、相关配置文件

**用户信息**保存在**/etc/passwd**中

在passwd配置文件中每行均由7个字段构成，每个字段用“:”分隔，每个字段都代表用户某方面的信息

* 从左至右：1.用户名 2.口令 3.用户标识号(UID) 4.用户组标识号(GID) 5.注释性描述 6.用户主目录 7.命令解释器

![image-20211017202037968](Linux.assets\image-20211017202037968.png)



**密码信息**保存在**/etc/shadow**中

在/etc/shadow文件中，一行对应一个用户的密码信息，每行均由9个字段构成，各个字段之间用":"分隔

* 从左至右：1.用户名 2.密码 3.最后一次修改的时间 4.最小时间间隔 5.最大时间间隔 6.警告时间 7.不活动时间 8.失效时间 9.标志

![image-20211017202458445](Linux.assets\image-20211017202458445.png)



系统中**所有用户组信息**都存放于**/etc/group**文件中，其中一行对应一个用户组的信息，每行均由4个字段构成，各个字段之间用":"分隔

从左至右：1.组名 2.组口令 3.组标识号(GID) 4.组成员

![image-20211017202846019](Linux.assets\image-20211017202846019.png)



用户组密码配置文件**/etc/gshadow**，该文件用于定义用户组口令、组管理员等信息，该文件root用户可读

* 从左至右：1.组名 2.组口令 3.组的管理员账号 4.组成员

![image-20211017202947988](Linux.assets\image-20211017202947988.png)







## 2、用户管理



### 创建用户

> useradd [选项] 用户名



例：创建用户tom

~~~shell
useradd tom
~~~

例：创建一个名为zhangqi 的用户，设置主目录为/var/zhangqi，作为root组的成员，加注释：101school，指定用户shell为：/bin/sh

~~~
useradd -d /var/zhangqi -g root -c 101school -s /bin/sh zhangqi
~~~





### 修改用户属性

> usermod [选项] 用户名

改变用户所在组

usermod -g 新组名 用户名

usermod -d 目录名 用户名



例：修改用户zhangqi为zhangqiming

~~~
usermod -l zhangqiming zhangqi
~~~

例：修改zhangqiming的主目录为/var/zhangqiming

~~~
usermod -d /var/zhangqiming zhangqiming
~~~

* 如果新的主目录不存在则需要先创建该目录

例：修改zhangqiming的注释信息为neusoft

~~~
usermod -c neusoft zhangqiming
~~~





### 删除用户

> userdel [-r] 用户名



例：删除zhangqiming用户及其主目录以及该用户的相关文档

~~~
userdel -r zhangqiming
~~~

一般情况下建议保留（不用-r）



### 管理用户登录密码

> passwd [选项] [用户名]

| 选项 | 功能说明         |
| ---- | ---------------- |
| -l   | 锁定用户密码     |
| -u   | 解锁用户密码     |
| -S   | 查询用户密码状态 |
| -d   | 删除用户密码     |



例：root管理员创建bob用户，并为其设置密码为“123456”，然后查看/etc/shadow文件中的bob用户的密码。再将bob的密码锁定，使bob无法登陆系统，查看/etc/shadow文件的变化，再解锁bob的密码，恢复bob对系统的访问权，再次查看/etc/shadow文件的变化

![image-20211017205132371](Linux.assets\image-20211017205132371.png)

![image-20211017205142121](Linux.assets\image-20211017205142121.png)

* 从本操作中可以看出锁定用户的密码只是在shadow文件中在该用户密码前加"!!"，而解锁也只是将"!!"去掉



例：查询bob用户的密码状态，加锁后再查询bob用户的密码状态

![image-20211017205416206](Linux.assets\image-20211017205416206.png)







## 3、用户组管理



### 创建用户组

> groupadd [选项] 用户组名称

该命令的常用选项是-r，功能是创建系统用户组。每一个用户组都有一个自己的ID，被称为GID。若≥1000则代表改组是普通用户组，反之则为系统用户组。如果使用了选项-r，对于第一次创建系统组的系统来说，新生成的系统用户组的GID从999开始递减，而普通用户组的GID应从1000开始增加



例：创建用户组student

```
groupadd student
```

例：创建一个用户fox，把他加入到student中

~~~
useradd -g student fox
~~~





### 修改用户组属性

> groupmod 选项 组名

| 选项 | 功能说明        |
| ---- | --------------- |
| -n   | 修改组名        |
| -g   | 修改组标识号GID |



例：修改用户组student为teacher

~~~
groupmod -n teacher student
~~~

例：tom本身在武当组，现在把他改到魔教组

~~~
groupmod -g mojiao tom
~~~





### 删除用户组

> groupdel 组名

在删除用户组时，被删除的用户组不能是某个用户的主组，否则无法删除。若必须删除，则应先删除该用户，然后再删除用户组



### 维护组中成员

> gpasswd 选项 用户名 组名

gpasswd命令可用于把用户添加到组、把用户从组中删除、把用户设为组管理员

| 选项 | 功能说明           |
| ---- | ------------------ |
| -a   | 添加用户到组       |
| -d   | 将用户从组中删除   |
| -A   | 设置用户为组管理员 |



例：将lili用户添加到teacher组

~~~
gpasswd -a lili teacher
~~~



## 4、文件/目录 所在组

当用户创建了一个文件后，这个文件的所在组就是该用户的所在组

### 查看文件/目录所在组

> ls -ahl

### 修改文件所在组

>chgrp 组名 文件名

例：使用root用户创建文件orange.txt，看看当前此文件属于哪个组，然后将这个文件所在组修改到fruit组

~~~
groupadd fruit
touch orange
chgrp fruit oragne.txt
~~~

![image-20211120150656745](Linux.assets\image-20211120150656745.png)



例：将zwj这个用户从原来的所在组修改到wudang组

~~~
usermod -g wudang zwj
~~~

![image-20211120151410430](Linux.assets\image-20211120151410430.png)





## 5、其他命令



### 查看用户信息的id命令

> id [选项] [用户名称]

| 选项 | 功能说明                 |
| ---- | ------------------------ |
| -g   | 显示用户所属群组的ID     |
| -G   | 显示用户所属附加群组的ID |
| -u   | 显示用户ID               |



例：查看lili用户的ID信息

~~~
id lili
~~~



### 输出指定用户所在组的groups命令

> groups [选项] [用户名]

| 选项     | 功能说明         |
| -------- | ---------------- |
| -help    | 显示命令帮助信息 |
| -version | 显示版本号       |



例：显示用户lili所在的组

~~~
groups lili
~~~



### 查看当前登录用户whoami命令

> whoami

显示登陆者自身的用户名称



### 查看当前用户w命令

> w

系统管理员在任何时刻都可以查看用户的行为



### 查看登录用户who命令

> who

系统管理员若想知道某一时刻有哪些用户登录到系统，可以使用系统提供的who命令，该命令可以查看当前登录系统的用户及其他相关系统信息



### 查看登录用户历史last命令

> last



### 修改用户口令有效期限的chage命令

> chage [选项] 用户名

| 选项 | 功能说明                                                   |
| ---- | ---------------------------------------------------------- |
| -m   | 密码可更改的最小天数。为零时代表任何时候都可以修改密码     |
| -W   | 用户密码到期前，提前收到警告信息的天数                     |
| -M   | 密码保持有效的最大天数                                     |
| -E   | 账号到期的日期。过了这天此账号将不可用                     |
| -d   | 上一次更改的日期                                           |
| -i   | 停滞时期。如果一个密码已过期这些天，那么此账号将不可用     |
| -l   | 列出当前的设置。可以帮助用户来确定他们的密码或账号何时过期 |



### 修改用户注释信息的chfn命令

> chfn [选项] [用户名]

| 选项 | 功能说明             |
| ---- | -------------------- |
| -f   | 设置真实姓名         |
| -h   | 设置家中的电话号码   |
| -o   | 设置办公室的地址     |
| -p   | 设置办公室的电话号码 |



### 修改用户Shell类型的chsh命令

> chsh [选项] [用户名]

例：查看系统安装的Shell

~~~
chsh -l
~~~

例：将tom用户的Shell修改为/bin/sh

~~~
chsh tom
/bin/sh
~~~





# 六、权限管理



## 1、基础知识

![image-20211120152212687](Linux.assets\image-20211120152212687.png)

0-9位说明：

1. 第0位确定文件类型（d，-，l，c，b）
   * l是连接，相当于windows的快捷方式
   * d是目录，相当于windows的文件夹
   * c是字符设备文件，比如鼠标，键盘
   * b是块设备，比如硬盘
   * -是普通文件
2. 第1-3位确定所有者（该文件的所有者）拥有该文件的权限 --User
3. 第4-6位确定所属组（同用户组的）拥有该文件的权限 --Group
4. 第7-9位确定其他用户拥有该文件的权限 --Other



**rwx权限**

作用在文件中：

* r代表可读read：可以读取 查看

* w代表可写write：可以修改但不代表可以删除，删除的前提是对该文件所在目录有写权限

* x代表可执行execute：可以被执行

作用在目录中：

* r代表可读read：可以读取，ls查看目录内容
* w代表可写write：可以修改 创建 删除 重命名
* x代表可执行execute：可以进入该目录

可用数字表示为：r=4，w=2，x=1，因此rwx=4+2+1=7





图中的1代表所属文件夹下有多少子文件或子文件夹

图中第一个root代表用户名

图中第二个root代表组名

图中的0代表0个字节

图中日期代表最后修改的日期

图中最后的名字代表文件名



## 2、修改权限

> chmod

**第一种方式**：用+、-、=变更权限

u：所有者  g：所有组  o：其他人  a：所有人（u,g,o的总和）

1. chmod u=rwx, g-rx,o=x 文件/目录名
2. chmod o+w 文件/目录名
3. chmod a-x 文件/目录名

例：给abc文件的所有者读写执行的权限，给所在组读写执行权限，给其他组执行权限

~~~
chmod u=rwx,g=rwx,o=x abc
~~~

例：给abc文件的所有者除去执行的权限，增加组写的权限

~~~
chmod u-x,g+w abc
~~~

例：给abc文件的所有用户添加读的权限

~~~
chmod a+r abc
~~~



**第二种方式**：通过数字变更权限

r=4,w=2,x=1 rwx=4+2+1=7

chmod u=rwx,g=rx,o=x 相当于 chmod 751

例：将/home/abc.txt文件的权限修改成rwxr-xr-x

~~~
chmod 751 /home/abc.txt
~~~



## 3、修改文件所有者

chown newowner 文件/目录 改变所有者

chown newowner:newgroup 文件/目录 改变所有者和所在组

-R 如果是目录，则使其下所有子文件或目录递归生效

例：将/home/abc.txt文件的所有者修改成tom

~~~
chown tom /home/abc.txt
~~~

例：将/home/kkk目录下所有的文件和目录的所有者都修改成tom

~~~
chown -R tom /home/kkk
~~~



## 4、修改文件或目录所在组

chgrp newgroup 文件/目录 改变所有组

例：将/home/abc.txt文件所在组修改成shaolin

~~~
chgrp shaolin /home/abc.txt
~~~

例：将/home/kkk目录下所有的文件和目录所在组都修改成shaolin

~~~
chgrop -R shaolin /home/kkk
~~~







# 七、远程登录

远程登录：xshell7

文件传输：xftp

**Telnet**

Telnet是基于TCP/IP网络的终端模拟程序。Telnet程序运行于用户本机，将本机连接到网络中的服务器。然后通过Telnet输入的命令，就会被服务器执行，就如同直接在服务器的控制台上输入命令一样。
为了成功的登录telnet，必须输入有效的用户名和密码。

**安全外壳协议（Secure Shell,SSH）**

SSH是支持通过网络登录其他机器。通过SSH程序，可以在远端的服务器上执行命令，也可以实现不同机器之间文件的拷贝或者移动。SSH提供强大的验证机制和安全的信息交流通道。

因为其安全特性，替代了远程登录(Remote Login，RLogin)，远程Shell(Remote Shell，RSH)，远程文件拷贝(Rmote Copy，RCP)等服务





# 八、定时任务调度

**crond和at的区别**

crond可以执行多次，而at只能执行一次



## **1、crond任务调度**

crontab进行定时任务的设置

**概述**

任务调度：是指系统在某个时间执行的特定的命令或程序

任务调度的分类：

1. 系统工作：有些重要的工作必须周而复始地执行，比如病毒扫描等
2. 个别用户工作：个别用户可能希望执行某些程序，比如对mysql的备份

 

> crontab [选项]

常用选项

* -e：编辑crontab定时任务
* -l：查询crontab任务
* -r：删除当前用户所有的crontab任务



**快速入门**

设置任务调度文件：/etc/crontab

设置个人任务调度。执行crontab -e命令

接着输入任务到调度文件

* 如：*/1 \* \* * * ls -l /etc/ > /tmp/to.txt
  * 意思是每小时的每分钟执行ls -l /etc/ > /tmp/to.txt命令

参数细节说明：

| 项目      | 含义                 | 范围                  |
| --------- | -------------------- | --------------------- |
| 第一个“*” | 一小时当中的第几分钟 | 0-59                  |
| 第二个“*” | 一天当中的第几个小时 | 0-23                  |
| 第三个“*” | 一个月当中的第几天   | 1-31                  |
| 第四个“*” | 一年当中的第几月     | 1-12                  |
| 第五个“*” | 一周当中的星期几     | 0-7（0和7都代表周日） |

特殊符号的说明：

| 特殊符号 | 含义                                                         |
| -------- | ------------------------------------------------------------ |
| *        | 代表任何时间。比如第一个“*”代表一小时中每分钟都执行一次的意思 |
| ,        | 代表不连续的时间。比如“0 8,12 16 * * *”代表在每天的8点0分，12点0分，16点0分都执行一次命令 |
| -        | 代表连续的时间范围。比如"0 5 * * 1-6 命令"代表在周一到周六凌晨5点0分执行命令 |
| */n      | 代表每隔多久执行一次。比如"*/10 * * * * 命令"代表每隔10分钟就执行一遍命令 |

特定时间执行任务案例：

| 时间              | 含义                                        |
| ----------------- | ------------------------------------------- |
| 45 22 * * * 命令  | 在22点45分执行命令                          |
| 0 17  * * 1 命令  | 每周一的17点0分执行命令                     |
| 0 5 1,15 * * 命令 | 每月1号和15号的凌晨5点0分执行命令           |
| 40 4 * * 1-5 命令 | 每周一到周五的凌晨4点40分执行命令           |
| */10 4 * * * 命令 | 每天的凌晨4点，每隔10分钟执行一次命令       |
| 0 0 1,15 * 1 命令 | 每月1号和15号，每周一的0点0分都会执行命令。 |

* 注意：星期几和几号最好不要同时出现，因为他们定义的都是天，容易让管理员混淆



例：每隔1分钟，将当前的日期信息追加到/tmp/mydate文件中

~~~
/1 * * * * date >> /tmp/mydate
~~~

例：每隔1分钟，将当前的日期和日历都追加到/home/mycal文件中

写一个脚本文件

![image-20211120174507878](Linux.assets\image-20211120174507878.png)

![image-20211120174435447](Linux.assets\image-20211120174435447.png)![image-20211120174704111](Linux.assets\image-20211120174704111.png)

crontab -e  每隔一分钟执行一次脚本文件

![image-20211120175223635](Linux.assets\image-20211120175223635.png)



例：每天凌晨2:00将mysql数据库testdb备份到文件中

步骤1： crontab -e

步骤2: 0 2 * * * mysqldump -u root -proot testdb >> /home/db.bak



**总结**

第一步：写脚本

第二步：给权限

第三步：任务调度





## 2、at定时任务

基本介绍

1. at命令是一次性定时计划服务，at的守护进程atd会以后台模式运行，检查作业队列来进行
2. 默认情况下，atd守护进程每60秒检查作业队列，有作业时，会检查作业运行时间，如果时间与当前时间匹配，则运行此作业
3. at命令试一次性定时计划任务，执行完一个任务后不再执行次任务了
4. 在使用at命令的时候，一定要保证atd进程的启动，可以使用相关命令来查看：ps -ef | grep atd



> at [选项] [时间]

Ctrl+D 结束at命令的输入

| 选项          | 含义                                                     |
| ------------- | -------------------------------------------------------- |
| -m            | 当指定的任务被完成后，将给用户发送邮件，即使没有标准输出 |
| -I            | atq的别名                                                |
| -d            | atrm的别名                                               |
| -v            | 显示任务被执行的时间                                     |
| -c            | 打印任务的内容到标准输出                                 |
| -V            | 显示版本信息                                             |
| -q <队列>     | 使用指定的队列                                           |
| -f <文件>     | 从指定文件读入任务而不是从标准输入读入                   |
| -t <时间参数> | 以时间参数的形式提交要运行的任务                         |



例：2天后的下午5点执行 /bin/ls /home

![image-20211121090625967](Linux.assets\image-20211121090625967.png)

* 输入两次Ctrl+d结束输入
* 如果输错的话Ctrl+backspace删除写错的代码
* Ctrl+c强制退出

例：atq名来查看系统中没有执行的工作任务

![image-20211121090821927](Linux.assets\image-20211121090821927.png)

例：明天17点，输出时间到指定文件内，比如/root/date100.log

![image-20211121091231538](Linux.assets\image-20211121091231538.png)

例：2分钟后，输出时间到指定文件内，比如/root/date200.log

![image-20211121091727982](Linux.assets\image-20211121091727982.png)

例：删除已经设置的任务，atrm 编号

![image-20211121091923453](Linux.assets\image-20211121091923453.png)





# 九、磁盘分区、挂载



## 1、原理

Linux无论有几个分区，分给哪一个目录使用，它归根结底就只有一个根目录，一个独立且唯一的文件结构，Linux中每个分区都是用来组成整个文件系统的一部分。

Linux采用了一种叫“载入”的处理方法，它的整个文件系统中包含了一整套的文件和目录，且将一个分区和一个目录联系起来。这时要载入的一个分区将使它的存储空间在一个目录下获得。

![image-20211121093705983](Linux.assets\image-20211121093705983.png)

![image-20211121093545669](Linux.assets\image-20211121093545669.png)



**硬盘说明**

Linux硬盘分IDE硬盘和SCSI硬盘，目前基本上是SCSI硬盘

对于IDE硬盘，驱动器标识符为"hdx~"，其中“hd”表名分区所在设备的类型，这里是指IDE硬盘了。“x”为盘号（a为基本盘，b为从属盘，c为辅助主盘，d为辅助从属盘），“~”代表分区，前四个分区用数字1-4表示，它们是主分区或扩展分区，从5开始是逻辑分区。例，hda3表示一个IDE硬盘上的第三个主分区或扩展分区，hdb2表示为第二个IDE硬盘上的第二个主分区或扩展分区。

对于SCSI硬盘则标识为“sdx~”，SCSI硬盘使用“sd”来表示分区所在设备的类型，其余则和IDE硬盘的表示方法一样。





## 2、查看挂载情况

> lsblk 或者 lsblk -f

![image-20211121094956255](Linux.assets\image-20211121094956255.png)



## 3、增加一块硬盘

步骤：

1. 虚拟机添加硬盘
2. 分区
3. 格式化
4. 挂载
5. 设置自动挂载



**第一步**：添加硬盘一直点下一步，重启后输入lsblk指令即可看到

<img src="Linux.assets\image-20211121095724865.png" alt="image-20211121095724865" style="zoom:50%;" />



<img src="Linux.assets\image-20211121095847393.png" alt="image-20211121095847393" style="zoom:50%;" />

<img src="Linux.assets\image-20211121100046384.png" alt="image-20211121100046384" style="zoom: 80%;" />



**第二步**：分区命令 fdisk /dev/sdb

开始对/sdb分区

m 显示命令列表

p 显示磁盘分区 同fdisk -l

n 新增分区

d 删除翻去

w 写入并退出

说明：开始分区后输入n，新增分区，然后选择p，分区类型为主分区。两次回车默认剩余全部空间。最后输入w写入分区并退出，若不保存退出输入q



![image-20211121100820371](Linux.assets\image-20211121100820371.png)

![image-20211121100945207](Linux.assets\image-20211121100945207.png)



**第三步**：格式化

完成第二步后输入lsblk -f发现没有UUID，说明还没有唯一的40位标识符，没有格式化

![image-20211121101112167](Linux.assets\image-20211121101112167.png)



格式化硬盘

分区命令：mkfs -t ext 4 /dev/sdb1

其中ext4是分区类型

![image-20211121101408170](Linux.assets\image-20211121101408170.png)

![image-20211121101440156](Linux.assets\image-20211121101440156.png)





**第四步**：

挂载

> mount 设备名称 挂载目录

卸载

> umount 设备名称 或者 umount 挂载目录

* 注意：用命令行挂载，重启后会失效



把sdb1挂载到/目录下的newdisk

![image-20211121101824915](Linux.assets\image-20211121101824915.png)





**第五步**：永久挂载

通过修改/etc/fstab实现挂载

添加完成后执行mount -a 即刻生效



![image-20211121102526585](Linux.assets\image-20211121102526585.png)

![image-20211121102810636](Linux.assets\image-20211121102810636.png)

修改完文件后重启，重启后发现挂载成功

![image-20211121102952098](Linux.assets\image-20211121102952098.png)





## 4、磁盘情况查询



**查询系统整体磁盘使用情况**

> df -h



![image-20211121103126925](Linux.assets\image-20211121103126925.png)



**查询指定目录的磁盘占用情况**

> du -h /目录

查询指定目录的磁盘占用情况，默认为当前目录 du -h

-s 指定目录占用大小汇总

-h 带计量单位

-a 含文件

--max-depth=1 子目录深度

-c 列出明细的同时增加汇总值



例：查询/opt目录的磁盘占用情况，深度为1

<img src="Linux.assets\image-20211121104035783.png" alt="image-20211121104035783" style="zoom:80%;" />

<img src="Linux.assets\image-20211121104124183.png" alt="image-20211121104124183" style="zoom:80%;" />

<img src="Linux.assets\image-20211121104156472.png" alt="image-20211121104156472" style="zoom:80%;" />





**工作实用指令**

例：统计/opt文件夹下文件个数

~~~
ll -l /opt | grep "^-" | wc -l
~~~

![image-20211121105205689](Linux.assets\image-20211121105205689.png)

例：统计/opt文件夹下目录个数

~~~
ll -l /opt | grep "^d" | wc -l
~~~

例：统计/opt文件夹下文件的个数，包括子文件夹里的

~~~
ll -lR /opt | grep "^-" | wc -l
~~~

![image-20211121105409400](Linux.assets\image-20211121105409400.png)

例：统计/opt文件夹下目录的个数，包括子文件夹里的

~~~
ll -lR /opt | grep "^d" | wc -l
~~~

例：以树状显示目录结构（如果没有tree，则用yum install tree安装）

~~~
tree /home
~~~





# 十、网络配置



![image-20211121112102518](Linux.assets\image-20211121112102518.png)



**查看虚拟网络编辑器和修改IP地址**

<img src="Linux.assets\image-20211121112316380.png" alt="image-20211121112316380" style="zoom: 67%;" />



## 1、指定ip

直接修改配置文件来指定IP，这样配稍微有点麻烦，其实就在虚拟网络编辑器的图形化界面配就行了，下面这个只是一种方法

vi /etc/sysconfig/network-scripts/ifcfg-ens33

例如将ip地址配置为静态的192.168.200.130

下列代码对应到ifcfg-ens33文件中（有的改，没有的添）

~~~
BOOTPROTO="static"
#IP地址
IPADDR=192.168.200.130
#网关
GATEWAY=192.168.200.2
#域名解析器
DNS1=192.168.200.2
~~~

重启网络服务或重启系统生效

service network restart

reboot



## 2、设置主机名和hosts映射



**设置主机名**

为了方便记忆可以给linux系统设置主机名，也可以根据需要修改主机名

指令hostname：查看主机名

修改文件在/etc/hostname指定

修改后重启生效



**设置hosts映射**

**windows**

在C:\Windows\System32\drivers\etc\hosts文件指定即可

![image-20211121135155913](Linux.assets\image-20211121135155913.png)

![image-20211121135240736](Linux.assets\image-20211121135240736.png)

**Linux**

在/etc/hosts文件指定即可

![image-20211121135657294](Linux.assets\image-20211121135657294.png)

* 其实在hosts命名时不一定非要是自己电脑的名字，可以自己取名，比如我把自己的Windows命名为MyLaptop

![image-20211121140113193](Linux.assets\image-20211121140113193.png)

![image-20211121140150586](Linux.assets\image-20211121140150586.png)



## 3、主机名解析过程

> **Hosts**：一个文本文件，用来记录IP和Hostname（主机名）的映射关系。
>
> **DNS**：Domain Name System域名系统，是 互联网上作为域名和IP地址相互映射的一个分布式数据库。

应用实例：用户在浏览器输入了www.baidu.com

1. 浏览器先检查浏览器缓存中有没有该域名解析IP地址，有就先调用这个IP完成解析；如果没有DNS解析器缓存，如果有则直接返回IP完成解析。这两个缓存可以理解为本地解析器缓存。

2. 一般来说，当电脑第一次成功访问某一个网站后，在一定时间内，浏览器或操作系统会存储他的IP地址（DNS解析记录），例如在cmd中输入

   ~~~
   ipconfig /displaydns	//DNS域名解析存储
   ipconfg /flushdns		//手动清理DNS缓存
   ~~~

3. 如果本地解析器缓存没有找到对应映射，检查系统中hosts文件中有没有配置对应的域名IP映射，如果有，则完成解析并返回

4. 如果本地DNS解析器缓存和hosts文件中均没有找到对应的IP，则到域名服务DNS进行解析域。**简单来说**就是先在本地浏览器找有没有DNS缓存，没有的话再在hosts找，再没有就去互联网的DNS找，再没有则返回不存在

   ![image-20211121144837350](Linux.assets\image-20211121144837350.png)





# 十一、进程管理



## 1、基础知识

在Linux中，每个执行的程序都称为一个进程。每一个进程都分配一个ID号（pid，进程号）。

每个进程都可能以两种方式存在。前台与后台：所谓前台进程就是用户目前屏幕上可以进行操作的；后台进程则是实际在操作，但由于屏幕尚无法看到的进程，通常使用后台方式进行。

一般系统的服务都是以后台进程的方式存在，而且都会常驻在系统中。知道关机才结束。



## 2、ps显示系统执行的进程

ps命令用来查看目前系统中有哪些正在执行以及它们的执行情况。可以不加参数

| ps -a      | 显示当前终端的所有进程信息                             |
| ---------- | ------------------------------------------------------ |
| **ps -u**  | **以用户的格式显示进程信息**                           |
| **ps -x**  | **显示后台进程运行的参数**                             |
| **ps -ef** | **以全格式显示当前所有的进程 -e显示所有进程 -f全格式** |

![image-20211121151704340](Linux.assets\image-20211121151704340.png)



> ps -ef 以全格式显示当前所有的进程 -e显示所有进程 -f全格式

![image-20211121152834174](Linux.assets\image-20211121152834174.png)

<img src="Linux.assets\image-20211121153009211.png" alt="image-20211121153009211" style="zoom:67%;" />



## 3、kill终止进程

若是某个进程执行一般需要停止时，或是已消耗很大的系统资源时，此时可以考虑停止该进程。使用kill命令来完成此项任务

> kill [选项] 进程号

> killall 进程名称

常用选项：

* -9：表示强迫进程立刻停止



例：踢掉某个非法登录用户

~~~
kill 进程号
~~~

例：重视远程服务登录sshd，在适当时候再次重启sshd服务

~~~
kill sshd对应的进程号
/bin/systemctl start sshd.service
~~~

例：终止多个gedit

~~~
killall gedit
~~~

![image-20211121154248728](Linux.assets\image-20211121154248728.png)

例：强制杀死一个终端

~~~
kill -9 bash对应的进程号
~~~

![image-20211121154825077](Linux.assets\image-20211121154825077.png)





## 4、pstree查看进程树

> pstree [选项]

可以用更加直观的来看进程信息

常用选项：

* -p：显示进程的PID
* -u：显示进程的所属用户



例：树状显示进程的pid

~~~
pstree -p
~~~

例：树状显示进程的用户

~~~
pstree -u
~~~





## 5、服务管理

服务（service）本质就是进程，但是是在后台运行，通常会监听某个端口，等待其他程序的请求，比如mysql，sshd，防火墙等，因此我们又称为**守护进程**，是Linux中非常重要的知识点。



### service管理指令

1. service 服务名[start|stop|restart|reload|status]
2. 在CentOS7.0后很多服务不再使用service，而是systemctl
3. service指令管理的服务可以在/etc/init.d查看



### **查看服务名**

**第一种方式**：setup

按tab键进行选择

带\*号的会随着linux的启动而启动，若想去掉*号，光标移上去按空格

![image-20211121161149528](Linux.assets\image-20211121161149528.png)



**第二种方式**：/etc/init.d看到service指令的管理服务







### **服务的运行级别**

Linux系统有7种运行级别（runlevel）：常用的是级别3和级别5

运行级别0：系统停机状态，系统默认运行级别不能设为0，否则不能正常启动

运行级别1：单用户工作状态，root权限，用于系统维护，禁止远程登录

运行级别2：多用户状态（没有NFS），不支持网络

运行级别3：完全的多用户状态（有NFS），登录后进入控制台命令行模式

运行级别4：系统未使用，保留

运行级别5：X11控制台，登录后进入图形GUI模式

运行级别6：系统正常关闭并重启，默认运行级别不能设为6，否则不能正常启动



开机的流程：

开机 -> BIOS -> /boot -> systemd进程1 -> 运行级别 -> 运行级对应的服务





### **chkconfig指令**

1. 通过chkconfig命令可以给服务的各个运行级别设置 启动/关闭
2. chkconfig 指令管理的服务在/etc/init/d查看
3. 在Centos7.0后，很多服务使用systemctl管理

> chkconfig --list [| grep xxx]

> chkconfig 服务名 --list

> chkconfig --level 5 服务名 on/off



例：对network服务进行各种操作，把network在3运行级别关闭自启动

~~~
chkconfig --level 3 network off
~~~

* chkconfig重新设置服务后自启动或关闭，需要重启机器reboot生效





### systemctl管理指令

> systemctl [start | stop | restart | status] 服务名

systemctl指令管理的服务在/usr/lib/systemd/system查看



**systemctl设置服务的自启动状态**

1. systemctl list-unit-files [| grep 服务名] （查看服务开机启动状态，grep可以进行过滤）
2. systemctl enable 服务名 （设置服务开机启动）
3. systemctl disable 服务名 （关闭服务开机启动）
4. systemctl is-enabled 服务名 （查询某个服务是否是自启动的）



例：查看当前防火墙状态，关闭防火墙和重启防火墙

~~~
systemctl list-unit-files | grep firewalld
systemctl stop firewalld
systemctl start firewalld
~~~

![image-20211121164250989](Linux.assets\image-20211121164250989.png)



### firewall指令

在真正的生产环境，往往需要将防火墙打开，但问题来了，如果我们把防火墙打开，那么外部请求数据包就不能跟服务器监听端口通讯，这时需要打开指定的端口，如80、22、8080等

打开端口

> firewall-cmd --permanent --add-pore=端口号/协议

关闭端口

> firewall-cmd --permanet --remove-port=端口号/协议

重新载入才能生效

> firewall-cmd --reload

查询端口是否开放

> firewall-cmd --query-port=端口/协议



例：开放111端口

~~~
firewall-cmd --permanent --add-port=111/tcp
需要firewall-cmd --reload
~~~

例：再次关闭111端口

~~~
firewall-cmd --permanent --remove-port=111/tcp
需要firewall-cmd --reload
~~~





### top动态监控进程

top与ps命令很相似，他们都用来显示正在执行的进程。top和ps最大的不同是top在执行一段时间可以更新正在运行的进程。动态监控进程。

> top [选项]

| 选项    | 功能                             |
| ------- | -------------------------------- |
| -d 秒数 | 指定top命令每隔几秒更新。默认3秒 |
| -i      | 使top不显示任何闲置或者僵死进程  |
| -p      | 通过指定监控进程ID来仅仅         |

![image-20211121191454727](Linux.assets\image-20211121191454727.png)



交互操作说明：

| 操作 | 功能                      |
| ---- | ------------------------- |
| P    | 以CPU使用率排序，默认此项 |
| M    | 以内存使用率排序          |
| N    | 以PID排序                 |
| u    | 输入用户的用户名实施监控  |
| q    | 退出top                   |



例：监控tom用户

~~~
top
u 再输入tom
~~~

例：结束tom的登录

~~~
top
u 再输入tom
k 再输入bash对应的PID号
输入9 回车
~~~

例：指定系统状态更新的时间（每隔10s自动更新，默认是3s）

~~~
top -d 10
~~~





### netstat

查看系统网络情况

> netstat [选项]

选项说明：

-an 按一定顺序排列输出

-p 显示哪个进程在调用



![image-20211121193502087](Linux.assets\image-20211121193502087.png)

例：查看服务名为sshd的服务的信息

~~~
netstat -anp | grep sshd
~~~





# 十二、rpm

rpm用于互联网下载包的打包即安装工具，包含在某些Linux分发版中。它的生成具有.RPM扩展名的文件。RPM是RedHat Package Manager（RedHat软件包管理工具）的缩写，类似于windows的setup.exe，这一文件格式名称虽然打上了RedHat的标志，但理念是通用的。Linux的分发版本都有采用（suse,redhat,centos等），可以算是公认的行业标准了。



## 1、查询已安装

> rpm -qa|grep xx

一个rpm包名：firefox-60.2.2-1.el7.centos.x86_64

名称：firefox

版本号：60.2.2-1

适用操作系统：el7.centos.x86_64（表示centos7.x的64位操作系统，如果是i686、i386表示32位系统，noarch表示通用）



其他查询指令

| 指令                    | 意义                      |
| ----------------------- | ------------------------- |
| rpm -qa （grep \| xxx） | 查询所安装的所有rpm软件包 |
| rpm -q 软件包名         | 查询软件包是否安装        |
| rpm -qi 软件包名        | 查询软件包信息            |
| rpm -ql 软件包名        | 查询软件包中的文件        |
| rpm -qf 文件全路径名    | 查询文件所属的软件包      |



## 2、安装

> rpm -ivh RPM包全路径名称

参数说明：

* i=install 安装
* v=verbose 提示
* h=hash 进度条



如何找到RPM包的路径？

![image-20211122094304294](Linux.assets\image-20211122094304294.png)

![image-20211122094314371](Linux.assets\image-20211122094314371.png)

然后复制到/opt目录下，再进行安装





## 3、卸载

> rpm -e RPM包的名称

有些软件包会依赖我想卸载的软件包，如果我想强制卸载

> rpm -e --nodeps RPM包的名称







# 十三、yum

yum（yellow dog updater modified）是一个shell前端软件包管理器。基于rpm包管理，能够从指定的服务器自动下载rpm包并安装，可以自动处理依赖性关系，并且一次安装所有依赖的安装包



## 1、查询

查询yum服务器是否有需要安装的软件

> yum list | grep xx 软件列表



## 2、安装

> yum install xxx







# 十四、Shell编程



## 1、基础知识

Shell是一个命令行解释器，为用户提供了一个向Linux内核发送请求以便运行程序的界面系统级程序，用户可以用Shell来启动、挂起、停止或者编写一些程序。

![image-20211122141634694](Linux.assets\image-20211122141634694.png)



**脚本的格式要求**

1. 脚本以#!/bin/bash开头
2. 脚本需要有可执行权限



**编写第一个Shell脚本**

创建一个Shell脚本，输出Hello World（不用sh）

![image-20211122142429790](Linux.assets\image-20211122142429790.png)

![image-20211122142607368](Linux.assets\image-20211122142607368.png)

![image-20211122142502960](Linux.assets\image-20211122142502960.png)

![image-20211122142712005](Linux.assets\image-20211122142712005.png)

![image-20211122142728655](Linux.assets\image-20211122142728655.png)



**脚本的常用执行方式**

方式1：输入脚本的绝对路径或相对路径

* 首先要赋予helloworld.sh脚本的+x权限再执行脚本

方式2：sh+脚本

* 不用赋予脚本+x权限，直接执行即可

  ![image-20211122142922221](Linux.assets\image-20211122142922221.png)



**多行注释**

> :<<!
>
> ​	内容
>
> !



## 2、变量

Linux Shell变量分为**系统变量**和**用户自定义变量**。

**系统变量**：$HOME、$PWD、$SHELL、$USER等



显示当前shell中所有变量

> set



**基本语法**

1. 定义变量：变量=值
2. 撤销变量：unset 变量
3. 声明静态变量：readonly变量（不能unset）

<img src="Linux.assets\image-20211122144501574.png" alt="image-20211122144501574" style="zoom:80%;" />

<img src="Linux.assets\image-20211122144620746.png" alt="image-20211122144620746" style="zoom:80%;" />



**定义变量规则**

1. 变量名称可以由字母、数字和下划线组成，但是不能以数字开头
2. 等号两侧不能有空格
3. 变量名称一般习惯为大写
4. A=\`date\`反引号（tab上面那个键），运行里面的命令并把结果返回给变量A
5. A=$(date)等价于反引号





## 3、设置环境变量

**基本语法**

将shell变量输出为环境变量（全局变量）

> export 变量名 = 变量值 

让修改后的配置信息立即生效

> source 配置文件

查询环境变量的值

> echo $变量名





## 4、位置参数变量

当我们执行一个shell脚本时，如果希望获取到命令行的参数信息，就可以使用到位置参数变量。

比如： ./myshell.sh 100 200 ，这就是一个执行shell的命令行，可以在myshell脚本中获取到参数信息



**基本语法**

n为数字，$0代表命令本身，$1-$9代表第一到第九个参数，十以上的参数需要用大括号如${10}

> $n

这个变量代表命令行中的所有参数，$*把所有的参数看成一个整体

> $*

这个变量也代表命令行中所有参数，不过$@把每个参数区分对待

> $@

这个变量代表命令行中所有参数的个数

> $#

<img src="Linux.assets\image-20211122151715185.png" alt="image-20211122151715185" style="zoom:80%;" />

![image-20211122151752128](Linux.assets\image-20211122151752128.png)





## 5、预定义变量

shell设计者事先已经定义好的变量，可以直接在shell脚本中使用



**基本语法**

当前进程的进程号（PID）

> $$

后台运行的最后一个进程的进程号

> $!

最后一次执行的命令的返回状态，如果这个变量值为0，证明上一个命令正确执行；如果这个变量的值非0，证明上一个命令执行不正确

> $?



![image-20211123104411843](Linux.assets\image-20211123104411843.png)

![image-20211123104452375](Linux.assets\image-20211123104452375.png)



## 6、运算符



**基本语法**

1. "$((运算式))" 或 "$[运算式]" 或 expr m + n
   * 注意：expr运算符之间有空格

2. expr \\*、/、% 乘 除 取余



例：计算（2+3）×4的值

~~~shell
#!/bin/bash
res=$[(2+3)*4]
echo "(2+3)x4=$res"
~~~

![image-20211123110254016](Linux.assets\image-20211123110254016.png)

例：求出命令行的两个参数的和

~~~shell
#!/bin/bash
SUM=$[$1+$2]
echo "和为$SUM"
~~~

![image-20211123110652897](Linux.assets\image-20211123110652897.png)





## 7、条件判断



**基本语法**

> [ condition ]

* 注意condition和中括号前后要有空格
* 非空返回true，可使用$?验证（0为true，>1为false）



**字符串比较**

> =



**两个整数的比较**

> -lt	小于
>
> -le	小于等于
>
> -eq	等于
>
> -gt	大于
>
> -ge	大于等于
>
> -ne	不等于



**按照文件权限进行判断**

> -r	有读的权限
>
> -w	有写的权限
>
> -x	有执行的权限



**按照文件类型进行判断**

> -f	文件存在并且是一个常规的文件
>
> -e	文件存在
>
> -d	文件存在并且是一个目录



例："ok"是否等于"ok"

~~~shell
#!/bin/bash
if [ "ok" == "ok" ]
then
        echo "equal"
fi
~~~

例：23是否大于22

~~~shell
#!/bin/bash
if [ 23 gt 22 ]
then
        echo "gt"
fi
~~~

例：/root/shcode/aaa.txt目录中的文件是否存在

~~~shell
#!/bin/bash
if [ -f /root/shcode/aaa.txt ]
then
        echo "yes"
fi
~~~





## 8、流程控制



### if语句

**基本语法**

> if [ 条件判断式 ]
>
> then
>
> ​	代码
>
> fi



> if [条件判断式]
>
> then 
>
> ​	代码
>
> elif [ 条件判断式子 ]
>
> then
>
> ​	代码
>
> else
>
> ​	代码
>
> fi

* 注意[ 条件判断式 ]，中括号和判断式间必须有空格



例：编写shell程序，输入参数大于输出及格，小于60输出不及格

~~~shell
#!/bin/bash
score=$1
if [ $score -ge 60 -a $score -le 100 ]
then
        echo "及格"
elif [ $score -lt 60 -a $score -ge 0 ]
then
        echo "不及格"
else
        echo "无效成绩"
fi
~~~

![image-20211123114123643](Linux.assets\image-20211123114123643.png)





### case语句

**基本语法**

> case $变量名 in 
>
> "值1")
>
> 如果变量的值等于“值1”，则执行程序
>
> ;;
>
> "值2")
>
> 如果变量的值等于“值2”，则执行程序
>
> ;;
>
> *)
>
> 如果变量的值都不是以上值，则执行此程序
>
> ;;
>
> esac



例：当命令行参数为“1”时，输出“周一”，为“2”时输出“周二”，其他情况输出“other”

~~~shell
#!/bin/bash
day=$1
case $day in
"1")
        echo "周一"
;;
"2")
        echo "周二"
;;
*)
        echo "other"
;;
esac
~~~

![image-20211123114939388](Linux.assets\image-20211123114939388.png)







### for循环

**基本语法1**

> for 变量 in 值1 值2 值3...
>
> do
>
> ​	程序
>
> done

**基本语法2**

> for ((初始值;循环控制条件;变量变化))
>
> do
>
> ​	程序
>
> done



例：打印命令行输入的参数

~~~shell
#!/bin/bash
for i in "$*"
do
        echo "num is $i"
done

echo "============="

for j in "$@"
do
        echo "num is $j"
done
~~~

![image-20211123133734011](Linux.assets\image-20211123133734011.png)

![image-20211123133824115](Linux.assets\image-20211123133824115.png)

例：从1加到100并输出结果

~~~shell
#!/bin/bash
SUM=0
for((i=1; i<=100; i++))
do
        SUM=$[$SUM+$i]
done
echo "1-100的和为：$SUM"
~~~

例：从1加到参数的和

~~~shell
#!/bin/bash
SUM=0
END=$1
for((i=1; i<=$1; ++i))
do
        SUM=$[$SUM+$i]
done
echo "1-$1 的和为：$SUM"
~~~



### while循环

**基本语法**

> while [ 条件判断式 ]
>
> do
>
> ​	程序
>
> done

* 条件判断式和中括号有空格

例：统计从1到n的和

~~~shell
#!/bin/bash
SUM=0
i=0
while [ $i -le $1 ]
do
        SUM=$[$SUM+$i]
        i=$[$i+1]
done
echo "1到$1 的和为：$SUM"
~~~

![image-20211123140642479](Linux.assets\image-20211123140642479.png)





## 9、read读取控制台输入

**基本语法**

> read (选项) (参数)

选项：

* -p：指定读取值时的提示符
* -t：指定读取值时的等待时间（秒），如果没有在指定的时间内输入就不再等待

参数：

* 变量：指定读取值的变量名



例：读取控制台输入一个num1值

~~~shell
#!/bin/bash
read -p "请输入一个数num1=" NUM1
echo "你输入的数为：$NUM1"
~~~

例：读取控制台输入一个num2值，在5秒内输入

~~~shell
#!/bin/bash
read -t 5 -p "请输入一个数NUM2=" NUM2
echo "你输入的数为：$NUM2"
~~~



## 10、函数

shell编程和其他编程语言一样，有系统函数，也可以自定义函数。



### 系统函数

**basename**

功能：返回完整路径最后/的部分，常用于获取文件名

> basename [pathname] [suffix]

功能：basename命令会删掉所有的前缀包括最后一个/字符，然后将字符串显示出来

> basename [string] [suffix]

suffix为后缀，如果suffix被指定了，basename会将pathname或string中的suffix去掉



例：返回/home/aaa/test.txt的"text.txt"部分和去掉.txt的部分

~~~shell
basename /home/aaa/test.txt
basename /home/aaa/test.txt .txt
~~~

![image-20211123142447854](Linux.assets\image-20211123142447854.png)





**dirname**

返回完整路径最后/的前面部分，常用于返回路径部分

> dirname 文件绝对路径



例：返回/home/aaa/test.txt的/home/aaa

~~~
dirname /home/aaa/test.txt
~~~

![image-20211123142743793](Linux.assets\image-20211123142743793.png)







### 自定义函数

**基本语法**

> [ function ] funname[()]
>
> {
>
> ​	Action;
>
> ​	[return int;]
>
> }

调用直接写函数名：funname [值]



例：计算输入两个参数的和

~~~shell
#!/bin/bash
function getSum() {
        SUM = $[$n1+$n2]
        echo "$n1 和 $n2 的和为：$SUM"
}

read -p "输入一个数n1：" n1
read -p "输入一个数n2：" n2

getSum $n1 $n2
~~~

![image-20211123143614566](Linux.assets\image-20211123143614566.png)













