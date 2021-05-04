const createModal = (
    modal,
    additionalClass = null,
    width = '400px',
    actionElement = null,
    callback = f => f) => {

    const mask = document.createElement('div');
    mask.classList.add('modal-mask');
    document.body.appendChild(mask);

    const closingButton = document.createElement('span');
    closingButton.innerHTML = '&times;';
    closingButton.classList.add('close')
    closingButton.onclick = () => {
        closeModal(mask, modal);
    }

    modal.classList.remove('modal-content');
    modal.classList.add('modal');
    modal.classList.add(additionalClass);
    modal.style.width = width;
    modal.appendChild(closingButton);

    if (actionElement !== null) {
        addActionElement(mask, modal, actionElement, callback);
    };

};

const closeModal = (mask, modal) => {
    document.body.removeChild(mask);
    modal.classList.add('modal-content');

};

const addActionElement = (mask, modal, actionElement, callback) => {
    actionElement.onclick = () => {
        callback();
        closeModal(mask, modal);
    };
}