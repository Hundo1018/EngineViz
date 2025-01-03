from manim import *

class AABBScene(Scene):
    def construct(self):
        # 添加標題
        title = Text("AABB 碰撞檢測演算法", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 添加座標軸
        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-4.5, 4.5, 1],
            axis_config={"include_numbers": True}
        )
        self.play(Create(axes))

        # 繪製兩個 AABB
        box_a = Rectangle(width=4, height=3, color=BLUE).shift(LEFT * 2)
        box_b = Rectangle(width=3, height=2, color=GREEN).shift(RIGHT * 4)

        label_a = Text("Box A", font_size=24, color=BLUE).next_to(box_a, UP)
        label_b = Text("Box B", font_size=24, color=GREEN).next_to(box_b, UP)

        self.play(Create(box_a), Create(box_b))
        self.play(Write(label_a), Write(label_b))

        # 動態移動 Box B 並檢測碰撞
        collision_text = Text("", font_size=32, color=YELLOW).to_edge(DOWN)

        def update_collision_text():
            """根據檢測結果更新文字"""
            if check_collision(box_a, box_b):
                collision_text.set_text("碰撞！")
                collision_text.set_color(RED)
                box_b.set_color(RED)
            else:
                collision_text.set_text("無碰撞")
                collision_text.set_color(GREEN)
                box_b.set_color(GREEN)

        def check_collision(rect1, rect2):
            """執行 AABB 碰撞檢測"""
            r1 = get_rect_bounds(rect1)
            r2 = get_rect_bounds(rect2)
            return not (
                r1["max_x"] < r2["min_x"] or
                r1["min_x"] > r2["max_x"] or
                r1["max_y"] < r2["min_y"] or
                r1["min_y"] > r2["max_y"]
            )

        def get_rect_bounds(rect):
            """取得矩形的邊界值"""
            center = rect.get_center()
            x, y = center[:2]  # 只取 x 和 y 值
            w, h = rect.width / 2, rect.height / 2
            return {
                "min_x": x - w, "max_x": x + w,
                "min_y": y - h, "max_y": y + h
            }

        self.add(collision_text)
        update_collision_text()  # 初始化狀態

        # 移動動畫並即時檢測
        for step in range(12):
            self.play(box_b.animate.shift(LEFT * 0.6), run_time=0.5)
            update_collision_text()
            self.wait(0.5)

        self.wait(2)

        # 動畫結束
        self.play(FadeOut(box_a, box_b, label_a, label_b, collision_text, title, axes))
