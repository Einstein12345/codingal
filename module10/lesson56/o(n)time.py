# Program to show n time complexity by entering any n.
def function1(n):
    count=0
    for i in range(1,n+1):
        count+=1
    print("when n is ",n,"count= ",count)
function1(10)
function1(20)
function1(42)
print("whith every n the time taken and the itretion will increase ")
# analysis
# here time taken and iteration will change with n 
# when n increas, the time taken and itreration will also increase
# this  is known as linear time complexity, represented by O(n)