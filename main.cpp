#include <iostream>
#include<algorithm>
using namespace std;

int main(){
    int n,s[20];
    bool allpass;
    bool allfail;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>s[i];
    }
    sort(s,s+n);

    if(s[0]>60 && s[n-1]>60){
        allpass=true;
    }
    if(s[0]<60 && s[n-1]<60){
        allfail=true;
    }
    for(int m=0;m<n;m++){

        cout<<s[m]<<" ";
    }
    cout<<endl;

    if(allpass){
        cout<<"best case"<<endl;
        cout<<s[0]<<endl;
    }
    if(allfail){
        cout<<s[n-1]<<endl;
        cout<<"worst case"<<endl;
    }
    if(!allpass && !allfail){
        for(int k=1;k<n;k++){
            if(s[k]>60){
                cout<<s[k-1]<<endl;
                cout<<s[k];
                break;
            }
        }
    }
}
















