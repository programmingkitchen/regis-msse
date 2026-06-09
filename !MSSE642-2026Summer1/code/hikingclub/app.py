from typing import Any

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

UPCOMING_EVENTS = [
    {
        "id": 1,
        "month": "JUN",
        "day": "04",
        "time": "10:00 AM",
        "title": "HIKE: THURSDAY MORNING SEMI-FITNESS AT VICKERY CREEK",
        "status": "EVENT STARTED",
        "status_class": "status-live",
        "difficulty": "D2",
        "spots": "15 spots filled, 1 waiting",
        "description": (
            "A brisk morning fitness hike with varied terrain and creek views. "
            "Good choice for moderately active hikers."
        ),
        "location": "Vickery Creek - Grooveway Park Entrance",
    },
    {
        "id": 2,
        "month": "JUN",
        "day": "05",
        "time": "12:30 PM",
        "title": "HIKE: YONAH PRESERVE PLUS YONAH MOUNTAIN",
        "status": "GET ON THE WAITING LIST",
        "status_class": "status-wait",
        "difficulty": "D4",
        "spots": "11 spots filled",
        "description": (
            "A challenging mountain route with sustained elevation gain and "
            "great summit views."
        ),
        "location": "Yonah Preserve / Yonah Mountain",
    },
    {
        "id": 3,
        "month": "JUN",
        "day": "06",
        "time": "8:00 AM",
        "title": "HIKE: KMNBP KOLB FARM LOOP",
        "status": "REGISTER NOW",
        "status_class": "status-open",
        "difficulty": "D2",
        "spots": "3 of 15 spots filled",
        "description": (
            "A moderate loop with rolling hills, wooded sections, and a "
            "steady pace for morning hikers."
        ),
        "location": "Kennesaw Mountain National Battlefield Park",
    },
    {
        "id": 4,
        "month": "JUN",
        "day": "06",
        "time": "9:00 AM",
        "title": "VOLUNTEER: NATIONAL TRAILS DAY - GIVING BACK",
        "status": "GET ON THE WAITING LIST",
        "status_class": "status-wait",
        "difficulty": "D3",
        "spots": "12 spots filled",
        "description": (
            "Trail stewardship day focused on cleanup and maintenance with "
            "club volunteers and leaders."
        ),
        "location": "National Trails Day Work Site",
    },
    {
        "id": 5,
        "month": "JUN",
        "day": "07",
        "time": "9:00 AM",
        "title": "WATER: EASY PADDLE AT HOLLIS Q LATHAM RESERVOIR",
        "status": "REGISTER NOW",
        "status_class": "status-open",
        "difficulty": "D3",
        "spots": "2 of 8 spots filled",
        "description": (
            "Relaxed paddle session on calm water with beginner-friendly pace "
            "and gear check at launch."
        ),
        "location": "Hollis Q. Latham Reservoir",
    },
    {
        "id": 6,
        "month": "JUN",
        "day": "08",
        "time": "8:30 AM",
        "title": "HIKE: STONE MOUNTAIN TWICE IN THE MORNING!",
        "status": "REGISTER NOW",
        "status_class": "status-open",
        "difficulty": "D3",
        "spots": "3 of 12 spots filled",
        "description": (
            "Two summit pushes in one session for endurance training and "
            "citywide panoramic views."
        ),
        "location": "Stone Mountain Park",
    },
    {
        "id": 7,
        "month": "JUN",
        "day": "09",
        "time": "6:05 PM",
        "title": "INDOOR CLIMB: INDOOR CLIMBING @ CRA",
        "status": "REGISTER NOW",
        "status_class": "status-open",
        "difficulty": "PAID D4",
        "spots": "1 of 8 spots filled",
        "description": (
            "Evening indoor climbing session with belay support, route practice, "
            "and safety orientation."
        ),
        "location": "CRA Climbing Gym",
    },
    {
        "id": 8,
        "month": "JUN",
        "day": "10",
        "time": "10:00 AM",
        "title": "HIKE: CLOUDLAND CANYON WITH A NEW ROUTE",
        "status": "GET ON THE WAITING LIST",
        "status_class": "status-wait",
        "difficulty": "D5",
        "spots": "12 spots filled, 3 waiting",
        "description": (
            "Advanced canyon hike with steep sections, scenic overlooks, and a "
            "new route variation for experienced hikers."
        ),
        "location": "Cloudland Canyon State Park",
    },
]


def _event_by_id(event_id: int) -> dict[str, str] | None:
    return next((event for event in UPCOMING_EVENTS if event["id"] == event_id), None)


