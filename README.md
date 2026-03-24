# Web Harmonium & Web Tools by Atul singh

This repository is a collection of web-based devotional utilities and virtual Indian musical instruments built specifically for standard modern web browsers. The project is designed as a fully client-side application running completely on Vanilla HTML, CSS, and JavaScript.

## Features & Tools Included

### 1. Virtual Musical Instruments
- **Web Harmonium (`webharmonium.html`)**: A playable virtual harmonium that operates using your computer keyboard or any attached MIDI keyboard. It implements the Web Audio API to manipulate real `.wav` samples of a harmonium, including volume control, octave transposition, root note/pitch adjustments, and artificial reverb.
- **Web Tambura (`webtambura.html`)**: A looping ambient virtual Tambura drone. It allows practitioners to select their pitch/shruti (C, C#, D, E, etc.) as well as enabling "Madhyam Shruthi", helping provide a backing drone for classical singing, chanting, or meditation.
- **Loop Player (`loops.html`)**: A dynamic audio module that pulls from a configuration file (`loop-db.json`) allowing you to continually play devotional looping tracks or segmented audios.

### 2. Devotional Tracking & Utilities
- **24/7 Akanda Nama Monitor (`akandanama_next.html`)**: A beautifully designed, auto-updating web schedule to manage and highlight active chanting slots. Integrated directly with the device's current date and time (standardized to IST), this utility easily allows organizing volunteer chanting rotations.
- **Vishnu Sahasra Namam Tracker**:
  - `vishnu_namam.html`: Dedicated text-viewer for reading the Archanai.
  - `vishnu-sahasra-namam.html`: Viewer tailored for the Parayanam (continuous reading) portion.
- **Parayanam Tracker (`parayanam.html`)**: Generic reading or progress tracking utility.
- **Nama Writing Sheet (`nama_sheet.html`)**: A specialized digital layout sheet for users maintaining a mantra writing count (like Likhita Japa). 

### 3. General Utilities
- **Exercise Timer (`exercisetimer.html`)**: Simple web-based timing tool.
- **Date Time & TimeZone Converter (`DateTimeZone.html`)**: Easily check and convert current times against various timezones.

## Technology Stack

The project focuses on creating rich user experiences entirely on the client, minimizing backend requirements:
- **Core logic**: Vanilla JavaScript.
- **Audio synthesis**: Web Audio API combined with short `.wav` sample files and convolution reverb. 
- **User Interface**: HTML5 and `W3.css` for a lightweight and responsive mobile-first presentation.
- **PWA Ready**: Features a `manifest.json` and a `serviceworker.js` to potentially allow caching on mobile devices for offline access and simple home screen installation as a Progressive Web App.

## Getting Started

Because this application does not require a backend runtime (like Node.js or Python), you can start using the tools immediately:

1. Clone or download the repository to your local machine.
2. Ensure you have a modern web browser installed (Chrome, Firefox, Safari, or Edge).
3. If running locally, you can open any of the HTML pages (such as `index.html`) directly in your browser. 
4. *Note:* For some advanced Web Audio functionalities (like MIDI inputs or local file fetching for `loop-db.json`), you may need to serve the directory locally using a simple web server (e.g., `npx http-server`, `python -m http.server`, or the Live Server extension in VS Code).

## Usage

Navigate to `index.html` as the main hub to explore and launch the individual web applications effortlessly from one directory.
