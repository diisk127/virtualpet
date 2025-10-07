const hungerBar = document.getElementById("hunger");
const moodBar = document.getElementById("mood");
const hygieneBar = document.getElementById("hygiene");
const energyBar = document.getElementById("energy");
const petImg = document.getElementById("petImage");

// อัปเดตแท่งสถานะจากข้อมูล pet
function updateBars(pet) {
  hungerBar.value = pet.hunger;
  moodBar.value = pet.mood;
  hygieneBar.value = pet.hygiene;
  energyBar.value = pet.energy;
}

// ฟังก์ชันเรียกเมื่อกดปุ่ม
function interact(action) {
  fetch(`/interact/${action}`, { method: "POST" })
    .then(res => res.json())
    .then(pet => {
      updateBars(pet);
      updateImage(action);
    })
    .catch(err => console.error(err));
}

// เปลี่ยนรูปแมวตาม action
function updateImage(action) {
  if (action === "feed") petImg.src = "static/cat_feed.png";
  else if (action === "shower") petImg.src = "static/cat_clean.png";
  else if (action === "play") petImg.src = "static/cat_play.png";
  else if (action === "rest") petImg.src = "static/cat_sleep.png";

  setTimeout(() => {
    petImg.src = "static/normal_cat.png";
  }, 2000);
}

// เรียก update ทุก 5 วิ
setInterval(() => {
  fetch("/update", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      // อัปเดต bar หรือ text บนหน้าเว็บ
      document.getElementById("hunger").value = data.hunger;
      document.getElementById("mood").value = data.mood;
      document.getElementById("energy").value = data.energy;
      document.getElementById("hygiene").value = data.hygiene;
    });
}, 5000);