def _chatbot_reply(message: str) -> str:
    text = message.strip().lower()
    if not text:
        return "Please type a message and I can help with hiking club info."

    if any(word in text for word in ["hello", "hi", "hey"]):
        return (
            "Hello! I can help with trips, payments, memberships, "
            "or leader requirements."
        )

    if any(word in text for word in ["trip", "hike", "local", "excursion"]):
        return (
            "You can browse trips at /trips, local hikes at /trips/local, "
            "and paid excursions at /trips/excursions."
        )

    if any(word in text for word in ["pay", "payment", "dues", "refund"]):
        return (
            "Membership dues can be paid at /payments/membership-dues. "
            "Excursion payments use /payments/excursions/<trip_id>."
        )

    if any(word in text for word in ["member", "register", "profile"]):
        return (
            "Member actions include /members, /members/<member_id>/profile, "
            "and trip registration at /trips/<trip_id>/register."
        )

    if any(word in text for word in ["leader", "first aid", "physical"]):
        return (
            "Leader compliance is tracked at "
            "/leaders/<leader_id>/compliance."
        )

    if any(word in text for word in ["security", "password", "login"]):
        return (
            "Security endpoints include /auth/login, /auth/change-password, "
            "and /security/password-policy."
        )

    return (
        "I can answer questions about routes in this demo app. "
        "Try asking about trips, payments, members, leaders, or security."
    )


def _payload() -> dict[str, Any]:
    json_data = request.get_json(silent=True)
    if isinstance(json_data, dict):
        return json_data
    form_data = request.form.to_dict()
    if form_data:
        return form_data
    return request.args.to_dict()


def _render(action: str, details: str = "") -> str:
    data = _payload()
    print(f"{action} | details={details} | payload={data}")
    payload_line = data if data else "No payload sent"
    return (
        f"<h2>{action}</h2>"
        f"<p>{details}</p>"
        f"<pre>{payload_line}</pre>"
    )


@app.get("/")
def index() -> str:
    return render_template("index.html", upcoming_events=UPCOMING_EVENTS)


@app.get("/events/<int:event_id>")
def event_detail(event_id: int) -> str:
    event = _event_by_id(event_id)
    if event is None:
        return "<h2>Event not found</h2>", 404
    return render_template("event_detail.html", event=event)


@app.post("/events/<int:event_id>/signup")
def event_signup(event_id: int) -> Any:
    event = _event_by_id(event_id)
    if event is None:
        return "<h2>Event not found</h2>", 404
    print(f"Event Signup | event_id={event_id} | title={event['title']}")
    return redirect(url_for("event_signup_thanks", event_id=event_id))


@app.get("/events/<int:event_id>/signup/thanks")
def event_signup_thanks(event_id: int) -> str:
    event = _event_by_id(event_id)
    if event is None:
        return "<h2>Event not found</h2>", 404
    return render_template("signup_thanks.html", event=event)


@app.post("/api/chat")
def chat() -> Any:
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", ""))
    reply = _chatbot_reply(message)
    print(f"Chatbot | message={message} | reply={reply}")
    return jsonify({"reply": reply})


@app.get("/hiking")
def hiking() -> str:
    return (
        "Welcome to the Hiking Club! Explore nature with local hikes and "
        "global excursions."
    )


@app.post("/auth/login")
def login() -> str:
    return _render("Login", "Authenticate member, leader, or admin")


@app.post("/auth/logout")
def logout() -> str:
    return _render("Logout", "End current user session")


@app.post("/auth/change-password")
def change_password() -> str:
    return _render("Change Password", "Update user password")


@app.get("/members")
def list_members() -> str:
    return _render("List Members", "Show all members (mock list)")


@app.post("/members")
def create_member() -> str:
    return _render("Create Member", "Register a new hiking club member")


@app.get("/members/<int:member_id>")
def get_member(member_id: int) -> str:
    return _render("Get Member", f"View member {member_id}")


@app.put("/members/<int:member_id>")
def update_member(member_id: int) -> str:
    return _render("Update Member", f"Update member {member_id}")


@app.get("/members/<int:member_id>/profile")
def get_member_profile(member_id: int) -> str:
    return _render("Get Member Profile", f"Load profile for member {member_id}")


@app.put("/members/<int:member_id>/profile")
def update_member_profile(member_id: int) -> str:
    return _render(
        "Update Member Profile",
        f"Update profile fields for member {member_id}",
    )


@app.get("/members/<int:member_id>/medical")
def get_member_medical(member_id: int) -> str:
    return _render(
        "Get Member Medical",
        f"View confidential medical details for member {member_id}",
    )


@app.put("/members/<int:member_id>/medical")
def update_member_medical(member_id: int) -> str:
    return _render(
        "Update Member Medical",
        f"Update confidential medical details for member {member_id}",
    )


@app.get("/members/<int:member_id>/performance-notes")
def get_performance_notes(member_id: int) -> str:
    return _render(
        "Get Performance Notes",
        f"View fitness and performance notes for member {member_id}",
    )


@app.post("/members/<int:member_id>/performance-notes")
def add_performance_note(member_id: int) -> str:
    return _render(
        "Add Performance Note",
        f"Add fitness note for member {member_id}",
    )


@app.post("/admin/members/<int:member_id>/ban")
def ban_member(member_id: int) -> str:
    return _render("Ban Member", f"Ban member {member_id} for policy violation")


@app.post("/admin/members/<int:member_id>/unban")
def unban_member(member_id: int) -> str:
    return _render("Unban Member", f"Restore access for member {member_id}")


