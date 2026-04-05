# 📧Email Triage AI Environment

An RL-based AI environment where an agent learns to handle emails 
using reward-based decision making — built on OpenEnv principles.

##  Problem Statement
Emails flood our inbox daily. This environment trains an AI agent 
to automatically triage emails — just like a smart assistant would.

## How It Works

The agent observes an email type and takes an action.
Correct decisions are rewarded. Wrong ones are not.

### Email States
| State | Description |
|-------|---------------|
| urgent | Needs immediate reply |
| spam | Should be ignored |
| normal | Route to right person |
| phishing | Dangerous, must ignore |

### Actions
- `reply` — respond to email
- `ignore` — discard email  
- `forward` — send to right person

### Reward Logic
| Email | Correct Action | Reward |
|-------|---------------|--------|
| urgent | reply | 1.0 |
| spam | ignore | 1.0 |
| normal | forward | 1.0 |
| phishing | ignore | 1.0 |
| any | wrong action | 0.0 |

##  Difficulty Levels
- **Easy** — urgent, spam
- **Medium** — + normal
- **Hard** — + phishing

## 🚀Run Locally
```bash
python inference.py
° Sample Output
Email: urgent, Action: reply, Score: 1.0
Email: spam, Action: ignore, Score: 1.0
Email: phishing, Action: ignore, Score: 1.0
Final Score: 1.0
🛠️ Built With
Python 3
OpenEnv-style architecture
Rule-based inference agent
