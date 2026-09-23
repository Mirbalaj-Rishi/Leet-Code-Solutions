#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
       int first_m = matrix[0][0];
       int m = matrix.size();
       int n = matrix[0].size();
        int i_found = 0;
       //search row
       if(m > 1){
            for(int i =1; i < m; i++){
                int amount = matrix[i][0];
                //cout << i <<" "<< amount << " " << m << endl;
                if(first_m <= target && target < amount){
                    i_found = i - 1; // i - 1 avoids the last line so we dont mix up rows
                    break;
                }else if(i+1 == m && amount <= target){ // if the last row has the target
                    i_found = i; //  include the last line 
                    break;
                }
                first_m = amount;
            }
       }
       //search column
        for(int j = 0; j < n; j++){
            int returned_value = matrix[i_found][j];
            if( returned_value == target){
                return true;
            }
        }

       return false;
    }
};

