import sys
from data_storage.file_storage import FileStorage
from problem_solver.fibonacci import Fibonnaci
from problem_solver.primeVerifier import PrimeVerifier
from my_app.my_app import MyApp


def run_app():
    file_storage_fibo = FileStorage("fibonacci.input.txt","fibonacci.output.txt")
    file_storage_prime = FileStorage("prime.input.txt","prime.output.txt")
    problem_solver_prime = PrimeVerifier()
    problem_solver_fibo = Fibonnaci()
    my_app_1 = MyApp(file_storage_prime,problem_solver_prime)
    my_app_2 = MyApp(file_storage_fibo,problem_solver_fibo)
    my_app_1.run()
    my_app_2.run()

def main():
    run_app()


if __name__ == "__main__":
  main()
