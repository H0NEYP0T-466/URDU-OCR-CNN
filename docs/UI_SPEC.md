# UI Specification Document
# URDU-OCR-CNN Project

**Version:** 1.0  
**Last Updated:** December 2025  
**Project:** Urdu Handwritten Character Recognition System

---

## Table of Contents

1. [Overview](#1-overview)
2. [Layout and Structure](#2-layout-and-structure)
3. [Design System](#3-design-system)
4. [Button and Control Behavior](#4-button-and-control-behavior)
5. [Input Validation and Feedback](#5-input-validation-and-feedback)
6. [Responsive Design Rules](#6-responsive-design-rules)
7. [Canvas Drawing UI](#7-canvas-drawing-ui)
8. [Prediction Display](#8-prediction-display)
9. [Accessibility Considerations](#9-accessibility-considerations)
10. [Developer Integration Notes](#10-developer-integration-notes)
11. [Component Diagrams](#11-component-diagrams)

---

## 1. Overview

### 1.1 Purpose

The URDU-OCR-CNN web application provides an intuitive, modern interface for recognizing handwritten Urdu characters and digits using deep learning technology. The UI supports both image upload and canvas drawing input methods, with real-time predictions displayed alongside confidence scores.

### 1.2 Target Users

- **Primary Users:** Urdu speakers and learners who need character recognition
- **Secondary Users:** Researchers and developers working with Urdu OCR
- **Accessibility:** Users with varying levels of technical expertise and physical abilities

### 1.3 Key Features

- Dual input modes: Image upload and canvas drawing
- Model type selection: Character (36 classes) or Digit (10 classes)
- Real-time prediction with confidence scores
- Top-5 prediction results display
- Responsive design for desktop, tablet, and mobile
- Right-to-left (RTL) support for Urdu text
- Dark theme optimized for extended use


---

## 2. Layout and Structure

### 2.1 Page Hierarchy

```
App
├── Header
├── HomePage
│   ├── Hero Section
│   ├── Model Type Selector
│   ├── Input Mode Selector
│   ├── Main Content Area
│   │   ├── Input Section (ImageUploader OR DrawingCanvas)
│   │   └── Prediction Result Section
│   ├── Feature Cards
│   └── Supported Characters Section
└── Footer
```

### 2.2 Header Component

**Location:** Top of all pages  
**Height:** ~70px (desktop), ~140px (mobile - stacked layout)

**Elements:**
- **Logo Icon:** 40x40px gradient box with Urdu "ا" character
- **Title:** "Urdu OCR" with gradient text effect
- **Subtitle:** "Handwritten Character Recognition"
- **Navigation Links:**
  - "Supported Characters" (smooth scroll)
  - "About" (smooth scroll to footer)

**Layout:**
- Desktop: Horizontal flex with space-between
- Mobile: Vertical flex, center-aligned

**Styling:**
- Background: Linear gradient from `#1a1a1a` to `#0a0a0a`
- Border bottom: 1px solid `#262626`
- Box shadow: `0 4px 6px -1px rgba(0, 0, 0, 0.5)`

### 2.3 Home Page Components

#### 2.3.1 Hero Section

**Purpose:** Introduction and context  
**Alignment:** Center

**Elements:**
- **Title:** Dynamic based on selected model type
  - "Urdu Character Recognition" OR "Urdu Digit Recognition"
  - Font size: 2.25rem (36px), Bold
  - Color: `#f9fafb`
- **Description Text:**
  - Font size: 1.125rem (18px)
  - Color: `#9ca3af` (gray)
  - Max width: 672px, center-aligned

#### 2.3.2 Model Type Selector

**Purpose:** Switch between character and digit recognition models  
**Alignment:** Center

**Elements:**
- Label: "Select Model:" (gray, 0.875rem)
- Two toggle buttons in a container:
  - "Character Recognition"
  - "Digit Recognition"

**Behavior:**
- Active button: Yellow background (`#FFC107`), black text
- Inactive button: Transparent, gray text
- Smooth transition on selection
- Resets prediction state when changed

#### 2.3.3 Input Mode Selector

**Purpose:** Toggle between upload and draw modes  
**Alignment:** Center

**Elements:**
- Two toggle buttons:
  - "Upload Image"
  - "Draw Character" OR "Draw Digit" (dynamic text)

**Styling:**
- Container: Dark gray background (`#1a1a1a`), 1px border
- Active button: Dark background, yellow text
- Inactive button: Transparent, gray text

#### 2.3.4 Main Content Area

**Layout:** Two-column grid on desktop, single column on mobile/tablet  
**Grid Columns:** 
- Desktop (≥1024px): 2 equal columns (1fr 1fr)
- Mobile/Tablet (<1024px): 1 column

**Left/Top Panel: Input Section**
- Background card: `#1a1a1a`
- Border: 1px solid `#262626`
- Border radius: 12px
- Padding: 24px
- Box shadow: `0 10px 15px -3px rgba(0, 0, 0, 0.5)`

**Right/Bottom Panel: Prediction Result**
- Same card styling as input section
- Displays prediction output

#### 2.3.5 Image Upload Module

**Component:** `ImageUploader`

**Drop Zone Dimensions:**
- Width: 100% of container
- Min height: 300px
- Border: 2px dashed `#404040`
- Border radius: 8px

**States:**
1. **Empty State:**
   - Upload cloud icon (SVG)
   - Text: "Drag & drop an image here"
   - Subtext: "or click to select a file"
   - Format info: "PNG, JPG, JPEG, BMP (max 5MB)"

2. **Hover/Active State:**
   - Border color: Yellow (`#FFC107`)
   - Background: Slight tint (`#1e293b`)

3. **Preview State:**
   - Image preview (max width: 100%)
   - Filename display
   - File size display
   - Two action buttons: "Clear" and "Predict Character"

#### 2.3.6 Drawing Canvas Module

**Component:** `DrawingCanvas`

**Canvas Dimensions:**
- Size: 400x400px (fixed)
- Background: White (`#FFFFFF`)
- Border: 2px solid `#404040`
- Border radius: 8px
- Cursor: Crosshair

**Controls:**
- **Brush Size Slider:**
  - Range: 5px to 30px
  - Default: 15px
  - Display: Current size in pixels
  
- **Action Buttons:**
  - "Clear" button (secondary style)
  - "Predict Character/Digit" button (primary style)

**Drawing Style:**
- Stroke color: Black (`#000000`)
- Line cap: Round
- Line join: Round
- Line width: Based on brush size

**Overlay:**
- Instruction text when canvas is empty
- "Draw an Urdu character here" OR "Draw an Urdu digit here (۰-۹)"

#### 2.3.7 Prediction Panel

**Component:** `PredictionResult`

**States:**

1. **Loading State:**
   - Spinning loader animation
   - Text: "Analyzing character..."

2. **Error State:**
   - Error icon (SVG, red)
   - Error title: "Error"
   - Error message (dynamic)
   - "Try Again" button

3. **Empty/Placeholder State:**
   - Lightbulb icon (SVG, gray)
   - Text: "Upload or draw a character to see prediction"

4. **Result State:**
   - **Main Prediction Card:**
     - Label: "Predicted Character"
     - Large Urdu character display (4-6rem font size)
     - Urdu font: 'Noto Nastaliq Urdu', serif
     - RTL direction
   
   - **Confidence Meter:**
     - Header: "Confidence" label with percentage
     - Progress bar with fill animation
     - Color gradient: Yellow (`#FFC107` to `#FFB300`)
   
   - **Processing Time:**
     - Small text: "Processing time: X.XXms"
   
   - **Top 5 Predictions List:**
     - Title: "Top 5 Predictions"
     - Each item shows:
       - Rank number (1-5)
       - Urdu character (RTL)
       - Horizontal bar chart
       - Probability percentage
   
   - **Action Button:**
     - "Try Another Image" (secondary button)

#### 2.3.8 Feature Cards Section

**Layout:** 3-column grid on desktop, 1-column on mobile  
**Gap:** 24px

**Each Feature Card Contains:**
- Icon in colored circle (48x48px)
  - Colors: Blue/Yellow, Green, Purple
- Feature title
- Feature description text

**Cards:**
1. **AI-Powered:**
   - Icon: Lightbulb
   - Color: Yellow/Blue theme
   - Text: Deep learning CNN for accurate recognition

2. **Fast & Accurate:**
   - Icon: Lightning bolt
   - Color: Green theme
   - Text: Predictions in milliseconds

3. **Comprehensive Support:**
   - Icon: Sliders
   - Color: Purple theme
   - Text: All Urdu alphabets and digits

#### 2.3.9 Supported Characters Section

**ID:** `supported-characters` (for smooth scroll)

**Layout:**
- Two subsections: Alphabets and Digits
- Grid of character cards

**Character Cards:**
- Grid: Auto-fill, min 120px columns
- Background: `#1a1a1a`
- Border: 1px solid `#262626`
- Border radius: 8px
- Padding: 16px
- Hover effect: Yellow border, slight lift

**Card Content:**
- Large Urdu character (2rem, yellow color)
- Character name in English (0.75rem, gray)

### 2.4 Footer Component

**Location:** Bottom of page  
**Background:** Dark gradient

**Layout:** 3-column grid on desktop, 1-column on mobile

**Sections:**
1. **About:**
   - Title: "Urdu OCR"
   - Brief description

2. **Quick Links:**
   - GitHub Repository link

3. **Technology:**
   - Tech stack badges: React, FastAPI, TensorFlow, TypeScript

**Copyright:**
- Bottom bar
- Text: "© 2025 Urdu OCR. Built with ❤️ for the Urdu language."

### 2.5 Loading Spinner Component

**Component:** `LoadingSpinner`

**Design:**
- Circular spinner
- Size: 48x48px (default)
- Border: 4px
- Border color: `#262626`
- Border top color: `#FFC107` (yellow)
- Animation: Continuous rotation (1s linear)

**Optional Message:**
- Displayed below spinner
- Font size: 0.875rem
- Color: `#9ca3af`


---

## 3. Design System

### 3.1 Color Palette

#### Primary Colors

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| Primary Yellow | `#FFC107` | rgb(255, 193, 7) | Primary actions, highlights, active states |
| Primary Yellow Dark | `#FFB300` | rgb(255, 179, 0) | Hover states, gradients |
| Black | `#111111` | rgb(17, 17, 17) | Text on yellow buttons, high contrast |
| White | `#FFFFFF` | rgb(255, 255, 255) | Canvas background, icons |

#### Background Colors

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Background Primary | `#111111` | Main page background |
| Background Secondary | `#1a1a1a` | Cards, containers |
| Background Tertiary | `#0a0a0a` | Gradients, darker sections |

#### Border and Divider Colors

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Border Light | `#262626` | Card borders, dividers |
| Border Medium | `#404040` | Input borders, hover states |
| Border Dark | `#525252` | Focus states, emphasis |

#### Text Colors

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Text Primary | `#f9fafb` | Headings, important text |
| Text Secondary | `#e5e7eb` | Body text, general content |
| Text Tertiary | `#9ca3af` | Subtitles, descriptions, placeholders |

#### Semantic Colors

| Purpose | Color | Hex Code | Usage |
|---------|-------|----------|-------|
| Success | Green | `#34d399` | Success messages, positive indicators |
| Success Dark | Dark Green | `#10b981` | Gradients, hover states |
| Warning | Yellow | `#fbbf24` | Warning badges, alerts |
| Error | Red | `#f87171` | Error messages, validation errors |
| Info | Purple | `#a855f7` | Information badges, accents |

### 3.2 Typography

#### Font Families

1. **Primary Font (English/Interface):**
   - Font: `'Inter'`
   - Fallbacks: `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
   - Source: Google Fonts
   - Weights: 300, 400, 500, 600, 700

2. **Urdu Font:**
   - Font: `'Noto Nastaliq Urdu'`
   - Fallback: `serif`
   - Source: Google Fonts
   - Weights: 400, 700
   - Special properties: `direction: rtl; text-align: right;`

#### Type Scale

| Element | Font Size | Font Weight | Line Height | Color |
|---------|-----------|-------------|-------------|-------|
| Hero Title (H1) | 2.25rem (36px) | 700 | 1.2 | `#f9fafb` |
| Section Title (H2) | 1.25rem (20px) | 600 | 1.3 | `#f9fafb` |
| Subsection Title (H3) | 1.125rem (18px) | 600 | 1.4 | `#f9fafb` |
| Feature Title | 1rem (16px) | 600 | 1.5 | `#f9fafb` |
| Body Large | 1.125rem (18px) | 400 | 1.6 | `#9ca3af` |
| Body Regular | 1rem (16px) | 400 | 1.6 | `#e5e7eb` |
| Body Small | 0.875rem (14px) | 400 | 1.5 | `#9ca3af` |
| Caption | 0.75rem (12px) | 400 | 1.4 | `#9ca3af` |
| Urdu Character (Display) | 4-6rem (64-96px) | 600 | 1 | `#FFC107` |
| Urdu Character (Card) | 2rem (32px) | 600 | 1.2 | `#FFC107` |
| Button Text | 0.875-1rem | 500 | 1 | Varies |

#### Text Styles

- **RTL Support:** All Urdu text uses `direction: rtl` and `text-align: right`
- **Letter Spacing:** Default (0) for all text
- **Text Transform:** None (preserve case)

### 3.3 Spacing System

**Base Unit:** 0.25rem (4px)

| Size Name | Value (rem) | Value (px) | Usage |
|-----------|-------------|------------|-------|
| xs | 0.25rem | 4px | Tiny gaps |
| sm | 0.5rem | 8px | Small spacing |
| md | 0.75rem | 12px | Medium spacing |
| lg | 1rem | 16px | Default spacing |
| xl | 1.5rem | 24px | Section spacing |
| 2xl | 2rem | 32px | Large section spacing |
| 3xl | 2.5rem | 40px | Extra large spacing |
| 4xl | 4rem | 64px | Hero spacing |

### 3.4 Border Radius

| Size | Value | Usage |
|------|-------|-------|
| Small | 0.25rem (4px) | Small elements, badges |
| Medium | 0.5rem (8px) | Buttons, inputs, canvas |
| Large | 0.75rem (12px) | Cards, major containers |
| Full | 9999px | Pills, circular elements |

### 3.5 Shadows

| Name | Value | Usage |
|------|-------|-------|
| Small | `0 1px 3px rgba(0, 0, 0, 0.5)` | Subtle elevation |
| Medium | `0 4px 6px -1px rgba(0, 0, 0, 0.5)` | Cards, buttons |
| Large | `0 10px 15px -3px rgba(0, 0, 0, 0.5)` | Main cards, emphasis |
| Extra Large | `0 20px 25px -5px rgba(0, 0, 0, 0.7)` | Hover states |
| Colored | `0 0 0 3px rgba(255, 193, 7, 0.5)` | Focus rings |

### 3.6 Animations and Transitions

#### Standard Transitions

```css
transition: all 0.2s ease;  /* Default for most interactions */
transition: all 0.3s ease;  /* For smoother, more noticeable changes */
```

#### Key Animations

1. **Spin (Loading):**
   - Duration: 1s
   - Timing: linear
   - Iteration: infinite
   - Transform: `rotate(0deg)` to `rotate(360deg)`

2. **Fade In:**
   - Duration: 0.3s
   - Timing: ease-in
   - Opacity: 0 to 1

3. **Slide Up:**
   - Duration: 0.3s
   - Timing: ease-out
   - Transform: `translateY(20px)` to `translateY(0)`
   - Opacity: 0 to 1

4. **Scale In:**
   - Duration: 0.2s
   - Timing: ease-out
   - Transform: `scale(0.95)` to `scale(1)`
   - Opacity: 0 to 1

5. **Pulse (Skeleton Loading):**
   - Duration: 2s
   - Timing: cubic-bezier(0.4, 0, 0.6, 1)
   - Iteration: infinite
   - Opacity: 1 to 0.5 to 1

#### Interaction Effects

- **Button Press:** `transform: scale(0.95)` (active state)
- **Card Hover:** `transform: scale(1.05)` or `translateY(-2px)`
- **Progress Bar Fill:** Width transition over 0.5s

### 3.7 Iconography

**Icon Library:** SVG icons (inline)  
**Source:** Custom SVG paths, Heroicons style  
**Default Size:** 24x24px (1.5rem)  
**Stroke Width:** 2px  
**Color:** Inherits from parent or explicit color

**Common Icons:**
- Upload cloud (upload section)
- Lightbulb (features, placeholder)
- Lightning bolt (features)
- Sliders (features)
- Error circle (error states)
- Checkmark (success)


---

## 4. Button and Control Behavior

### 4.1 Button Types and Styles

#### 4.1.1 Primary Button

**Visual:**
- Background: `#FFC107` (yellow)
- Text: `#111111` (black)
- Padding: 10px 24px
- Border radius: 8px
- Font weight: 500
- No border

**States:**
- **Default:** Yellow background
- **Hover:** Background `#FFB300`, cursor pointer
- **Focus:** Box shadow `0 0 0 3px rgba(255, 193, 7, 0.5)`
- **Active (pressed):** `transform: scale(0.95)`
- **Disabled:** Opacity 0.5, cursor not-allowed, no hover effect

**Usage:** Primary actions like "Predict Character", "Submit"

#### 4.1.2 Secondary Button

**Visual:**
- Background: `#262626` (dark gray)
- Text: `#e5e7eb` (light gray)
- Padding: 10px 24px
- Border: 1px solid `#404040`
- Border radius: 8px
- Font weight: 500

**States:**
- **Default:** Dark background
- **Hover:** Background `#404040`, border `#525252`
- **Focus:** Box shadow `0 0 0 3px rgba(64, 64, 64, 0.5)`
- **Active:** `transform: scale(0.95)`
- **Disabled:** Opacity 0.5, cursor not-allowed

**Usage:** Secondary actions like "Clear", "Try Another Image"

#### 4.1.3 Toggle Button (Mode/Model Selectors)

**Visual:**
- Container: Dark background with border
- Individual buttons: Transparent background, gray text (inactive)
- Active button: Highlighted (yellow or dark with yellow text)
- Padding: 8px 20px
- Border radius: 8px

**Behavior:**
- Single selection only (radio-like)
- Smooth transition between states
- Active state persists until another option is selected
- Keyboard accessible (Tab, Enter/Space to toggle)

### 4.2 Control Behaviors

#### 4.2.1 Upload Button

**Component:** Image Uploader Drop Zone

**Interaction Flow:**
1. **Initial State:** Show upload icon and instruction text
2. **Click Action:** Opens file picker dialog
3. **File Selection:** 
   - Validates file (type and size)
   - If valid: Shows preview with filename and size
   - If invalid: Shows error message
4. **Preview State:** Shows "Clear" and "Predict Character" buttons

**File Acceptance:**
- Formats: PNG, JPG, JPEG, BMP
- Max size: 5MB
- Single file only

**Drag and Drop:**
1. **Drag Enter:** Border changes to yellow, background tint
2. **Drag Over:** Maintains active state
3. **Drop:** Same validation as file selection
4. **Drag Leave:** Returns to default state

#### 4.2.2 Clear Button

**Locations:** 
- Image Uploader (when preview is shown)
- Drawing Canvas (when canvas has content)

**Behavior:**
1. Click action removes current input
2. Image Uploader: Clears preview, resets to empty state
3. Canvas: Fills canvas with white background
4. Disabled during prediction processing
5. No confirmation dialog (instant action)

**Visual Feedback:**
- Immediate transition to empty state
- No loading indicator needed

#### 4.2.3 Submit/Predict Button

**Labels (Dynamic):**
- "Predict Character" (character model)
- "Predict Digit" (digit model)
- "Processing..." (during prediction)

**Behavior:**
1. **Enabled When:**
   - Image is uploaded OR canvas has content
   - Not currently processing

2. **Click Action:**
   - Button text changes to "Processing..."
   - Button becomes disabled
   - Sends data to backend API
   - Shows loading spinner in prediction panel

3. **On Success:**
   - Button re-enables
   - Text returns to default
   - Prediction panel shows results

4. **On Error:**
   - Button re-enables
   - Prediction panel shows error state

#### 4.2.4 Model Type Toggle

**Options:**
- "Character Recognition"
- "Digit Recognition"

**Behavior:**
1. Single selection enforced
2. On change:
   - Clears current prediction results
   - Updates hero title and descriptions
   - Changes submit button text
   - Updates canvas instruction text
3. Smooth visual transition
4. State preserved during session

#### 4.2.5 Input Mode Toggle

**Options:**
- "Upload Image"
- "Draw Character/Digit"

**Behavior:**
1. Single selection enforced
2. On change:
   - Switches visible input component
   - Preserves prediction results
   - Smooth fade transition
3. Component-specific controls appear/disappear

#### 4.2.6 Brush Size Slider

**Location:** Drawing Canvas controls

**Properties:**
- Type: Range input
- Min: 5px
- Max: 30px
- Default: 15px
- Step: 1px

**Behavior:**
1. Real-time update of brush size
2. Displays current value next to slider
3. Affects subsequent strokes (not existing ones)
4. Disabled during prediction processing

**Visual:**
- Track: Dark gray background
- Thumb: Yellow accent
- Value label: Updates immediately

#### 4.2.7 Navigation Links (Header)

**Type:** Button elements with smooth scroll

**Behavior:**
1. **Click Action:** Smooth scroll to target section
2. **Hover:** Yellow text, light background
3. **Focus:** Visible focus ring
4. **Active:** No special state (scroll completes quickly)

**Scroll Behavior:**
- `behavior: 'smooth'`
- `block: 'start'`
- Animation duration: ~500ms (browser default)

### 4.3 Keyboard Navigation

**Focus Order:**
1. Header navigation links
2. Model type selector buttons
3. Input mode selector buttons
4. Input component controls (upload button or canvas)
5. Action buttons (Clear, Predict)
6. Prediction panel (if focusable elements present)
7. Footer links

**Keyboard Shortcuts:**
- **Tab:** Next focusable element
- **Shift + Tab:** Previous focusable element
- **Enter/Space:** Activate button or control
- **Escape:** Close error messages (if dismissible)

### 4.4 Touch/Mobile Interactions

**Touch Targets:**
- Minimum size: 44x44px (iOS) / 48x48px (Android)
- Adequate spacing between interactive elements (8px minimum)

**Canvas Touch Drawing:**
- Single-touch drawing enabled
- Touch start: Begin path
- Touch move: Draw line
- Touch end: Complete stroke
- Multi-touch disabled (prevents accidental zooming)

**Drag and Drop (Mobile):**
- Native file picker preferred on mobile
- Drag and drop less reliable, so click-to-upload is primary


---

## 5. Input Validation and Feedback

### 5.1 Image Upload Validation

#### 5.1.1 File Type Validation

**Accepted Types:**
- image/png (.png)
- image/jpeg (.jpg, .jpeg)
- image/bmp (.bmp)

**Error Message (Invalid Type):**
```
"Invalid file type. Please upload a PNG, JPG, JPEG, or BMP image."
```

**Visual Feedback:**
- Red text error message below drop zone
- Error icon displayed
- Border remains default (not yellow)

#### 5.1.2 File Size Validation

**Maximum Size:** 5MB (5,242,880 bytes)

**Error Message (Too Large):**
```
"File size exceeds 5MB limit. Please upload a smaller image."
```

**Visual Feedback:**
- Same as file type error
- File size displayed if available

#### 5.1.3 File Count Validation

**Maximum Files:** 1 (single file only)

**Error Message (Multiple Files):**
```
"Please upload only one image at a time."
```

### 5.2 Canvas Drawing Validation

#### 5.2.1 Empty Canvas Check

**Validation:** Prevent submission of blank canvas

**Behavior:**
- Submit button disabled when canvas is empty
- `hasContent` state tracks if any drawing exists
- Enabled after first stroke

**Visual Feedback:**
- Disabled button (opacity 0.5, no hover effect)
- Instruction overlay visible when empty

#### 5.2.2 Canvas Content Detection

**Method:** Track drawing events
- Mouse down/touch start sets `hasContent = true`
- Clear action sets `hasContent = false`

### 5.3 API Error Handling

#### 5.3.1 Network Errors

**Error Scenarios:**
- Connection timeout
- Network unavailable
- Server not responding

**Error Message:**
```
"Unable to connect to the server. Please check your connection and try again."
```

**Visual Feedback:**
- Error state in prediction panel
- Red error icon
- "Try Again" button to retry

#### 5.3.2 Server Errors (5xx)

**Error Message:**
```
"Server error occurred. Please try again later."
```

**Additional Info:** Display HTTP status code if available

#### 5.3.3 Client Errors (4xx)

**Common Errors:**

1. **400 Bad Request:**
   ```
   "Invalid image data. Please upload a valid image."
   ```

2. **413 Payload Too Large:**
   ```
   "Image size too large for processing."
   ```

3. **415 Unsupported Media Type:**
   ```
   "Image format not supported."
   ```

4. **422 Unprocessable Entity:**
   ```
   "Unable to process image. Please try a different image."
   ```

#### 5.3.4 Prediction Confidence Threshold

**Low Confidence Indicator:**
- If top prediction confidence < 50%: Display warning badge
- Message: "Low confidence - result may be inaccurate"
- Badge style: Warning color (yellow/orange)

### 5.4 Success Feedback

#### 5.4.1 Successful Prediction

**Feedback Elements:**
1. **Visual Transition:**
   - Smooth fade-in of prediction panel
   - Scale-in animation for main character

2. **Result Display:**
   - Large predicted character prominently displayed
   - Confidence percentage with progress bar
   - Processing time shown
   - Top-5 predictions list

3. **Completion State:**
   - Submit button returns to enabled state
   - "Try Another Image" button appears

#### 5.4.2 File Upload Success

**Feedback:**
- Image preview displayed immediately
- Filename and size shown
- Action buttons appear (Clear, Predict)
- Smooth transition animation

### 5.5 Loading States

#### 5.5.1 Prediction Processing

**Indicators:**
1. **Button State:**
   - Text: "Processing..."
   - Disabled state

2. **Prediction Panel:**
   - Loading spinner (rotating animation)
   - Message: "Analyzing character..."

3. **Duration Display:**
   - Processing time shown after completion

#### 5.5.2 Component Loading

**Initial Page Load:**
- Skeleton screens for major components (if needed)
- Fade-in animation when content ready

### 5.6 Empty States

#### 5.6.1 No Prediction Yet

**Visual:**
- Lightbulb icon (gray)
- Message: "Upload or draw a character to see prediction"
- Centered in prediction panel

#### 5.6.2 No Image Selected

**Visual:**
- Upload cloud icon
- Instruction text
- Click/drag prompt

### 5.7 Validation Summary

| Input Type | Validation | Error Location | Error Style |
|------------|------------|----------------|-------------|
| File Type | Client-side | Below upload zone | Red text + icon |
| File Size | Client-side | Below upload zone | Red text + icon |
| Empty Canvas | Client-side | Button disabled | Opacity change |
| API Errors | After submission | Prediction panel | Error state card |
| Network Errors | After submission | Prediction panel | Error state card |

### 5.8 Error Message Design

**Container:**
- Background: `rgba(239, 68, 68, 0.2)` (red tint)
- Border: 1px solid `rgba(239, 68, 68, 0.3)`
- Border radius: 8px
- Padding: 12px

**Content:**
- Icon: Error circle (red)
- Title: "Error" (bold, red)
- Message: Error description (regular weight)
- Action: "Try Again" button (optional)

**Placement:**
- Upload errors: Directly below upload zone
- Prediction errors: In prediction result panel


---

## 6. Responsive Design Rules

### 6.1 Breakpoint System

| Breakpoint | Min Width | Max Width | Target Devices |
|------------|-----------|-----------|----------------|
| Mobile Small | 0px | 639px | Small phones (portrait) |
| Mobile Large | 640px | 767px | Large phones (portrait) |
| Tablet | 768px | 1023px | Tablets, small laptops |
| Desktop | 1024px | 1279px | Laptops, desktops |
| Desktop Large | 1280px | ∞ | Large desktops, external monitors |

### 6.2 Layout Adjustments by Breakpoint

#### 6.2.1 Mobile (< 768px)

**Header:**
- Layout: Vertical stack
- Logo and title: Centered
- Navigation: Full-width buttons
- Height: ~140px (increased due to stacking)

**Hero Section:**
- Title: 1.75rem (28px) - reduced from 2.25rem
- Text: 1rem (16px) - reduced from 1.125rem
- Padding: 1rem (reduced)

**Model & Input Mode Selectors:**
- Full width buttons
- Vertical stack if needed
- Increased touch target sizes (min 48px height)

**Main Content Grid:**
- Single column layout
- Input section: Full width
- Prediction panel: Full width, below input
- Gap: 1.5rem (reduced from 2rem)

**Feature Cards:**
- Single column
- Full width cards
- Gap: 1rem

**Character Cards Grid:**
- 3-4 columns (auto-fill, min 80px)
- Reduced from desktop's min 120px
- Smaller padding: 0.75rem

**Canvas:**
- Responsive sizing: Max-width 100%
- Height adjusts to maintain aspect ratio
- Touch-optimized controls

**Footer:**
- Single column layout
- Centered text
- Vertical spacing increased

**Typography Adjustments:**
- Hero title: 1.75rem
- Section titles: 1.125rem
- Body text: 0.875-1rem
- Character display: 3-4rem (reduced)

#### 6.2.2 Tablet (768px - 1023px)

**Header:**
- Horizontal layout (if space allows)
- May stack on smaller tablets

**Main Content Grid:**
- Single column OR two columns depending on content
- Character recognition: Prefer single column for better canvas size
- Prediction panel below or beside (if 2-col)

**Feature Cards:**
- Two columns
- Adequate spacing

**Character Cards:**
- 6-8 columns (auto-fill, min 100px)

**Canvas:**
- Larger size possible
- Still responsive with max-width

**Footer:**
- Two or three columns
- Better use of horizontal space

#### 6.2.3 Desktop (≥ 1024px)

**Header:**
- Full horizontal layout
- Space-between alignment
- Logo left, nav right

**Main Content Grid:**
- Two equal columns (1fr 1fr)
- Side-by-side input and prediction
- Gap: 2rem

**Feature Cards:**
- Three columns
- Equal spacing

**Character Cards:**
- Auto-fill grid, min 120px
- Optimal viewing for all characters

**Canvas:**
- Fixed 400x400px (optimal for model input)

**Footer:**
- Three columns
- Full horizontal layout

**Container Max Width:**
- 1280px with auto margins (centered)

### 6.3 Component-Specific Responsive Behavior

#### 6.3.1 Image Uploader

**Mobile:**
- Drop zone height: Min 250px
- Preview image: Max-width 100%
- Buttons: Full width or stacked

**Desktop:**
- Drop zone height: Min 300px
- Preview image: Centered, max reasonable size
- Buttons: Side by side

#### 6.3.2 Drawing Canvas

**Mobile:**
- Canvas width: 100% (max 400px)
- Canvas height: Same as width (square aspect)
- Brush slider: Full width
- Buttons: Full width, stacked

**Tablet:**
- Canvas: 350-400px
- Better button spacing

**Desktop:**
- Canvas: Fixed 400x400px
- Buttons: Side by side

**Touch vs. Mouse:**
- Touch: Larger brush size default (20px)
- Mouse: Standard default (15px)
- Touch: Larger clear/submit buttons

#### 6.3.3 Prediction Result Panel

**Mobile:**
- Character size: 3rem
- Top-5 list: More compact
- Confidence bars: Shorter
- Percentages: Smaller text

**Desktop:**
- Character size: 4-6rem
- Top-5 list: Spacious layout
- Full-width confidence bars
- Larger percentages

#### 6.3.4 Model/Mode Selectors

**Mobile:**
- Buttons may stack if text is long
- Min height: 44px
- Full width container

**Desktop:**
- Always horizontal
- Compact padding
- Inline container

### 6.4 Responsive Typography

| Element | Mobile | Tablet | Desktop |
|---------|--------|--------|---------|
| Hero Title | 1.75rem | 2rem | 2.25rem |
| Section Title | 1.125rem | 1.25rem | 1.25rem |
| Body Text | 0.875rem | 1rem | 1rem |
| Urdu Character | 3-4rem | 4-5rem | 4-6rem |
| Button Text | 0.875rem | 0.875rem | 0.875-1rem |

### 6.5 Spacing Adjustments

| Spacing Type | Mobile | Tablet | Desktop |
|--------------|--------|--------|---------|
| Container Padding | 1rem | 1.5rem | 2rem |
| Grid Gap | 1rem | 1.5rem | 2rem |
| Card Padding | 1rem | 1.25rem | 1.5rem |
| Section Margin | 2rem | 3rem | 4rem |

### 6.6 Image and Media Queries

**CSS Media Queries Used:**

```css
/* Mobile First Approach */

/* Base styles (Mobile) */
/* 0-767px */

@media (min-width: 768px) {
  /* Tablet */
}

@media (min-width: 1024px) {
  /* Desktop */
}

@media (min-width: 1280px) {
  /* Large Desktop */
}
```

### 6.7 Responsive Testing Guidelines

**Test On:**
1. iPhone SE (375x667)
2. iPhone 12 Pro (390x844)
3. iPad (768x1024)
4. iPad Pro (1024x1366)
5. Desktop (1920x1080)
6. Desktop (1280x720)

**Testing Checklist:**
- [ ] All text is readable at all sizes
- [ ] Touch targets are at least 44x44px on mobile
- [ ] No horizontal scrolling on any breakpoint
- [ ] Images scale appropriately
- [ ] Canvas is functional on touch devices
- [ ] Buttons are accessible and not overlapping
- [ ] Navigation works on all screen sizes
- [ ] Prediction results display correctly

### 6.8 Orientation Considerations

**Portrait Mode (Mobile/Tablet):**
- Preferred layout: Vertical stacking
- Canvas: Square, max-width 100%
- Prediction: Below input

**Landscape Mode (Mobile/Tablet):**
- Consider two-column where space allows
- Canvas: May be smaller to fit viewport height
- Navigation: Remains accessible

**Desktop:**
- Orientation less critical
- Layout optimized for standard landscape monitors


---

## 7. Canvas Drawing UI

### 7.1 Canvas Specifications

#### 7.1.1 Canvas Dimensions and Properties

**Size:**
- Width: 400px (fixed on desktop)
- Height: 400px (fixed on desktop)
- Responsive: Max-width 100% on mobile, maintains aspect ratio

**Background:**
- Color: White (`#FFFFFF`)
- Purpose: Consistent with model training data

**Border:**
- Width: 2px
- Style: Solid
- Color: `#404040` (medium gray)
- Radius: 8px (rounded corners)

**Cursor:**
- Type: Crosshair
- Indicates drawing mode

**Touch Action:**
- Value: `none`
- Prevents scrolling/zooming while drawing

#### 7.1.2 Drawing Properties

**Stroke Style:**
- Color: Black (`#000000`)
- Width: Variable (5-30px, default 15px)
- Line cap: `round` (smooth stroke ends)
- Line join: `round` (smooth corners)

**Context Settings:**
```javascript
ctx.strokeStyle = 'black';
ctx.lineWidth = brushSize; // 5-30px
ctx.lineCap = 'round';
ctx.lineJoin = 'round';
```

### 7.2 Drawing Interactions

#### 7.2.1 Mouse Interactions

**Mouse Down:**
1. Begin new path
2. Move to cursor position
3. Set `isDrawing = true`
4. Set `hasContent = true`

**Mouse Move:**
1. Only active if `isDrawing === true`
2. Draw line to current position
3. Stroke the path

**Mouse Up:**
1. Set `isDrawing = false`
2. Complete current stroke

**Mouse Leave:**
1. Set `isDrawing = false`
2. Complete current stroke
3. Prevents drawing outside canvas

#### 7.2.2 Touch Interactions

**Touch Start:**
1. Get first touch position
2. Begin new path
3. Set `isDrawing = true`
4. Set `hasContent = true`

**Touch Move:**
1. Only active if `isDrawing === true`
2. Get current touch position
3. Draw line to position
4. Stroke the path

**Touch End:**
1. Set `isDrawing = false`
2. Complete current stroke

**Coordinate Calculation:**
```javascript
// Accounts for canvas scaling and positioning
const rect = canvas.getBoundingClientRect();
const scaleX = canvas.width / rect.width;
const scaleY = canvas.height / rect.height;
const x = (clientX - rect.left) * scaleX;
const y = (clientY - rect.top) * scaleY;
```

### 7.3 Canvas Controls

#### 7.3.1 Brush Size Slider

**Component:** Range input

**Properties:**
- Min: 5px
- Max: 30px
- Default: 15px (20px on touch devices)
- Step: 1px

**Layout:**
- Label: "Brush Size:"
- Slider: Horizontal, full width
- Value display: "15px" (updates in real-time)

**Styling:**
- Track: Dark gray
- Thumb: Yellow (`#FFC107`)
- Value label: Gray text, right-aligned

**Behavior:**
- Real-time update on slide
- Affects next strokes only
- Disabled during prediction

#### 7.3.2 Clear Button

**Location:** Bottom left of canvas controls

**Label:** "Clear"

**Style:** Secondary button

**Behavior:**
1. Click to clear entire canvas
2. Fills canvas with white
3. Sets `hasContent = false`
4. No confirmation required
5. Disabled during prediction

**Visual Feedback:**
- Instant canvas clear
- Button briefly shows active state

#### 7.3.3 Submit Button

**Location:** Bottom right of canvas controls

**Label:**
- Default: "Predict Character" or "Predict Digit"
- Loading: "Processing..."

**Style:** Primary button (yellow)

**Enabled When:**
- `hasContent === true`
- Not currently loading

**Behavior:**
1. Convert canvas to base64 PNG
2. Send to prediction API
3. Disable button and show loading state
4. Update prediction panel

### 7.4 Canvas States

#### 7.4.1 Empty State

**Visual:**
- Clean white canvas
- Instruction overlay (semi-transparent)
- Text: "Draw an Urdu character here" or "Draw an Urdu digit here (۰-۹)"

**Controls:**
- Submit button disabled
- Clear button disabled
- Brush slider enabled

#### 7.4.2 Drawing State

**Visual:**
- Visible strokes on canvas
- No overlay

**Controls:**
- Submit button enabled
- Clear button enabled
- Brush slider enabled

#### 7.4.3 Processing State

**Visual:**
- Canvas remains visible with drawing
- Loading indicator in prediction panel

**Controls:**
- Submit button disabled (text: "Processing...")
- Clear button disabled
- Brush slider disabled
- Canvas drawing disabled

#### 7.4.4 Disabled State

**Visual:**
- Canvas has `.disabled` class
- Slightly reduced opacity
- Cursor: default (not crosshair)

**Behavior:**
- No drawing possible
- All events prevented

### 7.5 Canvas Instruction Overlay

**Position:** Absolutely positioned over canvas center

**Styling:**
- Background: `rgba(0, 0, 0, 0.05)` (subtle tint)
- Text color: `#9ca3af` (gray)
- Font size: 1rem
- Padding: 1rem
- Border radius: 8px

**Visibility:**
- Shown when `hasContent === false`
- Hidden when any drawing exists
- Fade animation on hide

### 7.6 Canvas Accessibility

**ARIA Labels:**
```html
<canvas
  aria-label="Drawing canvas for Urdu character input"
  role="img"
  aria-describedby="canvas-instructions"
>
```

**Instructions Element:**
```html
<div id="canvas-instructions" class="sr-only">
  Use mouse or touch to draw an Urdu character on the white canvas.
  Use the brush size slider to adjust stroke width.
  Click Clear to erase, or Predict to submit your drawing.
</div>
```

### 7.7 Canvas Data Export

**Format:** PNG (base64-encoded)

**Method:**
```javascript
const imageData = canvas.toDataURL('image/png');
```

**Data URL Structure:**
```
data:image/png;base64,iVBORw0KGgoAAAANS...
```

**API Transmission:**
- Sent in request body as JSON
- Field: `image_data`
- Encoding: Base64 string

---

## 8. Prediction Display

### 8.1 Prediction Panel States

#### 8.1.1 Empty/Placeholder State

**Visual Elements:**
- Lightbulb icon (gray, 48x48px)
- Message: "Upload or draw a character to see prediction"
- Centered in panel
- Light gray color scheme

**Layout:**
- Vertically and horizontally centered
- Icon above text
- 16px gap between elements

#### 8.1.2 Loading State

**Visual Elements:**
- Spinning loader (48x48px)
- Message: "Analyzing character..."
- Centered in panel

**Animation:**
- Circular rotation: 1s linear infinite
- Border animation: Yellow accent

#### 8.1.3 Error State

**Visual Elements:**
- Error circle icon (red, 48x48px)
- Title: "Error" (red, bold)
- Error message (white text)
- "Try Again" button (primary style)

**Layout:**
- Vertically centered
- Icon at top
- Title, message, button stacked
- 16px gaps

**Error Container:**
- Background: `rgba(239, 68, 68, 0.2)`
- Border: 1px solid `rgba(239, 68, 68, 0.3)`
- Border radius: 12px
- Padding: 24px

#### 8.1.4 Result State (Success)

**Layout Sections:**
1. Main Prediction Card
2. Confidence Meter
3. Processing Time
4. Top-5 Predictions List
5. Action Button

### 8.2 Main Prediction Display

#### 8.2.1 Predicted Character

**Label:**
- Text: "Predicted Character"
- Font size: 0.875rem
- Color: `#9ca3af` (gray)
- Margin bottom: 8px

**Character Display:**
- Font size: 4-6rem (64-96px)
- Font family: 'Noto Nastaliq Urdu', serif
- Font weight: 600
- Color: `#FFC107` (yellow)
- Direction: RTL
- Text align: Right
- Background: Subtle gradient or glow (optional)

**Container:**
- Background: `#1a1a1a`
- Border: 1px solid `#262626`
- Border radius: 12px
- Padding: 24px
- Margin bottom: 16px
- Box shadow: Large elevation

#### 8.2.2 Confidence Meter

**Header:**
- Label: "Confidence" (left-aligned)
- Percentage: "95%" (right-aligned, yellow)
- Display: Flex, space-between
- Margin bottom: 8px

**Progress Bar:**
- Height: 8px
- Background: `#262626` (dark gray track)
- Border radius: 9999px (fully rounded)
- Overflow: Hidden

**Progress Fill:**
- Background: Linear gradient `#FFC107` to `#FFB300`
- Width: Dynamic (0-100%)
- Height: 100%
- Transition: Width 0.5s ease
- Animation: Smooth fill from 0 to final percentage

**Confidence Thresholds:**
- 80-100%: Green tint
- 50-79%: Yellow tint (default)
- 0-49%: Yellow with warning badge

### 8.3 Processing Time

**Display:**
- Text: "Processing time: 45.23ms"
- Font size: 0.875rem
- Color: `#9ca3af`
- Margin: 12px 0

**Format:**
- Always show 2 decimal places
- Unit: "ms" (milliseconds)

### 8.4 Top-5 Predictions List

#### 8.4.1 Section Header

**Title:** "Top 5 Predictions"

**Styling:**
- Font size: 1rem
- Font weight: 600
- Color: `#f9fafb`
- Margin bottom: 12px

#### 8.4.2 Prediction Item

**Layout:** Horizontal flex, space-between

**Left Side:**
- Rank number: "1.", "2.", etc.
- Font size: 0.875rem
- Color: `#9ca3af`
- Min width: 24px

- Predicted character (Urdu)
- Font size: 1.5rem
- Font family: 'Noto Nastaliq Urdu'
- Color: `#FFC107`
- Direction: RTL

**Right Side:**
- Horizontal bar (visual representation)
  - Background: `#262626`
  - Fill: `#FFC107` gradient
  - Width: Proportional to probability
  - Height: 6px
  - Border radius: 3px

- Percentage text: "95.0%"
  - Font size: 0.875rem
  - Color: `#e5e7eb`
  - Min width: 48px (right-aligned)

**Item Spacing:**
- Vertical gap: 12px between items
- Horizontal gap: 12px between elements

**Example Structure:**
```
1.  ا  [████████████████████] 95.0%
2.  ب  [███                  ]  5.0%
3.  پ  [█                    ]  2.0%
4.  ت  [█                    ]  1.5%
5.  ٹ  [                     ]  0.5%
```

#### 8.4.3 Top-5 Container

**Styling:**
- Background: Slightly darker than main card
- Border: 1px solid `#262626`
- Border radius: 8px
- Padding: 16px
- Margin top: 16px

### 8.5 Action Button

**Button:** "Try Another Image"

**Style:** Secondary

**Location:** Bottom of prediction panel

**Behavior:**
- Click to reset prediction state
- Returns to empty state
- Clears results
- Maintains input (canvas/upload)

### 8.6 Animation and Transitions

#### 8.6.1 Result Appearance

**Main Character:**
- Animation: Scale in (0.95 to 1)
- Duration: 0.3s
- Easing: Ease-out

**Confidence Bar:**
- Animation: Width transition
- Duration: 0.5s
- Easing: Ease-out
- Delay: 0.1s (after character appears)

**Top-5 List:**
- Animation: Slide up
- Duration: 0.3s
- Easing: Ease-out
- Delay: 0.2s
- Stagger: 50ms between items (optional)

#### 8.6.2 State Transitions

**Loading to Result:**
- Fade out spinner: 0.2s
- Fade in result: 0.3s
- Total transition: ~0.5s

**Result to Empty:**
- Fade out: 0.2s
- Fade in placeholder: 0.2s

### 8.7 Responsive Adjustments

**Mobile (<768px):**
- Character size: 3-4rem
- Top-5 bars: Shorter, stacked labels
- Percentages: Smaller text
- Reduced padding

**Tablet (768-1023px):**
- Character size: 4-5rem
- Standard layout with slight compression

**Desktop (≥1024px):**
- Character size: 4-6rem
- Full spacious layout
- Optimal readability

### 8.8 Accessibility Features

**ARIA Attributes:**
```html
<div role="region" aria-live="polite" aria-label="Prediction results">
  <!-- Prediction content -->
</div>
```

**Confidence Meter:**
```html
<div role="progressbar" 
     aria-valuenow="95" 
     aria-valuemin="0" 
     aria-valuemax="100"
     aria-label="Prediction confidence: 95%">
</div>
```

**Screen Reader Announcements:**
- "Prediction complete: Character [X] with 95% confidence"
- "Top predictions: [list items]"


---

## 9. Accessibility Considerations

### 9.1 WCAG 2.1 Compliance

**Target Level:** AA (minimum), AAA where feasible

### 9.2 Color and Contrast

#### 9.2.1 Contrast Ratios

**Text Contrast:**
- Normal text (≥14px): Minimum 4.5:1
- Large text (≥18px or 14px bold): Minimum 3:1
- Primary yellow (`#FFC107`) on black (`#111111`): >7:1 ✓
- Light gray text (`#e5e7eb`) on dark (`#111111`): >12:1 ✓
- Medium gray (`#9ca3af`) on dark (`#111111`): >4.5:1 ✓

**Interactive Elements:**
- Focus indicators: 3:1 minimum against background
- Button states: Clear visual differentiation

#### 9.2.2 Color Independence

- **Never rely on color alone** for information
- **Example:** Error states use icon + color + text
- **Example:** Confidence uses percentage + bar + color

### 9.3 Keyboard Navigation

#### 9.3.1 Focus Management

**Focus Order:**
1. Skip to main content link (optional)
2. Header navigation
3. Model type selector
4. Input mode selector
5. Input component (upload/canvas)
6. Action buttons
7. Prediction panel (if interactive)
8. Footer links

**Focus Indicators:**
- Visible outline or box shadow
- Color: Yellow (`rgba(255, 193, 7, 0.5)`)
- Width: 3px
- Never remove `:focus` styles

#### 9.3.2 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Tab | Move to next focusable element |
| Shift + Tab | Move to previous focusable element |
| Enter / Space | Activate button or control |
| Escape | Dismiss modal/error (if applicable) |

**Canvas Keyboard Access:**
- Canvas itself not keyboard-operable (limitation)
- All actions available via buttons (keyboard accessible)
- Alternative: Upload image option always available

### 9.4 Screen Reader Support

#### 9.4.1 ARIA Landmarks

```html
<header role="banner">
<nav role="navigation" aria-label="Main navigation">
<main role="main">
<footer role="contentinfo">
```

#### 9.4.2 ARIA Labels and Descriptions

**Image Uploader:**
```html
<div role="button" 
     aria-label="Upload image file"
     aria-describedby="upload-instructions">
```

**Canvas:**
```html
<canvas 
  aria-label="Drawing canvas for Urdu character input"
  role="img">
```

**Prediction Panel:**
```html
<div role="region" 
     aria-live="polite" 
     aria-label="Prediction results">
```

**Progress Bars:**
```html
<div role="progressbar"
     aria-valuenow="95"
     aria-valuemin="0"
     aria-valuemax="100"
     aria-label="Prediction confidence: 95%">
```

#### 9.4.3 Live Regions

**Prediction Updates:**
- `aria-live="polite"` on prediction panel
- Announces results when available
- Announces errors when they occur

**Loading States:**
- Announce "Analyzing character..." when processing starts
- Announce completion or error

### 9.5 Visual Accessibility

#### 9.5.1 Text Sizing

- Base font size: 16px (1rem)
- All text scalable via browser zoom
- Support up to 200% zoom without horizontal scrolling
- Responsive design ensures layout adapts

#### 9.5.2 Icons and Visual Indicators

- All icons have text labels or `aria-label`
- Icons are supplementary, not sole indicators
- SVG icons have proper `role` and `aria-label`

#### 9.5.3 Animation and Motion

**Respect `prefers-reduced-motion`:**

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Animations Used:**
- Spinner: Can be reduced
- Fade-ins: Can be instant
- Slide-ups: Can be instant
- No flashing or strobing effects (violates WCAG)

### 9.6 Touch and Motor Accessibility

#### 9.6.1 Touch Targets

**Minimum Sizes:**
- Mobile: 44x44px (iOS HIG)
- Android: 48x48px
- Desktop: 24x24px (acceptable with mouse)

**Applied To:**
- All buttons
- All clickable areas
- Canvas touch drawing
- Slider thumbs

#### 9.6.2 Spacing

- Minimum 8px spacing between interactive elements
- Prevents accidental activation
- Especially critical on mobile

### 9.7 Error Identification and Recovery

#### 9.7.1 Error Messages

- Clear and specific
- Suggest corrective action
- Not dismissible automatically (user-controlled)
- Both visual and text-based

**Example:**
```
❌ Invalid file type. Please upload a PNG, JPG, JPEG, or BMP image.
[OK button]
```

#### 9.7.2 Form Validation

- Real-time or on-submit
- Error messages associated with inputs
- `aria-invalid="true"` on invalid inputs
- `aria-describedby` links to error message

### 9.8 Language and RTL Support

#### 9.8.1 Urdu Text (RTL)

**CSS Properties:**
```css
.urdu-text {
  font-family: 'Noto Nastaliq Urdu', serif;
  direction: rtl;
  text-align: right;
}
```

**HTML Attributes:**
```html
<span lang="ur" dir="rtl">ا</span>
```

#### 9.8.2 Mixed Content

- Interface in English (LTR)
- Urdu characters in RTL
- Proper directional isolation
- Unicode bidi algorithm support

### 9.9 Accessibility Testing Checklist

**Manual Tests:**
- [ ] Keyboard-only navigation works completely
- [ ] Screen reader announces all content correctly
- [ ] Focus indicators are visible on all interactive elements
- [ ] Color contrast meets WCAG AA standards
- [ ] Text is readable at 200% zoom
- [ ] Touch targets meet minimum size requirements
- [ ] Error messages are clear and actionable
- [ ] All images have alt text or aria-labels
- [ ] RTL Urdu text displays correctly
- [ ] Reduced motion preference is respected

**Automated Tools:**
- axe DevTools
- WAVE browser extension
- Lighthouse accessibility audit
- Pa11y or similar CLI tools

### 9.10 Accessibility Statement

Include on site or in documentation:

```
Accessibility Statement

We are committed to ensuring digital accessibility for people of all abilities.
We continually improve the user experience and apply relevant accessibility standards.

If you encounter any accessibility barriers, please contact us:
[Contact information]

Conformance: WCAG 2.1 Level AA
```

---

## 10. Developer Integration Notes

### 10.1 Backend API Integration

#### 10.1.1 API Base URL

**Environment Variable:**
```
VITE_API_BASE_URL=http://localhost:8000
```

**Production:**
```
VITE_API_BASE_URL=https://api.your-domain.com
```

#### 10.1.2 Prediction Endpoints

**1. Image Upload Prediction**

```
POST /api/v1/predict
Content-Type: multipart/form-data

Request:
- file: File (PNG, JPG, JPEG, BMP)

Response:
{
  "prediction": "ا",
  "confidence": 0.95,
  "top_5": [
    {"character": "ا", "probability": 0.95},
    {"character": "ب", "probability": 0.02},
    ...
  ],
  "processing_time_ms": 45.23
}
```

**2. Canvas Drawing Prediction**

```
POST /api/v1/predict/canvas
Content-Type: application/json

Request:
{
  "image_data": "data:image/png;base64,iVBORw0KGgo..."
}

Response:
{
  "prediction": "ا",
  "confidence": 0.95,
  "top_5": [...],
  "processing_time_ms": 45.23
}
```

**3. Get Supported Classes**

```
GET /api/v1/classes

Response:
{
  "classes": ["ا", "ب", "پ", ...],
  "count": 46
}
```

**4. Health Check**

```
GET /health

Response:
{
  "status": "healthy",
  "model_loaded": true,
  "version": "1.0.0"
}
```

#### 10.1.3 Error Responses

**Standard Error Format:**
```json
{
  "detail": "Error message",
  "error_type": "InvalidImageError"
}
```

**HTTP Status Codes:**
- 200: Success
- 400: Bad Request (invalid input)
- 413: Payload Too Large
- 415: Unsupported Media Type
- 422: Unprocessable Entity
- 500: Internal Server Error
- 503: Service Unavailable

### 10.2 Frontend Service Layer

#### 10.2.1 API Service Structure

**File:** `src/services/api.ts`

**Methods:**
- `predictFromFile(file: File): Promise<PredictionResponse>`
- `predictFromCanvas(imageData: string): Promise<PredictionResponse>`
- `getClasses(): Promise<ClassesResponse>`
- `healthCheck(): Promise<HealthResponse>`

**Axios Configuration:**
```typescript
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});
```

#### 10.2.2 Error Handling

**Interceptor Pattern:**
```typescript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      // Server responded with error status
      return Promise.reject(error.response.data);
    } else if (error.request) {
      // No response received
      return Promise.reject({
        detail: 'Network error. Please check your connection.',
      });
    } else {
      // Request setup error
      return Promise.reject({
        detail: 'An unexpected error occurred.',
      });
    }
  }
);
```

### 10.3 State Management

#### 10.3.1 Prediction Hook

**File:** `src/hooks/usePrediction.ts`

**State:**
```typescript
interface PredictionState {
  result: PredictionResponse | null;
  isLoading: boolean;
  error: string | null;
}
```

**Actions:**
- `predictImage(file: File, modelType: ModelType)`
- `predictCanvas(imageData: string, modelType: ModelType)`
- `reset()`

#### 10.3.2 Component State

**Local State (useState):**
- Input mode selection
- Model type selection
- Canvas content tracking
- Image preview state
- Brush size

### 10.4 Image Processing

#### 10.4.1 Client-Side Validation

**File:** `src/utils/imageUtils.ts`

**Functions:**
- `validateImage(file: File): ValidationResult`
- `createImagePreview(file: File): string`
- `revokeImagePreview(url: string): void`
- `formatFileSize(bytes: number): string`

**Validation Rules:**
```typescript
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB
const ACCEPTED_TYPES = ['image/png', 'image/jpeg', 'image/bmp'];
```

#### 10.4.2 Canvas to Image Conversion

**Method:**
```typescript
const canvas = canvasRef.current;
const imageData = canvas.toDataURL('image/png');
```

**Data URL Structure:**
- Prefix: `data:image/png;base64,`
- Body: Base64-encoded PNG data
- Transmitted as-is to API

### 10.5 Styling Integration

#### 10.5.1 CSS Modules (Component-Scoped)

**Pattern:**
- Each component has matching `.css` file
- Imported into component file
- Class names scoped to component

**Example:**
```typescript
import './DrawingCanvas.css';
```

#### 10.5.2 Global Styles

**File:** `src/styles/globals.css`

**Includes:**
- CSS Reset
- Font imports
- Utility classes
- Global variables (if using CSS custom properties)

#### 10.5.3 Font Loading

**Google Fonts Import:**
```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&family=Inter:wght@300;400;500;600;700&display=swap');
```

**Font Stack:**
```css
/* English/Interface */
font-family: 'Inter', system-ui, -apple-system, sans-serif;

/* Urdu */
font-family: 'Noto Nastaliq Urdu', serif;
```

### 10.6 Build and Deployment

#### 10.6.1 Environment Variables

**Development (`.env.development`):**
```
VITE_API_BASE_URL=http://localhost:8000
```

**Production (`.env.production`):**
```
VITE_API_BASE_URL=https://api.production-domain.com
```

#### 10.6.2 Build Configuration

**Vite Config:** `vite.config.ts`
```typescript
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    sourcemap: true,
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
});
```

#### 10.6.3 Docker Integration

**Frontend Dockerfile:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 5173
CMD ["npm", "run", "preview"]
```

### 10.7 Performance Considerations

#### 10.7.1 Image Optimization

- Client-side validation before upload
- Max file size enforcement (5MB)
- Canvas resolution optimized for model (400x400px)

#### 10.7.2 Code Splitting

- Route-based splitting (if multiple pages)
- Lazy loading for heavy components
- Dynamic imports for utilities

#### 10.7.3 Caching

**API Responses:**
- Consider caching `/api/v1/classes` (rarely changes)
- No caching for predictions (always fresh)

**Static Assets:**
- Browser caching for fonts, icons
- CDN for production static files

### 10.8 Testing Integration Points

#### 10.8.1 Component Tests

**Test Files:**
- `*.test.tsx` alongside components
- Testing Library (@testing-library/react)
- Vitest as test runner

**Key Test Cases:**
- Image upload flow
- Canvas drawing and submission
- Prediction display
- Error handling
- Responsive behavior

#### 10.8.2 API Mocking

**MSW (Mock Service Worker):**
```typescript
const handlers = [
  rest.post('/api/v1/predict', (req, res, ctx) => {
    return res(
      ctx.json({
        prediction: 'ا',
        confidence: 0.95,
        top_5: [...],
        processing_time_ms: 45.23,
      })
    );
  }),
];
```

### 10.9 Monitoring and Analytics

#### 10.9.1 Error Tracking

**Consider Integration:**
- Sentry for error tracking
- Log all API errors
- Track failed predictions

#### 10.9.2 Usage Analytics

**Events to Track:**
- Predictions initiated
- Model type selections
- Input mode preferences
- Error occurrences
- Average processing time

### 10.10 Security Considerations

#### 10.10.1 Input Sanitization

- File type validation (client + server)
- File size limits enforced
- No executable file types allowed
- Canvas data validated server-side

#### 10.10.2 CORS Configuration

**Backend CORS Settings:**
```python
origins = [
    "http://localhost:5173",  # Development
    "https://your-domain.com",  # Production
]
```

#### 10.10.3 Content Security Policy

**Recommended Headers:**
```
Content-Security-Policy: default-src 'self'; 
  img-src 'self' data: blob:; 
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  font-src 'self' https://fonts.gstatic.com;
```


---

## 11. Component Diagrams

### 11.1 Page Layout Wireframe

```
┌─────────────────────────────────────────────────────────────┐
│ HEADER                                                       │
│ [Logo] Urdu OCR                        [Nav Links]          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                       HERO SECTION                           │
│         Urdu Character Recognition                           │
│   Upload or draw a handwritten character...                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│            MODEL TYPE SELECTOR                               │
│  [Character Recognition]  [Digit Recognition]               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│            INPUT MODE SELECTOR                               │
│     [Upload Image]    [Draw Character]                      │
└─────────────────────────────────────────────────────────────┘

┌──────────────────────────┬──────────────────────────────────┐
│  INPUT SECTION           │  PREDICTION PANEL                │
│                          │                                  │
│  ┌────────────────────┐  │  ┌─────────────────────────┐    │
│  │                    │  │  │  Predicted Character     │    │
│  │   Upload/Canvas    │  │  │         ا               │    │
│  │                    │  │  │  Confidence: 95%        │    │
│  │                    │  │  │  [████████████░░░░]      │    │
│  └────────────────────┘  │  └─────────────────────────┘    │
│                          │                                  │
│  [Clear]  [Predict]      │  Top 5 Predictions:             │
│                          │  1. ا  [████████████] 95%       │
│                          │  2. ب  [██░░░░░░░░░░]  2%       │
│                          │  3. پ  [█░░░░░░░░░░░]  1%       │
│                          │                                  │
└──────────────────────────┴──────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    FEATURE CARDS                             │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐                │
│  │  [Icon] │    │  [Icon] │    │  [Icon] │                │
│  │ AI-     │    │ Fast &  │    │  36     │                │
│  │ Powered │    │ Accurate│    │ Chars   │                │
│  └─────────┘    └─────────┘    └─────────┘                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│              SUPPORTED CHARACTERS                            │
│  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐                     │
│  │ ا │ │ ب │ │ پ │ │ ت │ │ ٹ │ │ ث │   ...              │
│  └───┘ └───┘ └───┘ └───┘ └───┘ └───┘                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ FOOTER                                                       │
│ [About]  [Links]  [Tech]                © 2025 Urdu OCR     │
└─────────────────────────────────────────────────────────────┘
```

### 11.2 Image Upload Component Flow

```
┌─────────────────────────────────────────┐
│         IMAGE UPLOADER                  │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │        [Cloud Icon]               │  │
│  │  Drag & drop an image here        │  │
│  │  or click to select a file        │  │
│  │  PNG, JPG, JPEG, BMP (max 5MB)    │  │
│  └───────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
              ↓ (File Selected)
┌─────────────────────────────────────────┐
│         IMAGE PREVIEW                   │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │                                   │  │
│  │        [Image Preview]            │  │
│  │                                   │  │
│  └───────────────────────────────────┘  │
│  filename.png                           │
│  2.3 MB                                 │
│                                         │
│  [Clear]          [Predict Character]   │
└─────────────────────────────────────────┘
              ↓ (Submit)
┌─────────────────────────────────────────┐
│         LOADING STATE                   │
│                                         │
│          [Spinning Loader]              │
│       Analyzing character...            │
│                                         │
└─────────────────────────────────────────┘
              ↓ (Success)
┌─────────────────────────────────────────┐
│      PREDICTION RESULT                  │
│  (See Prediction Panel Wireframe)       │
└─────────────────────────────────────────┘
```

### 11.3 Drawing Canvas Component Flow

```
┌─────────────────────────────────────────┐
│      DRAWING CANVAS (Empty)             │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │                                   │  │
│  │  Draw an Urdu character here      │  │
│  │         (Overlay text)            │  │
│  │                                   │  │
│  └───────────────────────────────────┘  │
│                                         │
│  Brush Size: [━━━━━━○━━━━] 15px        │
│                                         │
│  [Clear - Disabled] [Predict - Disabled]│
└─────────────────────────────────────────┘
              ↓ (Drawing starts)
┌─────────────────────────────────────────┐
│      DRAWING CANVAS (Active)            │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │          ╱╲                       │  │
│  │         ╱  ╲   (User drawn)       │  │
│  │        ╱────╲                     │  │
│  │                                   │  │
│  └───────────────────────────────────┘  │
│                                         │
│  Brush Size: [━━━━━━○━━━━] 15px        │
│                                         │
│  [Clear]          [Predict Character]   │
└─────────────────────────────────────────┘
              ↓ (Submit)
┌─────────────────────────────────────────┐
│         PROCESSING                      │
│  Canvas remains visible                 │
│  Button shows: "Processing..."          │
│  All controls disabled                  │
└─────────────────────────────────────────┘
```

### 11.4 Prediction Panel States

```
┌─────────────────────────────────────────┐
│    EMPTY STATE                          │
│                                         │
│           [Lightbulb Icon]              │
│                                         │
│   Upload or draw a character            │
│   to see prediction                     │
│                                         │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│    LOADING STATE                        │
│                                         │
│           [Spinning Icon]               │
│                                         │
│       Analyzing character...            │
│                                         │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│    ERROR STATE                          │
│                                         │
│           [Error Icon]                  │
│              Error                      │
│   Unable to process image.              │
│   Please try again.                     │
│                                         │
│           [Try Again]                   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│    RESULT STATE                         │
│                                         │
│  Predicted Character                    │
│         ┌─────┐                         │
│         │  ا  │  (Large, yellow)        │
│         └─────┘                         │
│                                         │
│  Confidence                        95%  │
│  [████████████████████░]                │
│                                         │
│  Processing time: 45.23ms               │
│                                         │
│  Top 5 Predictions                      │
│  1. ا  [████████████████░░] 95.0%      │
│  2. ب  [███░░░░░░░░░░░░░░]  2.0%      │
│  3. پ  [█░░░░░░░░░░░░░░░░]  1.5%      │
│  4. ت  [█░░░░░░░░░░░░░░░░]  1.0%      │
│  5. ٹ  [░░░░░░░░░░░░░░░░░]  0.5%      │
│                                         │
│        [Try Another Image]              │
└─────────────────────────────────────────┘
```

### 11.5 Mobile Layout (< 768px)

```
┌───────────────────┐
│     HEADER        │
│   [Logo]          │
│   Urdu OCR        │
│   [Nav]           │
└───────────────────┘
│     HERO          │
│   (Title)         │
│   (Description)   │
└───────────────────┘
│ MODEL SELECTOR    │
│ [Char] [Digit]    │
└───────────────────┘
│ INPUT SELECTOR    │
│[Upload] [Draw]    │
└───────────────────┘
│                   │
│  INPUT SECTION    │
│  (Full width)     │
│                   │
└───────────────────┘
│                   │
│ PREDICTION PANEL  │
│  (Full width)     │
│  (Below input)    │
│                   │
└───────────────────┘
│  FEATURE CARDS    │
│  (Single column)  │
└───────────────────┘
│ CHAR GRID         │
│ (3-4 columns)     │
└───────────────────┘
│     FOOTER        │
│  (Single column)  │
└───────────────────┘
```

### 11.6 Component Interaction Flow

```
┌──────────────┐
│   User       │
└──────┬───────┘
       │
       ├─→ Selects Model Type (Character/Digit)
       │       ↓
       │   Updates: Hero text, button labels, instructions
       │
       ├─→ Selects Input Mode (Upload/Draw)
       │       ↓
       │   Shows: ImageUploader OR DrawingCanvas
       │
       ├─→ Provides Input (Upload file OR Draw)
       │       ↓
       │   Enables: Predict button
       │
       ├─→ Clicks Predict
       │       ↓
       │   ┌─────────────────┐
       │   │ Send to API     │
       │   │ Show Loading    │
       │   └────┬────────────┘
       │        │
       │   ┌────▼────────┐  ┌─────────────┐
       │   │  Success    │  │   Error     │
       │   └────┬────────┘  └────┬────────┘
       │        │                 │
       │   Display Result    Display Error
       │        │                 │
       │   ┌────▼─────────────────▼────┐
       │   │   Prediction Panel        │
       │   │   (Result or Error)       │
       │   └───────────────────────────┘
       │
       └─→ Can reset and try again
```

### 11.7 Screenshot Placeholders

**Note:** Replace with actual screenshots during implementation

#### Desktop View
```
[Screenshot: Full desktop layout with two-column grid]
Filename: desktop-full-view.png
Shows: Header, hero, selectors, two-column main content, features, footer
```

#### Image Upload Mode
```
[Screenshot: Upload interface with preview]
Filename: upload-mode.png
Shows: Drag-and-drop zone, file preview, action buttons
```

#### Drawing Canvas Mode
```
[Screenshot: Canvas with drawn character]
Filename: canvas-mode.png
Shows: Canvas with Urdu character, brush controls, action buttons
```

#### Prediction Result
```
[Screenshot: Complete prediction result display]
Filename: prediction-result.png
Shows: Large predicted character, confidence bar, top-5 list
```

#### Mobile View
```
[Screenshot: Mobile layout vertical stack]
Filename: mobile-view.png
Shows: Responsive single-column layout on mobile device
```

#### Error State
```
[Screenshot: Error message display]
Filename: error-state.png
Shows: Error icon, message, and retry button
```

---

## 12. Appendices

### 12.1 Urdu Characters Reference

**Complete List of Supported Characters:**

| # | Character | Name | English Transliteration |
|---|-----------|------|------------------------|
| 1 | ا | Alif | Alif |
| 2 | ب | Bā | Bay |
| 3 | پ | Pā | Pay |
| 4 | ت | Tā | Tay |
| 5 | ٹ | Ṭā | Ttay |
| 6 | ث | S̱ā | Say |
| 7 | ج | Jīm | Jeem |
| 8 | چ | Chā | Chay |
| 9 | ح | Ḥā | Hay (1) |
| 10 | خ | Khā | Khay |
| 11 | د | Dāl | Daal |
| 12 | ڈ | Ḍāl | Ddaal |
| 13 | ذ | Ẕāl | Zaal |
| 14 | ر | Rā | Ray |
| 15 | ڑ | Ṛā | Rray |
| 16 | ز | Zā | Zay |
| 17 | ژ | Zhā | Zhay |
| 18 | س | Sīn | Seen |
| 19 | ش | Shīn | Sheen |
| 20 | ص | Ṣād | Swaad |
| 21 | ض | Ẓād | Zwaad |
| 22 | ط | T̤ā | Twa |
| 23 | ظ | Z̤ā | Zwa |
| 24 | ع | 'Ayn | Ayn |
| 25 | غ | Ġayn | Ghain |
| 26 | ف | Fā | Faa |
| 27 | ق | Qāf | Qaaf |
| 28 | ک | Kāf | Kaaf |
| 29 | گ | Gāf | Gaaf |
| 30 | ل | Lām | Laam |
| 31 | م | Mīm | Meem |
| 32 | ن | Nūn | Noon |
| 33 | و | Vā'o | Waw |
| 34 | ہ | Hā | Hay (2) |
| 35 | ی | Yā | Yaa |
| 36 | ے | Yā Barrī | Yaa Barri |

**Urdu Digits:**

| # | Character | Value |
|---|-----------|-------|
| 1 | ۰ | 0 |
| 2 | ۱ | 1 |
| 3 | ۲ | 2 |
| 4 | ۳ | 3 |
| 5 | ۴ | 4 |
| 6 | ۵ | 5 |
| 7 | ۶ | 6 |
| 8 | ۷ | 7 |
| 9 | ۸ | 8 |
| 10 | ۹ | 9 |

### 12.2 Browser Support

| Browser | Minimum Version | Notes |
|---------|----------------|-------|
| Chrome | 90+ | Full support |
| Firefox | 88+ | Full support |
| Safari | 14+ | Full support |
| Edge | 90+ | Full support |
| Opera | 76+ | Full support |
| Mobile Safari | iOS 14+ | Touch optimized |
| Chrome Mobile | 90+ | Touch optimized |

### 12.3 Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Dec 2025 | Dev Team | Initial UI specification |

### 12.4 References

- **WCAG 2.1 Guidelines:** https://www.w3.org/WAI/WCAG21/quickref/
- **Material Design:** https://material.io/design
- **React Documentation:** https://react.dev/
- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **Urdu Typography:** https://www.unicode.org/charts/PDF/U0600.pdf

---

**End of UI Specification Document**

*For questions or updates to this specification, please contact the development team or open an issue on GitHub.*

