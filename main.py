import preprocessor
import optimizator

task = preprocessor.initialization()
result = optimizator.optimize(task)
# postprocessor(result)