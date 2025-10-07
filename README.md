# Virtual Pet Web App (Flask)
---
## Video  walktrough
 * link :
## Grading

| ชื่อ | บทบาทหลัก | Self Grade | Peer Grade | เหตุผลโดยย่อ | งาน coder (Coder tasks) |
|------|--------------|-------------|-------------|----------------|--------------------------|
| **ชม** | Planner | 98 | 99 | วางแผนงานดี คิดโครงสร้างโปรเจกต์ชัดเจน สื่อสารกับเพื่อนดี ทำตามแผนตรงเวลา | เขียนเอกสารแผนงาน (Project Plan), ช่วยวางโครงร่างระบบ, ดูภาพรวม Sprint |
| **ดิส** | Coder | 98 | 99 | เขียนโค้ดรวดเร็ว เข้าใจความต้องการของแผนงานดี ปรับตาม feedback ได้ไว | พัฒนาโค้ดหลักของระบบ, เชื่อมต่อ backend/frontend, ทำ demo |
| **ค่าเฉลี่ยกลุ่ม** | – | – | **99 / 100** | พวกเรารู้สึกว่าทำงานร่วมกันได้ดีมาก ทั้งสองฝ่ายมีความรับผิดชอบ และสื่อสารกันราบรื่น ผลงานครบทุกเกณฑ์ที่กำหนดไว้ (I–IV) | – |

---

###  Project Evaluation Criteria
- **I.** Convinced Project Pitch  
- **II.** Plausible Project Plan  
- **III.** Workable Prototype Sprint  
- **IV.** Bankable Final Project  


## A simple single-pet simulator where you take care of a virtual Cat by feeding, showering, playing, and letting it rest — with persistent state stored in a JSON file.
 * Interaction หลัก: Feed / Shower / Play / Rest
 * Persistence: pet_state.json
 * Feature ปัจจุบัน + Stretch Goals

## Project Layout
```text
virtual_pet/           <-- โฟลเดอร์โปรเจกต์หลัก
│
├── app.py             <-- Flask app
├── pet.json           <-- สถานะแมว (สร้างตอนแรก)
├── README.md          <-- อธิบายโปรเจกต์
├── .gitignore         <-- ไฟล์ ignore เช่น .DS_Store
│
├── templates/         <-- HTML templates
│   └── index.html
│
├── static/            <-- ไฟล์ static (CSS, JS, รูปภาพ)
│   ├── style.css      <-- CSS ของโปรเจกต์ 
│   ├── script.js      <-- JS ของโปรเจกต์ 
│   ├── normal_pic.png
│   ├── happy_pic.png
│   ├── sleepy_pic.png
│   ├── tired_pic.png
│   └── (ไฟล์อื่น ๆ เช่น รูปอาหาร, icons)
│
└── .DS_Store          
```

## Key Features
---
* Single Cat Pet with dynamic status
* Feed / Shower / Play / Rest buttons
* Hunger / Hygiene / Mood / Energy status bars
* Persistent state via pet_state.json
* Responsive UI with emojis

## Stretch Goals (Planned) 

* Auto Decay — Pet stats decrease over time
* Animations when interacting
* Sound Effects

## Tech Stack
* Backend : Python 3 + Flask
* Frontend : HTML, CSS, JavaScript
* Storage : JSON File (pet_state.json)

## Usage Guide
🍗 Feed
decreases Hunger

🛁 Shower
Increases Hygiene

🎮 Play
Improves Mood

💤 Rest
Restores Energy

ทุกครั้งที่กดปุ่ม ค่าจะอัปเดต และบันทึกลง JSON ทันที

## Data Persistence 
 * All pet stats are stored in: pet_state.json
 * On page load → Flask reads JSON
 * On action → Flask updates and rewrites JSON

