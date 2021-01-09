# 开发环境

## conda建立虚拟环境

```bash
conda create -n py37 python=3.7
```

## 激活虚拟环境

```bash
conda activate py37
```

## 安装使用的Python包

```bash
pip install SciPy numpy==1.19.3 PySide2 schemdraw
```

## 下载仓库

```bash
git clone https://github.com/OriPoin/EECalculator.git
```

# TODO

- [X] 基本的GUI框架
  - [X] 基本框架
  - [ ] 跟随系统主题
    - [X] KDE
    - [ ] Windows
- [ ] 计算器
  - [ ] 科学计算器
  - [ ] PCB 布线
  - [ ] 单位转换
  - [ ] 运放电路
  - [ ] 经典电路
    - [X] RC 滤波器截至频率
    - [X] 电容放电
    - [X] NE555 频率计算
    - [ ] 更多
  - [ ] RF
    - [ ] 巴特沃斯滤波器
- [ ] 更多
  - [ ] 支持缓存和保存
  - [ ] 使用nodejs加强我们的兼容性
  - [ ] 类似于Chromium的标签化UI界面

# 更多

&emsp;&emsp;如果你对这个项目感兴趣，请致电[OriPoin@outlook.com](mailto:OriPoin@outlook.com)，或者fork我们的仓库，根据我们的文档编写自己想要的计算器，提交pr。
