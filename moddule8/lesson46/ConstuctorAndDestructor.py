class employee:
    def __init__(self):      #initializing (constructor)
        print("employee creations")      
    def __del__(self):      #deleting (destructor)
        print("destructor called and employee is deleted")

obj=employee()
del obj       