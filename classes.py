class Task:
    def __init__(self, model_file, stress_max, population_size, diametr_restr, work_dir):
        self.model_file = model_file
        self.stress_max = stress_max
        self.population_size = population_size
        self.diametr_restr = diametr_restr
        self.work_dir = work_dir

class Vector:
    def __init__(self, variables):
        self.variables = variables
        self.stress = None