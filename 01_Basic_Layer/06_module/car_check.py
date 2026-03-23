# car_check.py - 小车校验模块（存校验函数）
# 导入配置模块的常量
from car_config import MAX_SPEED, MIN_SPEED, VALID_DIRS

# 速度校验函数
def check_speed(original_speed):
    if original_speed > MAX_SPEED:
        print(f"⚠️ 速度超标（{original_speed}），修正为{MAX_SPEED}")
        return MAX_SPEED
    elif original_speed < MIN_SPEED:
        print(f"⚠️ 速度过低（{original_speed}），修正为{MIN_SPEED}")
        return MIN_SPEED
    return original_speed

# 方向校验函数
def check_direction(direction):
    if direction not in VALID_DIRS:
        print(f"❌ 方向非法（{direction}）")
        return False
    return True

# 距离校验函数
def check_distance(distance):
    if distance <= 0:
        print("❌ 距离非法（≤0）")
        return False
    return True