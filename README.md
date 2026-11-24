# Password Strength Checker

A beginner-friendly Python cybersecurity portfolio project that evaluates a user-provided test password against a set of basic password-strength rules and provides improvement recommendations.

> **Important:** This is an educational rule-based checker. Its score is not a guarantee that a password is secure and is not a precise measurement of password entropy or resistance to guessing.

## Features

- Rejects empty input and asks the user to try again.
- Checks password length against a 12-character target.
- Detects uppercase letters, lowercase letters, digits, and special characters.
- Checks whether the password matches a small built-in list of common passwords.
- Calculates a simple score out of 5.
- Classifies the result as **Weak**, **Moderate**, or **Strong**.
- Provides recommendations based on the checks that failed.
- Runs automated self-tests using Python `assert` statements.
- Organizes the program into functions to make it easier to read, test, and maintain.

## Project structure

```text
Password Strength Checker/
├── password_checker.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10 or later (the project was tested with Python 3.12).
- No third-party Python packages are required.

## Run the project

Open a terminal in the project folder and run:

```bash
python password_checker.py
```

The program runs its automated self-tests first. If they pass, it asks for an invented test password and displays a security report.

## How the score works

The checker awards one point for each condition:

| Condition | Point |
|---|---:|
| At least 12 characters | 1 |
| Contains an uppercase letter | 1 |
| Contains a lowercase letter | 1 |
| Contains a digit | 1 |
| Contains a special character | 1 |
| **Maximum** | **5** |

The basic classification is:

- **Weak:** score 0–2
- **Moderate:** score 3–4
- **Strong:** score 5

A password found in the built-in common-password list is classified as **Weak**, even if it receives 5/5 on the five basic checks.

## Functions

| Function | Purpose |
|---|---|
| `get_password()` | Requests a non-empty password from the user. |
| `check_characters(password)` | Detects uppercase, lowercase, digits, and special characters. |
| `check_common_password(password)` | Checks the password against the built-in common-password list. |
| `calculate_score(length, character_checks)` | Calculates the score out of 5. |
| `classify_strength(score, is_common)` | Returns Weak, Moderate, or Strong. |
| `get_recommendations(...)` | Creates recommendations for missing criteria. |
| `display_results(...)` | Prints the final password evaluation report. |
| `run_self_tests()` | Checks important expected behaviours using assertions. |
| `main()` | Coordinates the program from input to final report. |

## Testing

The built-in tests check examples of:

- Character detection.
- Common-password detection.
- Score calculation.
- Strength classification.
- Common passwords being classified as Weak.
- Recommendations for a weak password.
- No recommendations when all basic criteria are met.

Example test input to try manually:

| Test password | Expected behaviour |
|---|---|
| `abc` | Weak; several recommendations |
| `password123` | Weak; detected as common |
| `Hello123` | Does not meet the length target and lacks a special character |
| `CyberSecurity2026!` | Meets all five basic criteria; Strong under this project's rules |
| Empty input | The program asks again |

## Security considerations and limitations

- The password is entered using ordinary `input()`, so it is visible while typing. A future improvement could use Python's `getpass` module.
- The common-password list is very small and cannot identify every weak or exposed password.
- The checker does not check breached-password databases or external services.
- The five-point score checks simple character and length rules. It does not calculate true password entropy or accurately estimate guessing time.
- A long, randomly generated passphrase can be stronger than a shorter password that merely mixes character types.
- The program does not save or transmit the password by design; avoid adding code that logs, stores, or sends real passwords.
- Do not use real personal or account passwords when demonstrating this educational project. Use invented test examples.

## Possible future improvements

- Hide typed input with `getpass`.
- Expand the common-password checks using a carefully maintained local list.
- Add tests for spaces, Unicode characters, and longer inputs.
- Consider a well-established password-strength estimation library such as `zxcvbn`, while explaining that estimates are not guarantees.
- Improve the user interface and add clearer explanations of why a password may be predictable.

## Learning outcomes

This project practises Python variables, strings, input, conditions, loops, Boolean values, functions, lists, dictionaries, `any()`, `len()`, f-strings, return values, assertions, and basic software testing. It also introduces password hygiene, common-password risks, brute-force attacks, dictionary attacks, passphrases, and password entropy.

## Disclaimer

This project is for learning and demonstration. It is not a professional security auditing tool and should not be used as the sole basis for deciding whether a password is safe.
