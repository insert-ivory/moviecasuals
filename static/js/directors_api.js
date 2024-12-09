document.getElementById('wiki_api').addEventListener('submit', async function (e) {
    e.preventDefault();

    // Get the first and last name from the form
    const firstName = document.querySelector('[name="first_name"]').value.trim();
    const lastName = document.querySelector('[name="last_name"]').value.trim();
    const query = `${firstName} ${lastName} director`;

    // Get the result container and clear previous results
    const resultContainer = document.querySelector('[name="biography"]');
    resultContainer.innerHTML = '';
    const missingResult = document.getElementById('missing-content');

    // Remove any existing error message
    const existingError = document.getElementById('error-message');
    if (existingError) {
        existingError.remove();
    }

    // Check if the query is valid
    if (!firstName || !lastName) {
        const errorMessage = document.createElement('p');
        errorMessage.id = 'error-message';
        errorMessage.className = 'text-danger';
        errorMessage.innerText = 'Name fields cannot be empty. Ensure you enter both the first and last names.';
        missingResult.appendChild(errorMessage);
        return;
    }

    try {
        // Fetch search results from Wikipedia
        const response = await fetch(`https://en.wikipedia.org/w/api.php?origin=*&action=query&list=search&format=json&srsearch=${encodeURIComponent(query)}&uselang=en`);
        const data = await response.json();

        // Check if there are any search results
        if (!data.query.search.length) {
            const errorMessage = document.createElement('p');
            errorMessage.id = 'error-message';
            errorMessage.className = 'text-danger';
            errorMessage.innerText = `No biography found for "${query}". Please try again with a different name.`;
            missingResult.appendChild(errorMessage);
            return;
        }

        // Get the first result and its page ID
        const firstResult = data.query.search[0];
        const pageid = firstResult.pageid;

        // Fetch the page extract (biography) for the first result
        const extractResponse = await fetch(`https://en.wikipedia.org/w/api.php?origin=*&action=query&prop=extracts&format=json&pageids=${pageid}&exintro&explaintext`);
        const extractData = await extractResponse.json();

        // Get the page content and extract text
        const page = extractData.query.pages[pageid];
        let text = page.extract || 'No summary available.';

        // Check if there is a summary available
        if (text === 'No biography available.') {
            const errorMessage = document.createElement('p');
            errorMessage.id = 'error-message';
            errorMessage.className = 'text-danger';
            errorMessage.innerText = `No biography found for "${query}". Please try again with a different name.`;
            missingResult.appendChild(errorMessage);
            return;
        }

        // Truncate the text to a readable length
        text = truncateToSentence(text, 2000);

        // Display the result in the result container
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

