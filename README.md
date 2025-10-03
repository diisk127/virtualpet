## Project Structure
```plaintext
virtual_pet/
│── app.py
│── pet_state.json
│── static/
│   ├── style.css
│   └── script.js
│── templates/
│   └── index.html
```
# Virtual Pet Web App (Flask)
---

## A simple single-pet simulator where you take care of a virtual Cat by feeding, showering, playing, and letting it rest — with persistent state stored in a JSON file.
 *  Interaction หลัก: Feed / Shower / Play / Rest
 *  Persistence: pet_state.json
 *  Feature ปัจจุบัน + Stretch Goals

# Key Features
---
* Single Cat Pet with dynamic status
* Feed / Shower / Play / Rest buttons
* Hunger / Hygiene / Mood / Energy status bars
* Persistent state via pet_state.json
* Responsive UI with emojis

# Stretch Goals (Planned) 
---
* Auto Decay - Pet stats decrease over time
* Animations when interacting
* Sound Effects

# Tech Stack
---
* Backend : Python 3 + Flask
* Frontend : HTML, CSS, JavaScript
* Storage : JSON File (pet_state.json)

# Usage Guide
---

*  🍗Feed : Increases Hunger

*  🛁 Shower : Increases Hygiene

* 🎮 Play : Improves Mood

* 💤 Rest : Restores Energy

* ทุกครั้งที่กดปุ่ม ค่าจะอัปเดต และบันทึกลง JSON ทันที

# Data Persistence 
---
 *  All pet stats are stored in: pet_state.json
 *  On page load → Flask reads JSON
 *  On action → Flask updates and rewrites JSO

# Roadmap Ideas
---
* Multi-Pet System
* Leveling / XP
* Notification Reminder
