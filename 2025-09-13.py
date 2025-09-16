from dataclasses import dataclass


# 定义一个轻量且不可变的数据类
@dataclass(slots=True, frozen=True)
class Point:
    x: float
    y: float


def demo() -> None:
    p = Point(3.0, 4.0)
    # 无 __dict__，说明启用了 __slots__，更省内存/更快属性访问
    print("has __dict__? ->", hasattr(p, "__dict__"))

    # 尝试修改将抛出 FrozenInstanceError（来自 dataclasses）
    try:
        # type: ignore[attr-defined]  # 演示目的
        p.x = 10.0  # 不可变：将失败
    except Exception as e:
        print("mutation blocked:", type(e).__name__, "-", e)

    # 依然可以创建“修改后副本”（函数式风格）
    p2 = Point(x=p.x + 1, y=p.y - 1)
    print("p:", p)
    print("p2:", p2)


if __name__ == "__main__":
    demo()
