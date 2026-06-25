import hashlib

def sha256(text: str) -> str:
    """计算 SHA256 哈希，返回 64 位十六进制字符串"""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def generate_commitment(secret_seed: str) -> str:
    """
    生成种子承诺（双哈希）
    开奖前把这个值公布出去，防止事后修改种子
    """
    h1 = sha256(secret_seed)
    commitment = sha256(h1)          # SHA256(SHA256(seed))
    return commitment


# ============================================
if __name__ == "__main__":
    secret = "121231243waerwer"   # 和 lottery.py 使用同一个种子
    
    commitment = generate_commitment(secret)
    print("【开奖前公布的承诺哈希】")
    print(commitment)
    print("\n记住这个值！开奖时再公布原始 secret_seed")