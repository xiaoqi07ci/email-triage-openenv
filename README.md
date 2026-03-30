# email-triage-openenv
Email Triage AI Environment

This project simulates an AI system that handles emails.

States:
- urgent
- spam
- normal
- phishing

Actions:
- reply
- ignore
- forward

Reward:
- Correct action = 1.0
- Wrong action = 0.0

Tasks:
- Easy: urgent, spam
- Medium: + normal
- Hard: + phishing
