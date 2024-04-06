import os

def median(*args):
    sorted_args = sorted(args)
    n = len(sorted_args)
    if n % 2 == 0:
        return (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2
    else:
        return sorted_args[n // 2]

def modulus(*args):
    counts = {}
    for num in args:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return modes[0]

def main():
    numbers = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        num_input = input("Masukkan angka : ")
        if num_input.replace('.', '', 1).isdigit(): 
            num = int(num_input)
            numbers.append(num)
        else:
            print("Input tidak valid. Masukkan angka.")
            continue
        
        lanjut = input("Lanjut y/n : ")
        if lanjut.lower() != 'y':
            break

    if numbers:
        avg = sum(numbers) / len(numbers)
        med = median(*numbers)
        mod = modulus(*numbers)
        print(f"Deret angka = {numbers}")
        print(f"Hasil mean = {avg:.2f}")
        print(f"Hasil median = {med}")
        print(f"Hasil modus = [{mod}]")
    else:
        print("Tidak ada data untuk dihitung.")

main()