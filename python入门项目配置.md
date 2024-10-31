# python入门项目环境配置

## 环境配置

工欲善其事，必先利其器。进行合理的环境配置，可以让你大大提升效率。
本人使用windows系统，vscode + python插件 + python解释器 + 虚拟环境 + git

## vscode安装和python环境配置

第三版书籍中有python和vscode配置的内容（第一章），以及git的基本操作（附录D）。这里补充了github和git bash的相关配置。

1. 下载vscode安装包并安装
2. 打开vscode，点击左下角的扩展按钮，搜索python，安装python插件
3. 下载python解释器，本人使用3.12.7版本，书中使用3.7.2版本，下载地址：`https://www.python.org/downloads/`
4. 选择解释器路径，在vscode中按f1，输入`python:select interpreter`，选择刚下载的解释器路径
5. 在终端（cmd）中输入python --version，查看版本号是否正确,确认安装成功

## git和github

### git、github安装和配置

1. 下载git安装包并安装，地址：`https://git-scm.com/downloads`
2. 注册github账号，使用github账号登录vscode，并安装github插件
3. 如果你不喜欢cmd命令行，可以将gitbash集成到VS code中
   <mark>这一步可以不做，但如果做了，可以更方便地使用git命令，且可以帮你熟悉Linux命令</mark><br>
   在vscode中更改settings.json文件，添加如下内容：

    ```json
       "terminal.integrated.profiles.windows": {
           "Git Bash": {
               "path": "D:\\developer\\Git\\bin\\bash.exe",//这里是你自己的的bash路径
           }
           },
    ```

    ```json
       "terminal.integrated.defaultProfile.windows": "Git Bash", //这里是设置默认的终端
       //假如你不熟悉linux命令，可以不更改这一条，默认使用powershell或cmd命令行也可以
    ```

   具体写法如图所示：

   ![20241031104937](https://fuyunyou-note.oss-cn-wuhan-lr.aliyuncs.com/typora-user-images/20241031104937.png)

   注意添加逗号，把新加的项和其他项隔开。如果是在文件的末尾新加项（即新加的项是最后一项），不需要添加逗号，如下图所示。

   ![20241031105553](https://fuyunyou-note.oss-cn-wuhan-lr.aliyuncs.com/typora-user-images/20241031105553.png)

4. 按" ctrl+` "(数字1左边的那个键)，可以快捷呼出终端，确认gitbash已经集成到vscode中，这样就可以使用git命令而无需另外打开gitbash窗口。

5. 使用github插件，可以方便地与github进行交互，包括创建仓库、克隆仓库、推送代码、查看修改内容等。不需要下列命令，但还是给出来：

    git的基本操作
    1. git --version 查看git版本
    2. git config --global user.name "你的用户名"
    3. git config --global user.email "你的邮箱"
    4. git init 初始化一个仓库
    5. git status 查看当前仓库状态
    6. git add "文件名"  添加文件到暂存区
    7. git commit -m "提交说明"  提交到本地仓库
    8. git push 推送到远程仓库
    9. git pull 从远程仓库拉取代码
    10. git remote add origin "仓库地址"  添加远程仓库地址

    github的基本操作
    11. 注册github账号
    12. 创建一个仓库，仓库名为你的项目名
    13. 克隆仓库到本地：`git clone 仓库地址`
    14. 在本地修改代码，然后提交到远程仓库：`git add 文件名` `git commit -m "提交说明"` `git push`
    15. 在github上查看修改内容

### 以上操作在做什么？

git是版本控制工具，可以帮助你管理代码，比如你在写代码时，可以随时保存，然后可以回到之前的版本（相当于游戏中的存档功能），也可以比较不同版本之间的差异。善用git可以极大的提升开发效率，想象一下你在写代码时，不小心把代码覆盖了，你还需要从头再来，这时，使用git，你可以很轻松地恢复到之前的版本，节省了大量时间。如果没有存档，一命通关游戏实在是太可怕了。

github是代码托管平台，你可以把你的代码放在github上，其他人可以访问，也可以与你协作。不使用github，单独使用git也是可以的，同样能进行版本控制，所有的操作都在本地进行。

vscode是代码编辑器，可以让你方便地编写代码，同时集成了git和github插件，可以让你更方便地使用git和github。不需要再输入`add`,`commit`,`push`命令，只需要在vscode中编写代码，然后点击右上角的小按钮，就可以将代码上传到github。

将gitbash集成到vscode中，可以让你在vscode中使用git命令和许多linux命令，而不用打开gitbash窗口。

<mark>注意: git bash中的操作是linux命令，文件路径是以linux风格，而不是windows风格，如果你不明白什么是linux，不熟悉linux命令，可以不更改默认终端，使用powershell或cmd命令行。</mark>

![20241031114914](https://fuyunyou-note.oss-cn-wuhan-lr.aliyuncs.com/typora-user-images/20241031114914.png)

在终端窗口的右边，展开折叠的选项卡，更换为poweshell或cmd（conmmand prompt）命令行。

## 使用python虚拟环境

### 为什么要使用虚拟环境？

python开发往往要用到许多第三方库（别人写好发布的代码，提供给你使用），不同的开发项目使用的库可能不同，如果安装在系统目录下，可能会出现版本冲突，导致项目运行异常。因此，最佳实践是使用虚拟环境，把第三方库安装在虚拟环境中，不影响系统环境。如果出现问题，可以直接删除虚拟环境，重新安装。

### 如何创建虚拟环境？

   1. 为你的项目创建一个文件夹，如myproject，进入该文件夹，打开终端（cmd）
   2. 输入命令：`python -m venv myenv`（·myenv·是你虚拟环境的名字,可以自己定义）
   3. 创建成功后，会在当前目录下生成一个名为myenv的文件夹，该文件夹就是虚拟环境。
   4. 激活虚拟环境：进入myenv\Scripts文件夹，输入命令：`activate.bat`（windows）或`source activate`（linux或mac）
   5. 激活成功后，命令行前会出现（myenv）字样，表示当前环境为myenv。
   6. 在虚拟环境中可以安装第三方库：`pip install 库名`

事实上，在任意位置使用`python -m venv myenv`命令都可以创建虚拟环境，但为了方便管理，建议在项目目录下创建虚拟环境。这样，每个项目的代码和它的依赖库都在一个文件夹中，一目了然，方便管理。作为新手，要在一开始学习的时候养成良好的文件管理，分类归纳的习惯，可以避免很多麻烦，少走许多弯路。

书中也给出了虚拟环境创建的相关内容（第18章），关于虚拟环境的更多内容，可以参考<a href="https://docs.python.org/zh-cn/3/library/venv.html">官方文档</a>、<a href="https://zhuanlan.zhihu.com/p/689181205">知乎文章</a>。
