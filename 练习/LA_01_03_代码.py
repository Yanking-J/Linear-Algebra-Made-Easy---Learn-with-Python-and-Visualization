"""
LA_01_03《向量加减法》· 本节完整代码
=====================================
《线性代数》| 鸢尾花书:数学不难

配套讲义: 讲义/LA_01_03_向量加减法.html
教材原文: LA_01_03_向量加减法.pdf
教材代码: LA_01_03_01.ipynb / LA_01_03_02.ipynb / LA_01_03_03.ipynb

怎么用
------
方式 A(推荐): 在项目根目录跑整个文件
    python 练习/LA_01_03_代码.py

方式 B: 打开 python 交互窗口,按小点整段复制粘贴。
    每一小点都是【自包含】的 —— import 和变量定义都齐全,
    单独粘任何一段都能跑,不依赖前面跑过什么。

注意: 带 plt 的小点会弹出图窗,关掉窗口脚本才继续往下跑。
"""

import numpy as np
import matplotlib.pyplot as plt


def 标题(s):
    print("\n" + "=" * 60)
    print("  " + s)
    print("=" * 60)


# =====================================================================
# 小点 ①  向量加法 —— 对应分量相加
# =====================================================================
def 小点1_加法():
    标题("小点 ①  向量加法 —— 对应位置分量相加")

    import numpy as np

    a_vec = np.array([4, 1])
    b_vec = np.array([1, 2])

    # 一个加号就够了 —— NumPy 自动逐个分量相加
    a_plus_b = a_vec + b_vec

    print("a       =", a_vec)
    print("b       =", b_vec)
    print("a + b   =", a_plus_b, "   <- [4+1, 1+2]")

    print()
    print("--- 对比: Python 原生 list 的 + 是【拼接】,不是加法 ---")
    print("[4, 1] + [1, 2] =", [4, 1] + [1, 2], "  <- 接成了 4 个数,不是相加!")
    print("这就是为什么做数学一定要先 np.array() 转成数组。")

    print()
    print("--- 维数必须相同,否则报错 ---")
    try:
        np.array([1, 2]) + np.array([1, 2, 3])
    except ValueError as e:
        print("np.array([1,2]) + np.array([1,2,3])  ->  ValueError")
        print("  ", e)

    print()
    print("--- RGB 三原色: 加法 = 混光 ---")
    e1 = np.array([1, 0, 0])          # 红
    e2 = np.array([0, 1, 0])          # 绿
    e3 = np.array([0, 0, 1])          # 蓝

    print("e1(红) + e2(绿) =", e1 + e2, "  黄")
    print("e1(红) + e3(蓝) =", e1 + e3, "  品红")
    print("e2(绿) + e3(蓝) =", e2 + e3, "  青")
    print("e1 + e2 + e3    =", e1 + e2 + e3, "  白")


