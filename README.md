# Client-Server Programming Tasks (Python Socket Programming)

This project contains solutions for four basic client-server programming tasks using Python socket programming.

---

## Requirements

- Python 3.x
- Basic understanding of sockets
- Two terminals / command prompts (one for server, one for client)

---

## Task 1: Client Sends IP Address and Device Name

### Problem Statement

Create a basic client-server program where the client informs the server of the client’s IP address and device name whenever a client is connected, and the server prints that information.

---

## Task 2: Vowel Counter Client-Server Program

Create a basic client-server program where the server receives a message from the client and counts how many vowels are there in the message.

Conditions:
- If there are no vowels: Not enough vowels
- If there are at most two vowels: Enough vowels I guess
- If there are more than two vowels: Too many vowels

---

## Task 3: Multi-threaded Vowel Counter Server

Create a basic multi-threaded client-server program where the server receives a message from the client and counts vowels.

Same conditions as Task 2.  
The server must handle multiple clients simultaneously using threads.

---

## Task 4: Salary Calculation Client-Server Program

Create a basic client-server program where the server takes the number of hours a person worked from the client and calculates salary.

Salary Rules:
- If hours worked is less than or equal to 40: Tk 200 per hour
- If hours worked is greater than 40: Tk 8000 plus Tk 300 for each hour worked over 40 hours


---

## How to Run

Start server:
python server.py

Start client:
python client.py
