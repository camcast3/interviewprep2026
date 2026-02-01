from typing import List


def verify_sudoku_board(sudoku_board: List[List[int]]) -> bool:
    row = [set() for _ in range(9)]
    column = [set() for _ in range(9)]
    subgird = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        print(f"\n--- Row {r} ---")
        for c in range(9):
            num = sudoku_board[r][c]

            # Skip empty cells (represented by 0)
            if num == 0:
                continue

            print(f"Cell [{r}][{c}] = {num}", end=" | ")

            if num in row[r]:
                print(f"❌ DUPLICATE in row {r}")
                return False
            elif num in column[c]:
                print(f"❌ DUPLICATE in column {c}")
                return False
            elif num in subgird[r // 3][c // 3]:
                print(f"❌ DUPLICATE in subgrid [{r // 3}][{c // 3}]")
                return False
            else:
                row[r].add(num)
                column[c].add(num)
                subgird[r // 3][c // 3].add(num)
                print(f"✓ Valid")

    print("\n✅ Sudoku board is VALID!")
    return True
