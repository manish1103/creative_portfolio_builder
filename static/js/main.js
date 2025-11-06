// main.js - Smart Portfolio Hub

// ========== Navigation Active Link Highlight ==========
const navLinks = document.querySelectorAll("nav ul li a");
navLinks.forEach(link => {
  link.addEventListener("click", () => {
    navLinks.forEach(l => l.classList.remove("active"));
    link.classList.add("active");
  });
});

// ========== Contact Form Submission ==========
const contactForm = document.querySelector("form");
if (contactForm) {
  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = contactForm.querySelector("input[type='text']").value.trim();
    const email = contactForm.querySelector("input[type='email']").value.trim();
    const message = contactForm.querySelector("textarea").value.trim();

    if (name && email && message) {
      alert(`✅ Thank you, ${name}! Your message has been sent successfully.`);
      contactForm.reset();
    } else {
      alert("⚠️ Please fill out all fields before submitting.");
    }
  });
}

// ========== Theme Toggle ==========
const themeBtn = document.createElement("button");
themeBtn.textContent = "🌙 Dark Mode";
themeBtn.style.position = "fixed";
themeBtn.style.bottom = "20px";
themeBtn.style.right = "20px";
themeBtn.style.padding = "10px 15px";
themeBtn.style.border = "none";
themeBtn.style.borderRadius = "8px";
themeBtn.style.cursor = "pointer";
themeBtn.style.background = "#222";
themeBtn.style.color = "#fff";
document.body.appendChild(themeBtn);

let darkMode = false;
themeBtn.addEventListener("click", () => {
  darkMode = !darkMode;
  if (darkMode) {
    document.body.style.background = "#121212";
    document.body.style.color = "#fff";
    themeBtn.textContent = "☀️ Light Mode";
  } else {
    document.body.style.background = "#f8f9fa";
    document.body.style.color = "#000";
    themeBtn.textContent = "🌙 Dark Mode";
  }
});

// ========== Scroll Animation ==========
window.addEventListener("scroll", () => {
  const elements = document.querySelectorAll("section, .project");
  elements.forEach(el => {
    const pos = el.getBoundingClientRect().top;
    if (pos < window.innerHeight - 100) {
      el.style.opacity = 1;
      el.style.transform = "translateY(0)";
      el.style.transition = "all 0.6s ease-in-out";
    }
  });
});
