document.getElementById('wiki_api').addEventListener('submit', async function (e) {
    e.preventDefault();

    const firstName = document.querySelector('[name="first_name"]').value.trim();
    const lastName = document.querySelector('[name="last_name"]').value.trim();
    const query = `${firstName} ${lastName} director`;

    const resultContainer = document.querySelector('[name="biography"]');
    resultContainer.innerHTML = '';
    const missingResult = document.getElementById('missing-content');

    const existingError = document.getElementById('error-message');
    if (existingError) {
        existingError.remove();
    }

    if (!firstName || !lastName) {
        const errorMessage = document.createElement('p');
        errorMessage.id = 'error-message';
        errorMessage.className = 'text-danger';
        errorMessage.innerText = 'Name fields cannot be empty. Ensure you enter both the first and last names.';
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
            errorMessage.innerText = `No biography found for "${query}". Please try again with a different name.`;
            missingResult.appendChild(errorMessage);
            return;
        }

        const firstResult = data.query.search[0];
        const pageid = firstResult.pageid;

        const extractResponse = await fetch(`https://en.wikipedia.org/w/api.php?origin=*&action=query&prop=extracts&format=json&pageids=${pageid}&exintro&explaintext`);
        const extractData = await extractResponse.json();

        const page = extractData.query.pages[pageid];
        let text = page.extract || 'No summary available.';

        if (text === 'No biography available.') {
            const errorMessage = document.createElement('p');
            errorMessage.id = 'error-message';
            errorMessage.className = 'text-danger';
            errorMessage.innerText = `No biography found for "${query}". Please try again with a different name.`;
            missingResult.appendChild(errorMessage);
            return;
        }

        text = truncateToSentence(text, 2000);

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

// Function to truncate text to a specified length, ending at the last sentence
function truncateToSentence(text, maxLength) {
    if (text.length <= maxLength) return text;

    const truncated = text.slice(0, maxLength);
    const lastSentenceEnd = truncated.lastIndexOf('.');
    return lastSentenceEnd !== -1 ? truncated.slice(0, lastSentenceEnd + 1) : truncated;
}

