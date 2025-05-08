document.getElementById('toggle-options').addEventListener('click', function() {
    const optionsMenu = document.getElementById('options-menu');
    optionsMenu.classList.toggle('visible');
    optionsMenu.classList.toggle('hidden');
});

document.getElementById('increase-font').addEventListener('click', function() {
    document.body.classList.add('accessibility-font');
});

document.getElementById('decrease-font').addEventListener('click', function() {
    document.body.classList.remove('accessibility-font');
});

document.getElementById('add-contrast').addEventListener('click', function() {
    document.body.classList.add('accessibility-contrast');
});

document.getElementById('remove-contrast').addEventListener('click', function() {
    document.body.classList.remove('accessibility-contrast');
});

document.getElementById('zoom-in').addEventListener('click', function() {
    zoom(1.2);
});

document.getElementById('zoom-out').addEventListener('click', function() {
    zoom(0.8);
});

document.getElementById('reset-zoom').addEventListener('click', function() {
    resetZoom();
});

function zoom(scale) {
    const content = document.getElementById('content');
    let currentScale = 1; // Default scale
    const transform = content.style.transform;

    if (transform) {
        const match = transform.match(/\d+(\.\d+)?/);
        if (match) {
            currentScale = parseFloat(match[0]);
        }
    }

    content.style.transform = `scale(${currentScale * scale})`;
}

function resetZoom() {
    const content = document.getElementById('content');
    content.style.transform = 'scale(1)';
}
