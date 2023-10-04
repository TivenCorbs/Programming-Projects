import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;
import java.util.*;
import java.util.ArrayList;
import org.junit.Test;

public class CarFleetTests {

    Car car1 = new Car(1,1,34.4f);
    Car car2 = new Car(343,2,34.5f);
    Car car3 = new Car(125,3,54.5f);
    CarFleet fleet = new CarFleet();


    @Test
    public void TestaddCar(){
        assertEquals(true, fleet.addCar(car1));
        assertEquals(true, fleet.addCar(car2));
        assertEquals(true, fleet.addCar(car3));
    }
    @Test
    public void TestprocessRequests(){
        Queue<Integer> list = new Queue<Integer>();
        list.enqueue(1);
        list.enqueue(2);
        list.enqueue(3);
        List<Car> myList = Arrays.asList(car1,car2,car3);
        List<Car> expected = fleet.processRequests(list);
        assertEquals(myList.size(),expected.size());
        
    }


}

