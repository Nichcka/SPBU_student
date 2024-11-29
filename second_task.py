import itertools 
alphabet = "UAGC" 
stop_codons = ["UAA", "UAG", "UGA"] 
length = 12 
 
list_of_RNA = [] 
 
for combo in itertools.product(alphabet, repeat=length): 
    string = "".join(combo) 
    list_of_RNA.append(string) 
print(f"Количество последовательностей РНК из 12 нуклеотидов: {len(list_of_RNA)}") 
#16777216 

codon_strings = [] 
for string in list_of_RNA: 
    codons = [] 
    for i in range(0, len(string), 3): 
        codons.append(string[i:i+3]) 
    codon_strings.append(codons) 
 
count = 0 
for codon_list in codon_strings: 
    found_stop_codon = False 
    for codon in codon_list: 
        if codon in stop_codons: 
            count += 1 
            found_stop_codon = True 
            break 
print(f"Количество последовательностей со стоп-кодонами: {count}") 
#2931375 

seq = len(list_of_RNA) - count 
print(f"Количество возможных последовательностей из 12 нуклеотидов: {seq}") 
 
print(f"Различных отрезков цепи РНК длины 15 можно встретить: {seq*3}") 
