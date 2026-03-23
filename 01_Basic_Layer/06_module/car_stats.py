# car_stats.py - 小车统计模块（存统计函数）

# 数据统计函数
def calculate_stats(valid_paths):
    if not valid_paths:
        return {"total_distance":0, "forward_distance":0, "light_count":0, "max_speed":0, "avg_speed":0}
    
    total_dist = 0
    forward_dist = 0
    light_count = 0
    speed_list = []
    
    for path in valid_paths:
        total_dist += path["distance"]
        speed_list.append(path["speed"])
        if path["direction"] == "forward":
            forward_dist += path["distance"]
        if path["light"]:
            light_count += 1
    
    max_speed = max(speed_list)
    avg_speed = round(sum(speed_list)/len(speed_list), 1)
    
    return {
        "total_distance": total_dist,
        "forward_distance": forward_dist,
        "light_count": light_count,
        "max_speed": max_speed,
        "avg_speed": avg_speed
    }