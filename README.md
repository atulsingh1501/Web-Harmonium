# Swara Harmonium

This repository exclusively hosts the **Swara Harmonium**, a virtual musical instrument built by Atul Singh for modern web browsers. The project is designed as a fully client-side application, utilizing Vanilla HTML, CSS, and JavaScript.

## Features

- **Playable Interface**: A realistic, skeuomorphic virtual harmonium.
- **Keyboard & MIDI Support**: Play using your computer keyboard or attach any compatible MIDI keyboard using the Web MIDI API.
- **Web Audio API**: Implements real `.wav` samples of a harmonium, complete with volume control, octave transposition, root note/pitch adjustments, and artificial reverb.
- **Progressive Web App**: Features a `manifest.json` and a `serviceworker.js` to allow caching on devices for offline access.

## Getting Started

Because this application relies entirely on client-side logic without any required backend runtime:

1. Clone or download the repository to your local machine.
2. Open `index.html` in your web browser (Chrome, Firefox, Safari, or Edge) to experience the virtual harmonium case. 
3. *Note:* For some advanced Web Audio functionalities (like MIDI inputs), you may need to serve the directory locally using a lightweight web server (e.g., `npx http-server`, `python -m http.server`, or the Live Server extension in VS Code).

## Usage

Simply visit the main page (`index.html`) to "open" the harmonium and start playing!
