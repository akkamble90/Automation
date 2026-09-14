Web Security Automation Framework (WSAF)
# Automated Security Testing Framework (DAST)

A dynamic web application security testing framework that automates vulnerability verification for OWASP Top 10 flaws—focusing on **Reflected Cross-Site Scripting (XSS)** and **Authentication Brute-Force/Weak Credentials**—using **Python**, **pytest**, and **Selenium WebDriver** with optional **OWASP ZAP** proxy inspection.

---

## Visual Reports & Test Artifacts

### 1. HTML Execution Summary Report
The framework leverages `pytest-html` to generate a unified, standalone test execution report detailing test runs, pass/fail status, execution duration, and metadata.

<!-- Replace the path below with your captured report screenshot -->
![pytest-html Test Execution Report](security_automation/reports/screenshots/report_dashboard.png)
---

### 2. Vulnerability Execution Evidence

<p align="center">
  <img src="reports/screenshots/success_admin123.png" width="48%" alt="Authentication Vulnerability Found" />
  <img src="reports/screenshots/xss_alert_trigger.png" width="48%" alt="XSS Exploit Reflection" />
</p>

* **Left:** Successful brute-force exploit demonstrating authentication bypass using weak credentials (`admin123`).
* **Right:** Triggered DOM alert / payload reflection verification during automated XSS fuzzing.

---

### 3. Execution Terminal & Live Logs

<!-- Replace with a screenshot of your passing terminal session -->
![Terminal Execution Output](reports/screenshots/terminal_run.png)

---

## System Architecture

Built on the **Page Object Model (POM)** to decouple low-level browser interaction from security test logic:

```text
                        +----------------------------+
                        |       pytest Engine        |
                        +--------------+-------------+
                                       |
                   +-------------------+-------------------+
                   |                                       |
                   v                                       v
         +-------------------+                   +-------------------+
         |   test_auth.py    |                   |    test_xss.py    |
         +---------+---------+                   +---------+---------+
                   |                                       |
                   +-------------------+-------------------+
                                       |
                                       v
                       +-------------------------------+
                       |   Page Object Model (POM)     |
                       |    (LoginPage / SearchPage)   |
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |      Selenium WebDriver       |
                       |    (Chrome Headless / GUI)    |
                       +---------------+---------------+
                                       |
                                [HTTP / HTTPS]
                                       |
                                       v
                     +-----------------------------------+
                     |      OWASP ZAP Proxy Listener     |
                     |         (127.0.0.1:8080)          |
                     +-----------------+-----------------+
                                       |
                                [Forward Traffic]
                                       |
                                       v
                     +-----------------------------------+
                     |      Target Web Application       |
                     |      (e.g., OWASP Juice Shop)     |
                     +-----------------------------------+
