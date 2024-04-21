// game/static/js/app.js

// Define AngularJS application module
const app = angular.module('areenaApp', []);

// Define a controller
app.controller('arenaController', function($scope, $http) {
    // Define the arena grid dimensions
    const rows = 8;
    const cols = 8;

    // Initialize the arena grid
    $scope.initializeArena = function() {
        $scope.arena = [];
        for (let y = 0; y < rows; y++) {
            let column = [];
            for (let x = 0; x < cols; x++) {
                column.push(0); // 0 represents an empty square
            }
            $scope.arena.push(column);
        }

        // Populate the arena grid with gladiators (for demonstration purposes)
        $scope.arena[2][1] = 11; // Place team 1 gladiator 1 at position (2, 1)
        $scope.arena[2][6] = 21; // Place team 2 gladiator 1 at position (2, 6)
    };

    // Function to fetch the first home team gladiator
    // $scope.getFirstHomeTeamGladiator = function() {
    //     $http.get('api')
    //         .then(function(response) {
    //             // On successful API response, return the data
    //             return response.data;
    //         })
    //         .catch(function(error) {
    //             console.error('Error fetching gladiator', error);
    //             // Return null or handle the error
    //             return null;
    //     });
    // };


    // $scope.getFirstHomeTeamGladiator()
    //     .then(function(gladiator) {
    //     // Set the active gladiator once it's fetched
    //     $scope.activeGladiator = gladiator;
    //     console.log("Active gladiator:", $scope.activeGladiator);
    // });

        // $scope.arena[2][0] = -1; // Place rock at position (2, 0)

    $scope.printArena = function() {
        for (let y = 0; y < rows; y++) {
            let rowStr = '';
            for (let x = 0; x < cols; x++) {
                rowStr += $scope.arena[x][y] + ' ';
            }
            console.log('[' + rowStr.trim() + ']');
        }
    };

    $scope.init = function() {
        $scope.initializeArena();
        $scope.printArena();
    }
    $scope.init();

    // Function to check if a square is empty
    $scope.isEmpty = function(row, col) {
        return $scope.arena[row][col] === 0;
    };

    // Define the testJS function
    $scope.testJS = function() {
        // Print something to console.log
        console.log("Testing JS function");
    };

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

    // Function to handle gladiator movement
    $scope.move = function (direction, gladiator) {
        switch (direction) {
            case 'up':
                // if gladiator is not in 1st row AND just above gladiator is empty space
                if (gladiator.y > 0 && $scope.arena[gladiator.y - 1][gladiator.x] === 0) {
                    gladiator.y -= 1;
                    // Update the arena to reflect the new gladiator position
                    $scope.arena[gladiator.y][gladiator.x] = $scope.arena[gladiator.y + 1][gladiator.x];
                    $scope.arena[gladiator.y + 1][gladiator.x] = 0;
                }
                break;
            case 'down':
                // if gladiator is not in 8th row AND just below gladiator is empty space
                if (gladiator.y < 7 && $scope.arena[gladiator.y + 1][gladiator.x] === 0) {
                    gladiator.y += 1;
                    // Update the arena to reflect the new gladiator position
                    $scope.arena[gladiator.y][gladiator.x] = $scope.arena[gladiator.y - 1][gladiator.x];
                    $scope.arena[gladiator.y - 1][gladiator.x] = 0;
                }
                break;
            case 'left':
                if (gladiator.x > 0 && $scope.arena[gladiator.y][gladiator.x - 1] === 0) {
                    gladiator.x -= 1;
                    // Update the arena to reflect the new gladiator position
                    $scope.arena[gladiator.y][gladiator.x] = $scope.arena[gladiator.y][gladiator.x + 1];
                    $scope.arena[gladiator.y][gladiator.x + 1] = 0;
                }
                break;
            case 'right':
                if (gladiator.x < 7 && $scope.arena[gladiator.y][gladiator.x + 1] === 0) {
                    gladiator.x += 1;
                    // Update the arena to reflect the new gladiator position
                    $scope.arena[gladiator.y][gladiator.x] = $scope.arena[gladiator.y][gladiator.x - 1];
                    $scope.arena[gladiator.y][gladiator.x - 1] = 0;
                }
                break;
        }
    };

});