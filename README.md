  # 🏦 Apex Bank Management System

A robust, **Object-Oriented** Banking Application built with Python. This system simulates real-world banking operations, including account type differentiation (Savings vs. Current), secure PIN authentication, and permanent data persistence using file handling.

## 🌟 Key Features

* **Dual Account Logic:** Implements **Inheritance** to handle `Saving_Ac` and `Current_Ac` with specific business rules (e.g., transaction limits for Savings).
* **Data Persistence:** Uses `credentials.txt` and `credentials_c.txt` as a flat-file database to remember balances even after the program closes.
* **Detailed Passbook:** Automatically generates a `passbook.txt` log with timestamps for every transaction using the `datetime` module.
* **Robust Error Handling:** Employs `try-except` blocks to catch `ValueError` and `IndexError`, ensuring the app doesn't crash during invalid inputs.
* **Secure Access:** Dictionary-based lookup for fast account verification and PIN security.

---

## 🛠️ Technical Stack

* **Language:** Python 3.x
* **Concepts:** Object-Oriented Programming (Classes, Inheritance, Super), File I/O, Exception Handling, String Manipulation (`strip`, `split`).
* **Libraries:** `datetime` (for transaction logging).

---

## 🚀 How It Works

1. **Initialization:** On startup, the system reads the latest balances from the `.txt` credential files.
2. **Authentication:** Users enter their Account Number and PIN. The system validates these against the internal dictionary.
3. **Transactions:** * **Deposit:** Updates the balance and logs the entry.
    * **Withdrawal:** Checks for sufficient funds and account-specific limits before processing.
4. **Auto-Save:** Every successful transaction triggers a write-back to the credential files to prevent data loss.

---

## 📂 Project Structure

```text
.
├── main.py              # The core logic of the application
├── credentials.txt      # Database for Savings Accounts (Key:Value)
├── credentials_c.txt    # Database for Current Accounts
├── passbook.txt         # Auto-generated transaction history
└── README.md            # Project documentation  

 ---
```
## 📝 Future Improvements



- [ ] **Transfer Feature:** Implement a method to move money between accounts.
- [ ] **GUI:** Build a Graphical User Interface using Tkinter or CustomTkinter.
- [ ] **Security:** Integrate Encryption for the `pins` dictionary to protect user data.

---

## 👤 Author

**Mayur Gund** *Python Developer | OOP Enthusiast*

> "Building robust systems, one line of code at a time."

---
