#include <iostream>
#include <vector>
#include "Eigen/Dense"
#include <cmath>

using namespace std;

double f(int n, int choose_f) {
    switch(choose_f){
        case 1:
            return n*n;
        case 2:
            return pow(n,3) + cos(n)*pow(n,4);
        case 3:
            return pow(n,n);
        case 4:
            return pow(n,3)+ n*n + n + 1;
    }
}

// In các phần tử của ma trận
void cout_matrix(vector<vector<double>> x) {
    for (const auto& row : x) {
        for (double element : row) {
            std::cout << element << " ";
        }
        std::cout << std::endl;
    }
}

vector<vector<double>> chuyenVi(const vector<vector<double>>& matrix) {
    // Lấy số hàng và số cột của ma trận ban đầu
    int rows = matrix.size();
    int cols = matrix[0].size();

    // Khởi tạo ma trận chuyển vị với số hàng và số cột ngược lại
    vector<vector<double>> transposed(cols, vector<double>(rows));

    // Lặp qua từng phần tử của ma trận ban đầu và gán vào vị trí tương ứng trong ma trận chuyển vị
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            transposed[j][i] = matrix[i][j];
        }
    }

    // Trả về ma trận chuyển vị
    return transposed;
}

// Hàm nhân hai ma trận
vector<vector<double>> multiplyMatrices(const vector<vector<double>>& matrix1, const vector<vector<double>>& matrix2) {
    int rows1 = matrix1.size();
    int cols1 = matrix1[0].size();
    int rows2 = matrix2.size();
    int cols2 = matrix2[0].size();

    // Kiểm tra tính hợp lệ của phép nhân
    if (cols1 != rows2) {
        cout << "Không thể nhân hai ma trận này." << endl;
        return {};
    }

    // Khởi tạo ma trận kết quả với kích thước phù hợp
    vector<vector<double>> result(rows1, vector<double>(cols2, 0));

    // Thực hiện phép nhân ma trận
    for (int i = 0; i < rows1; ++i) {
        for (int j = 0; j < cols2; ++j) {
            for (int k = 0; k < cols1; ++k) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    return result;
}


// Tính ma trận nghịch đảo của một ma trận vuông
vector<vector<double>> inverse(const vector<vector<double>>& A) {
    // Chuyển đổi ma trận vector sang Eigen::MatrixXd
    Eigen::MatrixXd eigA(A.size(), A[0].size());
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < A[0].size(); j++) {
            eigA(i, j) = A[i][j];
        }
    }

    // Tính ma trận nghịch đảo
    Eigen::MatrixXd invA = eigA.inverse();

    // Chuyển đổi ma trận Eigen::MatrixXd sang vector
    vector<vector<double>> invAVec(invA.rows(), vector<double>(invA.cols()));
    for (int i = 0; i < invA.rows(); i++) {
        for (int j = 0; j < invA.cols(); j++) {
            invAVec[i][j] = invA(i, j);
        }
    }

    return invAVec;
}


int check(double (*function)(int, int), int a, int b, int step, int choose_f, int &luythua) {
    int rows;
    int cols = 2;
    int cols_y = 1;
    rows = int((b - a) / step) + 1;

    //cout << "columns of matrix: " << rows << "\n";

    // Khởi tạo ma trận là một vector 2 chiều
    vector<vector<double>> matrixX(rows, vector<double>(cols));
    vector<vector<double>> matrixY(rows, vector<double>(cols_y));

    // Nhập dữ liệu cho ma trận
    for (int i = 0; i < rows; ++i) {
        matrixY[i][0] = log2(function(a + i * step, choose_f));
        //cout << "f("<< a+i*1 <<") = n^2 = " << function(a+i*step, choose_f) << "\n";
        matrixX[i][0] = log2(a + i * step);
        matrixX[i][1] = 1;
    }

    //cout_matrix(matrixX);
    //cout_matrix(matrixY);

    vector<vector<double>> result(2, vector<double>(1));
    result = multiplyMatrices(multiplyMatrices((inverse(multiplyMatrices(chuyenVi(matrixX), matrixX))), chuyenVi(matrixX)), matrixY);
    double alpha = result[0][0];
    //cout << "alpha = " << alpha;


    if(alpha>0){
        int alpha_temp = ceil(alpha);
        //cout<<"\nalpha_temp = "<<alpha_temp;
        // f(n) = a0 + a1*n + a2*n^2 + ... + a_alpha * n^alpha
        // Y = N*A
        // (alpha_temp x 1) = (alpha_temp x alpha_temp) * (alphatemp x 1)
        vector<vector<double>> N(alpha_temp, vector<double>(alpha_temp));
        vector<vector<double>> Y(alpha_temp, vector<double>(1));
        vector<vector<double>> A(alpha_temp, vector<double>(1));
        A = multiplyMatrices(inverse(N), Y);
        if (A[alpha_temp-1][0] != 0){ // he so a_alpha khac 0 => deg{f(n)} = n^alpha => f(n) = O(n^alpha)
            luythua = alpha_temp;
            return 1; 
        } 
        else {return 0;}
    }
    else {
        return 0;
    }
}

int main() {
    int choose_f;
    int luythua;
    cout<<"Nhap ham f(n) muon kiem tra [1,4]:"; cin>>choose_f;
    while((4<choose_f) || (choose_f<1)){
        cout<<"Nhap choose_f de chon f(n) gia tri [1,4]!!!";
        cout<<"\nNhap lai choose_f: ";
        cin>>choose_f;
    }

    int a,b,step;
    cout<<"Nhap a,b nguyen duong (a<b).\n";
    cout<<"a = "; cin>>a;
    cout<<"b = "; cin>>b;
    cout<<"Nhap step:"; cin>>step;
    while((b<=a) || ((b-a)%step)!=0){
        cout<<"Nhap lai a, b va step!";
        cout<<"\na = "; cin>>a;
        cout<<"b = "; cin>>b;
        cout<<"step = ";cin>>step;
    }

    int result = check(f, a, b, step, choose_f, luythua);
    if (result == 1) {
        cout << "=> f(n) = O(n^"<< luythua<<")";
    }
    else {
        cout << "=> Khong phai!";
    }
    return 0;
}