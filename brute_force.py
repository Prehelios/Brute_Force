import itertools
import hashlib
import time

# Function to display a banner
def display_banner():
    print("=" * 50)
    print(" " * 10 + "Brute-Force Password Cracker")
    print("=" * 50)

# Function to get user input with validation
def get_user_input():
    hash_type = input("Entrez le type de hashage (md5/sha1): ").lower()
    if hash_type not in ["md5", "sha1"]:
        print("Type de hashage non valide. Veuillez choisir entre 'md5' ou 'sha1'.")
        return get_user_input()

    target_hash = input("Entrez le mot de passe hashé: ")
    max_length = int(input("Entrez la longueur maximale du mot de passe à tester: "))
    return hash_type, target_hash, max_length

# Function to hash the password based on the chosen algorithm
def hash_password(password, hash_type):
    if hash_type == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()

# Function to try each generated password
def try_password(password, hash_type, target_hash):
    hashed_password = hash_password(password, hash_type)
    if hashed_password == target_hash:
        print(f"Mot de passe trouvé: {password}")
        return True
    return False

# Main brute-force loop with progress tracking
def brute_force(hash_type, target_hash, max_length):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    start_time = time.time()
    total_attempts = 0
    
    for length in range(1, max_length + 1):
        print(f"[*] Test des mots de passe de longueur {length}...")
        for attempt in itertools.product(charset, repeat=length):
            total_attempts += 1
            password = "".join(attempt)
            if try_password(password, hash_type, target_hash):
                print(f"[*] Total de tentatives: {total_attempts}")
                print(f"[*] Temps écoulé: {time.time() - start_time:.2f} secondes")
                return True
    print("Mot de passe non trouvé dans les combinaisons générées.")
    print(f"[*] Total de tentatives: {total_attempts}")
    print(f"[*] Temps écoulé: {time.time() - start_time:.2f} secondes")
    return False

# Execution flow
def main():
    display_banner()
    hash_type, target_hash, max_length = get_user_input()
    print("[*] Démarrage de l'attaque de brute-force...")
    brute_force(hash_type, target_hash, max_length)

if __name__ == "__main__":
    main()
