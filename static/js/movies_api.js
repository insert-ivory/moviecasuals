document.getElementById('wiki_api').addEventListener('submit', async function (e) {
    e.preventDefault();

    const movieTitle = document.querySelector('[name="title"]').value.trim();
    const query = `${movieTitle} movie`;

    const resultContainer = document.querySelector('[name="description"]');
    resultContainer.innerHTML = '';
    const missingResult = document.getElementById('missing-content');

    const existingError = document.getElementById('error-message');
    if (existingError) {
        existingError.remove();
    }

    if (!movieTitle) {
        const errorMessage = document.createElement('p');
        errorMessage.id = 'error-message';
        errorMessage.className = 'text-danger';
        errorMessage.innerText = 'Movie title cannot be empty. Please enter a valid movie title.';
        missingResult.appendChild(errorMessage);
        return;
    }

    try {

        const response = await fetch(`https://en.wikipedia.org/w/api.php?origin=*&action=query&list=search&format=json&srsearch=${encodeURIComponent(query)}&uselang=en`);
        const data = await response.json();

        if (!data.query.search.length) {
            const errorMessage = document.createElement('p');
            errorMessage.id = 'error-message';
            errorMessage.className = 'text-danger';
            errorMessage.innerText = `No matches found for "${query}". Please try again with a different movie title.`;
            missingResult.appendChild(errorMessage);
            return;
        }

        const firstResult = data.query.search[0];
        const pageid = firstResult.pageid;

        const extractResponse = await fetch(`https://en.wikipedia.org/w/api.php?origin=*&action=query&prop=extracts&format=json&pageids=${pageid}&exintro&explaintext`);
        const extractData = await extractResponse.json();

        const page = extractData.query.pages[pageid];
        let text = page.extract || 'No summary available.';

        if (text === 'No summary available.') {
            const errorMessage = document.createElement('p');
            errorMessage.id = 'error-message';
            errorMessage.className = 'text-danger';
            errorMessage.innerText = `No description found for "${query}". Please try again with a different movie title.`;
            missingResult.appendChild(errorMessage);
            return;
        }

        text = truncateDescription(text, 2000);

        resultContainer.innerHTML = `${text}`;
    } catch (error) {
        const errorMessage = document.createElement('p');
        errorMessage.id = 'error-message';
        errorMessage.className = 'text-danger';
        errorMessage.innerText = 'We encountered an error while retrieving the data. Please try again in a few moments.';
        missingResult.appendChild(errorMessage);
        console.error(error);
    }
});

// Function to truncate text to a specified length, ensuring it does not exceed maxLength
function truncateDescription(text, maxLength) {
    if (text.length <= maxLength) return text;

    const truncated = text.slice(0, maxLength);
    const lastSentenceEnd = truncated.lastIndexOf('.');

    return lastSentenceEnd !== -1 ? truncated.slice(0, lastSentenceEnd + 1) : truncated;
}
