class Person {
    public:
        int work;
        int sleep;
        int age;
        Person(int work, int sleep, int age){
            this->work = work;
            this->sleep = sleep;
            this->age = age;
        }
        int stressLevel(){
            int dmReturn;
            if(age >= 18){
                dmReturn = 20;
            }
            else{
                dmReturn = 15;
            }
            return (work - sleep) + dmReturn; 
        }
};

