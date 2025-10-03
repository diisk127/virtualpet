from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# ค่าเริ่มต้นสัตว์เลี้ยง
pet = {
    "hunger": 100,
    "mood": 100,
    "hygiene": 100,
    "energy": 50,
    "last_visit": time.time()
}

# ฟังก์ชัน regen energy
def regen_energy():
    now = time.time()
    elapsed = now - pet["last_visit"]
    pet["energy"] = min(100, pet["energy"] + int(elapsed // 10))
    pet["last_visit"] = now

@app.route("/")
def index():
    regen_energy()
    return render_template("index.html", pet=pet)

@app.route("/interact/<action>", methods=["GET","POST"])
def interact(action):
    regen_energy()
    if action == "feeding":
        pet["hunger"] = min(100, pet["hunger"] + 10)
    elif action == "playing":
        pet["mood"] = min(100, pet["mood"] + 10)
        pet["energy"] = max(0, pet["energy"] - 5)
    elif action == "showering":
        pet["hygiene"] = min(100, pet["hygiene"] + 15)
    elif action == "resting":
        pet["mood"] = min(100, pet["mood"] + 5)
        pet["energy"] = min(100, pet["energy"] + 10)
    return jsonify(pet)

if __name__ == "__main__":
    app.run(debug=True, port=3005)
