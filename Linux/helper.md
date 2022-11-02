## Linux目录说明

#### 1. 一级目录

|目录|作用|
|--|--|
|/bin/|存放系统命令的目录，普通用户和root都可以执行，放在bin下的命令在单用户模式下也可以执行|
|/sbin/|保存与系统环境设置相关的命令，只有root可以使用这些命令进行系统环境设置，但是有些命令可以允许普通用户查看|
|/usr/bin/|存放系统命令的目录，普通用户和超级用户都可以执行。这些命令和系统启动无关，在单用户模式下不能执行|
|/usr/sbin/|存放根文件系统不必要的系统管理命令，如多数服务程序，只有root可以用|
|/boot/|系统启动目录，保存与系统启动相关的文件，如内核文件和启动引导程序grub文件等|
|/dev/|设备文件保存位置|
|/etc/|配置文件保存位置。系统内所有采用默认安装方式（rpm安装）的服务配置文件全部保存在此目录中，如用户信息、服务的启动脚本、常用服务的配置文件等。|
|/home/|普通用户的宿主目录。在创建用户时，每个人用户要有一个默认登录和保存自己数据的位置，就是用户的宿主目录，所有普通用户的宿主目录是在/home/下建立一个和用户名相同名的目录。如用户joe的宿主目录就是/home/joe|
|/lib/|系统调用的函数库保存位置|
|/lost+found/|当系统意外崩溃或意外关机时，产生的一些文件碎片会存放在这里。在系统启动的过程中，fsck工具会检查这里，并修复已经损坏的文件系统。这个目录只在每个分区中出现，例如，/lost+found就是根分区的备份恢复目录，/boot/lost+found就是/boot分区的备份恢复目录|
|/media/|挂载目录。系统建议是用来挂载媒体设备的，如软盘和光盘|
|/mnt/|挂载目录。早期Linux中只有这一个挂载目录，并没有细分。现在系统建议这个目录用来挂载额外的设配，如U盘、移动硬盘和其他操作系统的分区|
|/misc/|挂载目录。系统建议用来挂载NFS服务的共享目录。虽然系统准备了三个默认挂载目录/media/、/mnt/、/misc/，但是到底在哪个目录中挂载什么设备可以有管理员自己决定。|

#### 2. 二级目录

|目录|作用|
|--|--|
|/opt/|第三方安装的软件保存位置。这个目录是放置和安装其他软件的位置，手工安装的源码包软件都可以安装到这个目录中。|
|/proc/|虚拟文件系统。该目录中的数据并不保存在硬盘上，而是保存在内存中。主要保存系统的内核、进程、外部设备状态和网络状态等。如/proc/cpuinfo是保存CPU信息。|
|/sys/|虚拟文件系统。与/proc/目录类似，该目录中的数据都保存在内存中，主要保存与内核相关信息|
|/root/|root的宿主目录。普通用宿主目录在/home/下，root宿主目录在/下|
|/srv/|服务数据目录。一些系统服务启动之后，可以在这个目录中保存所需要的数据|
|/tmp/|临时目录。系统存放临时文件的目录，在该目录下，所有用户都可以访问和写入。建议此目录中不能保存重要数据，最好每次开机把该目录清空|
|/usr/|系统软件资源目录，注意usr不是user的缩写，而是"Unix software resource"的缩写，，所以不是存放用户数据的目录，而是存放系统软件资源的目录。系统中安装的软件大多数保存在这里。|
|/usr/lib/|应用程序调用的函数库保存的位置|
|/usr/X11R6|图形界面系统保存位置|
|/usr/local/|手工安装的软件保存位置。一般建议源代码包软件安装在这个位置|
|/usr/share/|应用程序的资源文件保存位置。如帮助文档、说明文档和字体目录|
|/usr/src/|源码包保存位置。手工下载的源码包和内核源码包都可以保存到这里。|
|/var/|动态数据保存位置。主要保存缓存、日志以及软件运行所产生的文件|
|/var/www/|RPM包安装的Apache的网页主目录|
|/var/lib/|程序运行中需要调用或改变的数据保存位置。如MySQL的数据库保存在/var/lib/mysql/目录中|
|/var/log/|系统日志保存位置|
|/var/run/|一些服务和程序运行后，它们的PID保存的位置|
|/var/spool/|放置队列数据的目录。即排队等待其他程序使用的数据，比如邮件队列和打印队列|
|/var/spool/mail/|新收到的邮件队列保存位置。系统新收到的邮件会保存在此目录中|
|/var/spool/cron/|系统的定时任务队列保存位置。系统的计划任务会保存在这里|