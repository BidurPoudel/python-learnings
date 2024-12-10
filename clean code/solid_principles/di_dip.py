# in di we inject object of one class to another but we don't make abstract func
#  like this

# class Loggger:
#     def log(self, message:str):
#         print(f"Log: {message}")
        


# class Service:
#     def __init__(self,logger:Loggger):
#         self.logger = logger
     
#     def perform_task(self):
#         self.logger.log('Task performed successfully!')

# logger=Loggger()
# service = Service(logger)
# service.perform_task()


# in above code although di is done, service class is directly depends of logger object as Logger class is hard coded.. 
# in dependency inversion principle we make abstract class/method which is injected to other constructor like we did in dependency injection 

# in dip high-level module(in this case Service) should not depends on low level module(logger) 

# from abc import ABC, abstractmethod

# class ILogger(ABC):
#     @abstractmethod
#     def print_log(self,message: str):
#         pass


 
# class ConsoleLogger(ILogger):
#     def print_log(self, message: str):
#          print(f"Console: {message}")
         
# class FileLogger(ILogger):
#     def print_log(self, message:str):
#         print(f"FileLogger: {message}")


# class ServiceLogger:
#     def __init__(self, logger: ILogger):
#         self.logger = logger
        
#     def perform_task(self):
#         self.logger.print_log("Task performed successfully!")

# console_logger = ConsoleLogger()
# file_logger = FileLogger()

# service_logger1 = ServiceLogger(console_logger)
# service_logger2 = ServiceLogger(file_logger)

# service_logger1.perform_task()
# service_logger2.perform_task()


class CarType:
    def __init__(self, name: str, brand:str) -> None:
        self.name = name
        self.brand = brand 
    
    def show(self):
        return f"name of car: {self.name}\nbrand: {self.brand}"

class Car:
    def __init__(self, car_type: CarType) -> None:
        self.car_type = car_type
    
    def car_details(self):
        return self.car_type.show()


def main():
    car_type= CarType('honda', 'toyota') 
    car = Car(car_type)
    print(car.car_details())

if __name__ == "__main__":
    main()