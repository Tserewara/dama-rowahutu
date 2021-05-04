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
            createModal(modalContents[i], 'tags');
        }
        if (i === 2) {
            createModal(modalContents[i], 'category');
        }
    });
});

let article = {
    title: '',
    description: '',
    content: '',
    tags: [],
    category_id: 1
}


const getContent = () => editor.getHtml();

const getTitle = (articleString = '') => {

    try {
        const parser = new DOMParser();
        const articleHtml = parser.parseFromString(articleString, 'text/html');
        return articleHtml.querySelector('h1').textContent;

    } catch (error) {
        console.log('Nada aqui')

    }

}

const getDescription = () => {
    const descriptionEl = document.querySelector("#article-description")
    return descriptionEl.value;
};

const getCategory = () => {
    const categoryEl = document.querySelector("#category > select");
    return categoryEl.value;
}

const buildArticle = () => {
    const filledArticle = {
        ...article,
        title: getTitle(editor.getHtml()),
        description: getDescription(),
        content: getContent(),
        category_id: getCategory(),
    }

    console.log(JSON.stringify(filledArticle));
    sendArticloToApi(filledArticle)

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

    const response = await request.json();

    console.log(response);
}