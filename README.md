# E-Commerce Web System

A fully functional basic e-commerce website allowing users to browse products, manage a cart, and simulate checkout. This project includes an admin panel for product and order management.

## 🚀 Tech Stack

- **Frontend:** React (TypeScript) with Vite
- **Backend:** Node.js with Express
- **Database:** MongoDB
- **Package Manager:** pnpm
- **Styling:** Vanilla CSS

## 📁 Project Structure

- `/client`: Frontend React application.
- `/server`: Backend Express API.
- `GEMINI.md`: Project specification and foundational mandates (**Source of Truth**).
- `DEVELOPMENT_PLAN.md`: Detailed 6-phase implementation roadmap.
- `AGENTS.md`: Entry point instructions for AI agents.

## 🛠️ Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (LTS recommended)
- [pnpm](https://pnpm.io/)
- [MongoDB](https://www.mongodb.com/) (Local or Atlas)

### Installation

1. Clone the repository.
2. Install dependencies for both client and server:

```bash
# Install server dependencies
cd server
pnpm install

# Install client dependencies
cd ../client
pnpm install
```

### Running the Application

**Start the Backend:**
```bash
cd server
pnpm run dev
```

**Start the Frontend:**
```bash
cd client
pnpm run dev
```

## 📝 Documentation

For detailed architectural rules, database schemas, and the development roadmap, please refer to:
- [GEMINI.md](./GEMINI.md)
- [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md)

---
*Created as a final project for Basic Web Systems.*
