document.addEventListener('DOMContentLoaded', function() {
    const likeBtn = document.getElementById('btn');
    const likedIcon = document.getElementById('liked-icon');

    likeBtn.addEventListener('click', function() {
        // Инвертируем цвет иконки при нажатии
        if (likedIcon.classList.contains('fa-heart-red')) {
            likedIcon.classList.remove('fa-heart-red');
        } else {
            likedIcon.classList.add('fa-heart-red');
        }

        // Здесь вы можете добавить код для отправки лайка на сервер, если это необходимо
    });
});