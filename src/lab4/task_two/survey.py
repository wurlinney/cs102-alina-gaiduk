class Respondent:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if self.age != other.age:
            return self.age > other.age
        return self.name < other.name

class Group:

    def __init__(self, name, min_age, max_age):
        self.name = name
        self.min_age = min_age
        self.max_age = max_age
        self.respondents = []

    def add_respondent(self, respondent):
        self.respondents.append(respondent)

    def __str__(self):
        respondents_info = ', '.join(f"{respondent.name} ({respondent.age})" for respondent in sorted(self.respondents))
        return f"{self.name}: {respondents_info}"

class MakeGroups:

    def __init__(self, borders):
       self.groups = self.make_groups(borders)

    def make_groups(self, borders):
        groups = []
        for i in range(len(borders) - 1, 0, -1):
            groups.append(Group(f"{borders[i - 1] + 1}-{borders[i]}", borders[i - 1] + 1, borders[i]))
        groups.append(Group(f"0-{borders[0]}", 0, borders[0]))
        groups.append(Group("101+", borders[-1] + 1, None))
        return groups

    def add_respondent(self, respondent):
        for group in self.groups:
            if group.max_age is None or group.min_age <= respondent.age <= group.max_age:
                group.add_respondent(respondent)
                break

    def get_age_groups_info(self):
        groups_info = []
        plus_101 = None
        for group in self.groups:
            if group.name == "101+":
                plus_101 = group
            elif group.respondents:
                groups_info.append(str(group))
        if plus_101 and plus_101.respondents:
            groups_info.insert(0, str(plus_101))

            return groups_info



    def read_personal_data(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line == 'END':
                    break
                else:
                    name, age = line.split(',', 1)
                    respondent = Respondent(name.strip(), int(age.strip()))
                    self.add_respondent(respondent)


if __name__ == '__main__':
    Borders = list(map(int, input('Введите возрастные границы: ').split()))
    age_group = MakeGroups(Borders)
    file_path = 'personal_data.txt'
    age_group.read_personal_data(file_path)
    for group_info in age_group.get_age_groups_info():
        print(group_info)