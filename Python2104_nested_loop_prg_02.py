# WAP to print pyramid of * equivalent triange
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

n = 5
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("* "*i)

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 