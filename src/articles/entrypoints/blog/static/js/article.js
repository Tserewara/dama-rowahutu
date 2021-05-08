const getContent = () => editor.getHtml();

const getTitle = (articleString = '') => {

    const parser = new DOMParser();
    const articleHtml = parser.parseFromString(articleString, 'text/html');
    if (articleString) {
        return articleHtml.querySelector('h1').textContent;
    }


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


const buildArticle = () => {
    return (
        {
            title: getTitle(editor.getHtml()),
            description: getDescription(),
            content: getContent(),
            category_id: getCategory(),
            tags: getTags(),
        })
};