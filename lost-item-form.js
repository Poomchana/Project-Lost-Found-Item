function showModal() {
  document.getElementById('success-modal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('success-modal').style.display = 'none';
}

// เมื่อกดบันทึกฟอร์ม
document.querySelectorAll('.item-form').forEach(form => {
  form.addEventListener('submit', e => {
    e.preventDefault();
    showModal();

    // ปิด modal และไปหน้า index4.html หลัง 2 วิ
    setTimeout(() => {
      closeModal();
      window.location.href = "index4.html";
    }, 2000);
  });
});