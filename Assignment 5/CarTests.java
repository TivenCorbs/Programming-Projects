import static org.junit.Assert.assertEquals;

import org.junit.Test;
public class CarTests{

 
    public static void main(String args[]){
        Car car1 = new Car(1,1,34.4f);
        Car car2 = new Car(343,2,34.5f);
        Car car3 = new Car(125,3,54.5f);
        car1.setId(23435);
        car1.setPricePerDay(13.4f);
        car1.setPowerSource(2);
        assertEquals(13.4f, car1.getPricePerDay());
        assertEquals(2,car1.getPowerSource());
        assertEquals(343,car2.getId());
        assertEquals(2,car2.getPowerSource());
        assertEquals(54.5f,car3.getPricePerDay()); 
    }
    


}