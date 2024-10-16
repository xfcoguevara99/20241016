
import array as array
def scrip0():
    vet = list(map(int,input().split()))

    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        vet[i] = 3 * vet[i]
        print(vet[i], end = " ")
    print()

def leitura_array():
    vet = array.array("i",map(int,input().split()))
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        print(vet[i],end = " ")
    print()
 
 
def insercao_dados():
    vC = [1,3.4,"a","ifsc"]
    print("vetor original: ",vC)
    input("Digite enter para prosseguir: ")
    vC.insert(0,56)
    vC.insert(3,"B")
    vC.append(11)
    for i in vC:
        print(i)
if __name__ == "__main__":
    #scrip0()
    #leitura_array()
    insercao_dados()
