const request = async (url, method, body) => {

    const baseUrl = '/api';

    const request = await fetch(`${baseUrl}/${url}`, {
        method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })
    return request;
};

const Api = {
    saveArticle: (article) => request('articles', 'post', article),
    saveTag: (tagName) => request('tags', 'post', tagName)
};
