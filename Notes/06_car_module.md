# 第六讲：Python模块与导入（import）—— 小车功能模块化实战
> 核心目标：将代码拆分为多文件模块，实现工程化开发、代码复用与高效维护

---

## 一、模块的本质与价值
### 1. 什么是模块？
- 一个 `.py` 文件就是一个**模块**，里面可以存放函数、变量、类等代码。
- 例如：`car_config.py`、`car_check.py` 都是独立模块。

### 2. 为什么要用模块？
- **代码解耦**：不同功能拆分到不同文件，避免单文件代码臃肿。
- **复用性高**：函数/常量定义一次，可在多个文件中导入使用。
- **便于维护**：修改某功能只需修改对应模块，不影响其他代码。
- **工程化基础**：真实项目都是多模块协作，为后续硬件控制铺垫。

---

## 二、模块导入的3种核心方式
| 导入方式 | 语法示例 | 特点 | 小车场景用法 |
|----------|----------|------|--------------|
| 导入整个模块 | `import car_check` | 调用时需加模块名前缀，避免命名冲突 | `car_check.check_speed(55)` |
| 导入指定成员 | `from car_config import MAX_SPEED` | 直接使用函数/变量，代码更简洁 | `MAX_SPEED` 直接参与速度校验 |
| 导入并起别名 | `import car_check as cc` | 简化调用，解决长模块名问题 | `cc.check_speed(55)` |

---

## 三、小车实战模块拆分规范
### 1. 模块职责划分
| 模块文件 | 核心职责 | 内容示例 |
|----------|----------|----------|
| `car_config.py` | 全局配置常量 | `MAX_SPEED`、`MIN_SPEED`、`VALID_DIRS` |
| `car_check.py` | 校验逻辑函数 | `check_speed()`、`check_direction()`、`check_distance()` |
| `car_stats.py` | 数据统计函数 | `calculate_stats()`（计算总距离、平均速度等） |
| `car_main.py` | 主程序入口 | 导入模块、整合逻辑、执行完整流程 |

### 2. 模块间依赖关系
- `car_check.py` 依赖 `car_config.py` 的常量（通过 `from car_config import ...` 导入）。
- `car_main.py` 依赖 `car_check.py` 和 `car_stats.py` 的函数。
- 避免**循环导入**（如A导入B，B又导入A），否则会报错。

---

## 四、关键语法与实操细节
### 1. 路径管理（Windows系统重点）
```python
import os
# 查看当前工作目录
print("当前路径：", os.getcwd())

# 切换到模块所在目录（Windows路径用r""避免转义）
target_path = r"F:\ASUS\Desktop\UNNC-EEE-RaspberryPi-Car\01_Basic_Layer\06_module"
if os.getcwd() != target_path:
    os.chdir(target_path)
```
- 注意：模块文件必须与主程序在**同一目录**，或在Python可识别的路径中。

### 2. 模块导入示例
```python
# 导入校验模块并起别名
import car_check as cc
# 导入统计模块的指定函数
from car_stats import calculate_stats
# 导入配置模块的常量
from car_config import MAX_SPEED, VALID_DIRS
```

### 3. 主程序入口规范
```python
if __name__ == "__main__":
    # 仅当直接运行此文件时，才执行主逻辑
    path_plan = [...]  # 预设路径
    valid_paths = []
    for path in path_plan:
        result = run_single_path(path)
        if result:
            valid_paths.append(result)
    stats = calculate_stats(valid_paths)
    print(stats)
```
- 作用：避免导入模块时自动执行主逻辑，仅在直接运行时触发。

---

## 五、内置模块与第三方模块
### 1. 内置模块（Python自带，无需安装）
| 模块名 | 核心用途 | 小车场景示例 |
|--------|----------|--------------|
| `math` | 数学计算 | 计算转弯角度、距离：`math.pi`、`math.sqrt()` |
| `time` | 时间控制 | 控制小车延时：`time.sleep(2)`（暂停2秒） |
| `os` | 系统操作 | 管理文件路径、切换目录：`os.chdir()` |

### 2. 第三方模块（需安装后导入）
- 示例：树莓派硬件控制库 `RPi.GPIO`
  ```bash
  # 安装命令（终端执行）
  pip install RPi.GPIO
  ```
  ```python
  # 导入并使用
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(18, GPIO.OUT)  # 配置引脚为输出模式
  ```

---

## 六、常见易错点与排查
### 1. 路径相关错误
- **报错**：`FileNotFoundError`
- **原因**：模块文件不在当前工作目录，或路径拼写错误。
- **解决**：用 `os.getcwd()` 确认路径，用 `os.chdir()` 切换到正确目录。

### 2. 导入相关错误
- **报错**：`ModuleNotFoundError` / `NameError`
- **原因**：模块名拼写错误、未导入所需函数/变量、循环导入。
- **解决**：检查模块文件名、导入语句，避免循环依赖。

### 3. 主程序未执行
- **现象**：运行后无输出。
- **原因**：主逻辑未写在 `if __name__ == "__main__":` 内，或缩进错误。
- **解决**：确保主程序代码缩进在该判断块下。

---

## 七、实战总结
1.  **模块是代码分层的核心**：将小车的配置、校验、统计功能拆分到独立文件，结构清晰。
2.  **导入是代码复用的关键**：通过 `import` 系列语法，实现跨文件调用函数与常量。
3.  **路径管理是基础**：Windows系统需特别注意路径转义与目录切换。
4.  **工程化思想**：主程序只负责整合调用，核心功能由模块提供，为后续硬件控制与复杂项目打下基础。

---

要不要我再帮你整理一份**模块导入速查表**，把常用语法和易错点做成一页纸，方便你随时查阅？