from flask import Flask, render_template, jsonify
import time
import requests

app = Flask(__name__)

# ข้อมูล pet
pet = {
    "hunger": 100,
    "mood": 100,
    "hygiene": 100,
    "energy": 50,
    "last_visit": time.time()
}

# ฟังก์ชัน regenerate energy
def regen_energy():
    now = time.time()
    elapsed = now - pet["last_visit"]
    pet["energy"] = min(100, pet["energy"] + int(elapsed // 10))
    pet["last_visit"] = now

# Route หน้าแรก
@app.route("/")
def index():
    regen_energy()
    return render_template("index.html", pet=pet)

# Route อัปเดต stats pet
@app.route("/interact/<action>")
def interact(action):
    regen_energy()
    if action == "feed":
        pet["hunger"] = min(100, pet["hunger"] + 10)
    elif action == "play":
        pet["mood"] = min(100, pet["mood"] + 10)
        pet["energy"] = max(0, pet["energy"] - 5)
    elif action == "shower":
        pet["hygiene"] = min(100, pet["hygiene"] + 15)
    elif action == "pet":
        pet["mood"] = min(100, pet["mood"] + 5)
    return jsonify(pet)

# Route ดึง Cat Fact จริง ๆ
@app.route("/cat_fact")
def cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()
        return jsonify({"fact": data["fact"]})
    except:
        return jsonify({"fact": "Could not fetch cat fact right now."})

# Route ดึงรูปสัตว์เลี้ยงสุ่ม (ใช้ Dog CEO API เพราะ Cat Facts ไม่มีรูป)
@app.route("/pet_image")
def pet_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        return jsonify({"image_url": data["message"]})
    except:
        return jsonify({"image_url": "https://cdn-icons-png.flaticon.com/512/616/616408.png"})

if __name__ == "__main__":
    app.run(debug=True, port=3005)
