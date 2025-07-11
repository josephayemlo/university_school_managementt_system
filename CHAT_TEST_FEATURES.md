# 📌 feature.md

## 🎯 Goal

Implement a real-time chat system within the school app, enabling:

- Group chat per department and level (created by Admin)
- Private messaging between students of the same department and level

---

## 🧩 Key Features

### 🔷 1. Group Chat (Department + Level Based)

- Admin creates chat rooms manually
- Each room is tied to a specific department and level
- Students can view and join their corresponding room
- Once joined, they can:

  - View message history
  - Send and receive real-time messages

### 🔷 2. Private Chat

- Students can access a list of classmates (same dept + level)
- Option to start a private chat with any classmate
- One-on-one real-time chat
- All private chats are saved and accessible later

### 🔷 3. General Functionality

- Real-time communication using Django Channels + Redis
- Messages stored in the database (for history)
- Message timestamps
- Join confirmation for group rooms
- Prevent unauthorized access to other groups or private threads

---

## 🔒 Access Rules

- Only Admins can create group rooms
- Students can only see/join rooms for their dept + level
- Students can only private chat with others in their dept + level

---

# 🗃️ data_models.md

## 1. ChatRoom

- id (Auto)
- name (Char)
- department (ForeignKey)
- level (Integer)
- created_by (Admin User FK)
- created_at (DateTime)

## 2. ChatRoomMembership

- id (Auto)
- user (Student FK)
- room (ChatRoom FK)
- joined_at (DateTime)

## 3. GroupMessage

- id (Auto)
- room (ChatRoom FK)
- sender (User FK)
- message (Text)
- timestamp (DateTime)

## 4. PrivateMessage

- id (Auto)
- sender (User FK)
- receiver (User FK)
- message (Text)
- timestamp (DateTime)

---

# 👥 user_story.md

## 🧑‍💼 Admin

- As an admin, I want to create chat rooms for specific departments and levels, so students can have structured group discussions.

## 👨‍🎓 Student (Group Chat)

- As a student, I want to be able to join the group chat room for my department and level, so I can connect with my peers.
- As a student, I want to see previous messages in the chat room, so I can catch up with conversations.
- As a student, I want to receive messages in real-time without refreshing, so chatting feels instant.

## 👨‍🎓 Student (Private Chat)

- As a student, I want to see a list of classmates in my department and level, so I know who I can chat with.
- As a student, I want to send a private message to a classmate, so we can have a 1-on-1 conversation.
- As a student, I want my private messages saved, so I can refer back to them later.
