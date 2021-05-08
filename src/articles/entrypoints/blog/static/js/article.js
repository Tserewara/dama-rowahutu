const getContent = () => editor.getHtml();

const getTitle = (articleString = '') => {

    try {
        const parser = new DOMParser();
        const articleHtml = parser.parseFromString(articleString, 'text/html');
        return articleHtml.querySelector('h1').textContent;

    } catch (error) {
        alert('Artigo precisa de um título');

    };

};

const getDescription = () => {
    const descriptionEl = document.querySelector("#article-description")
    return descriptionEl.value;
};

const getCategory = () => {
    const categoryEl = document.querySelector("#category > select");
    return categoryEl.value;
};


const getTags = () => tagList;


const buildArticleJSON = () => {
    return ({
        title: getTitle(editor.getHtml()),
        description: getDescription(),
        content: getContent(),
        category_id: getCategory(),
        tags: getTags(),
    });
};