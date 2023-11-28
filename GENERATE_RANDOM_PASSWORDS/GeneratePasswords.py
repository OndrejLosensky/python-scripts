import pandas as pd
import random
import string
import time 

def generate_password():
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choice to select characters randomly
    password = ''.join(random.choice(characters) for _ in range(16))
    return password

def main():
    start_time = time.time()
    num_passwords = 1000  # Number of passwords
    passwords_with_ids = {'Password': []}

    for i in range(num_passwords):
        password = generate_password()
        passwords_with_ids['Password'].append(password)

        if (i + 1) % 100 == 0:
            print(f"Generated {i + 1} random passwords!")

    df = pd.DataFrame(passwords_with_ids)
    csv_file_path = "passwords.csv"
    df.to_csv(csv_file_path, index=False)

    print(f"Generated passwords were saved to: {csv_file_path}")
    time_taken = round(time.time() - start_time, 2)
    print("Time taken: ", time_taken, "s")

if __name__ == "__main__":
    main()