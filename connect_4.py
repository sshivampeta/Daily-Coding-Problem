'''connect_4.py
Connect 4 game implementation with full game logic.

Connect 4 is a two-player game where opponents take turns dropping 
red or black discs into a 7x6 vertically suspended grid. 

The game ends when:
- One player creates a line of four consecutive discs (horizontal, vertical, or diagonal)
- No more spots left in the grid (draw)

Game Rules:
- 7 columns, 6 rows
- Players alternate turns
- Drop a disc in a column, it falls to the lowest available row
- First to get 4 in a row wins
'''

import logging
from enum import Enum
from typing import List, Tuple, Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


class Player(Enum):
    """Enum for players"""
    RED = 'R'
    BLACK = 'B'
    EMPTY = ' '


class ConnectFour:
    """
    Connect 4 game implementation.
    
    Board: 7 columns x 6 rows
    - Rows: 0 (bottom) to 5 (top)
    - Columns: 0 to 6 (left to right)
    """
    
    COLS = 7
    ROWS = 6
    
    def __init__(self):
        """Initialize the game board and state"""
        # Create empty board (row 0 is bottom)
        self.board = [[Player.EMPTY for _ in range(self.COLS)] for _ in range(self.ROWS)]
        
        # Track next available row for each column
        self.next_row = [0] * self.COLS
        
        # Current player (start with RED)
        self.current_player = Player.RED
        
        # Game state
        self.game_over = False
        self.winner = None
        self.move_count = 0
        
        logging.info("Game initialized: 7x6 board, RED starts")
    
    def drop_disc(self, col: int) -> bool:
        """
        Drop a disc in the specified column.
        
        Args:
            col: Column index (0-6)
        
        Returns:
            True if move successful, False if column is full
        """
        # Validate column
        if col < 0 or col >= self.COLS:
            logging.warning(f"Invalid column: {col}")
            return False
        
        # Check if column is full
        if self.next_row[col] >= self.ROWS:
            logging.warning(f"Column {col} is full")
            return False
        
        # Place disc
        row = self.next_row[col]
        self.board[row][col] = self.current_player
        self.next_row[col] += 1
        self.move_count += 1
        
        logging.info(f"Player {self.current_player.value} dropped disc in column {col} at row {row}")
        
        # Check for winner
        if self.check_winner(row, col):
            self.game_over = True
            self.winner = self.current_player
            logging.info(f"Player {self.current_player.value} WINS!")
            return True
        
        # Check for draw
        if self.move_count == self.COLS * self.ROWS:
            self.game_over = True
            logging.info("DRAW: Board is full")
            return True
        
        # Switch player
        self.current_player = Player.BLACK if self.current_player == Player.RED else Player.RED
        return True
    
    def check_winner(self, row: int, col: int) -> bool:
        """
        Check if the last move (at row, col) created a winning line.
        
        Check 4 directions from the placed disc:
        - Horizontal
        - Vertical
        - Diagonal (/)
        - Diagonal (\)
        
        Time Complexity: O(1) - only check from placed position
        """
        player = self.board[row][col]
        
        # Directions: right, up, diagonal-up-right, diagonal-up-left
        directions = [
            (0, 1),   # Horizontal
            (1, 0),   # Vertical
            (1, 1),   # Diagonal \
            (1, -1),  # Diagonal /
        ]
        
        for dr, dc in directions:
            # Count consecutive discs in this direction and opposite
            count = 1
            
            # Count in positive direction
            r, c = row + dr, col + dc
            while 0 <= r < self.ROWS and 0 <= c < self.COLS and self.board[r][c] == player:
                count += 1
                r += dr
                c += dc
            
            # Count in negative direction
            r, c = row - dr, col - dc
            while 0 <= r < self.ROWS and 0 <= c < self.COLS and self.board[r][c] == player:
                count += 1
                r -= dr
                c -= dc
            
            # Check if we have 4 in a row
            if count >= 4:
                logging.info(f"Found {count} in a row for {player.value} in direction ({dr}, {dc})")
                return True
        
        return False
    
    def get_board_state(self) -> List[List[str]]:
        """Return current board as list of strings"""
        return [[cell.value for cell in row] for row in self.board]
    
    def display_board(self):
        """Display the board in a nice format"""
        print("\n" + "=" * 29)
        print("Connect 4 - Current Board")
        print("=" * 29)
        
        # Display from top to bottom (reverse order)
        for row in range(self.ROWS - 1, -1, -1):
            print("| ", end="")
            for col in range(self.COLS):
                cell = self.board[row][col]
                # Highlight with colors in display
                if cell == Player.RED:
                    print("🔴", end=" ")
                elif cell == Player.BLACK:
                    print("🔵", end=" ")
                else:
                    print("·", end=" ")
            print("|")
        
        print("| ", end="")
        for col in range(self.COLS):
            print(col, end=" ")
        print("|")
        print("=" * 29 + "\n")
    
    def get_valid_moves(self) -> List[int]:
        """Return list of valid column indices"""
        return [col for col in range(self.COLS) if self.next_row[col] < self.ROWS]
    
    def get_game_status(self) -> str:
        """Return current game status"""
        if self.game_over:
            if self.winner:
                return f"Game Over - {self.winner.value} Wins!"
            else:
                return "Game Over - Draw!"
        else:
            return f"Current Turn: {self.current_player.value}"
    
    def reset(self):
        """Reset the game"""
        self.board = [[Player.EMPTY for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.next_row = [0] * self.COLS
        self.current_player = Player.RED
        self.game_over = False
        self.winner = None
        self.move_count = 0
        logging.info("Game reset")


class ConnectFourAI:
    """
    AI player for Connect 4 using minimax algorithm.
    
    Features:
    - Minimax with alpha-beta pruning
    - Difficulty levels (Easy, Medium, Hard)
    """
    
    def __init__(self, depth: int = 4):
        """
        Initialize AI.
        
        Args:
            depth: Search depth (higher = stronger, slower)
                   1-2: Easy
                   3-4: Medium
                   5+: Hard (slow)
        """
        self.depth = depth
        self.ai_player = Player.BLACK
        self.human_player = Player.RED
    
    def evaluate_position(self, board: List[List[Player]]) -> int:
        """
        Evaluate board position.
        
        Score based on:
        - Winning positions
        - Threat positions
        - Center control
        """
        score = 0
        
        # Center column control (higher value)
        center_col = ConnectFour.COLS // 2
        for row in range(ConnectFour.ROWS):
            if board[row][center_col] == self.ai_player:
                score += 3
            elif board[row][center_col] == self.human_player:
                score -= 3
        
        # Check all positions for patterns
        for row in range(ConnectFour.ROWS):
            for col in range(ConnectFour.COLS):
                # Check horizontal
                if col + 3 < ConnectFour.COLS:
                    score += self._evaluate_line(
                        [board[row][col + i] for i in range(4)], self.ai_player, self.human_player
                    )
                
                # Check vertical
                if row + 3 < ConnectFour.ROWS:
                    score += self._evaluate_line(
                        [board[row + i][col] for i in range(4)], self.ai_player, self.human_player
                    )
                
                # Check diagonal \
                if row + 3 < ConnectFour.ROWS and col + 3 < ConnectFour.COLS:
                    score += self._evaluate_line(
                        [board[row + i][col + i] for i in range(4)], self.ai_player, self.human_player
                    )
                
                # Check diagonal /
                if row + 3 < ConnectFour.ROWS and col - 3 >= 0:
                    score += self._evaluate_line(
                        [board[row + i][col - i] for i in range(4)], self.ai_player, self.human_player
                    )
        
        return score
    
    def _evaluate_line(self, line: List[Player], ai: Player, human: Player) -> int:
        """Evaluate a line of 4 positions"""
        ai_count = sum(1 for cell in line if cell == ai)
        human_count = sum(1 for cell in line if cell == human)
        empty_count = sum(1 for cell in line if cell == Player.EMPTY)
        
        # Winning position
        if ai_count == 4:
            return 10000
        if human_count == 4:
            return -10000
        
        # Strong positions
        if ai_count == 3 and empty_count == 1:
            return 100
        if human_count == 3 and empty_count == 1:
            return -100
        
        if ai_count == 2 and empty_count == 2:
            return 10
        if human_count == 2 and empty_count == 2:
            return -10
        
        return 0
    
    def get_best_move(self, game: ConnectFour) -> int:
        """
        Get best move using minimax algorithm.
        
        Time Complexity: O(7^depth) in worst case
        Space Complexity: O(depth) for recursion stack
        """
        best_score = float('-inf')
        best_col = None
        valid_moves = game.get_valid_moves()
        
        for col in valid_moves:
            # Make move temporarily
            row = game.next_row[col]
            game.board[row][col] = self.ai_player
            game.next_row[col] += 1
            
            # Evaluate position
            score = self._minimax(game, self.depth - 1, float('-inf'), float('inf'), False)
            
            # Undo move
            game.board[row][col] = Player.EMPTY
            game.next_row[col] -= 1
            
            if score > best_score:
                best_score = score
                best_col = col
        
        return best_col if best_col is not None else valid_moves[0]
    
    def _minimax(self, game: ConnectFour, depth: int, alpha: float, beta: float, is_max: bool) -> int:
        """Minimax algorithm with alpha-beta pruning"""
        # Terminal conditions
        if depth == 0:
            return self.evaluate_position(game.board)
        
        # Check for winning move
        valid_moves = game.get_valid_moves()
        if not valid_moves:
            return self.evaluate_position(game.board)
        
        if is_max:
            # Maximizing player (AI)
            max_eval = float('-inf')
            for col in valid_moves:
                row = game.next_row[col]
                game.board[row][col] = self.ai_player
                game.next_row[col] += 1
                
                eval_score = self._minimax(game, depth - 1, alpha, beta, False)
                
                game.board[row][col] = Player.EMPTY
                game.next_row[col] -= 1
                
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            
            return max_eval
        else:
            # Minimizing player (Human)
            min_eval = float('inf')
            for col in valid_moves:
                row = game.next_row[col]
                game.board[row][col] = self.human_player
                game.next_row[col] += 1
                
                eval_score = self._minimax(game, depth - 1, alpha, beta, True)
                
                game.board[row][col] = Player.EMPTY
                game.next_row[col] -= 1
                
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            
            return min_eval


# --------------------------------------------------
# TEST CASES AND GAMEPLAY
# --------------------------------------------------
def test_basic_gameplay():
    """Test basic game mechanics"""
    print("\n" + "=" * 50)
    print("TEST 1: Basic Gameplay")
    print("=" * 50)
    
    game = ConnectFour()
    game.display_board()
    
    # Test moves
    moves = [3, 3, 4, 4, 5, 5, 6]  # Column indices
    for col in moves:
        if game.game_over:
            break
        game.drop_disc(col)
        game.display_board()
        print(game.get_game_status())


def test_horizontal_win():
    """Test horizontal win condition"""
    print("\n" + "=" * 50)
    print("TEST 2: Horizontal Win")
    print("=" * 50)
    
    game = ConnectFour()
    
    # RED: 0, BLACK: 1, RED: 1, BLACK: 1, RED: 2, BLACK: 1, RED: 3 (wins)
    moves = [0, 1, 1, 1, 2, 1, 3]
    
    for col in moves:
        if game.game_over:
            break
        result = game.drop_disc(col)
        print(f"Move: column {col}, status: {result}")
    
    game.display_board()
    print(game.get_game_status())


def test_vertical_win():
    """Test vertical win condition"""
    print("\n" + "=" * 50)
    print("TEST 3: Vertical Win")
    print("=" * 50)
    
    game = ConnectFour()
    
    # RED: 0, BLACK: 1, RED: 0, BLACK: 1, RED: 0, BLACK: 1, RED: 0 (wins)
    moves = [0, 1, 0, 1, 0, 1, 0]
    
    for col in moves:
        if game.game_over:
            break
        game.drop_disc(col)
    
    game.display_board()
    print(game.get_game_status())


def test_diagonal_win():
    """Test diagonal win condition"""
    print("\n" + "=" * 50)
    print("TEST 4: Diagonal Win")
    print("=" * 50)
    
    game = ConnectFour()
    
    # Setup diagonal win scenario
    moves = [0, 1, 1, 2, 3, 2, 2, 3, 3, 4, 3]
    
    for col in moves:
        if game.game_over:
            break
        game.drop_disc(col)
    
    game.display_board()
    print(game.get_game_status())


def test_draw():
    """Test draw condition"""
    print("\n" + "=" * 50)
    print("TEST 5: Draw (Full Board)")
    print("=" * 50)
    
    game = ConnectFour()
    
    # Pattern that fills board without winner
    # This is a simplified pattern - not actual draw sequence
    cols = [3, 3, 3, 3, 4, 4, 4, 4, 2, 2, 2, 2, 5, 5, 5, 5, 1, 1, 1, 1, 6, 6, 6, 6, 0, 0, 0, 0]
    
    for col in cols:
        if game.game_over:
            break
        game.drop_disc(col)
    
    game.display_board()
    print(game.get_game_status())


def test_invalid_moves():
    """Test invalid move handling"""
    print("\n" + "=" * 50)
    print("TEST 6: Invalid Moves")
    print("=" * 50)
    
    game = ConnectFour()
    
    # Test invalid column
    result = game.drop_disc(10)
    print(f"Drop in column 10: {result}")
    
    # Fill a column
    for _ in range(6):
        game.drop_disc(0)
    
    # Try to drop in full column
    result = game.drop_disc(0)
    print(f"Drop in full column: {result}")
    print(f"Valid moves: {game.get_valid_moves()}")


def test_ai_player():
    """Test AI gameplay"""
    print("\n" + "=" * 50)
    print("TEST 7: AI Player (Demo)")
    print("=" * 50)
    
    game = ConnectFour()
    ai = ConnectFourAI(depth=3)
    
    print("Game: Human (RED) vs AI (BLACK)")
    game.display_board()
    
    # Simulate a few moves
    moves = [3, 4, 3, 5]  # Human moves
    for i, col in enumerate(moves):
        if game.game_over:
            break
        
        # Human move
        print(f"\n--- Turn {i + 1} ---")
        print(f"Human plays column {col}")
        game.drop_disc(col)
        game.display_board()
        
        if game.game_over:
            break
        
        # AI move
        ai_col = ai.get_best_move(game)
        print(f"AI plays column {ai_col}")
        game.drop_disc(ai_col)
        game.display_board()


def main():
    """Run all tests"""
    print("=" * 50)
    print("CONNECT 4 GAME TESTS")
    print("=" * 50)
    
    test_basic_gameplay()
    test_horizontal_win()
    test_vertical_win()
    test_diagonal_win()
    test_draw()
    test_invalid_moves()
    test_ai_player()


if __name__ == "__main__":
    main()
