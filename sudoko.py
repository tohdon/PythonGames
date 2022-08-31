import  copy, random, sys

EMPTY_SPACE='.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH

class sudokuGrid:
    def __init__(self, originalsetup):
        self.originalsetup = originalsetup
        self.grid = {}
        self.resetGrid()
        self.moves = []
		
    def resetGrid(self):
        for x in range(1, GRID_LENGTH+1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x,y)] = EMPTY_SPACE		
        print(self.originalsetup)
        assert len(self.originalsetup) == FULL_GRID_SIZE
        i = 0
        y = 0
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x,y)] = self.originalsetup[i]
                i +=1
            y +=1

    def makeMove(self, column, row, number):
        x = 'ABCDEFGHI'.find(column)
        y = int(row) -1
        
        if self.originalsetup[y *GRID_LENGTH + x] != EMPTY_SPACE:
            return False
        self.grid[(x,y)] = number
        self.moves.append(copy.copy(self.grid))
        return True
        
    def unddo(self):
        if self.moves ==[]:
            return
        self.moves.pop()
        
        if self.moves ==[]:
            self.resetGrid()
        else:
            self.grid = copy.copy(self.moves[-1])
        
    def display(self):
        print('    ABC     DEF     GHI')
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x ==0:
                    print(str(y + 1) +'  ', end='')
                
                print(self.grid[(x,y)] +' ', end='')
                if x == 2 or x ==5:
                    print('| ', end='')
            print()
            if y == 2 or y ==5:    
                print('   ------+-------+------')
    def _isCompletesetOfNumbers(self, numbers):
        return sorted(numbers) == list('123456789')
        
    def issolved(self):
        for row in range(GRID_LENGTH):
            rowNumbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x,row)]
                rowNumbers.append(number)
            if not self._isCompletesetOfNumbers(rowNumbers):
                return False
                
        for column in range(GRID_LENGTH):
            columnNumbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column,y)]
                columnNumbers.append(number)
            if not self._isCompletesetOfNumbers(columnNumbers):
                return False
        for boxx in (0,3,6):
            for boxy in (0,3,6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(boxx + x, boxy + y)] 
                        boxNumbers.append(number)
                if not self._isCompletesetOfNumbers(boxNumbers):
                    return False

input('Press here to begin..')
with open('sudokupuzzles.txt') as puzzlesFile:
    puzzles = puzzlesFile.readlines()

for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()
    
grid = sudokuGrid(random.choice(puzzles))
while True:
    grid.display()
    
    if grid.issolved():
        print('Congrad. You have solve the puzzles!!')
        sys.exit()
    while True:
        print()
        print('Enter a move or RESET, NEW, UNDO, ORIGINAL, or QUIT!!')
        print('For example, a move looks like "B4 9",)')
        
        action = input('> ').upper().strip()
        
        if len(action)>0 and action[0] in ('R', 'N', 'U', 'O', 'Q'):
            break
        
        if len(action.split()) ==2:
            space, number = action.split()
            if len(space) !=2:
                continue
            
            column, row = space
            if column not in list('ABCDEFGHI'):
                print('There is no column', column)
                continue
            
            if not row.isdecimal() or not(1 <= int(row) <=9):
                print('There is no row', row)
                continue
            if not (1 <=int(number) <=9):
                print('Select a number from 1 to 9, not', number)
                continue
            break
    print()
    if action.startswith('R'):
        grid.resetGrid()
        continue
    if action.startswith('N'):
        grid = sudokuGrid(random.choice(puzzles))
        continue
    if action.startswith('U'):
        grid.unddo()
        continue
    if action.startswith('O'):
        originalGrid = sudokuGrid(grid.originalsetup)
        originalGrid.display()
        input('Press Enter to continue...')
        continue
    if action.startswith('Q'):
        
        print('Thank for playing!')
        sys.exit()


    if grid.makeMove(column, row, number) == False:
        print('Cannot overwrite original grid numbers')
        print('Enter ORIGINAL to view to original grid.')
        input('Press enter to continue...')







































































































































































































































































