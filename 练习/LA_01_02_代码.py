"""
LA_01_02《坐标系》· 本节完整代码
===================================
《线性代数》| 鸢尾花书:数学不难

配套讲义: 讲义/LA_01_02_坐标系.html
教材原文: LA_01_02_坐标系.pdf
教材代码: LA_01_02_01.ipynb / LA_01_02_02.ipynb / LA_01_02_03.ipynb

怎么用
------
方式 A(推荐): 在项目根目录跑整个文件
    python 练习/LA_01_02_代码.py

方式 B: 打开 python 交互窗口,按小点整段复制粘贴。
    每一小点都是【自包含】的 —— import 和变量定义都齐全,
    单独粘任何一段都能跑,不依赖前面跑过什么。
"""

import numpy as np


def 标题(s):
    print("\n" + "=" * 60)
    print("  " + s)
    print("=" * 60)


# =====================================================================
# 小点 ③-1  np.arange() 造一维数组
# =====================================================================
def 小点3_arange():
    标题("小点 ③-1  np.arange() —— 含头不含尾")

    import numpy as np

    # np.arange(start, stop, step)
    # 从 start 开始,每次加 step,一直到 stop —— 但 stop 本身【不包含】
    print("np.arange(-1, 2, 1)  ->", np.arange(-1, 2, 1))
    print("np.arange(0, 5, 1)   ->", np.arange(0, 5, 1))
    print("np.arange(0, 4, 1)   ->", np.arange(0, 4, 1))
    print()
    print("注意后两行: 写 5 才能取到 4,写 4 只到 3。")


# =====================================================================
# 小点 ③-2  np.meshgrid() 造二维网格
# =====================================================================
def 小点3_meshgrid():
    标题("小点 ③-2  np.meshgrid() —— 两个一维 → 两个二维")

    import numpy as np

    x1 = np.arange(-1, 2, 1)          # [-1  0  1]
    x2 = np.arange(-1, 2, 1)          # [-1  0  1]

    # 左边两个变量接住两个返回值,这叫【解包】unpacking
    xx1, xx2 = np.meshgrid(x1, x2)

    print("x1 =", x1, "  shape =", x1.shape, "  ndim =", x1.ndim)
    print()
    print("xx1 = 所有格点的 x1 坐标(x1 横着放,一行行往下复制)")
    print(xx1)
    print("shape =", xx1.shape, "  ndim =", xx1.ndim)
    print()
    print("xx2 = 所有格点的 x2 坐标(x2 竖着放,一列列往右复制)")
    print(xx2)
    print("shape =", xx2.shape, "  ndim =", xx2.ndim)

    print()
    print("--- 要定位一个格点,必须同时查两个数组的同一位置 ---")
    for (r, c) in [(0, 0), (0, 2), (2, 0), (1, 1)]:
        print(f"  [{r}][{c}] -> ({xx1[r][c]:2d}, {xx2[r][c]:2d})")

    print()
    print("--- 向量化: 一行算完 9 个点到原点的距离平方,不用写循环 ---")
    print(xx1**2 + xx2**2)


# =====================================================================
# 小点 ③-3  坑一: shape 的顺序是反的
# =====================================================================
def 小点3_坑一():
    标题("小点 ③-3  坑一 —— shape = (len(x2), len(x1))")

    import numpy as np

    x1 = np.arange(0, 3, 1)           # [0 1 2]   3 个数
    x2 = np.arange(0, 2, 1)           # [0 1]     2 个数

    xx1, xx2 = np.meshgrid(x1, x2)

    print("len(x1) =", len(x1), "  len(x2) =", len(x2))
    print()
    print("xx1 ="); print(xx1)
    print("shape =", xx1.shape, "  <- 是 (2,3),不是 (3,2)!")
    print()
    print("x1 管水平方向 -> 决定【列数】")
    print("x2 管竖直方向 -> 决定【行数】")
    print("而 shape 写成 (行数, 列数),所以顺序反过来了。")

    print()
    print("--- 三维也一样,只有前两个对调 ---")
    a1 = np.arange(0, 3, 1)           # 3
    a2 = np.arange(0, 5, 1)           # 5
    a3 = np.arange(0, 7, 1)           # 7
    A1, A2, A3 = np.meshgrid(a1, a2, a3)
    print(f"len = {len(a1)}, {len(a2)}, {len(a3)}   ->   shape = {A1.shape}")
    print("规律: (len(x2), len(x1), len(x3))")


# =====================================================================
# 小点 ③-4  坑二: xx2 上下是反的
# =====================================================================
def 小点3_坑二():
    标题("小点 ③-4  坑二 —— xx2 负数在上、正数在下")

    import numpy as np

    x2 = np.arange(-2, 3, 1)          # [-2 -1  0  1  2]  从小到大
    xx1, xx2 = np.meshgrid(x2, x2)

    print("x2 =", x2, "  (从小到大)")
    print()
    print("xx2 =")
    print(xx2)
    print()
    print("第 0 行是 -2(最上面),第 4 行是 2(最下面) —— 跟数学图的直觉相反。")
    print("原因: 数组的行号往下递增,而数学的 x2 轴往上递增。两者是反的。")


