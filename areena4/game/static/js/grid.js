// game/static/game/grid.js
document.addEventListener('DOMContentLoaded', function () {
    const gladiator = document.getElementById('gladiator');
    const squares = document.querySelectorAll('.square');

    let currentSquare = 0; // Start position of the gladiator

    document.addEventListener('keydown', function (e) {
        // Handle arrow key presses
        switch (e.key) {
            case 'ArrowUp':
                move('up');
                break;
            case 'ArrowDown':
                move('down');
                break;
            case 'ArrowLeft':
                move('left');
                break;
            case 'ArrowRight':
                move('right');
                break;
        }
    });

    function move(direction) {
        switch (direction) {
            case 'up':
                if (currentSquare >= 8) {
                    currentSquare -= 8;
                    updateGladiatorPosition();
                }
                break;
            case 'down':
                if (currentSquare < 56) {
                    currentSquare += 8;
                    updateGladiatorPosition();
                }
                break;
            case 'left':
                if (currentSquare % 8 !== 0) {
                    currentSquare -= 1;
                    updateGladiatorPosition();
                }
                break;
            case 'right':
                if ((currentSquare + 1) % 8 !== 0) {
                    currentSquare += 1;
                    updateGladiatorPosition();
                }
                break;
        }
    }

    function updateGladiatorPosition() {
        const currentSquareElement = squares[currentSquare];
        const rect = currentSquareElement.getBoundingClientRect();
        gladiator.style.top = `${rect.top}px`;
        gladiator.style.left = `${rect.left}px`;
    }
});