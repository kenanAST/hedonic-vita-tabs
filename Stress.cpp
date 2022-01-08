#include <iostream>
#include "Person.h"
using namespace std;




int main(){

    while(true){
        int work, sleep, age;
        cout << "Enter work: ";
        cin >> work;

        cout << "Enter sleep: ";
        cin >> sleep;

        cout << "Enter age: ";
        cin >> age;

        Person person(work, sleep, age);

        cout << "Stress Level: " << person.stressLevel() << "\n";
        if(person.stressLevel() < 20){
            cout << "Eat One Dose";
        }
        else if(person.stressLevel() >= 20 && person.stressLevel() <= 24){
            cout << "Eat Two Dose";
        }
        else{
            cout << "Eat Three Dose";
        }
        cout << "\n\n";
    }
}