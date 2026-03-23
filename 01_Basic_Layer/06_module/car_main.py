# car_main.py - 小车主程序（导入其他模块，执行核心逻辑）
# 导入自定义模块
import car_check as cc  # 校验模块，起别名cc
from car_stats import calculate_stats  # 统计模块，只导入指定函数
from car_config import VALID_DIRS  # 配置模块，只导入常量

# 开灯判断函数（主程序专属函数）
def judge_light(speed, direction):
    if speed >= 30 and direction == "forward":
        print("✅ 速度≥30且正向行驶，打开车灯")
        return True
    return False

# 单段路径执行函数
def run_single_path(path):
    speed = path["speed"]
    direction = path["direction"]
    distance = path["distance"]
    
    # 调用校验模块的函数
    if not cc.check_distance(distance):
        return None
    if not cc.check_direction(direction):
        return None
    corrected_speed = cc.check_speed(speed)
    
    light_on = judge_light(corrected_speed, direction)
    
    return {
        "distance": distance,
        "speed": corrected_speed,
        "direction": direction,
        "light": light_on
    }

# 主程序执行
if __name__ == "__main__":
    # 预设路径
    path_plan = [
        {"speed":28, "direction":"forward", "distance":12},
        {"speed":55, "direction":"right", "distance":6},
        {"speed":5, "direction":"forward", "distance":18},
        {"speed":40, "direction":"backward", "distance":-5},
        {"speed":35, "direction":"up", "distance":10},
        {"speed":32, "direction":"forward", "distance":15}
    ]
    
    print("🚗 小车开始智能行驶！")
    valid_paths = []
    for idx, path in enumerate(path_plan):
        print(f"\n=== 执行第{idx+1}段路径 ===")
        single_result = run_single_path(path)
        if single_result:
            valid_paths.append(single_result)
            print(f"✅ 执行成功 | 方向：{single_result['direction']} | 速度：{single_result['speed']} | 距离：{single_result['distance']} | 车灯：{'开' if single_result['light'] else '关'}")
    
    # 调用统计模块的函数
    stats = calculate_stats(valid_paths)
    print("\n================ 行驶完成 ================")
    print(f"📊 总有效距离：{stats['total_distance']} 米")
    print(f"📊 正向行驶距离：{stats['forward_distance']} 米")
    print(f"📊 开灯路段数：{stats['light_count']} 段")
    print(f"📊 最高速度：{stats['max_speed']} km/h")
    print(f"📊 平均速度：{stats['avg_speed']} km/h")