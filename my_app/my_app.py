from data_storage.file_storage import FileStorage
from problem_solver.fibonacci import Fibonnaci
from problem_solver.primeVerifier import PrimeVerifier
from problem_solver.i_problem_solver import IProblemSolver

class MyApp():
    def __init__(self,file_storage_instance:FileStorage,problem_solver_instance:IProblemSolver):
        self.file_storage_instance = file_storage_instance
        self.problem_solver = problem_solver_instance
    
    def run(self):
        data = self.file_storage_instance.read_data()
        results = self.problem_solver.compute_results(data)
        self.file_storage_instance.save_data(results)

    



