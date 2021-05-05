const { Editor } = toastui;

const editor = new Editor({
    el: document.querySelector('#editor'),
    height: '500px',
    initialEditType: 'markdown',
    previewStyle: 'vertical'
});


const modalTargets = document.querySelectorAll(".info-item");
const saveButtonEl = document.querySelector("#btn-save");
const modalContents = [
    document.querySelector("#description"),
    document.querySelector("#tags"),
    document.querySelector("#category"),
];

modalTargets.forEach((target, i) => {
    target.addEventListener('click', () => {
        if (i === 0) {
            createModal(
                modalContents[i],
                additionalClass = 'description',
                width = '50%',
                actionElement = document.querySelector("#btn-description"),
                callback = getDescription,
            );
        }

        if (i === 1) {
            createModal(modalContents[i],
                'tags',
                width = '50%'
            );
        }
        if (i === 2) {
            createModal(modalContents[i], 'category');
        }
    });
});


const getContent = () => editor.getHtml();

const getTitle = (articleString = '') => {

    try {
        const parser = new DOMParser();
        const articleHtml = parser.parseFromString(articleString, 'text/html');
        return articleHtml.querySelector('h1').textContent;

    } catch (error) {
        console.log('Nada aqui');

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

const buildArticle = () => {
    const article = {
        title: getTitle(editor.getHtml()),
        description: getDescription(),
        content: getContent(),
        category_id: getCategory(),
        tags: getTags(),
    }

    console.log(JSON.stringify(article));
    sendArticloToApi(article);

}

saveButtonEl.onclick = buildArticle;


const sendArticloToApi = async (article) => {
    const request = await fetch('/api/articles', {
        method: 'post',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(article)
    })

    if (!request.ok) {
        const response = await request.json();
        alert(response['message']);
    }
}