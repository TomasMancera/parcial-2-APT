import json

from .i_data_storage import IDataStorage

class FileStorage(IDataStorage):
    def __init__(self,input_path,output_path):
       self.output_path = output_path
       self.input_path = input_path
       

    def save_data(self, data):
      with open(self.output_path, 'w') as file:
        lines = [f"{item}\n" for item in data]
        file.writelines(lines)


    def read_data(self):
        result = []
        with open(self.input_path, encoding="utf-8") as file:
           for i in file:
              result.append(int(i))
        result.pop(0)
        
        return result
            
