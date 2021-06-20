const getContent = () => editor.getHTML();

const getTitle = () => {

    const articleString = editor.getHTML()

    const parser = new DOMParser();
    const articleHtml = parser.parseFromString(articleString, 'text/html');
    if (articleString) {
        try {
            return articleHtml.querySelector('h1').textContent;
        } catch (error) {
            alert("Título precisa ser no formato # Título")
        }
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
            title: getTitle(),
            description: getDescription(),
            content: getContent(),
            category_id: getCategory(),
            tags: getTags(),
        })
};