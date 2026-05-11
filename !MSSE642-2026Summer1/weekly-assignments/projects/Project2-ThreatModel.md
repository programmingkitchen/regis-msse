# Hands-On Assignment #2: Vulnerability Analysis

## Assignment 2 Group Project: The Secure Software Development Lifecycle and the Threat Model

**Version 3.6, Revised 5/11/2026**

---

## General Directions

- This is a collaboration project. You are encouraged to work in groups of 2 or 3.

---

## Part 1: Secure Design Document Overview (1 to 2 pages)

Write a short Design Document that will include secure software concepts applicable to the **Hiking Club Application**. You can choose another application with prior approval, but it should have the same characteristics of a traditional relational-database application. Other good examples could include a reservation system different from the Hiking Club (hotel, yoga class, college class enrollment), an eCommerce system, or a Blog with multiple users who have the ability to post and reply to the posts of others.

The Design Document for Week 1 should include:

1. A high-level project description in your own words (summarize the given software description). Summarize in one paragraph (up to 5 sentences). Do not copy the existing project description.

2. A description of the organization that will use the application.

3. A description of the environment where the application will be deployed (cloud, co-located in a data center, server closet in the office of the organization, etc.). You will have to decide this.

4. Include a general discussion of secure concepts applicable to the Hiking Club Application. Look for clues in the "Software Project Description." Just identify the areas that require security. The details about how to make these areas secure are the subject of Part 2, the Threat Model.

---

## Part 2: Hiking Club Threat Model Assessment

For Part 2, you will develop a threat model for your Secure Design Document (Part 1).

### Architectural Description of Software System

The system is made up of the following architectural components:

- **Front End Web Server**
- **Backend Database Server**
- **Admin Web Client (HTML)** — The view that an administrator sees when logging into a browser. It does not represent a separate software application from the Member Web Client.
- **Member Web Client (HTML)** — The view that a regular member sees when logging into a browser. It does not represent a separate software application from the Admin Web Client.
- **Guest Web Client (HTML)** — The view that a non-logged-in user sees in a browser. It does not represent a separate software application from the Admin or Member Web Client.

---

### Front End Web Server

The Front End Web Server allows the following:

#### Guest Browsing
- Guests can see things that do not require a login.
- The main User Story: *"I would like to see a listing of all of the available trips."*

#### Authentication
- Allow Member Client users (hiking club members) to authenticate.
- Allow Admin Client users (trip leaders and administrators) to authenticate.

#### Authorization
- Allow logged-in members to register for events.
- Allow logged-in members to edit their own profile only.
- Allow trip leaders and administrators to post new events and perform additional admin functions (CRUD operations) and reporting.
- Allow trip leaders and administrators to see confidential information about members.
- Allow administrators to have access to the treasury portal where money is collected and distributed for paid events.

---

### Backend Database Server

The backend database server must be located in a private network and only the Frontend Web Server should be able to communicate with it. The Backend Database Server should be behind a firewall.

---

### Admin Client

For the purpose of this model, "Admin Client" means a view of the application that is unique for admins. It will have functionality, for example, to edit data for all users. This does not mean that there needs to be a software client installed on the user's device, other than a browser. You could choose to design a "fat client," but it's not required.

There are two types of Admins:

#### 1. Trip Leader
- a. Post new events.
- b. Perform all CRUD operations on events they have posted, but not events created by other trip leaders.
- c. Mark the completion status of registered members for their events: "Completed Event," "Did Not Complete," "No Show."
- d. Select members from the wait list to the event manually (trip leader can pick and choose which members to accept).
- e. Drop registered members from an event.
- f. See information about members not available to anyone except trip leaders (medical information, "private" notes written about members by trip leaders).
- g. Run reports on members (e.g., how many times did a member register for an event and not show up without canceling, how many times does a member register for an event and cancel, etc.).
- h. Set maximum and minimum numbers for their events only.

#### 2. System Admin
- a. Create and disable user accounts.
- b. Create and disable trip leader accounts.
- c. Run sanity checks to ensure that the database has not been tampered with.
- d. Set up a payment portal to receive payments for paid trips.
- e. Has access to the treasury portal for all paid trips and can run reports to examine cash flow for all trips. Can withdraw money to pay for trip expenses.

---

### Member Client

For the purpose of this model, "Member Client" means a view of the application that is unique for members. It will include functionality, for example, to edit the member's own profile, but not the profile of others. This does not mean that there needs to be a software client installed on the user's device, other than a browser. You could choose to design a "fat client," but it's not required.

- Members can view upcoming events sorted by date. When logged in, they can register for events. If an event has openings, they will be automatically added, but the leader has the ability to drop the member from an event if there are concerns that the member might not be able to complete the event.
- Members can edit their own profile but cannot edit the profile of other members.
- Members can see non-confidential information about other members, but only administrators (trip leaders and system administrators) can see confidential information.

---

### Guest Client

For the purpose of this model, "Guest Client" means a view of the application that is unique for users that are not logged into the application. It includes functionality to view a listing of all available trips without the ability to see data that is available only for logged-in users.

---

## Deliverables for Part 2

### Deliverable Part 2A: Diagram

A diagram including the following:

1. Systems and components described above:
   - a. Front End Web Server
   - b. Backend Database Server
   - c. Member Client
   - d. Admin Client
   - e. One or more firewalls
   - f. At least two networks inside of the trusted boundary
   - g. IP addresses for each component (clearly label public and private)

2. Arrows showing how the data flows between each component in the diagram.
3. Trust boundaries depicted as dashed lines.

---

### Deliverable Part 2B: STRIDE Threat Model

Write several paragraphs describing the possible STRIDE threats (5 minimum).

---

### Deliverable Part 2C: OWASP Threat Model

Using the links below for the OWASP Generic Steps for Threat Modeling, complete a Threat Model Description covering the following 4 points:

1. **Assessment Scope** — What's on the line?
2. **Vulnerabilities** — What are they?
3. **Countermeasures** — What can you do about it?
4. **Prioritized Risks** — List them in order.

**OWASP References:**
- [OWASP Threat Modeling Category](https://wiki.owasp.org/index.php/Category:Threat_Modeling)
- [OWASP Application Threat Modeling](https://owasp.org/www-community/Application_Threat_Modeling)

**Submission:** Submit a Word document named in the following format (Mac users should submit a PDF):

```
LastnameFirstname_Assignment2.doc
```

---

## Tips

- Get ideas from the [OWASP Top Ten](https://owasp.org/www-project-top-ten/)

