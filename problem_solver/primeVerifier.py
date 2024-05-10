from .i_problem_solver import IProblemSolver

class PrimeVerifier(IProblemSolver):
    def compute_results(self,data):
        result = []
        for element in data:
            primeResult = self.__primeVerifier(element)
            result.append(f"{element} {primeResult}")
        return result

    def __primeVerifier(self,num:int) -> bool:
        for n in range(2, num):
            if num % n == 0:
                return False
        return True
        
            
     
       
 