import os

def main():
    numbers = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar
        num_input = input("Masukkan angka: ")
        if num_input.replace('.', '', 1).isdigit():
            numbers.append(float(num_input))
        else:
            print("Input tidak valid. Masukkan angka.")
        
        if input("Lanjut y/n: ").lower() != 'y':
            break

    if numbers:
        print(f"Hasil mean dari data: {numbers} = {sum(numbers) / len(numbers):.2f}")
    else:
        print("No data .")

main()