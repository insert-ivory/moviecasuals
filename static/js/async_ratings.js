document.addEventListener('DOMContentLoaded', () => {
    const ratingElements = document.querySelectorAll('.rating');

    ratingElements.forEach(rating => {
        const movieId = rating.getAttribute('data-movie-id');
        const stars = rating.querySelectorAll('.rating-star');

        // Retrieve the user's rating (sent from the backend in the response)
        const userRating = parseInt(rating.getAttribute('data-user-rating'), 10);

        // Highlight stars based on the user's rating
        stars.forEach(star => {
            const starValue = parseInt(star.getAttribute('data-value'), 10);

            if (userRating >= starValue) {
                star.classList.add('text-warning');  // Highlight the star
            } else {
                star.classList.add('text-muted');   // Make the star gray
            }
        });

        // Set up the click event for new ratings
        stars.forEach(star => {
            star.addEventListener('click', () => {
                const ratingValue = star.getAttribute('data-value');
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                fetch(`/rate_movie/${movieId}/`, {
                    method: 'POST',
                    body: new URLSearchParams({ rating: ratingValue }),
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('There was an issue with your rating submission. Please check and try again.');
                    }
                    return response.json();
                })
                .then(data => {
                    const averageRatingElement = document.getElementById(`average-rating${movieId}`);
                    if (averageRatingElement) {
                        averageRatingElement.textContent = data.new_average_rating;
                    }

                    // Update stars based on the new rating
                    stars.forEach(s => {
                        s.classList.toggle('text-warning', s.getAttribute('data-value') <= ratingValue);
                        s.classList.toggle('text-muted', s.getAttribute('data-value') > ratingValue);
                    });
                })
                .catch(error => {
                    console.error('Network Error:', error);
                    alert('There was a problem with the network. Please try again later.');
                });
            });
        });
    });
});