# Public Accounts Subscription System and Event Listing
> ⚠️ This is a Proof of Concept (POC) and is currently a Work In Progress (WIP). Not all features are complete.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Project Description](#project-description)
    - [Status](#status)
    - [Architechture](#architechture)
- [Frontend WebApp](#frontend-webapp)
- [Backend](#backend)

## Project Description
In this Proof of Concept (POC), I'm exploring how to feed an AI system with real-time data based on user feedback. The UI allows users to search for and like public Instagram accounts, which are then monitored for event-related content.

This POC also aims to integrate several components into a single solution, including a scraping tool, scheduled background jobs, a centralized PostgreSQL database, and a dockerized LLM for content analysis and summarization.

I will be sharing all technicals details during the building.

### Status
![status](https://img.shields.io/badge/status-work%20in%20progress-yellow)

### Architechture
Diagram

## Frontend WebApp
### Public Section (/)
- Landing page explaining:
  - What the app does.
  - How accounts are selected.
- Privacy: “We do not access your Instagram account.”
- Button for Google login.

### 🔐 Private Section (/dashboard)
- Public account search → add to favorites
- User's list of favorite accounts.
- Show detected events:
  - Feed sorted by upcoming date.
  - Display: estimated title, date, link to post, originating account.

## 🔧 Backend
### ✅ Authentication
- Google login (OAuth).
- Save in database: user_id, email, name, picture.

### Searches
- Google Programmable Search Engine together with Custom JSON API to fetch results. It is configured exclusively for instagram.com and various filters are applied to avoid retrieving posts and reels.

### ✅ Scraper (runs once per day, as a cron job)

### 🧠 Event Processing (NLP)
#### 🔍 What to look for in captions:
- Future dates: “July 15th”, “this Saturday”, “Friday the 12th”, etc.
- Keywords: “show”, “event”, “tickets”, “we're playing at”, “talk”, etc.