## Development Notes
* Frontend ใช้ HTML templates ล้วน พร้อม <style> และ <script> ฝังในหน้าเว็บเพื่อให้พัฒนาและปรับแก้ได้เร็ว—ไม่ต้องใช้ bundler
* แท่งสถานะ, รูปแมว, และ อิโมจิเด้งขึ้น จะอัปเดตแบบไดนามิกด้วย JavaScript ธรรมดา (vanilla JS) โดยเรียกจาก Flask
* ฟีดแบ็กแบบ modal ถูกสร้างโดยการใช้อิโมจิและข้อความสถานะ เพื่อให้ผู้ใช้เห็นผลลัพธ์ทันทีจากการโต้ตอบ
* การโต้ตอบทั้งหมด (feeding, playing, resting, showering) เรียก Flask endpoint /interact/<action> แบบเรียลไทม์ โดย backend จะลดค่า status decay ทุก 5 วินาทีอัตโนมัติ
* รูปแมวจะเปลี่ยนตาม action และจะกลับสู่รูปปกติหลังจากเวลาสั้น ๆ
* การเก็บข้อมูลใช้ ไฟล์ pet.json อ่าน/เขียนโดย Flask เพื่อรักษาสถานะของแมวข้าม session
* การจัดการข้อผิดพลาดพื้นฐาน หาก action หายไปหรือไม่ถูกต้องจะ default กลับสู่สถานะปกติของแมว
* การตรวจสอบและทดสอบยังไม่รวมอยู่ สามารถพิจารณาเพิ่มได้ เช่น:
  * การทดสอบ Flask routes (/ และ /interact/<action>) ด้วย pytest
  * ทดสอบฟังก์ชันช่วยเหลือ เช่น decay และการอัปเดตสถานะ
  * ทดสอบ UI สำหรับการเด้งของอิโมจิและการอัปเดตแท่งสถานะ


---

## Inspiration
หลายคนอยากเลี้ยงสัตว์ แต่ไม่มีเวลา / พื้นที่ / งบประมาณ  
ดังนั้น ความต้องการเลี้ยงสัตว์จึงกลายเป็นความรู้สึกที่ไม่สามารถทำได้จริง  

Virtual Pet จึงเป็นตัวเลือกที่เข้าถึงง่าย และไม่ต้องรับผิดชอบมากเหมือนสัตว์จริง  
มันช่วยบรรเทาความเหงา ความเครียด และภาวะโดดเดี่ยวได้  
การดูแลสิ่งมีชีวิตหนึ่ง (แม้จะเป็นดิจิทัล) ทำให้รู้สึกมีคุณค่าและมีเพื่อนอยู่ข้าง ๆ  

Virtual Pet เป็นการสร้างปฏิสัมพันธ์ที่จับต้องได้ในรูปแบบดิจิทัล  
ผู้ใช้สามารถให้อาหาร เล่น ปลอบ หรือดูแลให้มันมีพัฒนาการได้  

---

## Project Pitch
- เลี้ยง / ให้อาหาร / เพิ่มความสุข:  
  ผู้ใช้สามารถเลือกให้อาหารสัตว์ตามประเภท เช่น ขนม อาหารหลัก หรือของโปรด  
  เมื่อให้อาหารหรือเล่นด้วย Status ของสัตว์จะดีขึ้น เช่น Mood หรือ Energy  

- ระบบอารมณ์และสถานะ (Hunger, Mood, Energy, Hygiene):  
  สัตว์เลี้ยงมีค่าความต้องการที่เปลี่ยนไปตามเวลา เช่น หิว ง่วง เหงา สนุก  
  เมื่อผู้ใช้มีปฏิสัมพันธ์กับสัตว์ สัตว์จะเปลี่ยนพฤติกรรม เช่น หน้าหงอย นอน หรือเรียกร้องความสนใจ  

- Notification:  
  มีการแจ้งเตือนเมื่อเปิดหน้าเว็บ  

---

## Prototype Plan

### ชมพู่ (Responsible for Research & UI Design)

#### STEP 1: Research & Concept Design
- ศึกษาแนวคิดของ Virtual Pet ที่มีอยู่  
- กำหนดเป้าหมาย ปัญหา และฟีเจอร์หลัก  
- ระบุกลุ่มผู้ใช้งานเป้าหมาย (Target User)

