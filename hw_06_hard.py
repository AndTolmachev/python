class Worker:
    payment = None
    work_hour = None

    def __init__(self, worker_string):
        self.name = ' '.join(worker_string.split()[0: 2])
        self.salary = int(worker_string.split()[2])
        self.position = worker_string.split()[3]
        self.hour_norm = int(worker_string.split()[4])
        self.salary_per_hour = self.salary / self.hour_norm


work = {}
for linenum, line in enumerate(open('workers', 'r', encoding='UTF-8')):
    if linenum > 0:
        temp = Worker(line)
        work[temp.name] = temp
for linenum, line in enumerate(open('hours_of', 'r', encoding='UTF-8')):
    if linenum > 0:
        temp_worker = ' '.join(line.split()[0: 2])
        work[temp_worker].work_hour = int(line.split()[2])
        if work[temp_worker].hour_norm == work[temp_worker].work_hour:
            work[temp_worker].payment = work[temp_worker].salary

        elif work[temp_worker].hour_norm < work[temp_worker].work_hour:
            work[temp_worker].payment = ((work[temp_worker].work_hour - work[temp_worker].hour_norm)
                                         * work[temp_worker].salary_per_hour * 2) + work[temp_worker].salary
        else:
            work[temp_worker].payment = work[temp_worker].work_hour * work[temp_worker].salary_per_hour
for i in work:
    print(i, work[i].name, work[i].hour_norm, work[i].work_hour, work[i].salary, work[i].payment)

