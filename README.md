# Verifiable Lottery - 可验证公平抽奖系统

一个基于密码学承诺（Commit-Reveal）机制的**完全公开、可验证、不可操纵**的抽奖方案，专为小团体、社群、活动设计。

## ✨ 核心特性

- **事前承诺**：开奖前公布种子双哈希，防止事后修改结果
- **公开透明**：算法完全开源，任何人都可以独立验证
- **公平排序**：按参与者提交内容的 SHA256 哈希字典序排序，杜绝顺序作弊
- **支持任意输入**：参与者可提交任意字符串（不一定是纯数字）
- **密码学安全**：基于 SHA-256 + Commit-Reveal 模式
- **极简实现**：核心逻辑只有一个函数

## 🛠 使用流程

### 1. 开奖前（准备阶段）

1. 组织者运行 `commit_seed.py` 生成**种子承诺哈希**并公开，且注意一定要在收集参与者提交的随机字符串之前公开。
2. 收集所有参与者提交的随机字符串（可通过群聊、表单等方式）；为了防止一些攻击，一旦开始收集，本次抽奖不可终止。
3. 公布本项目代码和抽奖规则

### 2. 开奖阶段

1. 组织者公布原始 `secret_seed`
2. 运行 `lottery.py` 中的 `draw_lottery()` 函数得到中奖者
3. 公布结果

### 3. 验证阶段

任何人都可以用公布的 `secret_seed` + 所有参与者输入，重新运行抽奖函数验证结果是否正确。

## 📁 项目文件

- `lottery.py` —— 核心抽奖函数（主文件）
- `commit_seed.py` —— 生成开奖前承诺哈希
- `README.md` —— 本说明文件

## 🚀 快速开始

```bash
# 克隆项目
git clone https://github.com/mio-qwq/verifiable-lottery.git
cd verifiable-lottery

# 生成承诺哈希（开奖前执行）
python commit_seed.py

# 开奖（结束时执行）
python lottery.py
```

密码学原理

使用双哈希承诺：commitment = SHA256(SHA256(secret_seed))
参与者按自身输入的 SHA256 值排序
最终结果 = SHA256(seed_hash + sorted_user_hashes...) % N
整个过程完全确定性且公开可验证

⚠️ 注意事项

secret_seed 必须具有足够熵（建议使用长随机字符串）
参与者列表必须在开奖前固定，不能中途增删
本方案适合小团体信任场景（几十到几百人），不适合超大规模抽奖

📄 License

MIT License - 欢迎大家自由使用和改进

Made with ❤️ for fair and transparent communities

text---

### 使用建议

1. 把上面两个代码文件（`lottery.py` 和 `commit_seed.py`）一起上传
2. 把这个 `README.md` 也放进去
3. 在 GitHub 创建仓库时选择 **Public**（公开）
4. 可以再加一个 `.gitignore` 文件忽略 `__pycache__` 等

---

