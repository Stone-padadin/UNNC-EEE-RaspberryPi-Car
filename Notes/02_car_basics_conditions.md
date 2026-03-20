# 2026-03-20 学习笔记 📝
> 主题：树莓派小车项目 - Git仓库整理 + JupyterLab配置 + Python第二课（变量运算与条件判断）

---

## 一、Git 仓库问题解决 ✅
### 1. 问题背景
GitHub 仓库中出现大量缓存文件（`.ipynb_checkpoints`、`.virtual_documents` 等），影响仓库整洁。

### 2. 核心操作
- **`.gitignore` 配置**：已添加对 Jupyter/Python/系统/IDE 缓存文件的过滤规则
- **清理已提交缓存**：
  ```bash
  git rm -r --cached .  # 清空 Git 缓存
  git add .              # 重新添加文件（应用 .gitignore）
  git commit -m "Final clean: normalize directory"
  git push -f origin master:main  # 强制推送覆盖远程
  ```
- **目录规范**：将代码整理为 `01_Basic_Layer/01_variables/` 结构，避免命名混乱

### 3. 验证标准
GitHub 仓库仅保留：`01_Basic_Layer/`、`Notes/`、`.gitignore`、`README.md`，无任何缓存文件夹。

---

## 二、JupyterLab 自动打开仓库配置 ✅
### 1. 问题背景
重启 JupyterLab 后文件「消失」，本质是默认目录未设置为仓库路径。

### 2. 核心操作
1. 生成配置文件：
   ```bash
   jupyter lab --generate-config
   ```
2. 修改配置文件 `C:\Users\123\.jupyter\jupyter_lab_config.py`：
   ```python
   # 找到并修改这一行（去掉 # 注释）
   c.ServerApp.notebook_dir = 'F:/ASUS/Desktop/UNNC-EEE-RaspberryPi-Car'
   ```
3. 重启 JupyterLab，自动进入仓库目录。

### 3. 兜底方案
- 手动右键仓库内 `.ipynb` 文件 → 用 JupyterLab 打开
- 或通过 Anaconda Prompt 启动：
  ```bash
  jupyter lab --notebook-dir=F:\ASUS\Desktop\UNNC-EEE-RaspberryPi-Car
  ```

---

## 三、Python 第二课：变量运算与条件判断 🚗
### 1. 学习目标
- 掌握 Python 变量运算（算术/赋值/比较）
- 学会 `if/elif/else` 条件判断
- 结合「小车速度控制」完成实战代码

### 2. 核心知识点
| 知识点 | 语法 | 小车场景示例 |
|--------|------|--------------|
| 赋值运算 | `+=`/`-=`/`*=` | `car_speed += 5`（加速 5km/h） |
| 比较运算 | `>`/`<`/`>=`/`<=` | `car_speed > max_speed`（判断超速） |
| 条件判断 | `if/elif/else` | `if 超速: 减速; elif 低速: 加速; else: 保持` |
| 取模运算 | `%` | `car_speed % 2 == 0`（判断速度奇偶，优化稳定性） |

### 3. 实战代码（小车速度控制）
```python
# 初始化小车参数
car_speed = 30
max_speed = 50
min_speed = 10
speed_step = 5

# 变量运算：加速/超车
car_speed += speed_step
car_speed *= 1.2

# 条件判断：自动调速
if car_speed > max_speed:
    car_speed = max_speed
    print("⚠️ 超速！已减速到最大限速")
elif car_speed < min_speed:
    car_speed = min_speed
    print("⚠️ 速度过低！已加速到最低速度")
else:
    if 20 <= car_speed <= 40:
        print("✅ 经济模式行驶")
    else:
        print("✅ 正常模式行驶")

# 奇偶优化
if car_speed % 2 != 0:
    car_speed += 1
```

### 4. 易错点提醒
- 条件判断后必须加冒号 `:`
- Python 代码块靠缩进区分，缩进必须对齐
- 赋值运算 `+=` 是「变量 = 变量 + 数值」，顺序不可颠倒

### 5. 仓库归档
- 代码文件：`01_Basic_Layer/02_Condition/02_car_speed_control.ipynb`
- 笔记文件：`Notes/02_条件判断知识点.md`
- Git 提交：
  ```bash
  git add .
  git commit -m "Add Lesson2: car speed control with condition judgment"
  git push -f origin master:main
  ```

---

## 四、今日总结 📌
1. **工程化习惯**：完成 `.gitignore` 配置 + JupyterLab 目录设置，保证代码仓库整洁、文件不丢失
2. **Python 基础**：掌握变量运算与条件判断，能结合小车场景写可运行代码
3. **学习流程**：「学习 → 实战 → 整理归档 → Git 提交」，形成闭环，便于后续复习与迭代

---

要不要我帮你把这份笔记再精简成**一页速查版**，方便你随时翻看复习？