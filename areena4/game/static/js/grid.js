// game/static/game/grid.js
document.addEventListener('DOMContentLoaded', function () {

    document.addEventListener('keydown', function (e) {
        // Handle arrow key presses
        switch (e.key) {
            case 'ArrowUp':
                $scope.move('up', $scope.activeGladiator);
                break;
            case 'ArrowDown':
                $scope.move('down', $scope.activeGladiator);
                break;
            case 'ArrowLeft':
                $scope.move('left', $scope.activeGladiator);
                break;
            case 'ArrowRight':
                $scope.move('right', $scope.activeGladiator);
                break;
        }
    });

    $scope.move = function (direction, gladiator) {
        switch (direction) {
            case 'up':
                // if gladiator is not in 1st row AND just above gladiator is empty space
                if (gladiator.y > 0 && $scope.arena[gladiator.y - 1] === 0) {
                    gladiator.y -= 1
                    drawArena();
                }
                break;
            case 'down':
                // if gladiator is not in 8th row AND just below gladiator is empty space
                if (gladiator.y < 7 && $scope.arena[gladiator.y + 1] === 0) {
                    gladiator.y += 1;
                    updateGladiatorPosition(gladiator);
                }
                break;
            case 'left':
                if (gladiator.x > 0 && $scope.arena[gladiator.x - 1] === 0) {
                    gladiator.x -= 1
                    updateGladiatorPosition(gladiator);
                }
                break;
            case 'right':
                if (gladiator.x < 7 && $scope.arena[gladiator.x + 1] === 0) {
                    gladiator.x += 1;
                    updateGladiatorPosition(gladiator);
                }
                break;
        }
    }

    function updateGladiatorPosition(gladiator) {
        gladiator.x
        const currentY = arena[x].y;
        const rect = currentSquareElement.getBoundingClientRect();
        gladiator.style.top = `${rect.top}px`;
        gladiator.style.left = `${rect.left}px`;
    }
});