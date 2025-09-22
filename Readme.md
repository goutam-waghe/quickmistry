.

🛠 Service Booking Platform (Django Project Documentation)
📌 1. Project Overview

A web platform where:

Customers can book workers (Plumber, Electrician, AC repair, etc.).

Workers accept/reject job requests, complete them, and get paid.

Admin manages users, jobs, and payments.

Supports live chat and notifications for real-time updates.

📌 2. User Roles

Customer

Register/login.

Search workers by city, skill, rate, availability.

Book workers for jobs.

Chat with worker after booking.

Make payments (simulated or integrated later).

Give ratings & reviews.

See booking history.

Worker

Register/login.

Create profile with skills, category, city, hourly rate, availability.

Manage job requests (accept/reject).

Chat with customer.

Mark job as completed.

Track earnings & reviews.

Admin

Approve/reject worker registrations (optional).

Manage all users, jobs, payments.

View analytics (most booked workers, revenue reports).

📌 3. App Flow

User registers → chooses role (Customer/Worker).

Customer searches workers → selects → books.

Worker gets job request → accepts → job moves to “Ongoing”.

Chat room opens between customer & worker.

Worker completes job → Customer confirms → Payment processed.

Customer leaves review → Worker profile updates.

Notifications are sent for each action.

📌 4. Core Features
🔑 Authentication

Custom User model with role (customer, worker).

Use AbstractUser in Django.

Role-based redirects after login.

👤 User Profiles

Worker Profile: skills, category, hourly_rate, experience, availability, city.

Customer Profile: address, phone.

🔍 Worker Search

Filters: category, city, rate, availability.

Sort by rating, experience, price.

📅 Booking System

Customer books worker → Job created with status pending.

Worker accepts → Job status = accepted.

Worker completes → Job status = completed.

Customer confirms → Job status = finished + payment.

💸 Payments

Phase 1: Mark as “Paid” manually.

Phase 2: Integrate Razorpay/Stripe.

⭐ Ratings & Reviews

Customers leave ratings after job completion.

Average rating displayed on worker profile.

💬 Live Chat

Implemented using Django Channels (WebSockets).

Chat Room created when job is accepted.

Messages stored in ChatMessage.

🔔 Notifications

In-app notifications for:

New booking requests.

Job accepted/rejected.

Job completed.

Built with signals + WebSockets.

📌 5. Database Models (ERD Style)
User (Custom)

username, email, password

role (customer/worker/admin)

name, phone, profile_image

WorkerProfile

user (OneToOne with User)

service_category

skills

hourly_rate

experience

availability (bool)

city

CustomerProfile

user (OneToOne with User)

address

phone

Job

customer (FK → User)

worker (FK → User)

service_category

description

scheduled_time

status (pending, accepted, ongoing, completed, finished)

price

created_at

Review

job (FK → Job)

customer (FK → User)

worker (FK → User)

rating (1–5)

comment

created_at

ChatRoom

job (OneToOne → Job)

ChatMessage

room (FK → ChatRoom)

sender (FK → User)

message

timestamp

Notification

user (FK → User)

message

link (to redirect to job/chat/etc.)

is_read (bool)

created_at

📌 6. Views (Main Functions)

Auth Views

Register (choose role).

Login.

Logout.

Customer Views

Dashboard → upcoming bookings, history.

Search workers.

Book worker.

Chat with worker.

Notifications.

Worker Views

Dashboard → job requests, ongoing jobs.

Manage availability.

Accept/Reject jobs.

Chat with customer.

Notifications.

Admin Views

User management.

Job management.

Reports.