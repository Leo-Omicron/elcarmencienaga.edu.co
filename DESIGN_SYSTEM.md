# Design System - Institución Educativa El Carmen de Ciénaga

This document defines the official UI components and styles for the web properties of the institution.

## 1. Colors
*   **Deep Blue (Primary):** `#191253`
*   **Green (Secondary):** `#10b981` (Accent: `#43a447`)
*   **Gold (Highlight):** `#f59e0b` (Accent: `#ffe500`)
*   **Text (Dark):** `#333333`
*   **Background (Light):** `#f9fafb`
*   **White:** `#ffffff`

**Rule:** Do not use inline purple styles under any circumstances.

## 2. Components

### 2.1 Official Header (`.official-header`)
*   **Background:** Deep Blue (`#191253`)
*   **Content:** Must include the institution's shield on the left and the name "I.E. El Carmen de Ciénaga" on the right (or next to it).
*   **Navigation:** Links should be white and hover to Gold (`#ffe500`).

### 2.2 News Section (`.news-section`)
*   **Background:** Light gray/white.
*   **Title:** Deep Blue, centered.
*   **Cards (`.news-card`):** White background, subtle shadow, rounded corners. Include an image, title, excerpt, and a "Read More" button in Green.

### 2.3 YouTube Video Player (`.video-container`)
*   **Responsive Wrapper:** A wrapper to make the `iframe` responsive (16:9 aspect ratio).
*   **Container:** Should have a subtle border or shadow reflecting institutional colors.