# =====================================================================
# 小点 ④-1  单位向量与向量分解
# =====================================================================
def 小点4_分解():
    标题("小点 ④-1  单位向量 e1 e2 与向量分解")

    import numpy as np

    # 【这两行就是之前缺的】没有它们,后面用 e1 就会 NameError
    e1 = np.array([1, 0])
    e2 = np.array([0, 1])

    print("e1 =", e1, "  长度 =", np.linalg.norm(e1))
    print("e2 =", e2, "  长度 =", np.linalg.norm(e2))
    print("长度为 1 的向量叫【单位向量】")

    print()
    print("--- 向量分解: x = x1*e1 + x2*e2 ---")
    x = np.array([2, 3])
    print("x           =", x)
    print("2*e1        =", 2 * e1, "   <- 沿 x1 方向走 2 步")
    print("3*e2        =", 3 * e2, "   <- 沿 x2 方向走 3 步")
    print("2*e1 + 3*e2 =", 2 * e1 + 3 * e2, "   <- 拼回来了")
    print("完全相等吗?", np.array_equal(x, 2 * e1 + 3 * e2))

    print()
    print("--- 颜色对照 ---")
    print("  [0,0] 纯黑(零向量)   [1,0] 纯红=e1")
    print("  [0,1] 纯绿=e2        [1,1] 黄 = 红光+绿光")


# =====================================================================
# 小点 ④-2  换基底 —— 本节最重要的演示
# =====================================================================
def 小点4_换基底():
    标题("小点 ④-2  换基底 —— 同一个箭头,坐标却变了")

    import numpy as np

    x = np.array([2, 3])

    # 新基底: 拿另外两个向量当"尺子"
    b1 = np.array([1, 1])
    b2 = np.array([1, -1])

    # 解方程 c1*b1 + c2*b2 = x
    # np.column_stack 把 b1 b2 按【列】拼成矩阵
    B = np.column_stack([b1, b2])
    c = np.linalg.solve(B, x)         # 解线性方程组

    print("箭头 x =", x, " (一动没动)")
    print()
    print("用标准基底 e1 e2 量  ->  坐标 = [2, 3]")
    print("新基底 b1 =", b1, " b2 =", b2)
    print("用新基底 b1 b2 量    ->  坐标 =", c)
    print()
    print("验算:", c[0], "* b1 +", c[1], "* b2 =", c[0] * b1 + c[1] * b2)
    print()
    print(">>> 结论: 坐标不是向量自带的属性,")
    print(">>>       而是【拿某组基底去量它】量出来的结果。")
    print(">>>       换一把尺子,同一个东西就是另一串数字。—— 这就是 PCA 的种子")


# =====================================================================
# 小点 ⑤  三维: 单位向量、手性与行列式
# =====================================================================
def 小点5_三维():
    标题("小点 ⑤  三维坐标系 —— 右手系 vs 左手系")

    import numpy as np

    e1 = np.array([1, 0, 0])
    e2 = np.array([0, 1, 0])
    e3 = np.array([0, 0, 1])

    for 名, e in [("e1", e1), ("e2", e2), ("e3", e3)]:
        print(f"  {名} = {e}   长度 = {np.linalg.norm(e)}")

    x = np.array([2, 3, 5])
    print()
    print("x =", x, " = 2*e1 + 3*e2 + 5*e3 =", 2 * e1 + 3 * e2 + 5 * e3)

    print()
    print("--- 手性 = 行列式的符号 ---")
    R = np.column_stack([e1, e2,  e3])    # 右手系
    L = np.column_stack([e1, e2, -e3])    # 把 x3 倒过来 -> 左手系

    print("右手系三根轴的行列式 =", np.linalg.det(R))
    print("左手系三根轴的行列式 =", np.linalg.det(L))
    print("只是把 x3 倒过来,符号就翻了。(第 4 章会正式讲行列式)")

    print()
    print("--- 三维 meshgrid ---")
    a = np.arange(-4, 5, 1)
    A1, A2, A3 = np.meshgrid(a, a, a)
    print("A1.shape =", A1.shape, " ndim =", A1.ndim, " 总格点数 =", A1.size)


# =====================================================================
# 小点 ⑥  向量长度(L2 范数)
# =====================================================================
def 小点6_范数():
    标题("小点 ⑥  向量长度 L2 范数 —— 就是勾股定理")

    import numpy as np

    print("linalg = linear algebra(线性代数)的缩写,是 NumPy 的子模块")
    print()
    print(f"{'向量':<14}{'np.linalg.norm':<18}{'手算 sqrt(sum(xi^2))'}")
    print("-" * 55)

    for v in [np.array([3, 4]), np.array([1, 2, 2]),
              np.array([0, 0]), np.array([1, 0])]:
        库函数 = np.linalg.norm(v)
        手算 = np.sqrt(np.sum(v ** 2))
        print(f"{str(v):<14}{库函数:<18.4f}{手算:.4f}")

    print()
    print("两列完全一致 —— np.linalg.norm() 没有魔法,就是在做勾股定理。")

    print()
    print("--- 括号别写错(常见报错) ---")
    print("  np.linalg.norm(3, 4)    -> ValueError    圆括号的逗号 = 两个独立参数")
    print("  np.linalg.norm[3, 4]    -> TypeError     函数不能用方括号取下标")
    print("  np.linalg.norm([3, 4])  -> 5.0   OK      圆括号调用 + 方括号列表")

    print()
    print("零向量长度 = 0 | 非零向量长度 > 0 | 单位向量长度 = 1")


# =====================================================================
if __name__ == "__main__":
    小点3_arange()
    小点3_meshgrid()
    小点3_坑一()
    小点3_坑二()
    小点4_分解()
    小点4_换基底()
    小点5_三维()
    小点6_范数()

    print("\n" + "=" * 60)
    print("  全部跑完。对照讲义: 讲义/LA_01_02_坐标系.html")
    print("=" * 60)
