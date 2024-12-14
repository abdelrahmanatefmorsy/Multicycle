import tkinter as tk

# تعريف كلاس ORGate و ANDGate
class ORGate:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.draw_gate()

    def draw_gate(self):
        # رسم القوس الخلفي العريض
        self.canvas.create_arc(
            self.x - 50, self.y, self.x + 50, self.y + 100,
            start=270, extent=180, outline="black", width=2, style=tk.ARC
        )

        # رسم القوس العلوي (المنحني العلوي في الأمام)
        self.canvas.create_arc(
            self.x - 30, self.y, self.x + 100, self.y + 50,
            start=0, extent=180, outline="black", width=2, style=tk.ARC
        )

        # رسم القوس السفلي (المنحني السفلي في الأمام)
        self.canvas.create_arc(
            self.x - 30, self.y + 50, self.x + 100, self.y + 100,
            start=180, extent=180, outline="black", width=2, style=tk.ARC
        )

        # رسم خطوط المدخلات
        self.canvas.create_line(self.x - 80, self.y + 20, self.x - 50, self.y + 20, width=2)  # المدخل الأول
        self.canvas.create_line(self.x - 80, self.y + 80, self.x - 50, self.y + 80, width=2)  # المدخل الثاني

        # رسم خط المخرج
        self.canvas.create_line(self.x + 100, self.y + 50, self.x + 150, self.y + 50, width=2)  # المخرج

        # إضافة نص داخل البوابة
        self.canvas.create_text(self.x + 20, self.y + 50, text="OR", font=("Arial", 12, "bold"))


# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Logic Gates")

# إنشاء Canvas للرسم
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# إنشاء البوابات
or_gate = ORGate(canvas, 300, 100)    # بوابة OR

# تشغيل التطبيق
root.mainloop()
