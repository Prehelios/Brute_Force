# Brute_Force
Brute-Force Password Cracker 🕵️‍♂️
This Python script is a brute-force password cracker designed for educational purposes. It attempts to crack a hashed password using a brute-force approach by testing all possible combinations of characters within a defined set. The script supports MD5 and SHA-1 hash algorithms and can handle passwords containing lowercase letters, uppercase letters, and digits.
Features

    Hashing Algorithm Support: Choose between MD5 and SHA-1 for the target password hash.
    Character Set: Includes lowercase (a-z), uppercase (A-Z), and numeric characters (0-9).
    Customizable Length: Define the maximum password length to be tested.
    Progress Tracking: The script provides real-time updates on the password length being tested, the total number of attempts, and the time elapsed.
    Modular Design: Functions are clearly separated for readability and maintainability.

Usage

    Clone the Repository:

    bash

git clone https://github.com/Prehelios/Brute_Force/blob/main/brute_force.py
cd brute-force-password-cracker

Run the Script:

bash

    python bruteforce_pro.py

    Follow the On-Screen Prompts:
        Enter the hash type (md5 or sha1).
        Paste the hashed password.
        Specify the maximum password length to test.

    Wait for Results:
        The script will display the cracked password (if found), the total number of attempts, and the time taken.

Important Notice

⚠️ Disclaimer: This tool is intended solely for educational purposes and legal, ethical testing environments. Unauthorized use of brute-force techniques is illegal and unethical. Ensure you have explicit permission to perform such actions on the target system.
