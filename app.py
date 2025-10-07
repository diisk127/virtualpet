from flask import Flask, render_template, jsonify
import time
import json
import os

app = Flask(__name__)

# โหลดสถานะจากไฟล์ หรือสร้างใหม่
if os.path.exists("pet.json"):
    with open("pet.json", "r") as f:
        pet = json.load(f)
else:
    pet = {
        "hunger": 50,
        "mood": 50,
        "hygiene": 50,
        "energy": 50,
        "last_visit": time.time()
    }
    with open("pet.json", "w") as f:
        json.dump(pet, f)

def save_pet():
    with open("pet.json", "w") as f:
        json.dump(pet, f)

def apply_decay():
    now = time.time()
    elapsed = now - pet["last_visit"]
    decay_intervals = int(elapsed // 5)  # ทุก 5 วิ

    if decay_intervals > 0:
        for _ in range(decay_intervals):
            old_mood = pet["mood"]  # เก็บค่า mood ก่อนลด

            # ลดค่า Mood, Hygiene, Energy 2 หน่วย
            pet["mood"] = max(0, pet["mood"] - 2)
            pet["hygiene"] = max(0, pet["hygiene"] - 2)
            pet["energy"] = max(0, pet["energy"] - 2)

            # Hunger เพิ่มเท่ากับ Mood ที่ลด
            mood_drop = old_mood - pet["mood"]
            if mood_drop > 0:
                pet["hunger"] = min(100, pet["hunger"] + mood_drop)

        pet["last_visit"] = now
        save_pet()

@app.route("/")
def index():
    apply_decay()
    return render_template("index.html", pet=pet)

@app.route("/interact/<action>", methods=["GET", "POST"])
def interact(action):
    apply_decay()

    if action == "feeding":
        pet["hunger"] = max(0, pet["hunger"] - 5)
        pet["mood"] = min(100, pet["mood"] + 5)

    elif action == "showering":
        pet["hygiene"] = min(100, pet["hygiene"] + 5)

    elif action == "playing":
        pet["energy"] = max(0, pet["energy"] - 5)
        pet["mood"] = min(100, pet["mood"] + 5)

    elif action == "resting":
        pet["energy"] = min(100, pet["energy"] + 5)

    pet["last_visit"] = time.time()
    save_pet()
    return jsonify(pet)

# Route สำหรับ real-time update
@app.route("/update", methods=["POST"])
def update():
    apply_decay()
    return jsonify(pet)

if __name__ == "__main__":
    app.run(debug=True, port=3006)
