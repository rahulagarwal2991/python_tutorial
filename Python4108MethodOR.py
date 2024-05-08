class P:
    def property(self):
        print("Gaadi + bunglow + bank balance")

    def Business(self):
        print("Factory")

class C(P):
    def Business(self):
        print("Import Export")
        #super().Business()
    

c =  C()
c.property()
c.Business()
