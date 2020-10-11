import os

from settings import *

K_b = pygame.image.load(os.path.join("img", "king-black.png"))
Q_b = pygame.image.load(os.path.join("img", "queen-black.png"))
B_b = pygame.image.load(os.path.join("img", "bishop-black.png"))
H_b = pygame.image.load(os.path.join("img", "knight-black.png"))
R_b = pygame.image.load(os.path.join("img", "rook-black.png"))
P_b = pygame.image.load(os.path.join("img", "pawn-black.png"))

K_w = pygame.image.load(os.path.join("img", "king-white.png"))
Q_w = pygame.image.load(os.path.join("img", "queen-white.png"))
B_w = pygame.image.load(os.path.join("img", "bishop-white.png"))
H_w = pygame.image.load(os.path.join("img", "knight-white.png"))
R_w = pygame.image.load(os.path.join("img", "rook-white.png"))
P_w = pygame.image.load(os.path.join("img", "pawn-white.png"))

IMAGES = [pygame.transform.scale(K_w, IMG_SCALE),
          pygame.transform.scale(K_b, IMG_SCALE),
          pygame.transform.scale(Q_w, IMG_SCALE),
          pygame.transform.scale(Q_b, IMG_SCALE),
          pygame.transform.scale(B_w, IMG_SCALE),
          pygame.transform.scale(B_b, IMG_SCALE),
          pygame.transform.scale(H_w, IMG_SCALE),
          pygame.transform.scale(H_b, IMG_SCALE),
          pygame.transform.scale(R_w, IMG_SCALE),
          pygame.transform.scale(R_b, IMG_SCALE),
          pygame.transform.scale(P_w, IMG_SCALE),
          pygame.transform.scale(P_b, IMG_SCALE)]


class Piece:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.image = None
        self.firstMove = True

    def draw(self):
        """
        Draws piece
        :return: None
        """
        if self.color == WHITE:
            SCREEN.blit(IMAGES[self.image], to_coords(self.x, self.y))
        else:
            SCREEN.blit(IMAGES[self.image+1], to_coords(self.x, self.y))

    def move(self, x, y):
        """
        Updates x and y coordinates for Piece
        :param x: x coordinate on grid
        :param y: y coordinate on grid
        :return: None
        """
        self.x = x
        self.y = y

    def copy(self):
        """
        Creates a deep copy of the current piece
        :return: reference to a new Piece object
        """
        copy = type(self)(self.x, self.y, self.color)
        copy.image = self.image
        copy.firstMove = self.firstMove
        return copy


class King(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = 0

    def __repr__(self):
        return "King"

    def valid_moves(self, board):
        moves = []

        # Move 1 in each direction
        for x in range(self.x-1, self.x+2):
            for y in range(self.y-1, self.y+2):
                if board.valid_move((x, y), self.color):
                    moves.append((x, y))
        return moves


class Queen(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = 2

    def __repr__(self):
        return "Queen"

    def valid_moves(self, board):

        # Queen's move set is Rook and Bishop combined
        moves = Rook.valid_moves(self, board) + Bishop.valid_moves(self, board)

        return moves


class Bishop(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = 4

    def __repr__(self):
        return "Bishop"

    def valid_moves(self, board):
        moves = []

        # Up left
        x, y = self.x, self.y
        while board.valid_move((x-1, y-1), self.color):
            moves.append((x-1, y-1))
            if board.piece_at_coords((x-1, y-1)):
                break
            x -= 1
            y -= 1

        # Up right
        x, y = self.x, self.y
        while board.valid_move((x+1, y-1), self.color):
            moves.append((x+1, y-1))
            if board.piece_at_coords((x+1, y-1)):
                break
            x += 1
            y -= 1

        # Down left
        x, y = self.x, self.y
        while board.valid_move((x-1, y+1), self.color):
            moves.append((x-1, y+1))
            if board.piece_at_coords((x-1, y+1)):
                break
            x -= 1
            y += 1

        # Down right
        x, y = self.x, self.y
        while board.valid_move((x+1, y+1), self.color):
            moves.append((x+1, y+1))
            if board.piece_at_coords((x+1, y+1)):
                break
            x += 1
            y += 1

        return moves


class Knight(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = 6

    def __repr__(self):
        return "Knight"

    def valid_moves(self, board):
        moves = []

        # Move 1 diagonal, 1 straight
        for x in range(self.x-2, self.x+3):
            for y in range(self.y-2, self.y+3):
                if abs(self.x - x) == 2 and abs(self.y - y) == 1 or abs(self.x - x) == 1 and abs(self.y - y) == 2:
                    if board.valid_move((x, y), self.color):
                        moves.append((x, y))
        return moves


class Rook(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = 8

    def __repr__(self):
        return "Rook"

    def valid_moves(self, board):
        moves = []

        # Up
        for y in range(self.y-1, -1, -1):
            if board.valid_move((self.x, y), self.color):
                moves.append((self.x, y))
            if board.piece_at_coords((self.x, y)):
                break

        # Down
        for y in range(self.y+1, 8, 1):
            if board.valid_move((self.x, y), self.color):
                moves.append((self.x, y))
            if board.piece_at_coords((self.x, y)):
                break

        # Left
        for x in range(self.x-1, -1, -1):
            if board.valid_move((x, self.y), self.color):
                moves.append((x, self.y))
            if board.piece_at_coords((x, self.y)):
                break

        # Right
        for x in range(self.x+1, 8, 1):
            if board.valid_move((x, self.y), self.color):
                moves.append((x, self.y))
            if board.piece_at_coords((x, self.y)):
                break

        return moves


class Pawn(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = 10

    def __repr__(self):
        return "Pawn"

    def valid_moves(self, board):
        moves = []

        if board.bottomPlayerTurn:
            # Move forward 1
            if board.valid_move((self.x, self.y-1), self.color) \
                    and not board.piece_at_coords((self.x, self.y-1)):
                moves.append((self.x, self.y-1))

                # Move forward 2 on first move
                if board.valid_move((self.x, self.y-2), self.color) \
                        and not board.piece_at_coords((self.x, self.y-2)) \
                        and self.firstMove:
                    moves.append((self.x, self.y-2))

            # Attack diagonal left
            if board.valid_move((self.x-1, self.y-1), self.color) \
                    and board.enemy_at_coords((self.x-1, self.y-1), self.color):
                moves.append((self.x-1, self.y-1))

            # Attack diagonal right
            if board.valid_move((self.x+1, self.y-1), self.color) \
                    and board.enemy_at_coords((self.x+1, self.y-1), self.color):
                moves.append((self.x+1, self.y-1))
        else:
            # Move forward 1
            if board.valid_move((self.x, self.y+1), self.color) \
                    and not board.piece_at_coords((self.x, self.y+1)):
                moves.append((self.x, self.y+1))

                # Move forward 2 on first move
                if board.valid_move((self.x, self.y+2), self.color) \
                        and not board.piece_at_coords((self.x, self.y+2)) \
                        and self.firstMove:
                    moves.append((self.x, self.y+2))

            # Attack diagonal left
            if board.valid_move((self.x-1, self.y+1), self.color) \
                    and board.enemy_at_coords((self.x-1, self.y+1), self.color):
                moves.append((self.x-1, self.y+1))

            # Attack diagonal right
            if board.valid_move((self.x+1, self.y+1), self.color) \
                    and board.enemy_at_coords((self.x+1, self.y+1), self.color):
                moves.append((self.x+1, self.y+1))

        return list(set(moves))
