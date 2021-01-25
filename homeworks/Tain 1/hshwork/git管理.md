# git管理

## 创建版本管理库
1. 身份认定
   1. git config  --global user.name "jack"
   2. git config --global user.email "3044281868@qq.com"
2. 查看身份认定
   1. git config user.name	
   2. git config user.email
3. 创建空目录 mkdir
4. 已经进入目标文件夹后，使用`git init`*让git管理这个仓库*实现初始化。
   1. `ls `可以显示所有文件

## git常用指令
1. 查看当前状态 git status 
2.  添加到缓存区 git add 文件名  或者git add -a
3. 提交到版本库 git commit -m "注释，更改了什么"
## 时光穿梭机 版本回退
1. 查看版本，确定回退时刻点.
   1. git log 版本信息丰富id，author，date![](C:\Users\HSH\Desktop\md\屏幕截图 2021-01-24 132301.png)

   2. git log --pretty=oneline 较为简洁![](C:\Users\HSH\Desktop\md\oneline.png)

2. 进入某个版本的操作 

   1. git reset --hard 版本号

3. 重回未来 先用指令查看历史操作，以获得最新的commit id

   1. git reflog 

4. commit id不需要写完，四位就行，但要确保不重复

## 基于http协议的GitHub仓库使用

1. 创建本地文件夹，与线上名字一样
2. git clone 线上地址
3. 本地操作
4. git pull -rebase origin main
5. git push origin main 
## 如何将本地项目关联线上
1. git init 
2. git add
3. git commit -m ""
4. git remote add origin https://github... 远程关联主机
5. git pull --rebase origin main 合并本地线上仓库
6. git push origin main 推到线上仓库