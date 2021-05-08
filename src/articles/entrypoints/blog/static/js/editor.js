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

            );
        };

        if (i === 1) {
            createModal(modalContents[i],
                'tags',
                width = '50%',
                actionElement = document.querySelector("#btn-tags"),
            );
        }

        if (i === 2) {
            createModal(modalContents[i],
                'categories',
                width = '50%',
                actionElement = document.querySelector("#btn-category"),
            );
        }
    });
});


saveButtonEl.onclick = async () => {
    const articleJSON = buildArticleJSON();
    console.log(articleJSON);
    const response = await Api.saveArticle(articleJSON);
    if (response.ok) {
        console.log('Artigo Salvo')
    } else {
        console.log(await response.json())
    }
};
