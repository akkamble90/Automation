Web Security Automation Framework (WSAF)
A modular, automated Security Testing Framework designed to identify critical web vulnerabilities. This project demonstrates the integration of Automated Penetration Testing into a modern CI/CD pipeline using Selenium, Docker, and GitHub Actions.

Technical Architecture
The framework follows the Page Object Model (POM) design pattern to separate the test logic from the page-specific UI elements. This ensures the suite is maintainable and scalable.

Core Engine: Handles WebDriver initialization and supports dynamic switching between Headed (Local) and Headless (Cloud) execution modes.

Automation Layer: Built on Selenium for high-fidelity interaction with JavaScript-heavy applications.

Infrastructure: Orchestrated via GitHub Actions using Ephemeral Docker Containers to ensure a clean-room testing environment for every run.

Security Modules
The framework currently focuses on the following vulnerability classes from the OWASP Top 10:

1. Broken Authentication (test_auth.py)
Objective: Verifies if the application enforces strong credential policies.

Methodology: Automated dictionary attacks and weak-credential testing to identify bypass risks.

Verification: Monitors the session state and DOM changes to confirm unauthorized access.

2. Cross-Site Scripting - XSS (test_xss.py)
Objective: Identifies unsanitized input fields that allow client-side script injection.

Methodology: Injects specialized polyglot payloads into search bars and contact forms.

Verification: Utilizes Selenium Alert handling to detect successful payload execution in the browser's JavaScript context.

Deployment & Reporting
Continuous Integration: The suite is triggered on every git push to the main branch.

Environment Parity: Uses the bkimminich/juice-shop Docker image to eliminate "it works on my machine" inconsistencies.

Evidence Collection: Generates a self-contained HTML Security Report including:

Timestamps and platform metadata.

Detailed traceback of discovered vulnerabilities.

System logs from the WebDriver Manager.
