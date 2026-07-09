class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i<board.length; i++){
            HashSet<Character> rowSet = new HashSet<>();
            HashSet<Character> colSet = new HashSet<>();
            for(int j = 0; j<board.length;j++){
                if(board[i][j]!='.'){
                    if(!rowSet.contains(board[i][j])) {rowSet.add(board[i][j]);}
                    else {return false;}
                }
                if(board[j][i]!='.'){
                    if(!colSet.contains(board[j][i])) {colSet.add(board[j][i]);}
                    else{ return false;}
                }
            }
        }
        int d = 0;
        while(d<9){
            HashSet<Character> A = new HashSet<>();
            HashSet<Character> B = new HashSet<>();
            HashSet<Character> C = new HashSet<>();
           for(int i = d; i<d+3; i++){
            for(int j = 0; j<9; j++){
                if(board[i][j]=='.') continue;
                if (j / 3 == 0) {
                    if (A.contains(board[i][j])) {
                        return false;
                    } else {
                        A.add(board[i][j]);
                    }
                } else if (j / 3 == 1) {
                    if (B.contains(board[i][j])) {
                        return false;
                    } else {
                        B.add(board[i][j]);
                    }
                } else if (j / 3 == 2) {
                    if (C.contains(board[i][j])) {
                        return false;
                    } else {
                        C.add(board[i][j]);
                    }
                }
            }
           }
           System.out.println(A);
           System.out.println(B);
           System.out.println(C);
           d += 3; 
        }
        
        return true;
    }
}