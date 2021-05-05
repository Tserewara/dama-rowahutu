const buttonEl = document.querySelector("#add-tag");
const inputEl = document.querySelector("#tags > div.new-tag > input[type=text]");

buttonEl.onclick = () => {
    const { value } = inputEl;
    if (value) {
        sendTagToApi(value.trim());
    };

};

const sendTagToApi = async (tagName) => {

    const tag = { 'tag_name': tagName };

    const request = await fetch('/api/tags', {
        method: 'post',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(tag)
    });

    if (!request.ok) {
        const response = await request.json();
        alert(response['message'])
    } else {
        addNewTagToDOM(tagName);
    }

    inputEl.value = '';
}

const addNewTagToDOM = (tagName) => {
    const tag = document.createElement('span');
    tag.textContent = tagName;
    tag.classList.add('tag');
    tag.onclick = toggleTag;

    const tagContainer = document.querySelector('#tag-container');

    tagContainer.appendChild(tag);
}


const tagsEl = document.querySelectorAll(".tag");

const toggleTag = event => {
    const { target } = event;
    const { textContent } = target;

    if (!tagList.includes(textContent)) {
        target.classList.add('selected-tag');
        tagList.push(textContent);
    } else {
        target.classList.remove('selected-tag');
        tagList = tagList.filter(tag => tag != textContent);
    };
};

let tagList = [];

Array.from(tagsEl).map(tag => tag.onclick = toggleTag);