@app.get("/trips")
def list_trips() -> str:
    return _render("List Trips", "Show all local and paid excursion trips")


@app.post("/trips")
def create_trip() -> str:
    return _render("Create Trip", "Trip leader posts a new trip")


@app.get("/trips/local")
def list_local_trips() -> str:
    return _render("Local Trips", "Show free trips within a 3-hour drive")


@app.get("/trips/excursions")
def list_excursions() -> str:
    return _render("Paid Excursions", "Show paid trips across US and world")


@app.get("/trips/<int:trip_id>")
def get_trip(trip_id: int) -> str:
    return _render("Get Trip", f"View trip {trip_id} details and capacity")


@app.post("/trips/<int:trip_id>/register")
def register_trip(trip_id: int) -> str:
    return _render(
        "Register for Trip",
        f"Register member for trip {trip_id}; apply screening rules",
    )


@app.post("/trips/<int:trip_id>/cancel-registration")
def cancel_registration(trip_id: int) -> str:
    return _render(
        "Cancel Registration",
        f"Cancel member registration for trip {trip_id}",
    )


@app.post("/trips/<int:trip_id>/registrations/<int:member_id>/approve")
def approve_registration(trip_id: int, member_id: int) -> str:
    return _render(
        "Approve Registration",
        f"Leader approved member {member_id} for trip {trip_id}",
    )


@app.post("/trips/<int:trip_id>/registrations/<int:member_id>/reject")
def reject_registration(trip_id: int, member_id: int) -> str:
    return _render(
        "Reject Registration",
        f"Leader rejected member {member_id} for trip {trip_id}",
    )


@app.get("/trips/<int:trip_id>/waitlist")
def view_waitlist(trip_id: int) -> str:
    return _render("View Waitlist", f"Show waitlist for trip {trip_id}")


@app.post("/trips/<int:trip_id>/waitlist/promote")
def promote_waitlist(trip_id: int) -> str:
    return _render(
        "Promote Waitlist Member",
        f"Move next waitlisted member into trip {trip_id}",
    )


@app.post("/trips/<int:trip_id>/attendance/<int:member_id>")
def mark_attendance(trip_id: int, member_id: int) -> str:
    return _render(
        "Mark Attendance",
        (
            f"Set status for member {member_id} on trip {trip_id}: "
            "Finish, Did not Finish, or No Show"
        ),
    )


@app.get("/payments/membership-dues")
def membership_dues_info() -> str:
    return _render("Membership Dues", "Show dues amount and deadline details")


@app.post("/payments/membership-dues")
def pay_membership_dues() -> str:
    return _render("Pay Membership Dues", "Submit membership dues payment")


@app.get("/payments/excursions/<int:trip_id>")
def excursion_payment_info(trip_id: int) -> str:
    return _render(
        "Excursion Payment Info",
        f"Show payment requirements for trip {trip_id}",
    )


@app.post("/payments/excursions/<int:trip_id>")
def pay_excursion(trip_id: int) -> str:
    return _render("Pay Excursion Fee", f"Submit payment for trip {trip_id}")


@app.get("/payments/history/<int:member_id>")
def payment_history(member_id: int) -> str:
    return _render("Payment History", f"Show payment history for member {member_id}")


@app.get("/reports/unpaid-members/<int:trip_id>")
def unpaid_members_report(trip_id: int) -> str:
    return _render(
        "Unpaid Members Report",
        f"Report members who missed payment deadline for trip {trip_id}",
    )


@app.post("/trips/<int:trip_id>/drop-unpaid/<int:member_id>")
def drop_unpaid_member(trip_id: int, member_id: int) -> str:
    return _render(
        "Drop Unpaid Member",
        f"Drop unpaid member {member_id} from trip {trip_id}",
    )


@app.post("/trips/<int:trip_id>/refund/<int:member_id>")
def refund_member(trip_id: int, member_id: int) -> str:
    return _render(
        "Refund Member",
        f"Issue refund to member {member_id} for trip {trip_id}",
    )


@app.get("/leaders")
def list_leaders() -> str:
    return _render("List Leaders", "Show all trip leaders")


@app.post("/leaders")
def create_leader() -> str:
    return _render("Create Leader", "Create trip leader profile")


@app.get("/leaders/<int:leader_id>/compliance")
def get_leader_compliance(leader_id: int) -> str:
    return _render(
        "Leader Compliance",
        f"View first aid and annual physical status for leader {leader_id}",
    )


@app.put("/leaders/<int:leader_id>/compliance")
def update_leader_compliance(leader_id: int) -> str:
    return _render(
        "Update Leader Compliance",
        f"Update compliance records for leader {leader_id}",
    )


@app.get("/security/password-policy")
def get_password_policy() -> str:
    return _render("Password Policy", "View current password policy settings")


@app.put("/security/password-policy")
def update_password_policy() -> str:
    return _render(
        "Update Password Policy",
        "Set stronger password policy to reduce brute-force risk",
    )


if __name__ == "__main__":
    app.run(debug=True)
