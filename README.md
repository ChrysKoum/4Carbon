# 4Carbon

4Carbon is a project developed for the **Cassini 7th Hackathon**, focused on providing booking for ship managers, management of local goverment, monitoring of carbon emissions. This frontend application uses **Vite**, **React**, and **Tailwind CSS** to create a modern, responsive user interface. Future features will include dashboards, landing pages, and additional functionality.

<p align="center">
  <img src="https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white" alt="vite.js">
  <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB" alt="react">
  <img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="tailwindcss">
</p>

## Table of Contents

- [🛠️ Installation](#%EF%B8%8F-installation)
  - [Step 1: Clone the GitHub repository](#step-1-clone-the-github-repository)
  - [Step 2: Install dependencies](#step-2-install-dependencies)
- [💻 Usage](#-usage)
- [🔩 List of Dependencies](#-list-of-dependencies)

## 🛠️ Installation

### Step 1: Clone the GitHub repository

- Open your terminal and clone the repository:
   ```shell
   git clone https://github.com/YourUsername/4Carbon.git
   ```

### Step 2: Install dependencies

- Navigate to the **root directory** of the project:
   ```shell
   cd 4Carbon
   ```

- Install project dependencies with npm:
   ```shell
   npm install
   ```

### Step 3: Set up Tailwind CSS

- Tailwind CSS is already configured in the project. Ensure you have the correct configurations in `tailwind.config.js` and `src/index.css`:

  - `tailwind.config.js`:
    ```js
    /** @type {import('tailwindcss').Config} */
    export default {
      content: [
        './index.html',
        './src/**/*.{js,ts,jsx,tsx}'
      ],
      theme: {
        extend: {},
      },
      plugins: [],
    }
    ```

  - `src/index.css`:
    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

## 💻 Usage

### Start the development server:

- From the root of the project, run the following command to start the Vite development server:
```shell
npm run dev
```

## 🔩 List of Dependencies

### Development Dependencies:

- **vite**: A fast development tool for modern web applications.
- **tailwindcss**: A utility-first CSS framework for fast UI development.
- **prettier**: A code formatter for maintaining consistent code style.

### Frontend Dependencies:

- **react** and **react-dom**: Core libraries for building user interfaces with React.
- **react-router-dom**: A library for handling routing and navigation in React applications.
