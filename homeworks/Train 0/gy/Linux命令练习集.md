# Linux命令练习集

##### 小白拼死拼活半天了解的几条输进去能动的命令和从b站上学的皮毛

1. ## 命令

   ```
   命令 -选项（附加要求） 参数（路径）
   ```

   

2. ## 目录

   ```  
   ls      看目录
   
   ls /    …………………查看根目录
   ls /*   …………………看全
   ls -a(--all)   ……………看包括隐藏文件（.×××）在内的某一目录全 部内容
   ls -l(long)    ……………长格式显示（看详细信息）
   -h(human)  ……………（人性化），至少显示文件大小用合适的单位
   -d         ……………只查看目录详细信息
   -i(id)     ……………有个代码什么的
   
   mkdir      ……………创建新目录  mkdir /tmp/ass /tmp/dxp /tmp/dsf
   mkdir -p   ……………递归创建   mkdir -p /tmp/ass/ass/in
   
   cd         ……………切换
   
   pwd        ……………显示当前目录的路径
   
   rm   	   ……………删除
   rmdir      ……………删除空目录（目录中没有任何文件或目录）
   
   cp         ……………copy(文件或目录)    cp [原文件目录] [目标目录]
   -r		   ……………复制目录
   -p         ……………保留文件属性
   ```

   

3. 英文解释

   ```
   文件：
   d开头  目录
   -开头  文件
   l开头  软连接（为什么是软的）
   
   文件用户
   u所有者
   g所有组织
   o  others
   
   权限
   r读
   w写
   x执行
   -没有权限
   
   命令
   ls      list
   -a      all
   -l      looooong
   -h      human
   mk      make
   mkdir   make directories
   cd      change directory
   pwd     print working directory
   rm      remove
   redir   remove empty directories
   cp      copy
   -r      
   ```

   

4. 文件

   ```
   名称格式
   -rwx(u)re-(g)r--(o)
   ```

   

5. 

    

