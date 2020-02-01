# Implement Python Switch Case Statement using Dictionary
class switchWeek:
    rear = 0
    front = 0
    minor = 0
    misc = 0
    under = 0

    def rearEnd(self):
        self.rear = self.rear + 1
        return "rearEnd"

    def frontEnd(self):
        self.rear = self.rear + 1
        return "frontEnd"

    def Minor(self):
        self.Minor = self.Minor + 1
        return "minor"

    def under(self):
        self.under = self.under + 1
        return "under"

    def default(self):
        return "MISC"

    switcher = {
        "REAR END": rearEnd,
        "FRONT END": frontEnd,
        "MINOR DENT/SCRATCHES": Minor,
        "UNDERCARRIAGE": under,
    }

    def switch(self, damage):
        return switchWeek.switcher.get(damage, self.default)()

    print(switch("REAR END"))
    print(switch("FRONT END"))
    print(switch("MINOR DENT/SCRATCHES"))
    print(switch("UNDERCARRIAGE"))
