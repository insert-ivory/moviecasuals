document.addEventListener('DOMContentLoaded', () => {
    const commentForms = document.querySelectorAll('form[id^="/add_comment/"]');

    commentForms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const url = form.action;
            const formData = new FormData(form);
            const commentList = form.closest('.card').querySelector('.list-group');

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                });

                if (!response.ok) {
                    throw new Error('Comment submission failed. Please retry.');
                }

                const data = await response.json();

                // Format the date to match Django's format datetime
                const createdAt = new Date(data.created_at).toLocaleString('en-US', {
                    year: 'numeric',
                    month: 'short',
                    day: 'numeric',
                    hour: 'numeric',
                    minute: 'numeric',
                    hour12: true,
                });

                const newComment = document.createElement('li');
                newComment.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
                newComment.innerHTML = `
                    <div class="d-flex justify-content-between w-100">
                        <div>
                            <strong>${data.username}</strong>: ${data.text}
                        </div>
                        <div class="d-flex align-items-center">
                            <small class="text-muted mr-2">${createdAt}</small>
                            <div class="btn-group">
                                <a href="/edit_comment/${data.id}/" class="btn btn-sm btn-light edit-btn-main">Edit</a>
                                <a href="/delete_comment/${data.id}/" class="btn btn-sm btn-light delete-btn-main">Delete</a>
                            </div>
                        </div>
                    </div>
                `;
                commentList.append(newComment);
                form.reset();
            } catch (error) {
                console.error('Error:', error);
                alert('Submission failed. Please attempt to submit your comment again.');
            }
        });
    });
});

