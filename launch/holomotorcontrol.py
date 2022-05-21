using namespace std
#include <iostream>
#include <cmath>





class holorobot{
    public:
        int vx,vy,theta;         // translational velocity xdir, ydir, angular, angle, rad and heading direction  
        int alpha1,alpha2,alpha3,alpha4;
        int w1,w2,w3,w4;      //  Speed wheels 1-4(RPM)
        float rad;
        int head;
        framesize = 400 x 400;
        
        //defines the size of the robot 
        def setHeading();
        def calcWheelSpeed();
           

        
};

def setHeading(){
     theta = 90 ; // move straight 
            //passes coordinates to calculate wheel speed 
     vx = ;
     vy = ; 
            //defines the direction of movement  


}
def calcWheelSpeed(){
            alpha1 =0.785398;//45
            alpha2 =2.35619;//135
            alpha3 =3.92699;//225
            alpha4 =5.49779;//315
            //takes coordinates and computes wheel rpm 
            w1 = 1/Rad*sin(alpha1)*vx + cos(alpha1)vy + rad*theta;
            w2 = 1/Rad*sin(alpha2)*vx + cos(alpha2)vy + rad*theta;
            w3 = 1/Rad*sin(alpha3)*vx + cos(alpha3)vy + rad*theta;
            w4 = 1/Rad*sin(alpha4)*vx + cos(alpha4)vy + rad*theta;

            
        }


int main(){


}