# =====================================================================
# 小点 ②  平行四边形法则 —— 几何视角看加法
# =====================================================================
def 小点2_平行四边形法则():
    标题("小点 ②  平行四边形法则")

    import numpy as np
    import matplotlib.pyplot as plt

    a_vec = np.array([4, 1])
    b_vec = np.array([1, 2])
    a_plus_b = a_vec + b_vec

    print("a =", a_vec, " b =", b_vec, " a+b =", a_plus_b)
    print()
    print("教材原版 LA_01_03_02.ipynb 里有个小笔误:")
    print("  画向量 b 那一句 label=\"a\" 写错了,应该是 label=\"b\"")
    print("  (对照图例看:两条线都标成了 a,分不清谁是谁)")
    print("  下面的图已经改过来了。")

    plt.figure(figsize=(6, 6))

    # 向量 a:红色
    plt.quiver(0, 0, a_vec[0], a_vec[1],
               angles='xy', scale_units='xy', scale=1,
               color='r', label="a")

    # 向量 b:绿色 (教材原文这里 label 误写成 "a",已订正为 "b")
    plt.quiver(0, 0, b_vec[0], b_vec[1],
               angles='xy', scale_units='xy', scale=1,
               color='g', label="b")

    # 向量 a + b:紫红色,是平行四边形的对角线
    plt.quiver(0, 0, a_plus_b[0], a_plus_b[1],
               angles='xy', scale_units='xy', scale=1,
               color='m', label="a + b")

    # 补全平行四边形的另外两条边(虚线)
    plt.plot([b_vec[0], a_plus_b[0]], [b_vec[1], a_plus_b[1]], 'k--')
    plt.plot([a_vec[0], a_plus_b[0]], [a_vec[1], a_plus_b[1]], 'k--')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(0, 6)
    plt.ylim(0, 4)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', alpha=0.8, linestyle='-', linewidth=0.25)
    plt.legend()
    plt.title("平行四边形法则: a + b 是对角线")

    print()
    print("窗口弹出后看两条虚线 —— 它们和 a、b 分别平行,")
    print("四条边围成一个平行四边形,a+b 正是那条对角线。")
    print("关掉图窗,脚本才会继续往下跑。")
    plt.show()

    print()
    print("--- 零向量是加法单位元 ---")
    zero = np.array([0, 0])
    print("a + 0 =", a_vec + zero, "  <- 加零向量,自己不变")


# =====================================================================
# 小点 ④  三角形法则与交换律
# =====================================================================
def 小点4_三角形法则():
    标题("小点 ④  三角形法则与交换律")

    import numpy as np
    import matplotlib.pyplot as plt

    a_vec = np.array([4, 1])
    b_vec = np.array([1, 2])
    a_plus_b = a_vec + b_vec

    print("三角形法则: 把 b 的起点挪到 a 的终点,")
    print("从 a 的起点指向 b 的终点的箭头,就是 a + b。")
    print("跟平行四边形法则比,少画两条虚线,直接是个三角形。")

    plt.figure(figsize=(6, 6))

    # 先走 a:从原点出发
    plt.quiver(0, 0, a_vec[0], a_vec[1],
               angles='xy', scale_units='xy', scale=1,
               color='r', label="a")

    # 再走 b:起点挪到 a 的终点 (a_vec[0], a_vec[1])
    plt.quiver(a_vec[0], a_vec[1], b_vec[0], b_vec[1],
               angles='xy', scale_units='xy', scale=1,
               color='g', label="b (起点在 a 的终点)")

    # 结果 a+b:从原点直接指向终点
    plt.quiver(0, 0, a_plus_b[0], a_plus_b[1],
               angles='xy', scale_units='xy', scale=1,
               color='m', label="a + b")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(0, 6)
    plt.ylim(0, 4)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', alpha=0.8, linestyle='-', linewidth=0.25)
    plt.legend()
    plt.title("三角形法则: 先走 a,再走 b")

    print()
    print("第一个图窗:先走 a 再走 b。关掉它,看第二个图窗。")
    plt.show()

    print()
    print("--- 交换律: 换个顺序,先走 b 再走 a ---")

    plt.figure(figsize=(6, 6))

    plt.quiver(0, 0, b_vec[0], b_vec[1],
               angles='xy', scale_units='xy', scale=1,
               color='g', label="b")

    plt.quiver(b_vec[0], b_vec[1], a_vec[0], a_vec[1],
               angles='xy', scale_units='xy', scale=1,
               color='r', label="a (起点在 b 的终点)")

    plt.quiver(0, 0, a_plus_b[0], a_plus_b[1],
               angles='xy', scale_units='xy', scale=1,
               color='m', label="b + a")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(0, 6)
    plt.ylim(0, 4)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', alpha=0.8, linestyle='-', linewidth=0.25)
    plt.legend()
    plt.title("交换律: 先走 b,再走 a —— 终点没变")

    print("第二个图窗:先走 b 再走 a。关掉它,脚本继续跑完。")
    plt.show()

    print()
    print("a + b =", a_vec + b_vec)
    print("b + a =", b_vec + a_vec)
    print("两条路径终点相同吗?", np.array_equal(a_vec + b_vec, b_vec + a_vec))
    print(">>> 这就是向量加法的交换律: a + b = b + a")


