# 🟣 SecLearnz — Educational Payload Generation Framework

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Web%20Security-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Architecture-Modular-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Purpose-Educational-yellow?style=for-the-badge">
</p>

---

## 📌 Overview

**SecLearnz** is a **modular educational payload generation framework** designed to demonstrate how common web attack payloads are structured and how security controls respond to them.

The tool helps cybersecurity students, penetration testers, and researchers understand:

* Payload structures
* Injection contexts
* Encoding techniques
* Filter and validation behavior

SecLearnz generates **payload templates only** and does **not perform automatic exploitation**.

---

## 🎯 Objectives

* Demonstrate common web vulnerability payload patterns
* Provide clean, categorized payload templates
* Support multiple encoding formats
* Export payloads for security testing workflows
* Serve as a foundation for offensive security learning

---

## ✨ Features

### 🕷 XSS Payload Module

* Reflected XSS templates
* Stored XSS templates
* DOM-based XSS templates
* Context-aware payloads:

  * HTML context
  * Attribute context
  * JavaScript context

---

### 🗄 SQL Injection Payload Module

Supports multiple databases:

* MySQL
* PostgreSQL
* MSSQL

Includes:

* Error-based payload templates
* Union-based payload templates
* Blind injection simulation templates
* Comment bypass examples

---

### 💻 Command Injection Payload Module

Includes templates for:

* Linux environments
* Windows environments
* Separator-based injection examples

---

### 🔐 Encoding Support

Payload encoding options:

* URL Encoding
* Base64 Encoding
* Hex Encoding

---

### 📁 Export Support

Payloads can be exported as:

* TXT format
* JSON format

Saved automatically in:

```
outputs/
```

---

## 🖥 Tool Banner

```text
███████╗███████╗ ██████╗██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔════╝
███████╗█████╗  ██║     ██║     █████╗  ███████║██████╔╝██╔██╗ ██║███████╗
╚════██║██╔══╝  ██║     ██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║╚════██║
███████║███████╗╚██████╗███████╗███████╗██║  ██║██║  ██║██║ ╚████║███████║
╚══════╝╚══════╝ ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝

        EDUCATIONAL • PAYLOAD • FRAMEWORK
```

---

## 📁 Project Structure

```bash
SecLearnz/
├── seclearnz.py
├── README.md
├── modules/
│   ├── xss.py
│   ├── sqli.py
│   └── cmdi.py
├── utils/
│   └── encoder.py
└── outputs/
```

---

## ⚙️ Installation

### Requirements

* Python 3.8+
* Linux / Kali Linux recommended

---

### Clone Repository

```bash
git clone https://github.com/yourusername/seclearnz.git
```

```
cd seclearnz
```

---

## 🚀 Usage

---

### Generate XSS Payloads

```bash
python3 seclearnz.py --module xss
```

---

### Generate SQL Injection Payloads

```bash
python3 seclearnz.py --module sqli --db mysql
```

---

### Generate Command Injection Payloads

```bash
python3 seclearnz.py --module cmdi
```

---

### Encode Payloads

```bash
python3 seclearnz.py --module xss --encode url
```

---

### Export Payloads

TXT:

```bash
python3 seclearnz.py --module xss --export txt
```

JSON:

```bash
python3 seclearnz.py --module sqli --db mysql --export json
```

---

## 📂 Output Structure

```bash
outputs/
├── xss_payloads.txt
├── sqli_payloads.json
└── cmdi_payloads.txt
```

---

## 🧩 Architecture

* Modular design
* Separate payload modules
* Encoding utility module
* CLI-based execution
* Export support

---

## 🎓 Educational Value

SecLearnz helps users understand:

* Web attack payload logic
* Injection contexts
* Encoding impact
* Defensive filtering concepts

---

## ⚠️ Ethical Disclaimer

This tool is developed strictly for:

* Educational purposes
* Defensive security research
* Authorized penetration testing environments

Unauthorized use is strictly prohibited.

This project follows:

OWASP Code of Ethics

---

## 👨‍💻 Author

**Muhammad Hamza Zahid**

Cybersecurity Student
Ethical Hacking Enthusiast

---

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork the repository
* 📚 Use it for learning

---

### 🟣 SecLearnz — Learn. Understand. Secure.
