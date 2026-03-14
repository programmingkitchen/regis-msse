package com.flightreservation.ui;
import java.util.List;

import com.flightreservation.model.services.factory.ServiceFactory;
import com.flightreservation.model.services.reservationservice.IReservationService;
import com.flightreservation.model.domain.*;
import com.flightreservation.model.business.exception.*;
import com.flightreservation.model.services.exception.ReservationException;

/**
 * We need to pass in the app.properties file using the -D option.  We configure this in:
 * 
 * Run As (right click on project > 
 * Run Configurations (select from menu) > 
 * Arguments (tab of new window) > 
 * VM Arguments (bottom window)
 * 
 * FULL ARGUMENT (PUT THIS IN THE BOX AFTER CHANGING PATH)
 * WARNING:  follow this format exactly, no spaces anywhere. 
 * -Dprop_location:prop_location=C:\Users\rgran\Dropbox\ECLIPSE-WORKSPACE\MSSE670-AIRLINE-RESERVATION\AirlineReservation\config\application.properties
 * 
 * PATH (reference, you must change this)
 * C:\Users\rgran\Dropbox\ECLIPSE-WORKSPACE\MSSE670-AIRLINE-RESERVATION\AirlineReservation\config
 * 
 * @author Randall Granier
 *
 */

public class RunApp {
	
	/**
	 * Changed the old "ServiceFactory" to "SimpleServiceFactory."   We still have both options.
	 * The newly renamed SimpleServiceFactory was called with the following code:
	 * 
	 * SimpleServiceFactory factory = new SimpleServiceFactory();
	 * IReservationService reservation = factory.getReservationService();
	 *
	 * @param args
	 */

	/**
	 * 
	 * @param args
	 
	public static void main(String[] args) {
		
		ServiceFactory serviceFactory = ServiceFactory.getInstance();
		//IReservationService reservation;
		IReservationService reservation;
		
		//
		// USE THIS APPROOACH OF CASTING TO AN INTERFACE
		//
		// Here we are casting Factory output to ILoginService, which
		// means that loginService will only see methods declared in
		// the interface and implemented by LoginServiceImpl
		//
		try {
			//reservation = (IReservationService) serviceFactory.getService(IReservationService.NAME);
			reservation = (IReservationService) serviceFactory.getService(IReservationService.NAME);
			
			List<Flight> flightList = reservation.listFlights();
			
			//System.out.println(flightList);
			
			for (Flight flight : flightList) {
				System.out.println("Flight ID: " + flight.getId());
				System.out.println("Origin Airport: " + flight.getOriginAirport() + "\t\tDeparture Time: " + flight.getDepartureTime());
				System.out.println("Destination Airport: " + flight.getOriginAirport() + "\t\tArrival Time: " + flight.getArrivalTime());
			}
			
			reservation.reserveFlight(100);
			
		} catch (ServiceLoadException ex) {
			ex.printStackTrace();
		} catch (ReservationException ex) {
			ex.printStackTrace();
		}

	}  // end main
	
	*/
} // end class RunApp