# =====================================================================
# 小点 ⑤  结合律 —— 多个向量相加,分组顺序任意
# =====================================================================
def 小点5_结合律():
    标题("小点 ⑤  结合律 —— 分组顺序不影响结果")

    import numpy as np

    a = np.array([3, 1])
    b = np.array([1, 2])
    c = np.array([-1, 2])

    print("三个向量首尾相接(三角形法则推广到 3 个向量):")
    print("a =", a, " b =", b, " c =", c)
    print("走完 a、接着走 b、再接着走 c,终点就是 a+b+c")
    print("a+b+c =", a + b + c)

    print()
    print("--- 结合律: 先加哪两个,结果都一样 ---")
    path1 = (a + b) + c
    path2 = a + (b + c)
    path3 = (a + c) + b

    print("(a+b)+c =", path1, "  <- 先算 a+b,再加 c")
    print("a+(b+c) =", path2, "  <- 先算 b+c,再加 a")
    print("(a+c)+b =", path3, "  <- 先算 a+c,再加 b")
    print("三条路径终点都相同吗?",
          np.array_equal(path1, path2) and np.array_equal(path2, path3))

    print()
    print("--- 为什么结合律'理所当然'成立 ---")
    print("向量加法就是分量各自相加(小点①讲过),")
    print("而普通实数的加法本来就满足结合律,比如:")
    print("(3 + 1) + 5 =", (3 + 1) + 5, "   3 + (1 + 5) =", 3 + (1 + 5))
    print("向量不过是把这件事在每个分量上各做一遍,")
    print("分量满足的结合律,向量自然也满足。")

    print()
    print(">>> 交换律 + 结合律 合起来: a+b+c 不管先后顺序、不管先加哪两个,")
    print(">>> 结果永远一样 —— 这就是为什么可以放心写 a+b+c,不用纠结加括号。")


# =====================================================================
# 小点 ⑥  向量减法
# =====================================================================
def 小点6_减法():
    标题("小点 ⑥  向量减法")

    import numpy as np

    a = np.array([4, 1])
    b = np.array([1, 3])

    print("a =", a, " b =", b)
    print("a - b =", a - b, "   <- 分量各自相减")
    print("b - a =", b - a)
    print("a-b 和 b-a 互为相反数吗?", np.array_equal(a - b, -(b - a)))

    print()
    print("--- 减法 = 加上'相反向量' ---")
    print("-b =", -b, "   <- 长度不变,方向相反,也叫加法逆元")
    print("a + (-b) =", a + (-b))
    print("和 a - b 相等吗?", np.array_equal(a - b, a + (-b)))

    print()
    print("--- 关键几何直觉: a-b 是'从 b 指向 a'的箭头 ---")
    print("如果 a、b 都从原点出发(各自是一个'点'的坐标),")
    print("a-b 就是从 b 的终点指向 a 的终点的那支箭头。")
    print("a - b =", a - b, "  正好等于 a 的终点坐标减去 b 的终点坐标。")

    print()
    print("--- RGB: 减法 = 过滤掉某个颜色 ---")
    yellow = np.array([1, 1, 0])
    red = np.array([1, 0, 0])
    print("黄", yellow, " - 红", red, " =", yellow - red, " <- 绿,滤掉了红光")


# =====================================================================
if __name__ == "__main__":
    小点1_加法()
    小点2_平行四边形法则()
    小点4_三角形法则()
    小点5_结合律()
    小点6_减法()

    print("\n" + "=" * 60)
    print("  跑完。对照讲义: 讲义/LA_01_03_向量加减法.html")
    print("=" * 60)
