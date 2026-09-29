// JavaScript for gallery page modal functionality //
document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".piece-card");
    const backdrop = document.getElementById("piece-modal-backdrop");
    const modalImage = document.getElementById("piece-modal-image");
    const modalTitle = document.getElementById("piece-modal-title");
    const modalContent = document.getElementById("piece-modal-content");
    const modalAuthor = document.getElementById("piece-modal-author");
    const modalPrice = document.getElementById("piece-modal-price");

    cards.forEach(function (card) {
        card.addEventListener("click", function () {
            modalTitle.textContent = card.dataset.title;
            modalContent.textContent = card.dataset.content;
            modalAuthor.textContent = "By " + card.dataset.author;
            modalPrice.textContent = card.dataset.price;

            if (card.dataset.image) {
                modalImage.src = card.dataset.image;
                modalImage.alt = card.dataset.title;
                modalImage.style.display = "block";
            } else {
                modalImage.style.display = "none";
            }

            backdrop.classList.add("active");
        });
    });

    backdrop.addEventListener("click", function () {
        backdrop.classList.remove("active");
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            backdrop.classList.remove("active");
        }
    });
});