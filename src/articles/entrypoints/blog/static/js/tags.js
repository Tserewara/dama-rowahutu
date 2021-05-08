const buttonEl = document.querySelector("#add-tag");
const inputEl = document.querySelector("#tags > div.new-tag > input[type=text]");
let tagList = [];

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

const addNewTagToDOM = (tagName) => {
    const tag = document.createElement('span');
    tag.textContent = tagName;
    tag.classList.add('tag');
    tag.onclick = toggleTag;

    const tagContainer = document.querySelector('#tag-container');

    tagContainer.appendChild(tag);
}


Array.from(tagsEl).map(tag => tag.onclick = toggleTag);



buttonEl.onclick = async () => {
    const { value } = inputEl;
    if (value) {
        const response = await Api.saveTag({ tag_name: value.trim() });
        if (response.ok) {
            addNewTagToDOM(value);

        } else {
            alert(response['message'])
        }
    };
    inputEl.value = '';
};