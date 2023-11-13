import classes

def initialization():
    model_file = input('Введите путь к файлу модели: ')
    work_dir = input('Введите путь к рабочей папке: ')
    stress_max = float(input('Введите ограниечение на напряжения: '))
    population_size = int(input('Введите размер популяции: '))
    diametr_restr = float(input('Введите максимальный даиметр стержня: '))
    task1 = classes.Task(model_file, stress_max, population_size, diametr_restr, work_dir)
    return task1
