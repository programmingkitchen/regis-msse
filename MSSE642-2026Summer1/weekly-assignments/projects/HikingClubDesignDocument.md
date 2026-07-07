# Hiking Club — Software Project Description

## Overview

Atlanta, GA is a major metropolitan city characterized by continual business growth and urban sprawl resulting in long commutes for most workers. While Atlanta has tourist attractions, it is not considered to be a "tourist destination." The climate and proximity to many national and state parks as well as the Appalachian Trail foothills, however, make hiking a popular activity for residents of Atlanta and visitors. Atlanta is a place where it's nice to "get out of town to be in nature."

The **Georgia Hiking Club (GHC)** is a non-profit hiking club which allows members to participate in guided trips in Atlanta, the surrounding areas, and locations throughout the country and the world. The all-volunteer club does not have a physical office or salaried positions, though it does have officers who manage the club, including a CTO who manages the web server and web application.

The club has a budget that comes from business sponsorships and an annual membership fee.

The **Hiking Club Web Application** is the core of the business. All business is done through the web app and the club could not exist without it.

---

## Membership and Hikes

The GHC appeals to all ages and fitness levels, so the hikes are diverse. Some hikes appeal to beginner hikers who may or may not be in good physical condition. On the other end of the spectrum, advanced hikes appeal to hikers at the level of elite athlete. Hikes are rated for difficulty so that members can choose hikes that match their level of fitness.

---

## Similarity to Meetup

On the surface, the Hiking Club operates similarly to Meetup. It shares the following characteristics:

- Trip leaders (event organizers in Meetup) post trips that members will sign up to attend. These trips can be local or anywhere in the world.

- There are two kinds of trips:
  - **Free trips** — located in Atlanta and the surrounding areas (less than a 3-hour drive)
  - **Paid excursions** — to locations across the country and around the world

- Any member can sign up for local (free) trips.

- Groups are limited to minimum and maximum numbers.

- There are three categories of users:
  | Role | Permissions |
  |---|---|
  | **Regular Member** | Register for events and update their own profile |
  | **Trip Leader** | Post events and view member details visible only to leaders |
  | **Administrator** | Make changes to all information stored in the system |

---

## Problems Identified in Earlier Iteration

During an earlier iteration of the software, the application design was similar to Meetup, but stakeholders noticed several problems that threatened the organization:

- **No-shows and waiting list lockout** — Due to low-cost participation (most hikes are free for members and led by volunteers), events quickly filled up and had waiting lists. At the same time, members who registered often did not show up, meaning events ran below capacity while members on the waiting list were locked out unnecessarily.

- **Fitness mismatch** — Members signed up for events beyond their physical ability, causing issues that were annoying to the rest of the group and could in some cases be dangerous.

- **Inability to ban members** — Administrators needed the ability to ban members who did not follow the policies of the club.

- **Medical information not visible to leaders** — Leaders had no visibility into existing medical conditions of participants that might require first aid during the hikes.

---

## Authentication

Members, trip leaders, and administrators log in via an authentication page, where they supply a username (email) and password. Complex passwords are not enforced, and the site has been hacked with a brute force attack.

---

## Member Profiles and Event Tracking

The application keeps detailed information about members, in particular the history of events they have attended. For each event, leaders have the ability to mark each participant as:

- **Finish**
- **Did Not Finish**
- **No Show**

In addition, leaders can add notes about participants to assist in the screening process for future events. Leaders now have the ability to **reject event registrations** as appropriate.

The profile for each member includes:

- Existing medical conditions
- Notes about performance (fitness level)

The hiking club ensures that this information is kept **confidential**.

---

## Payment Portal

A payment portal was added to assist in collecting money for membership dues. Members can:

- Pay through the portal
- View their payment history
- See deadlines for payments

Money is also collected on the portal for select paid excursions. Trip leaders can run a report to determine which members did not meet their payment deadlines. This allows trip leaders to:

1. Drop members from the trip
2. Refund the money already paid
3. Move someone from the waiting list to fill the vacancy

---

## Trip Leader Requirements

Leaders must meet the following requirements:

- **First Aid Training** — current certification required
- **Annual Physical** — must be completed yearly

The details of any conditions affecting leaders are also stored in the database.
