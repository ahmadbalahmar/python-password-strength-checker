#What does this code mean?
#- print() tells Python to display a message on the screen.
#- The words inside quotation marks are the message.
#- Each line prints a separate message.
#print("Welcome to the Password Strength Checker!")
#print("This program helps you learn about password security.")





# ==========================================
# PASSWORD STRENGTH CHECKER
# Project: Cybersecurity Portfolio Project
# Language: Python
# ==========================================


# 1. CONFIGURATION

common_passwords = [
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "123456789",
    "iloveyou"
]


# 2. USER INPUT

def get_password():
    """Ask the user for a non-empty password."""

    while True:
        password = input("\nEnter test password: ")

        if password:
            return password

        print("[!] Password cannot be empty. Please try again.")


# 3. PASSWORD ANALYSIS

def check_characters(password):
    """Check which character types exist in the password."""

    has_uppercase = any(char.isupper() for char in password)

    has_lowercase = any(char.islower() for char in password)

    has_digit = any(char.isdigit() for char in password)

    has_special = any(
        not char.isalnum() and not char.isspace()
        for char in password
    )

    return {
        "uppercase": has_uppercase,
        "lowercase": has_lowercase,
        "digit": has_digit,
        "special": has_special
    }


def check_common_password(password):
    """Check whether the password is commonly used."""

    return password.lower() in common_passwords


# 4. STRENGTH CALCULATION

def calculate_score(length, character_checks):
    """Calculate the password strength score out of 5."""

    score = 0

    if length >= 12:
        score += 1

    if character_checks["uppercase"]:
        score += 1

    if character_checks["lowercase"]:
        score += 1

    if character_checks["digit"]:
        score += 1

    if character_checks["special"]:
        score += 1

    return score


def classify_strength(score, is_common):
    """Classify the password as Weak, Moderate or Strong."""

    if is_common:
        return "Weak"

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Moderate"

    else:
        return "Strong"


# 5. SECURITY RECOMMENDATIONS

def get_recommendations(length, character_checks, is_common):
    """Generate recommendations based on the password."""

    recommendations = []

    if is_common:
        recommendations.append(
            "Avoid commonly used passwords. Choose something unique."
        )

    if length < 12:
        recommendations.append(
            "Use at least 12 characters."
        )

    if not character_checks["uppercase"]:
        recommendations.append(
            "Add at least one uppercase letter."
        )

    if not character_checks["lowercase"]:
        recommendations.append(
            "Add at least one lowercase letter."
        )

    if not character_checks["digit"]:
        recommendations.append(
            "Add at least one number."
        )

    if not character_checks["special"]:
        recommendations.append(
            "Add at least one special character."
        )

    return recommendations


# 6. RESULTS

def display_results(password, character_checks, score,
                    strength, recommendations, is_common):
    """Display the final password evaluation."""

    print("\n" + "=" * 45)
    print("       PASSWORD SECURITY REPORT")
    print("=" * 45)

    print("\nPASSWORD ANALYSIS")
    print("-" * 35)

    print("Password length:", len(password))
    print("Meets 12-character target:", len(password) >= 12)

    print("\nCHARACTER ANALYSIS")
    print("-" * 35)

    print("Uppercase letters:", character_checks["uppercase"])
    print("Lowercase letters:", character_checks["lowercase"])
    print("Numbers:", character_checks["digit"])
    print("Special characters:", character_checks["special"])

    print("\nSECURITY CHECK")
    print("-" * 35)

    print("Common password:", is_common)

    print("\nSTRENGTH EVALUATION")
    print("-" * 35)

    print("Strength score:", score, "/ 5")
    print("Password strength:", strength)

    print("\nSECURITY RECOMMENDATIONS")
    print("-" * 35)

    if recommendations:

        for number, recommendation in enumerate(recommendations, start=1):
            print(f"{number}. {recommendation}")

    else:
        print("No recommendations based on these checks.")

    print("\n" + "=" * 45)
    print("          END OF SECURITY REPORT")
    print("=" * 45)


# 7. AUTOMATED TESTING

def run_self_tests():
    """Test the main functions using predefined examples."""

    print("Running automated tests...")

    # Test character checking
    result = check_characters("CyberSecurity2026!")

    assert result["uppercase"] is True
    assert result["lowercase"] is True
    assert result["digit"] is True
    assert result["special"] is True

    # Test common password detection
    assert check_common_password("password123") is True
    assert check_common_password("MyUniquePass2026!") is False

    # Test strength calculation
    score = calculate_score(18, result)
    assert score == 5

    # Test strength classification
    assert classify_strength(2, False) == "Weak"
    assert classify_strength(4, False) == "Moderate"
    assert classify_strength(5, False) == "Strong"

    # Common passwords must be classified as weak
    assert classify_strength(5, True) == "Weak"

    # Test recommendations
    weak_checks = check_characters("abc")

    recommendations = get_recommendations(
        3,
        weak_checks,
        False
    )

    assert len(recommendations) == 4

    # Test that a strong password needs no recommendations
    strong_recommendations = get_recommendations(
        18,
        result,
        False
    )

    assert len(strong_recommendations) == 0

    print("[SUCCESS] All automated tests passed!")


# 8. MAIN PROGRAM

def main():

    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    print("Enter an invented test password.")
    print("Your input will not be saved or transmitted.")

    # Get password
    password = get_password()

    # Analyse password
    length = len(password)

    character_checks = check_characters(password)

    is_common = check_common_password(password)

    # Calculate strength
    score = calculate_score(length, character_checks)

    strength = classify_strength(score, is_common)

    # Generate recommendations
    recommendations = get_recommendations(
        length,
        character_checks,
        is_common
    )

    # Display final report
    display_results(
        password,
        character_checks,
        score,
        strength,
        recommendations,
        is_common
    )


# 9. PROGRAM EXECUTION

if __name__ == "__main__":

    run_self_tests()

    main()
