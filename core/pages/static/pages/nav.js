// JavaScript for nav toggle functionality //
document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("nav-toggle");
    const nav = document.getElementById("site-nav");

    toggle.addEventListener("click", function () {
        const isOpen = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", isOpen);
    });
});