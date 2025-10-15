// login.js

// ฟังก์ชันเปิดปิดการแสดงรหัสผ่าน
function togglePassword(id, btn) {
  const passwordField = document.getElementById(id);
  const type = passwordField.type === "password" ? "text" : "password";
  passwordField.type = type;
  btn.textContent = type === "password" ? "👁" : "🙈";
}

// ฟังก์ชันจัดการการเข้าสู่ระบบ
function handleLogin(event) {
  event.preventDefault();  // หยุดการ submit แบบเดิม

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  // ตรวจสอบอีเมลและรหัสผ่าน
  if (email === "user@0000" && password === "0000") {
    // หากข้อมูลถูกต้องให้ไปที่หน้า all-items.html
    window.location.href = "all-items.html";  
  } else if (email === "admin@1234" && password === "1234") {
    // หากผู้ใช้เป็น admin ให้ไปที่หน้า user-admin.html
    window.location.href = "user-admin.html";  
  } else {
    alert("อีเมลหรือรหัสผ่านไม่ถูกต้อง");
  }
}

// ฟังก์ชันแสดงหน้า 'homepage' (ย้อนกลับไปหน้า homepage)
function showPage(page) {
  if (page === 'homepage') {
    window.location.href = "index.html";  // เปลี่ยนเป็นหน้า homepage หรือหน้าอื่นตามต้องการ
  }
}
