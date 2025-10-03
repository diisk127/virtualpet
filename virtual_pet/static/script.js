fetch('https://catfact.ninja/fact')
  .then(response => response.json())
  .then(data => {
    console.log(data.fact); // แสดงข้อเท็จจริงเกี่ยวกับแมว
  })
  .catch(error => console.error('Error fetching cat fact:', error));

fetch('https://catfact.ninja/breeds')
  .then(response => response.json())
  .then(data => {
    console.log(data.data); // แสดงรายการสายพันธุ์แมว
  })
  .catch(error => console.error('Error fetching cat breeds:', error));

  fetch('https://dog.ceo/api/breeds/image/random')
  .then(response => response.json())
  .then(data => {
    const imgElement = document.createElement('img');
    imgElement.src = data.message;
    document.body.appendChild(imgElement); // แสดงรูปแมวสุ่มบนหน้าเว็บ
  })
  .catch(error => console.error('Error fetching cat image:', error));
const catInfoDiv = document.getElementById('cat-info');

// ดึงข้อเท็จจริงเกี่ยวกับแมว
fetch('https://catfact.ninja/fact')
  .then(response => response.json())
  .then(data => {
    const factElement = document.createElement('p');
    factElement.textContent = data.fact;
    catInfoDiv.appendChild(factElement); // แสดงข้อเท็จจริงใน div ที่กำหนด
  })
  .catch(error => console.error('Error fetching cat fact:', error));

