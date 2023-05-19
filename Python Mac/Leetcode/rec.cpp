#include<iostream>
using namespace std;

void p(int a,int b){
    if(b==a){
        exit(0);
    }
    else{
        cout<<"\n"<<b;
        p(a,b+1);
    }
}

int main(){
    int a=10,b;
    p(a,0);
}