//CODE LINK : https://leetcode.com/problems/set-matrix-zeroes/description/


class Solution {
    public void setZeroes(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        boolean[] rows = new boolean[n];
        boolean[] cols = new boolean[m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(mat[i][j] == 0){
                    rows[i] = true;
                    cols[j] = true;
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(rows[i] == true || cols[j] == true){
                    mat[i][j] = 0;
                }
            }
        }
    }
}
