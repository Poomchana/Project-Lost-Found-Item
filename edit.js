// ✅ โหลดข้อมูลจาก localStorage แล้วใส่ใน input เมื่อเปิดหน้า
window.onload = () => {
  const data = JSON.parse(localStorage.getItem("editItem"));
  if (data) {
    document.getElementById("item").value = data.item || "";
    document.getElementById("detail").value = data.detail || "";
    document.getElementById("location").value = data.location || "";
    document.getElementById("date").value = data.date || "";
    document.getElementById("time").value = data.time || "";
  }
};

// ✅ ปุ่มกลับ
function goBack() {
  window.location.href = "user-admin.html";
}

// ✅ ปุ่มบันทึก (เสร็จสิ้น)
function saveData() {
  // ดึงค่าที่แก้ไข
  const updated = {
    item: document.getElementById("item").value,
    detail: document.getElementById("detail").value,
    location: document.getElementById("location").value,
    date: document.getElementById("date").value,
    time: document.getElementById("time").value
  };

  // เก็บข้อมูลใหม่ไว้ใน localStorage
  localStorage.setItem("editItem", JSON.stringify(updated));
  

  localStorage.setItem("editUpdated", "true");

  
  alert("✅ บันทึกข้อมูลเรียบร้อยแล้ว!");
  window.location.href = "user-admin.html";
}
