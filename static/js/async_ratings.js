document.addEventListener('DOMContentLoaded', () => {
    const ratingElements = document.querySelectorAll('.rating');

    ratingElements.forEach(rating => {
        const movieId = rating.getAttribute('data-movie-id');
        const stars = rating.querySelectorAll('.rating-star');

        // Retrieve the user's rating (sent from the backend in the response)
        const userRating = parseInt(rating.getAttribute('data-user-rating'), 10);

        // Highlight stars based on the user's rating
        updateStars(stars, userRating);

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
                    updateStars(stars, ratingValue);

                    // Update the data-user-rating attribute
                    rating.setAttribute('data-user-rating', ratingValue);
                })
                .catch(error => {
                    console.error('Network Error:', error);
                    alert('There was a problem with the network. Please try again later.');
                });
            });
        });
    });

    function updateStars(stars, ratingValue) {
        stars.forEach(star => {
            const starValue = parseInt(star.getAttribute('data-value'), 10);
            if (ratingValue >= starValue) {
                star.classList.remove('text-muted');
            } else {
                star.classList.remove('text-warning');
                star.classList.add('text-muted');   // Make the star gray
            }
        });
    }
});
