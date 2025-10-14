// ===== ฟังก์ชัน Modal =====
    function showModal() {
      document.getElementById('success-modal').style.display = 'flex';
    }
    function closeModal() {
      document.getElementById('success-modal').style.display = 'none';
    }

function closeModal() {
  const modal = document.getElementById("success-modal");
  modal.style.display = "none";
}
function goMain() {
  window.location.href = "index.html"; // ✅ กลับหน้า index ปกติ
}

function goHome() {
  closeModal();
  window.location.href = "index4.html"; // ✅ ไปหน้า index4 เมื่อเสร็จสิ้นฟอร์ม
}
