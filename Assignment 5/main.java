 import java.util.ArrayList;
public class main {

    public static void main(String[] args){
        Car car1 = new Car(1,1,41.2f);
        Car car2 = new Car(343,2,34.5f);
        Car car3 = new Car(125,3,54.5f);
        car1.setId(2);
        car1.setPricePerDay(13.4f);
        car1.setPowerSource(1);
        CarFleet myfleet = new CarFleet();
        if(myfleet.addCar(car1)==true){
        }
        if(myfleet.addCar(car2)==true){

        }
        if(myfleet.addCar(car3)==true){
        }
        Queue<Integer> myQueue = new Queue<Integer>();
        myQueue.enqueue(1);
        myQueue.enqueue(2);
        myQueue.enqueue(3);

        ArrayList<Car> mycar = myfleet.processRequests(myQueue);
        System.out.println(mycar.get(0).getId());
        System.out.println(mycar.get(1).getPricePerDay());
        System.out.println(mycar.get(2).getPricePerDay());
        System.out.println(mycar.size());

    }
    
}
