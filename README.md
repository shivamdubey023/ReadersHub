# 📚 Readers Hub

A vibrant community platform for book readers to connect, share books, discover recommendations, and grow together in their reading journey.

## 🎯 Overview

Readers Hub is a web-based platform designed to bring book enthusiasts together. Whether you're looking for your next great read, want to share your favorite books, or discuss literature with like-minded readers, Readers Hub is your go-to destination.

## ✨ Features

- **User Profiles**: Create personalized profiles showcasing your reading preferences and book collection
- **Book Sharing**: Share books from your collection with other readers in your community
- **Book Discovery**: Browse and discover new books recommended by community members
- **Book Reviews & Ratings**: Write reviews and rate books to help others make informed decisions
- **Reading Lists**: Create and manage custom reading lists and reading goals
- **Community Discussion**: Engage in discussions about books, authors, and reading topics
- **Book Recommendations**: Get personalized book suggestions based on your reading history
- **Social Features**: Follow other readers and see what they're reading and reviewing

## 🛠️ Technology Stack

- **Backend**: Python (Django/Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: (To be specified)
- **Version Control**: Git & GitHub

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)
- Git

## 🏗️ Architecture & Platform Features

Readers Hub supports advanced features for online web reading, e-commerce, and subscription models. The platform is architected with the following core modules:

### 1. Database & Domain Models
- **Users & Tokens**: Extends standard user profiles with token balances to allow micro-transactions for book access.
- **Subscriptions**: Tiered subscription models (`UserSubscription`) granting access to premium content.
- **Book Catalog**: Robust categorization featuring `Category`, `Genre`, and `Album`. Books include `summary`, `is_premium` flags, and `token_price`.
- **E-Commerce & Access**: `Transaction` models to handle token top-ups and subscriptions, and `UserBookAccess` to permanently unlock specific books.
- **Web Reading Experience**: `ReadingProgress` models strictly tracking current page and last read timestamps to allow seamless resuming.

### 2. Web Application Interface
- **`/explore`**: Central catalog to discover new books, view summaries, and filter by categories.
- **`/book/[id]`**: Detailed view for books, prompting users to either "Read Now", "Buy for X Tokens", or "Subscribe".
- **`/reader/[id]`**: A secure in-browser web reader designed to stream PDF/EPUB pages seamlessly without exposing raw downloadable files.
- **`/library`**: User dashboard housing purchased books, active reading progress, and token wallet.
- **`/pricing`**: Storefront for token bundles and subscription plans.

### 3. Key Workflows
- **Content Authorization**: The backend validates if a user holds an active subscription OR a direct `UserBookAccess` record before unlocking the PDF stream.
- **Secure File Delivery**: PDFs are hosted via secure cloud storage (e.g., AWS S3). The API generates short-lived, pre-signed URLs to protect against unauthorized downloads.

## 💡 Usage

### For Readers

1. **Sign Up**: Create an account on the platform
2. **Build Your Profile**: Add your reading preferences and bio
3. **Explore Books**: Browse the community book collection
4. **Share Books**: Upload and share books from your collection
5. **Write Reviews**: Rate and review books you've read
6. **Follow Users**: Connect with other readers who share your interests
7. **Create Reading Lists**: Organize books into custom lists

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Authors

- **Shivam Dubey** - Initial work and project creation


## 🗺️ Roadmap

- [ ] Mobile app version
- [ ] Advanced recommendation algorithm
- [ ] Book club features
- [ ] Reading challenges and gamification
- [ ] Integration with Goodreads API
- [ ] Social media sharing
- [ ] Advanced search and filtering

---

**Last Updated**: May 2026
