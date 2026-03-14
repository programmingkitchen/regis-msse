# MSSE670 


## Revision History

**8/27/22**

Uploaded Week 2 Fleet Rental Code.

Uploaded docs for the Airline Reservation Assignment

Test

## AIRLINE RESERVATION SYSTEM

1. The project is to implement a flight reservation application with a UI front (SWING, etc.) for both the travelers and the reservation manager.

2. The customer shall be able to register him/herself with the reservation site, enter personal profile information (name, address, email, and credit card information), prepare for itineraries, and book flights.

3. The reservation manager shall be able to publish and update flight information, and generate inventory report.

4. The following functionalities should be provided for the reservation manager:

4.1. A page for the manager to log in with username manager and password.

4.2. One page for the manager to add/cancel/list flights with the following information: airline code/name, flight number, departure location, departure day of the week/time, arrival location, arrival day of the week/time, cost of business class and cost of economy class ticket.

4.3. The flight number is a 3-digit number, prefixed with 0’s if less the actual number is less than 100. For simplicity, it is predefined that there are 10 seats of business class and 30 seats of economy class seats in each flight.

4.4. The airline code must be a two-letter code defined in
http://www.tvlon.com/resources/airlinecodes.htm

4.5. The airport location must be one of airport with a three-letter code defined in http://www.orbitz.com/App/global/airportCodes.jsp

4.6. The inventory report shall contain a summary of all fights in the reservation system 


5. The following functionalities should be provided for travelers:

5.1. A page for a traveler to register him/herself with name, address, username and password, email address, as well as credit card information (optional), including a 16-digit card number and a 4-digit expiration date.

5.2. A page for a traveler to log in with username and password.

5.3. A travel itinerary is a travel arrangement with one or more flights. It has the status reserved when it is created by a traveler, booked when it is paid, and canceled when it is deleted by the traveler from his/her itinerary list.
 
 5.4. A traveler shall be able to create and book a travel itinerary by going through the following steps:

5.4.1. Search for flight information by providing departure/arrival date/time and location, number of passengers, one-way or round trip.

5.4.2. A list of available itinerary options will be shown to the traveler, with departure/arrival and cost information. The departure time will be plus or minus hours within the specified departure time. It is possible that one itinerary contains one or more flights from one or more different airlines. The maximum legs in an itinerary are limited to 2.

5.4.3. Once the traveler selects an itinerary from the list, he or she has the option to reserve it.

5.4.4. Once the traveler reserves an itinerary, he or she has the option to book it by providing payment information via credit card. 

5.4.5. A traveler shall be able to cancel an itinerary from his/her itinerary list.

## FLEET RENTAL DEMO CODE

**Original Fleet Rental Design**
FleetRental is a fictitious car rental business that caters to high-end clients interested in renting high-performance and exotic cars. Cars such as Dodge Viper, Ford GT50, Lotus Elise, 911 Porsche, and Mercedes M3 are some of the cars that are offered initially. 

Based on marketing studies, only major U.S., cities will host this business, which includes New York, Chicago, Houston, Los Angeles, and Denver, the company HQ, will be first city where this is available as a pilot.

During the pilot phase of this application it will be built as a windows based fat-client used by customer support reps (CSRs). In this phase, all orders will be placed via CSRs. This implies that inventory browsing, rental rate info will only be conveyed by the CSR. 

Future implementation will make the application web enabled.
