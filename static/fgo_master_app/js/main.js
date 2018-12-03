function openURL(url) {
    location.href = url;
}

function calcStrWidth(id) {
    let elem = document.getElementById(id);
    let width = elem.offsetWidth || 0;
    return 100 / width;
}