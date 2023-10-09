<script>
    $(document).ready(function () {
        $(".like-button").click(function () {
            var postId = $(this).data("post-id");
            $.ajax({
                type: "POST",
                url: "{% url 'like_post' 0 %}".replace('0', postId),
                data: {
                    csrfmiddlewaretoken: "{{ csrf_token }}"
                },
                success: function (response) {
                    if (response.success) {
                        var totalLikes = response.total_likes;
                        $("#total-likes").text(totalLikes);
                    } else {
                        // Обработка ошибки, если не удалось добавить лайк
                        alert("Не удалось добавить лайк.");
                    }
                },
                error: function () {
                    // Обработка ошибки AJAX-запроса
                    alert("Произошла ошибка при отправке запроса.");
                }
            });
            return false; // Предотвращение перезагрузки страницы
        })
    });
</script>