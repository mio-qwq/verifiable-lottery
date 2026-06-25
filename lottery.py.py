import hashlib
from typing import List, Dict, Any

def sha256(text: str) -> str:
    """计算 SHA256 哈希，返回 64 位十六进制字符串"""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def draw_lottery(secret_seed: str, participant_inputs: List[str]) -> Dict[str, Any]:
    """
    核心抽奖函数（只做一件事：根据种子和参与者输入确定唯一获奖者）
    
    参数：
    1. secret_seed: str —— 秘密种子（开奖时才公布）
    2. participant_inputs: List[str] —— 所有参与者提交的字符串列表
       （每个字符串对应一个参与者，可以是任意内容）
    
    返回值：包含中奖信息的字典
    """
    if not participant_inputs:
        raise ValueError("参与者列表不能为空")
    
    N = len(participant_inputs)
    
    # 第一步：为每个参与者计算哈希，并创建带索引的列表（方便后面找回原始输入）
    participants = []
    for i, user_input in enumerate(participant_inputs):
        user_hash = sha256(user_input)
        participants.append({
            "index": i,                    # 原始列表中的位置
            "input": user_input,           # 参与者提交的原始字符串
            "user_hash": user_hash
        })
    
    # 第二步：按每个参与者的 user_hash 字典序排序（关键！保证顺序固定且公平）
    # 这样无论参与者提交顺序如何，最终排序结果都唯一确定
    sorted_participants = sorted(participants, key=lambda p: p["user_hash"])
    
    # 第三步：准备拼接大字符串
    # 先放种子的哈希
    seed_hash = sha256(secret_seed)
    combined = seed_hash
    
    # 再依次拼接所有排序后的参与者哈希
    for p in sorted_participants:
        combined += p["user_hash"]
    
    # 第四步：对这个超级长的字符串再做一次 SHA256，得到最终随机数
    final_hash = sha256(combined)
    final_int = int(final_hash, 16)      # 转成大整数
    
    # 第五步：取模决定获奖者索引
    winner_index = final_int % N
    
    # 第六步：取出中奖者信息
    winner = sorted_participants[winner_index]
    
    return {
        "winner_original_index": winner["index"],      # 在传入列表中的位置
        "winner_input": winner["input"],               # 参与者自己提交的字符串
        "winner_user_hash": winner["user_hash"],
        "final_hash": final_hash,
        "seed_hash": seed_hash,
        "total_participants": N,
        "winner_position_after_sort": winner_index     # 排序后列表中的位置
    }


# 
#
#
#
#
#
#
#
#
if __name__ == "__main__":
    # 数据
    test_inputs = [
        "参与者A的随1机字符串123",
        "hello worl1d 测1试",
        "Bob的超级长1随机数xxxxxxxxxxxxxxxxxxxxxxx",
        "中文测试字符1串哈哈1哈",
        "rando1m456"
    ]
    
    secret = "121231243waerwer"
    
    result = draw_lottery(secret, test_inputs)
    
    print("抽奖完成！")
    print("中奖者提交的内容:", result["winner_input"])
    print("最终哈希值:", result["final_hash"])
    print("总参与人数:", result["total_participants"])
    print("中奖者在排序后列表中的位置:", result["winner_position_after_sort"])