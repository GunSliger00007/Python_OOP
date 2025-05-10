class Distance:
    def __init__(self, feet=0, inch=0):
        self.feet = feet
        self.inch = inch

    def addDistance(self, other):
        total_feet = self.feet + other.feet
        total_inch = self.inch + other.inch

        if total_inch >= 12:
            total_feet += total_inch // 12
            total_inch = total_inch % 12

        return Distance(total_feet, total_inch)

d1 = Distance(12, 13)
d2 = Distance(15, 16)
d3 = d1.addDistance(d2)
print(f"{d3.feet} feet, {d3.inch} inches")