#### STEP 2: UI Flow & Wireframe
- ออกแบบหน้าจอหลักและโครงสร้างการใช้งาน  
- กำหนดตำแหน่งของปุ่ม เมนู และลำดับการใช้งาน  
- สร้าง Prototype คร่าว ๆ เพื่อทดสอบ UX/UI  

---

### ดิสก์ (Responsible for Development)

#### STEP 3: Development
- เขียนโครงสร้างระบบ  
- สร้างระบบให้อาหาร / สถานะ / ความรู้สึก  
- เพิ่มอนิเมชันตามอารมณ์ของสัตว์เลี้ยง

 ### ชมพู่และดิสร่วมกันทดสอบการตอบสนองพื้นฐาน 
---
##### ทดสอบที่ 1: Feed Interaction
สิ่งที่ทดสอบ:  
- เมื่อผู้ใช้กด “ให้อาหาร” → ค่าความหิว (Hunger) ลดลง  
- ค่า Mood เพิ่มขึ้นเล็กน้อย  
- ตัวละครแสดงสีหน้าพอใจ  

##### ทดสอบที่ 2: Play Interaction
สิ่งที่ทดสอบ:  
- เมื่อผู้ใช้กดปุ่มเล่น เช่น ลูกบอลหรือตุ๊กตา  
- ค่า Mood เพิ่มขึ้น  
- ตัวสัตว์แสดงสีหน้าเหนื่อย  

##### ทดสอบที่ 3: Time-Based Status
สิ่งที่ทดสอบ:  
- เมื่อปล่อยไว้ 5 วินาที  
  - Hunger เพิ่มขึ้น  
  - Mood ลดลง  
- ตัวละครแสดงอาการหิว เศร้า หรือง่วง  

---

## Testing and Debugging

### 1. การทดสอบ UX/UI  
ได้ดำเนินการทดสอบส่วนติดต่อผู้ใช้ (User Interface) และประสบการณ์ผู้ใช้ (User Experience)  
เพื่อประเมินความสะดวกในการใช้งานของระบบ ตรวจสอบการตอบสนองของปุ่ม เมนู และองค์ประกอบต่าง ๆ  
รวมถึงการใช้สี ฟอนต์ และ Layout ให้สอดคล้องกับธีม Virtual Pet  
ทั้งสำหรับผู้ใช้ใหม่และผู้ใช้ที่กลับมาเล่นซ้ำ  

---

### 2. การแก้ไขบั๊กด้านสถานะและค่าต่าง ๆ  
ตรวจสอบและแก้ไขข้อบกพร่องของค่าตัวแปร เช่น Hunger, Mood, Energy  
ให้มีการอัปเดตตรงตามการกระทำของผู้ใช้ เช่น การให้อาหารหรือเล่นด้วย  
รวมถึงตรวจสอบระบบเวลา (Timer) เพื่อให้มั่นใจว่าค่าต่าง ๆ เปลี่ยนแปลงอัตโนมัติตามเวลาที่ออกแบบไว้  

---

### 3. การตรวจสอบการแสดงผลบน UI  
ทดสอบการแสดงผลของค่าต่าง ๆ บนหน้าจอ เช่น Status Bar, Icon และ Animation ของสัตว์เลี้ยง  
เพื่อให้มั่นใจว่าผลลัพธ์ตรงกับสถานะจริงและอัปเดตแบบเรียลไทม์  
รวมถึงตรวจสอบความราบรื่นของภาพเคลื่อนไหวให้ไม่มีการกระตุกหรือหน่วง  

---

### 4. การรับข้อเสนอแนะและปรับปรุง Layout  
หลังจากการทดสอบภายใน ทีมได้ให้ผู้ใช้กลุ่มตัวอย่างทดลองใช้งานจริง  
เพื่อรับ Feedback และนำมาปรับปรุง Layout เช่น  
การจัดตำแหน่งปุ่มใหม่ การลดความซับซ้อนของหน้าจอ  
และเพิ่มความชัดเจนของข้อมูล เพื่อเตรียมความพร้อมก่อนการสาธิต (Demo)

---

## Roadmap Ideas
* Multi-Pet System
* Leveling / XP

