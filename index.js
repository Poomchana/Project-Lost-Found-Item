function contact() {
  // แสดงข้อมูลติดต่อในรูปแบบ alert
  alert(
    "ช่องทางการติดต่อ\n\n" +
    "Facebook: LostAndFoundOfficial\n" +
    "Line: @lostandfound\n" +
    "Tel: 02-123-4567"
  );
  // หลังจากแสดง alert แล้วให้ไปที่หน้า login.html
  setTimeout(function() {
    window.location.href = "login.html";  // ไปที่หน้า login.html หลังจากแสดง alert
  }, 1000);  // รอ 1 วินาทีก่อนที่จะเปลี่ยนหน้า
}

function goSignup() {
  // ไปหน้า signup.html
  window.location.href = "signup.html";
}

function goLogin() {
  // กดปุ่มเข้าสู่ระบบแล้วไปที่หน้า login.html
  contact(); // Call the contact function which shows the alert and then redirects
}



function profile() {
  // ไปหน้า
  window.location.href = "profile.html";
}

function details() {
  // ไปหน้า
  window.location.href = "login.html";

}
function contact() {
  // ไปหน้า signup.html
  window.location.href = "contact.html";
}