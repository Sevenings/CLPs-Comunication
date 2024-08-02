document.addEventListener('DOMContentLoaded', function () {

});


function getState() {
    //const url = 'https://api.exemplo.com/dados';  // Substitua com a URL da sua API
    const url = 'api/tag-status';  // Substitua com a URL da sua API

    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log('GetState Internal:', data);
            return data;
        })
        .catch(error => {
            console.error('Houve um problema com a requisição fetch get:', error);
        });
}


function setState(state) {
    const url = 'api/write-tag';  // Substitua com a URL da sua API

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({state: state})
    })
        .then(response => response.json())
        .then(data => {
            console.log('Post Sucess:', data)
        })
        .catch(error => {
            console.error('Houve um problema com a requisição fetch post:', error);
        });
}




function toggleBit(button) {
    let row = button.closest('tr');
    let bitStatus = row.querySelector('.status-indicator.bit-on, .status-indicator.bit-off');

    if (bitStatus.classList.contains('bit-on')) {
        console.log("[Button] Send: setState(false)")
        setState(false);
    } else {
        console.log("[Button] Send: setState(true)")
        setState(true);
    }

    let state = getState();
    console.log('Resultado do GET:', state)
    if (state.tag == true) {
        bitStatus.classList.remove('bit-off');
        bitStatus.classList.add('bit-on');
    } else {
        bitStatus.classList.remove('bit-on');
        bitStatus.classList.add('bit-off');
    }
}
